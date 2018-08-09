#!/usr/bin/env python -i
# -----------------------

from scipy.sparse.linalg import spsolve
from scipy.sparse import spdiags
from scipy import sparse

from numpy import *
from scipy import interpolate

import scipy.integrate
import sys
import time

import warnings
warnings.filterwarnings("ignore")

#from pylab import *

k_air = 0.025e-2 #[W/cmK]

Lambda = 2.5e-6
beta = array([0.0623, 0.6339, 0.2359, 0.5790, 1.2462, 0.5434, 0.4665, 0.2236])*1e-3
l    = array([0.0125, 0.0283, 0.0425, 0.1330, 0.2925, 0.6665, 1.6348, 3.5546])

pcm = 1e-5
g = 9.81


def step(x, x0, width):
    
    y = zeros_like(x)
    
    i = where((x > (x0-width)) & (x < (x0+width)))[0]
    y[i] = 0.5+0.5*sin((pi/2)*(x[i]-x0)/width)

    i = where(x>=x0+width)[0]
    y[i] = 1.0
    
    return y

class material(object):

    __slots__ = ('_k','_Cp','_rho','name')
    
    def __init__(self, name, k=None, Cp=None, rho=None):
        self.name = name
        self._k = k
        self._Cp = Cp
        self._rho = rho
        
    def __repr__(self):
        return self.name
        
    def __calc__(self, pol, T):
        
        
        
        if isscalar(pol):
            return ones_like(T)*pol
        
        elif len(pol) == 2:
            y = zeros_like(T)

            for c,p in zip(*pol):
                y = y + c*T**(p)
            
            return y

        elif len(pol) == 3:
            if pol[2] == 'tab':
                return interp(T, pol[0], pol[1])
    
        
    def k(self,T):
        return self.__calc__(self._k, T)

    def Cp(self,T):
        return self.__calc__(self._Cp, T)

    def rho(self,T):
        return self.__calc__(self._rho, T)


He = material('He', k=0.152e-2, rho=0.187e-3, Cp=9e-3)

Pb = material('Pb', k = 16e-2,
              rho = ([11.367, -0.0011944], [0,1]),
              Cp  = ([0.1751, -4.961e-5, 1.985e-8, -2.099e-12, -1.524e3], [0,1,2,3,-4]))
          
UOX = material('UOX', k=([5.17e-2, -1.29e-5], [0,1]), Cp=0.325, rho=10.5)    
MOX = material('MOX', k=0.018, Cp=0.325, rho=11.0)

MIN = material('MIN', k=0.26, Cp=0.325, rho=13.1)    

metal_fuel = material('metal fuel', k=([0.01175, 0.00025], [0,1]), Cp=0.19, rho=([16.173, -1e-3], [0,1]))
Zr_alloy = material('Zr alloy', k=([673, 1073], [0.18, 0.28], 'tab'), Cp=0.19, rho=([673, 1073], [15.5, 15.1], 'tab'))

Na = material('Na', k = 76e-2,
              Cp = ([1.658, -0.84789e-3, 4.4541e-7, -2.9926e3], [0,1,2,-2]),
              rho = ([1.012, -0.2205e-3, -1.923e-8, 5.637e-12], [0,1,2,3]))

steel = material('steel', k=26e-2, Cp=0.49, rho=7.9)


# Generate finite difference matrices for 2D problems
# ---------------------------------------------------

def Operators_XY(x, y, BC_type_x=['D','D'], BC_type_y=['D','D']):
    
    ny,nx = len(y),len(x)
    dy,dx = y[1]-y[0], x[1]-x[0]
    
    # Identity matrix
    # -----------------
    A0 = sparse.eye(nx*ny, nx*ny, dtype='f')

    # du/dx operators
    # --------------
    A1X = sparse.eye(ny*nx, ny*nx, k=1) - sparse.eye(ny*nx, ny*nx, k=-1)
    A2X = sparse.eye(ny*nx, ny*nx, k=-1) - 2*sparse.eye(ny*nx, ny*nx) + sparse.eye(ny*nx, ny*nx, k=1)

    
    if BC_type_x[0] == 'N':
        for i in range(0,ny):
            A2X[i*nx,i*nx+1] = 2.0

    if BC_type_x[1] == 'N':
        for i in range(0,ny):
            A2X[(i+1)*nx-1,(i+1)*nx-2] = 2.0
            

    # du/dy operators
    # -----------------
    A1Y = sparse.eye(ny*nx, ny*nx, k=nx) - sparse.eye(ny*nx, ny*nx, k=-nx)

    D0 = -2.0 * ones(nx*ny, 'f')
    DU = ones(nx*(ny), 'f')
    DL = ones(nx*(ny), 'f')

    for i in range(nx,nx*ny,nx):
        A1X[i-1,i] = 0.0
        A1X[i,i-1] = 0.0
        A2X[i-1,i] = 0.0
        A2X[i,i-1] = 0.0

    if BC_type_y[0] == 'N':
        DU[:nx*2] = 2.0

    if BC_type_y[1] == 'N':
        DL[-nx*2:] = 2.0    

    A2Y = sparse.spdiags([DL, D0, DU], [-nx, 0, nx], ny*nx, ny*nx)

    A1X = A1X / (2*dx)
    A1Y = A1Y / (2*dy)

    A2X = A2X / (dx**2)
    A2Y = A2Y / (dy**2)

    return A0, A1X, A1Y, A2X, A2Y
    



def Operators_RZ(r, z, BC_type_r=['D','D'], BC_type_z=['D','D']):
    
    nz,nr = len(z),len(r)
    dz,dr = z[1]-z[0], r[1]-r[0]
    
    # Identity matrix
    # -----------------
    A0 = sparse.eye(nr*nz, nr*nz, dtype='f')

    div_r = 1/tile(r,nz)
    div_r = sparse.spdiags([div_r], [0], nr*nz, nr*nz)
    
    # du/dr operators
    # --------------
    A1R = (sparse.eye(nz*nr, nz*nr, k=1) - sparse.eye(nz*nr, nz*nr, k=-1)) / (2*dr)
    A2R = (sparse.eye(nz*nr, nz*nr, k=-1) - 2*sparse.eye(nz*nr, nz*nr) + sparse.eye(nz*nr, nz*nr, k=1)) / (dr**2)
    
    if BC_type_r[0] == 'N':
        for i in range(0,nz):
            A2R[i*nr,i*nr+1] = 2.0 / (dr**2)
            A1R[i*nr,i*nr+1] = 0

    if BC_type_r[1] == 'N':
        for i in range(0,nz):
            A2R[(i+1)*nr-1,(i+1)*nr-2] = 2.0 / (dr**2)
            A1R[(i+1)*nr-1,(i+1)*nr-2] = 0
                         

    for i in range(nr,nr*nz,nr):
        A1R[i-1,i] = 0.0
        A1R[i,i-1] = 0.0
        A2R[i-1,i] = 0.0
        A2R[i,i-1] = 0.0
   
    #A2R = dot(div_r, A1R) + A2R
    A2R = (div_r * A1R) + A2R
    
    # du/dy operators
    # -----------------
    A1Z = sparse.eye(nz*nr, nz*nr, k=nr) - sparse.eye(nz*nr, nz*nr, k=-nr)

    D0 = -2.0 * ones(nr*nz, 'f')
    DU = ones(nr*(nz), 'f')
    DL = ones(nr*(nz), 'f')

    if BC_type_z[0] == 'N':
        DU[:nr*2] = 2.0

    if BC_type_z[1] == 'N':
        DL[-nr*2:] = 2.0    

    A2Z = sparse.spdiags([DL, D0, DU], [-nr, 0, nr], nz*nr, nz*nr)

    A1Z = A1Z / (2*dz)
    A2Z = A2Z / (dz**2)

    return A0, A1R, A1Z, A2R, A2Z
    


# First derivative upwind operator
# ----------------------------------

def Operator_X_UW(x, BC_type=('N','N')):
    
    nx = len(x)
    dx = x[1]-x[0]

    A0 = sparse.eye(nx, nx, k=0)
    A1 = 1/(dx)  * (sparse.eye(nx, nx, k=0) - sparse.eye(nx, nx, k=-1))

    return A0, A1
    
def BC_XY(x, y, BC_type_x=['D','D'], BC_type_y=['D','D'], BC_xl=None, BC_xu=None, BC_yl=None, BC_yu=None):

    ny,nx = len(y),len(x)
    dy,dx = y[1]-y[0], x[1]-x[0]
 
    # Set default BC = 0
    # -------------------
    if BC_xl == None:
        BC_xl = zeros(ny)
    if BC_xu == None:
        BC_xu = zeros(ny)
    if BC_yl == None:
        BC_yl = zeros(nx)
    if BC_yu == None:
        BC_yu = zeros(nx)
        

    # Generate 2nd derivative BC x vectors
    # -------------------------------------
    BC2_x = zeros(nx*ny)
    BC1_x = zeros(nx*ny)

    if BC_type_x[0] == 'N':
        for i in range(0,ny):
            BC2_x[i*nx] = -BC_xl[i] * (2/dx)
            BC1_x[i] = BC_xl[i]
            
    elif BC_type_x[0] == 'D':
        for i in range(0,ny):
            BC2_x[i*nx] = BC_xl[i] / (dx**2)

    if BC_type_x[1] == 'N':
        for i in range(0,ny):
            BC2_x[i*nx+nx-1] = BC_xu[i] * (2/dx)
            BC1_x[i] = BC_xu[i]

    elif BC_type_x[1] == 'D':
        for i in range(0,ny):
            BC2_x[i*nx+nx-1] = BC_xu[i] / (dx**2)

    
    # Generate 2nd derivative BC y vectors
    # -------------------------------------
    BC2_y = zeros(nx*ny, 'f')

    if BC_type_y[0] == 'N':
        BC2_y[:nx] = BC_yl * (2/dy)

    if BC_type_y[1] == 'N':
        BC2_y[-nx:] = BC_yu * (2/dy)

    if BC_type_y[0] == 'D':
        print(nx, BC2_yl)
        BC2_y[:nx] = BC_yl / (dy**2)

    if BC_type_y[1] == 'D':
        BC2_y[-nx:] = BC_yu / (dy**2)

    return BC1_x, zeros(nx*ny, 'f'), BC2_x, BC2_y



def BC_RZ(r, z, BC_type_r=['D','D'], BC_type_z=['D','D'], BC_rl=None, BC_ru=None, BC_zl=None, BC_zu=None):

    nz,nr = len(z), len(r)
    dz,dr = z[1]-z[0], r[1]-r[0]
 
    div_r = 1.0/tile(r,nz)
    div_r = diag(div_r)

    # Set default BC = 0
    # -------------------
    if BC_rl == None:
        BC_rl = zeros(nz)
    if BC_ru == None:
        BC_ru = zeros(nz)
    if BC_zl == None:
        BC_zl = zeros(nr)
    if BC_zu == None:
        BC_zu = zeros(nr)
        

    # Generate 2nd derivative BC r vectors
    # -------------------------------------
    BC2R = zeros(nr*nz)
    BC1R = zeros(nr*nz)

    if BC_type_r[0] == 'N':
        for i in range(0,nz):
            BC2R[i*nr] = -BC_rl[i] * (2/dr)
            BC1R[i*nr] = BC_rl[i]
            
    elif BC_type_r[0] == 'D':
        for i in range(0,nz):
            BC2R[i*nr] = BC_rl[i] / (dr**2)
            BC1R[i*nr] = BC_rl[i] / (2*dr)

    if BC_type_r[1] == 'N':
        for i in range(0,nz):
            BC2R[i*nr+nr-1] = BC_ru[i] * (2/dr)
            BC1R[i*nr+nr-1] = BC_ru[i]

    elif BC_type_r[1] == 'D':
        for i in range(0,nz):
            BC2R[i*nr+nr-1] = BC_ru[i] / (dr**2)
            BC1R[i*nr+nr-1] = BC_ru[i] / (2*dr)
    
    #print div_r
    BC2R = dot(div_r,BC1R) + BC2R
    
    
    # Generate 2nd derivative BC z vectors
    # -------------------------------------
    BC2Z = zeros(nr*nz, 'f')
    
    if BC_type_z[0] == 'N':
        BC2Z[:nr] = BC_zl * (2/dz)

    if BC_type_z[1] == 'N':
        BC2Z[-nr:] = BC_zu * (2/dz)

    if BC_type_z[0] == 'D':
        BC2Z[:nr] = BC_zl / (dz**2)

    if BC_type_z[1] == 'D':
        BC2Z[-nr:] = BC_zu / (dz**2)
        
    return BC1R, zeros(nr*nz, 'f'), BC2R, BC2Z






def dX(t,X,core):

    N = X[0]
    C = X[1:9]

    dX = zeros(9)
    
    dX[0] = (core.dk-beta.sum())/Lambda*N + sum(l*C)
    dX[1:9] = beta/Lambda*N - l*C
    
    return dX



class rod(object):
    
    def __init__(self, nr, nz, r_rod, h_rod, material, dr_gap, dr_clad, r_hole=0.0, T0=1000, T0_clad=700, P=400, aD=0.0, bond_material=He, clad_material=steel, axial_peaking=0.25):
        
        self.material = material
        self.aD = aD
        self.r_rod = r_rod = float(r_rod)
        self.h_rod = h_rod = float(h_rod)
        
        # Is there an annular hole in the core of the pellet?
        # ------------------------------------------------------
        if r_hole == 0:
            self.r = r = linspace(r_rod/nr, r_rod, nr, 'f')
        elif r_hole > 0:
            self.r = r = linspace(r_hole, r_rod, nr, 'f')
            
        self.z = z = linspace(0, h_rod, nz, 'f')

        # Preperare FD operators for solving heat conduction
        # ---------------------------------------------------
        A0, A1R, A2R, A2R, A2Z = Operators_RZ(r, z, ('N','N'), ('N','N'))
        self.A0, self.A1R, self.A = A0, A1R, A2R + A2Z

        # Peaking of axial power profile
        #self.P = P * (sin(z*pi/h_rod) / 0.6303 * axial_peaking + (1.0 - axial_peaking))

        if axial_peaking > 1.0:
            p = cos(pi*(z-h_rod/2.0)/(axial_peaking*h_rod))
            self.P = P * p / mean(p)
        else:
            self.P = P
        
        self.T = T0
        self.T0 = T0
        
        self.dr_gap = dr_gap
        self.dr_clad = dr_clad
        
        self.bond_material = bond_material
        self.clad_material = clad_material

        self.T_clad = T0_clad
        self.T_surf = T0_clad

    def solve(self, dt):

        P = self._P
        T = self._T
        ie = self.ie
        
        k = self.material.k(T)
        Cp = self.material.Cp(T)
        rho = self.material.rho(T)

        BC_ru = -self.dT_gap / self.dr_gap * (self.bond_material.k(T[ie])/k[ie])
        
        C = spdiags([k/(rho*Cp)], [0], len(k), len(k))
        A = C * self.A
        
        BC1R, BC1Z, BC2R, BC2Z = BC_RZ(self.r, self.z, ('N','N'), ('N','N'), BC_ru=BC_ru)
        self._T = spsolve(self.A0 - dt*A, T+dt*(k*(BC2R+BC2Z) + P)/(rho*Cp))
        

    def set_T0(self, dim=0):
        self.T0 = self.T_avg
        self.P0 = self.P_avg

    def __get_ie(self):
        return arange(self.nr-1, self.nr*self.nz, self.nr)

    def __get_ic(self):
        return arange(0, self.nr*self.nz, self.nr)

    def __get_nz(self):
        return self.z.shape[0]


    def __get_nr(self):
        return self.r.shape[0]

    def __get_T(self):
        return self._T.reshape((self.nz, self.nr))

    def __set_T(self, T):

        nz, nr = self.nz, self.nr

        if shape(T) == ():
            self._T = ones(nz*nr)*T

        elif shape(T) == (nr,):
            self._T = tile(T, nz)

        elif shape(T) == (nz,):
            self._T = repeat(T, nr)
        
        elif shape(T) == (nz,nr):
            self._T = ravel(T)

    def __get_P(self):
        return self._P.reshape((self.nz, self.nr))

    def __set_P(self, P):

        nz, nr = self.nz, self.nr

        if shape(P) == ():
            self._P = ones(nz*nr)*P

        elif shape(P) == (nr,):
            self._P = tile(P, nz)

        elif shape(P) == (nz,):
            self._P = repeat(P, nr)

        elif shape(P) == (nz,nr):
            self._P = ravel(P)
            

    def __get_T_clad(self):
        return self._T_clad

    def __set_T_clad(self, T_clad):

        nz = self.nz

        if shape(T_clad) == ():
            self._T_clad = ones(nz)*T_clad

        elif shape(T_clad) == (nz,):
            self._T_clad = T_clad
        
    # Return power/cm from pellet to clad
    # ------------------------------------
    def __get_P_F2C(self):

        # Get temperature on the edge of fuel pellet
        # --------------------------------------------
        T = self._T[self.ie]

        return self.dT_gap * self.bond_material.k(T) / self.dr_gap * (2*pi) * self.r_rod
        

    # Return delta T between edge of pellet and inner edge of clad
    # ------------------------------------------------------------
    def __get_dT_gap(self):

        # Heat conductivities of clad and gap
        # ------------------------------------
        k_c = self.clad_material.k(self.T_clad)
        k_g = self.bond_material.k(self.T_clad)

        return (self.TE - self.T_clad) / (1 + 0.5*k_g/k_c)
        

    # Return delta T between edge of pellet and inner edge of clad
    # ------------------------------------------------------------
    def __get_dT_clad(self):
       
        # Heat conductivities of clad and gap
        # ------------------------------------
        k_c = self.clad_material.k(self.T_clad)
        k_g = self.bond_material.k(self.T_clad)

        return (self.TE - self.T_clad) / (0.5 + k_c/k_g)
        

    # Return outer surface tamperature of cladding
    # ----------------------------------------------
    def __get_T_surf(self):
        return self.TE - self.dT_gap - self.dT_clad


    # Set outer surface tamperature of cladding
    # --------------------------------------------
    def __set_T_surf(self, T_surf):
        
        nz = self.nz

        if shape(T_surf) == ():
            T_surf = ones(nz)*T_surf

        elif shape(T_surf) != (nz,):
            raise 'Value error, wrong dimension of T_surf'

        # Heat conductivities of clad and gap
        # ------------------------------------
        k_c = self.clad_material.k(self.T_clad)
        k_g = self.bond_material.k(self.T_clad)
        
        dT_tot = self.TE - T_surf
        dT_clad = dT_tot * k_g/k_c / (1+k_g/k_c)
        dT_gap = dT_tot - dT_clad

        self.T_clad = self.TE - dT_gap - dT_clad / 2.0
    
    def __get_TC(self):
        return self._T[self.ic]

    def __get_TE(self):
        return self._T[self.ie]
    
    def __get_T_avg(self):

        aD = atleast_1d(self.aD)
        T_avg = zeros_like(aD)
        r_mult = tile(self.r, self.nz)
        
        for i,j in enumerate(self.i_fb):
            T_avg[i] = sum(self._T[j]*r_mult[j]) / sum(r_mult[j])
            
        return T_avg
        
    def __get_P_avg(self):
        
        r_mult = tile(self.r, self.nz)
        r_mult = reshape(r_mult, (self.nz, self.nr))

        return sum(self.P*r_mult) / sum(r_mult)

    def __get_dk(self):

        aD = atleast_1d(self.aD)
        dk = zeros_like(aD)
        T_avg = self.T_avg

        for i,T in enumerate(T_avg):
            dk[i] = aD[i] * (T - self.T0[i])

        return dk.sum()

    def __get_r_clad(self):

        return self.r_rod + self.dr_gap + self.dr_clad



    def __get_i_fb(self):
        
        i = []
        
        r = tile(self.r, self.nz)
        z = repeat(self.z, self.nr)

        h = float(self.h_rod)
        aD = atleast_1d(self.aD)

        n = len(aD)
    
        for j in range(n):
            z0,z1 = j*h/n, (j+1)*h/n
            i.append(where((z >= z0) & (z < z1))[0])
            
        return i

    i_fb = property(__get_i_fb)

    ic = property(__get_ic)
    ie = property(__get_ie)

    nz = property(__get_nz)
    nr = property(__get_nr)

    P = property(__get_P, __set_P)
    T = property(__get_T, __set_T)
    T_clad = property(__get_T_clad, __set_T_clad)
    T_surf = property(__get_T_surf, __set_T_surf)
    P_F2C = property(__get_P_F2C)
    
    dT_gap = property(__get_dT_gap)
    dT_clad = property(__get_dT_clad)

    r_clad = property(__get_r_clad)
    
    dk = property(__get_dk)

    TC = property(__get_TC)
    TE = property(__get_TE)
    
    T_avg = property(__get_T_avg)
    P_avg = property(__get_P_avg)



        
    



class channel(object):
    
    def __init__(self, nz, rod, p_over_d, coolant, v=None, T_in=None, aC=0.0, T_init=700, dm_duct=None, dA_duct=None, duct_material=steel, A_cool=None, d_h=None):
        
        self.rod = rod
        self.v = v
        self.z = z = linspace(-10, self.rod.h_rod+10, nz)
        self.T = ones_like(z)*T_init
        self.aC = aC
        self.T0 = T_in
        self.T_in = T_in
        self.material = coolant
        self.p_over_d = p_over_d
        
        # Cross sectional area of coolant channel
        # ----------------------------------------
        if A_cool == None:
            self.A_cool = 2*(sqrt(3)/4.0*(p_over_d*rod.r_clad*2)**2 - 0.5*pi*(rod.r_clad)**2)
        else:
            self.A_cool = A_cool
            
        # Hydraulic diameter of coolant channel
        # ----------------------------------------
        if d_h == None:
            self.d_h = (2*sqrt(3)*p_over_d**2/pi-1)*rod.r_clad
        else:
            self.d_h = d_h
            
        self.A0, self.A1 = Operator_X_UW(z, BC_type=('N','N'))
        self.core = None
        self.old_solve = False
        self.backward_FD = True

        # Set duct mass and area densities
        # -----------------------------------
        
        self.T_duct = copy(self.T)

        self.dm_duct = dm_duct        
        self.dA_duct = dA_duct
        
        self.duct_material = duct_material
        
    def solve(self, dt):
        
        self.rod.solve(dt)

        T = self.T
        k = self.material.k(T)
        Cp = self.material.Cp(T)
        rho = self.material.rho(T)
            
        if self.old_solve:

            P_F2C = interp(self.z, self.rod.z, self.rod.P_F2C, left=0, right=0) / self.A_cool

            BC1Z = zeros_like(self.z)
            BC1Z[0] = -self.T_in/self.dz

            A = -self.v * self.A1
            T = spsolve(self.A0 - dt*A, T + dt*((P_F2C/(rho*Cp)) - self.v*BC1Z))

            self.T=T
            self.rod.T_surf = interp(self.rod.z, self.z, self.T)

        else:
            
            T_surf = interp(self.z, self.rod.z, self.rod.T_surf, left=T[0], right=T[-1])
            T_edge = interp(self.z, self.rod.z, self.rod.TE, left=T[0], right=T[-1])
            
            z = self.z
            r = self.rod
            
            # Surface area of rod per vertical cm
            dA = 2*pi*self.rod.r_clad # cm2/cm
            
            # Heat transfer from clad to coolant
            h = k*self.Nu/self.d_h # W/(cm2*K)
            
            # Treat gap, cladding and surface layer of coolant as thin
            # thermally resistive layers
            k_bond = r.bond_material.k(T_edge-r.dT_gap/2.0)
            k_clad = r.clad_material.k(T_surf+r.dT_clad/2.0)
            
            # Calculate thermal resistance of thin layers (K/W/cm)
            R_bond = r.dr_gap/(k_bond * 2*pi * (r.r_rod+r.dr_gap/2.0))
            R_clad = r.dr_clad/(k_clad * 2*pi * (r.r_rod+r.dr_gap+r.dr_clad/2.0))            
            R_cool = 1.0/(dA*h)
            
            # Total thermal resistance
            R_tot = R_bond+R_clad+R_cool         
            
            # Power from fuel to coolant
            P_F2C = (T_edge-T)/R_tot / self.A_cool

            # Baoundary condition for advection
            BC1Z = zeros_like(self.z)
            BC1Z[0] = -self.T_in/self.dz
            
            # Solve finite difference equations
            # ----------------------------------
            if self.backward_FD:

                # FD operator for heat transfer from clad
                A_heat_rod  = sparse.spdiags([1.0/(R_tot*self.A_cool*rho*Cp)], [0], self.nz, self.nz)

                # Include heat transfer to duct
                # -------------------------------
                if (self.dA_duct != None) & (self.dm_duct != None):

                    # Thermal resistance from coolant to duct
                    R_duct = 1.0/(self.dA_duct*h)
                    
                    # FD operator for heat transfer to duct
                    A_heat_duct = sparse.spdiags([1.0/(R_duct*self.A_cool*rho*Cp)], [0], self.nz, self.nz)
                    
                    A = -self.v * self.A1 - A_heat_rod - A_heat_duct
                    self.T = spsolve(self.A0 - dt*A, T + dt*(T_edge/(R_tot*self.A_cool*rho*Cp)
                                                             + self.T_duct/(R_duct*self.A_cool*rho*Cp) - self.v*BC1Z))

                    # Update temperature of duct
                    dT_duct = dt * (self.T-self.T_duct) / (R_duct*self.duct_material.Cp(self.T_duct)*self.dm_duct)
                    self.T_duct = self.T_duct + dT_duct

                # Do not include heat transfer to duct
                # --------------------------------------
                else:
                    A = -self.v * self.A1 - A_heat_rod
                    self.T = spsolve(self.A0 - dt*A, T + dt*(T_edge/(R_tot*self.A_cool*rho*Cp) - self.v*BC1Z))
 
            else:
                A = -self.v * self.A1
                
                self.T = spsolve(self.A0 - dt*A, T + dt*((P_F2C/(rho*Cp)) - self.v*BC1Z))  
                
            # Update surface temperature of cladding
            r.T_surf = interp(r.z, z, self.T + (T_edge-self.T)*R_cool/R_tot)


    def __get_nz(self):
        return self.z.shape[0]
            
    def __get_Nu(self):

        T = self.T
        k = self.material.k(T)
        Cp = self.material.Cp(T)
        rho = self.material.rho(T)
        
        # Peclet number
        Pe = self.v * self.d_h * rho * Cp / k

        x = self.p_over_d
        
        # Nusselt number from Mikutyuk correltation (Nucl. Eng. and Design 2009)
        Nu = 0.047*(1-exp(-3.8*(x-1)))*(Pe**0.77 + 250)
        
        return Nu


    
    def set_T0(self):
        
        self.T0 = zeros(len(self.i_fb))
        
        for j,i in enumerate(self.i_fb):
            self.T0[j] = self.T[i].mean()
            
        self.rod.set_T0()

    def __get_dk(self):
                
        dk = zeros_like(self.aC)
        
        for j,i in enumerate(self.i_fb):
            dk[j] = self.aC[j]*(self.T[i].mean() - self.T0[j])
            
        return dk.sum() + self.rod.dk

            
    def __get_dz(self):
        return self.z[1]-self.z[0]
    
    def __get_T_avg(self):        
        i = where((self.z>=0) & (self.z <=self.rod.h_rod))[0]
        return self.T[i].mean()

    def __get_T_max(self):
        i = where((self.z>=0) & (self.z <=self.rod.h_rod))[0]
        return self.T[i].max()

    def __get_v(self):
        
        if self._v == None:
            return self.core.v
        else:
            return self._v

    def __set_v(self, v):
        self._v = v

    def __get_T_in(self):

        if self._T_in == None:
            return self.core.T_in
        else:
            return self._T_in
  
    def __set_T_in(self, T_in):
        self._T_in = T_in
      
    def __get_aC(self):
        return self._aC

    def __set_aC(self, aC):
        self._aC = atleast_1d(aC)

    def __get_i_fb(self):
        
        i = []

        z = self.z
        h = float(self.rod.h_rod)
        aC = atleast_1d(self.aC)

        if len(aC) >= 3:

            i.append(where(z < 0.0)[0])
            n = len(aC) - 2
            
            for j in range(n):
                z0,z1 = j*h/n, (j+1)*h/n
                i.append(where((z >= z0) & (z < z1))[0])

            i.append(where(z >= h)[0])
            
        elif len(aC) == 1:
            i.append(where((z >= 0.0) & (z <= h))[0])
            
        return i


    v = property(__get_v, __set_v)
    T_in = property(__get_T_in, __set_T_in)
    aC = property(__get_aC, __set_aC)
    i_fb = property(__get_i_fb)
    
    nz = property(__get_nz)
    dz = property(__get_dz)
    dk = property(__get_dk)

    T_avg = property(__get_T_avg)
    T_max = property(__get_T_max)

    Nu = property(__get_Nu)

class channel_2D(channel):
    pass


class core(object):
    pass
    

class core_channels(core):
    
    def __init__(self, channel, n_channels, dX=dX, v=100, T_in=700):
        
        self.channel = channel
        self.n_channels = n_channels
        
        self.v = v
        self.T_in = T_in
        
        self.dX = dX
        self.dk_CR = 0.0
        
        self.reset_ODE()


    def reset_ODE(self):

        self.t = 0.0
        self.P_norm = 1.0

        self.ode15s = scipy.integrate.ode(dX).set_integrator('vode', method='bdf', order=15, nsteps=5000)

        p0_1 = array([1.0])
        p0_2 = beta/l/Lambda
        
        p0 = concatenate((p0_1, p0_2))
        
        self.ode15s.set_initial_value(p0, 0.0)
        self.ode15s.set_f_params(self)
        

    # Solve coupled point kinetics and heat transport
    # ------------------------------------------------
        
    def solve_PK(self, dt, refine=1, output=True):

        for i in range(refine):

            self.t = self.t+dt/refine
            for c in self.channel:
                c.solve(dt/refine)        

        X = self.ode15s.integrate(self.ode15s.t+dt)
        
        self.P_norm = X[0]
        
        for c in self.channel:

            P = c.rod.P
            P = P / c.rod.P_avg

            c.rod.P = P * (self.P_norm*c.rod.P0)
        
    # Solve steady state heat transport
    # -----------------------------------
            
    def solve_SS(self, dt, err=0.01, output=True):
        
        #if output:
        #    print('----------------------------------------------')
        #    print('Solving steady state temperature profile    ')
        #    print('                                              ')


        E = [1.0] * len(self.channel)
        
        Tr = []
        Tc = []

        for c in self.channel:
            
            Tr.append(c.rod.T.copy())
            Tc.append(c.T.copy())
        
        first = True

        while mean(E) > err:
            
            E = []
            
            for i,c in enumerate(self.channel):
                c.solve(dt)
                e = (mean(abs(Tr[i]-c.rod.T)) + mean(abs(Tc[i]-c.T)))/2
                E.append(e)

                Tr[i] = c.rod.T.copy()
                Tc[i] = c.T.copy()

            if output:

                if not first:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

                #print('err = %.3f' %(mean(E))) 
                #print(' ')

            first = False

        for c in self.channel:
            c.set_T0()

        
    def __get_dk(self):
        
        dk = 0.0
        
        for c in self.channel:
            dk = dk+c.dk
        
        return self.dk_CR + dk


    # Get/set methods for coolant flow velocity
    # -------------------------------------------

    def __set_v(self, v):
        self._v = v

    def __get_v(self):

        if ndim(self._v) == 0:
            return self._v
        
        if ndim(self._v) == 2:
            return interp(self.t, self._v[0], self._v[1])



    # Get/set methods for coolant flow velocity
    # -------------------------------------------

    def __set_T_in(self, T_in):
        self._T_in = T_in

    def __get_T_in(self):

        if ndim(self._T_in) == 0:
            return self._T_in
        
        if ndim(self._T_in) == 2:
            return interp(self.t, self._T_in[0], self._T_in[1])


    # Get/set methods for external reactivity insertion (control rods)
    # -----------------------------------------------------------------
    def __set_dk_CR(self, dk_CR):
        self._dk_CR = dk_CR  

        
    def __get_dk_CR(self):

        if ndim(self._dk_CR) == 0:
            return self._dk_CR
        
        if ndim(self._dk_CR) == 2:
            return interp(self.t, self._dk_CR[0], self._dk_CR[1])


    def __get_channel(self):
        return self._channel

    def __set_channel(self, C):
        
        if isinstance(C,channel):
            C = [C]
            
        for c in C:
            c.core = self
            
        self._channel = C

    # Get method for coolant temperature out of the core
    # ---------------------------------------------------
    def __get_T_out(self):

        T_out = []
        n = []

        # Calculate average coolant temperature increase
        # -----------------------------------------------
        for i,c in enumerate(self.channel):
            T_out.append(c.T[-1])
            n.append(self.n_channels[i])

        T_out = average(T_out, weights=n)

        return T_out

    dk = property(__get_dk)

    v = property(__get_v, __set_v)
    T_in = property(__get_T_in, __set_T_in)
    T_out = property(__get_T_out)
    dk_CR = property(__get_dk_CR, __set_dk_CR)
    channel = property(__get_channel, __set_channel)
    



class core_selfcirc(core_channels):
    

    def __init__(self, channel, n_channels, dX=dX, T_in=700, z_IHX=5.0, V_upper_plenum=None):
        
        self.channel = channel
        self.n_channels = n_channels
        
        self.T_in = T_in
        self.z_IHX = z_IHX
        
        self.dX = dX
        self.dk_CR = 0.0


        # Set the volume of the upper sodium plenum
        # ------------------------------------------
        if V_upper_plenum == None:

            A = 0.0

            # Default is 2 X the pin area times the IHX height
            # --------------------------------------------------
            for i,c in enumerate(self.channel):
                A = A + pi*(c.rod.r_clad*c.p_over_d)**2 * self.n_channels[i]

            self.V_upper_plenum = A*z_IHX*100 * 2
            
        else:
            self.V_upper_plenum = V_upper_plenum

        self.T_upper_plenum = T_in
        self.reset_ODE()


    # Solve steady state heat transport and set upper plenum temperature
    # ------------------------------------------------------------------- 
    def solve_SS(self, dt, err=0.01, output=True):

        core_channels.solve_SS(self, dt, err=0.01, output=True)
        self.T_upper_plenum = self.T_out


    # Solve coupled point kinetics and heat transport
    # ------------------------------------------------
    def solve_PK(self, dt, refine=1, output=True):

        # First solve PK from parent class
        core_channels.solve_PK(self, dt, refine, output)

        # Then calculate the temperature change in the upper plenum
        # ----------------------------------------------------------
        coolant = self.channel[0].material
        
        # Total heat transer to upper plenum
        # ----------------------------------
        dq = 0.0
        
        for i,c in enumerate(self.channel):
            dm = c.v * c.A_cool * coolant.rho(c.T[-1]) * self.n_channels[i]
            dq = dq + dm * coolant.Cp(c.T[-1]) * (c.T[-1] - self.T_upper_plenum)

        # Update upper plenum temperature
        dT = dq / (coolant.Cp(self.T_upper_plenum) * self.V_upper_plenum * coolant.rho(self.T_upper_plenum))
        self.T_upper_plenum = self.T_upper_plenum + dT
        
        
    # Get/set methods for coolant flow velocity and pump pressure
    # -------------------------------------------------------------

    def __get_v(self):
        return sqrt((self.dp + self.P_buoy) / self.C_dp)
    
    def __get_P_buoy(self):
        
        coolant = self.channel[0].material
        d_rho = coolant.rho(self.T_upper_plenum) - coolant.rho(self.T_in)

        return -g*self.z_IHX*d_rho*1000

    def __set_dp(self, dp):
        self._dp = dp
        
    
    def __get_dp(self):

        if ndim(self._dp) == 0:
            return self._dp
        
        if ndim(self._dp) == 2:
            return interp(self.t, self._dp[0], self._dp[1])


    v = property(__get_v)
    dp = property(__get_dp, __set_dp)
    P_buoy = property(__get_P_buoy)


class ULOF(object):

    
    def __init__(self, aD=None, aC=None, v0=None, z_IHX=None, dp_0=None, nr=None, 
                 nz=None, h_rod=None, r_rod=None, P0=None, T_in=None, fuel=None, coolant=None,
                 p_over_d=None, dt=None, refine=10, coast_down=None, bond=None, dr_gap=None, dr_clad=None,
                 A_flow=None, d_h=None, axial_peaking=None):
        
        self.h_rod = h_rod
        self.r_rod = r_rod
        self.nr = nr
        self.nz = nz
        self.dr_gap = dr_gap
        self.dr_clad = dr_clad

        self.z_IHX = z_IHX

        self.v0 = v0
        self.dp_0 = dp_0
        self.coast_down = coast_down

        self.P0 = P0
        self.T_in = T_in

        self.aD = aD
        self.aC = aC

        self.fuel = fuel
        self.bond = bond
        self.coolant = coolant
        self.p_over_d = p_over_d

        self.dt = dt
        self.refine = refine

        self.A_flow = A_flow
        self.d_h = d_h
        self.axial_peaking=axial_peaking
        
        self.__has_setup__ = False

    def setup(self):
        
        if self.h_rod == None:
            raise('Error: h_rod must be set')

        if self.r_rod == None:
            raise('Error: r_rod must be set')

        if self.z_IHX == None:
            raise('Error: z_IHX must be set')

        if self.P0 == None:
            raise('Error: P0 must be set')

        if self.v0 == None:
            raise('Error: v0 must be set')

        if self.nr == None:
            raise('Error: nr must be set')

        if self.nz == None:
            raise('Error: nz must be set')

        if self.T_in == None:
            raise('Error: T_in must be set')

        if self.aD == None:
            raise('Error: aD must be set')

        if self.aC == None:
            raise('Error: aC must be set')

        if self.fuel == None:
            raise('Error: fuel must be set')

        if self.coolant == None:
            raise('Error: coolant must be set')
        
        if self.p_over_d == None:
            raise('Error: p_over_d must be set')
        
        if self.coast_down == None:
            raise('Error: coast_down must be set')
        
        if self.bond == None:
            raise('Error: bond must be set')

        if self.dr_gap == None:
            raise('Error: dr_gap must be set')

        if self.dr_clad == None:
            raise('Error: dr_clad must be set')
        
        self.r = rod(self.nr, self.nz, self.r_rod, self.h_rod, self.fuel, dr_gap=self.dr_gap, dr_clad=self.dr_clad,
                     bond_material=self.bond, T0=1000, T0_clad=self.T_in+5, P=self.P0, aD=self.aD, axial_peaking=self.axial_peaking)
        
        self.c = channel(self.nz, self.r, self.p_over_d, self.coolant, aC=self.aC, A_cool=self.A_flow, d_h=self.d_h)
        self.c.old_solve = True
        
        self.core = core_selfcirc([self.c], [1], z_IHX=self.z_IHX, T_in=self.T_in)
        self.core.dp = self.dp_0
        self.core.C_dp = self.core.dp/self.v0**2

        self.core.solve_SS(self.dt/self.refine, err=1e-2)
        self.c.set_T0()

        self.__has_setup__ = True




    def run(self, break_at_peak=True, output=False, t_stop=10, do_plot=False, outfile=None):

        t0 = time.time()
        
        if not self.__has_setup__:
            self.setup()
        
        t = arange(0, t_stop+self.dt, self.dt)

        self.t = []
        self.v = []
        self.P = []
        self.dk = []
        self.dP = []

        self.T_out = []
        self.T_clad = []
        self.T_fuel = []
        self.dk_fuel = []
        self.dk_cool = []
        self.natural = []
        
        dp = self.core.dp * exp(-t/self.coast_down)
        self.core.dp = t,dp

        if do_plot:

                fig = figure(1)

                cla()
                hold(True)

                TS0 = copy(self.r.T_surf)
                TE0 = copy(self.r.TE)
                TC0 = copy(self.r.TC)
                T_COOL0  = copy(self.c.T)

                plot(self.r.z, TE0, 'b--')
                plot(self.r.z, TC0, 'r--')
                plot(self.c.z, T_COOL0,  'g--')

                fig.canvas.draw()

   
        if output:

            print(" ")
            print("Solving dynamic problem   ")
            print(" ")
            print("t (s)        T_fuel (K)   T_out (K)    dk (pcm)     P (au)       v (cm/s)     natural (%)") 
            print('------------------------------------------------------------------------------------------')

        for i in range(10000):

            print("Time: {0:02.1f}".format(self.core.t) + ", T_out: {0:02.1f}".format(self.c.T[-1]-273) + " deg. C")

            if output:

                if i > 0:
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")


                print('%-12.1f %-12.1f %-12.1f %-12.2f %-12.2f %-12.2f %-12.2f %-12.2f' %(self.core.t, self.r.T_avg, self.c.T[-1], self.core.dk/pcm, self.core.P_norm, self.core.v, 100*self.core.P_buoy/(self.core.dp+self.core.P_buoy), self.core.T_upper_plenum))
                print(' ')

            self.core.solve_PK(self.dt, refine=self.refine)

            self.t.append(self.core.t)
            self.v.append(self.core.v)
            self.P.append(self.core.P_norm)
            self.dk.append(self.core.dk)

            self.T_out.append(self.c.T[-1])
            self.T_clad.append(self.c.rod.T_clad.max())
            self.T_fuel.append(self.c.rod.TC.max())
            self.dk_fuel.append(self.c.rod.dk)
            self.dk_cool.append(self.c.dk - self.c.rod.dk)
            self.natural.append(100*self.core.P_buoy/(self.core.dp+self.core.P_buoy))

            if do_plot:
                    
                      fig = figure(1)

                      cla()
                      hold(True)

                      plot(self.r.z, TS0, 'k--')
                      plot(self.r.z, TE0, 'b--')
                      plot(self.r.z, TC0, 'r--')
                      plot(self.c.z, T_COOL0,  'g--')

                      plot(self.r.z, self.r.T_surf, 'k')
                      plot(self.r.z, self.r.TE, 'b-')
                      plot(self.r.z, self.r.TC, 'r-')
                      plot(self.c.z, self.c.T,  'g-')

                      fig.canvas.draw()


            if (len(self.t) > 20):
                if all(gradient(array(self.T_out)[-20:]) < 0.0) & break_at_peak:

                    if output:
                        
                        print(' ')
                        print('Peak found at T_out = %.2f K.' %(max(self.T_out)))
                        print('Exiting... ')
                        print(' ')

                    break

                elif self.t[-1] >= t_stop:
                    print(' ')
                    #print('t_stop reached.')
                    #print('Exiting... ')
                    #print(' ')

                    break

            
            if outfile and (i%100 == 0):
                
                if outfile[-4:] == '.txt':

                    file = open(outfile, 'w')

                    file.write('t (s)        T_fuel (K)   T_out (K)    dk (pcm)     P (au)       v (cm/s)     natural (%)\n')
                    file.write('------------------------------------------------------------------------------------------\n')

                    for j in range(i):
                       file.write('%-12.1f %-12.1f %-12.1f %-12.2f %-12.2f %-12.2f %-12.2f\n' %(self.t[j], self.T_fuel[j], self.T_out[j], self.dk[j]/pcm, self.P[j], self.v[j], self.natural[j]))

                    file.close()
                    
        dt = time.time() - t0
              
        #print('Calculation time %i min %i sec' %((dt - mod(dt,60)) / 60, mod(dt,60)))
        #print(' ')
        print('---------------------------------------------')

          
        self.t = array(self.t)
        self.P = array(self.P)
        self.dk = array(self.dk)
  
        self.T_out = array(self.T_out)
        self.T_clad = array(self.T_clad)
        self.T_fuel = array(self.T_fuel)
        self.dk_fuel = array(self.dk_fuel)
        self.dk_cool = array(self.dk_cool)   
        self.v = array(self.v)
        
if __name__ == '__main__':

    if len(sys.argv) > 1:
        exec(compile(open(sys.argv[1]).read(), sys.argv[1], 'exec'))
    else:
        print('No input file. Exiting...')
        sys.exit()

    if '--plot' in sys.argv:
        do_plot = True
    else:
        do_plot = False


    if '--outfile' in sys.argv:
        i = sys.argv.index('--outfile')
        outfile = sys.argv[i+1]
    else:
        outifle = False

#        
#
#    #MOX = material('MOX', k=([673, 2373], [0.043, 0.021], 'tab'), Cp=0.325, rho=11.0)
#    MOX = material('MOX', k=0.025, Cp=0.325, rho=11.0)
#
#    # SFR (MOX)
#    # ----------
#
#    ulof = ULOF(h_rod=h_rod, r_rod=r_rod, P0=P0, v0=v0, nr=nr, nz=nz, T_in=T_in, aD=aD, aC=aC, z_IHX=z_IHX, dt=dt, refine=refine, bond=bond, fuel=fuel, dr_gap=dr_gap, dr_clad=dr_clad, dp_0=dp_0, p_over_d=p_over_d, coast_down=coast_down, coolant=coolant)
#
#    
#
#    ulof.setup()
#    ulof.run(break_at_peak=False, do_plot=do_plot, outfile=outfile, t_stop=1000)
#