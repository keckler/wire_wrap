import math
#from pylab import *
from x_prop import *

def ductdeform(TotalPressureDrop, DuctedAssemblySideLength, Duct, CoolantInletTemperature, 
			   PeakFastFlux, ResidenceTime, AssemblyPitch, YieldStrengthMargin, DuctGapMargin, 
			   DuctedAssemblyArea, DuctedAssemblyFTF, AssemblyHexagonFTF, maxDPA):
	
	DuctProperties = nonfuelsolidproperties(material=Duct, temperature=CoolantInletTemperature, fastflux=PeakFastFlux, stress=1, dpa=1, porosity=1)

	DuctElasticModulus = DuctProperties.elasticmodulus
	DuctPoissons       = DuctProperties.poissons
	DuctYieldStrength  = DuctProperties.yieldstrength

	if DuctYieldStrength < 0:
		print(DuctYieldStrength)

	YS = YieldStrengthMargin * DuctYieldStrength
	
	StepSize = 1e-3
	
	v = DuctPoissons
	E = DuctElasticModulus
	L = DuctedAssemblySideLength/2
	p = TotalPressureDrop/1e6/2
	
	Rt = 1.60
	
	GapMargin  = DuctGapMargin/10
	Gap        = 1.01 * GapMargin
	CollectTot = {}
	XX         = []
	XT         = []
	XG         = []
	XM         = []
	
	ColS = []
	i = 0
	t = 1e-30
	MaxStress  = 2 * DuctYieldStrength
	
	while MaxStress > YieldStrengthMargin * DuctYieldStrength:
	
		MaxStress = ((2 * L / t) + Rt - 0.5e0 + L / t * (0.5e0 * L / Rt / t - L / Rt / t / (0.6e1 + pi / L * Rt * t) * (0.1e1 + 0.157e1 / L * Rt * t + 0.558e0 / (L ** 2) * (Rt ** 2) * (t ** 2)) + 0.2e1 - math.sqrt(0.3e1)) * (-1 + 12 * Rt ** 2 / (2 * Rt - 1))) * p
		t += StepSize
	
	MinDuct = t
	
	while Gap < 5.0:
	
		if t < MinDuct:
	
			break
	
		t = 1e-30
	
		XGAP = -1
	
		while XGAP < GapMargin:
	
			Deflection = (0.2e1 * (0.2e1 * Rt * (0.3e-1 * Rt * math.log((Rt + 0.5e0) / (Rt - 0.5e0)) / (Rt * math.log((Rt + 0.5e0) / (Rt - 0.5e0)) - 0.1e1) * (1 - v ** 2) + 0.494e0 + 0.292e0 * (v ** 2) + 0.524e0 * v + 0.134e0 * (1 - v ** 2) * (Rt * math.log((Rt + 0.5e0) / (Rt - 0.5e0)) / (Rt * math.log((Rt + 0.5e0) / (Rt - 0.5e0)) - 0.1e1) - 0.1e1) * L / Rt / t * (0.5e0 - 0.1e1 / (0.6e1 + math.pi / L * Rt * t) * (0.1e1 + 0.157e1 / L * Rt * t + 0.558e0 / L ** 2 * Rt ** 2 * t ** 2))) - 0.2e1 * L ** 3 / t ** 3 * (1 - v ** 2) * (0.5e0 - 0.6e1 / (0.6e1 + math.pi / L * Rt * t) * (0.1e1 + 0.157e1 / L * Rt * t + 0.558e0 / L ** 2 * Rt ** 2 * t ** 2))) * p * L / E - 0.12e2 * (1 - v ** 2) * p * L ** 2 / E / t)/2
			XGAP = Gap - Deflection
			MaxStress = ((2 * L / t) + Rt - 0.5e0 + L / t * (0.5e0 * L / Rt / t - L / Rt / t / (0.6e1 + pi / L * Rt * t) * (0.1e1 + 0.157e1 / L * Rt * t + 0.558e0 / (L ** 2) * (Rt ** 2) * (t ** 2)) + 0.2e1 - math.sqrt(0.3e1)) * (-1 + 12 * Rt ** 2 / (2 * Rt - 1))) * p
	
			t += StepSize
	
		Collect = {t : t + Gap}
		CollectTot.update(Collect)
	
		XX.append(10*(t+Gap))
		XT.append(10*t)
		XG.append(10*(Gap))
	
		XM.append(GapMargin*20)
		ColS.append(MaxStress/(YieldStrengthMargin * DuctYieldStrength))
	
		Gap += StepSize
	
		i += 1
	
	MinTot = min(XX)
	
	DuctThickness     = 0
	GapThickness      = 0
	CombinedThickness = 0
	
	for k,v in CollectTot.items():
	
		if v*10 < MinTot * 1.01 and v*10 > MinTot*0.99:
	
			DuctThickness = k*10
			GapThickness  = MinTot - k*10
			CombinedThickness = v*10

	InterAssemblyGap0 = GapThickness/10

	# Duct-wall thickness in [cm]
	T   = DuctThickness/10

	# Mid-wall duct apothem in [cm]
	a   = DuctedAssemblyFTF/2 - T/2

	# Mean corner radius (relation taken from FFTF)
	R   = 1.60 * T

	# Radius-to-apothem relation
	B  = R/a

	# Unit force in the wall at the corner
	Wa = a * p * ( (2/math.sqrt(3)) - B * ((2/math.sqrt(3)) - 1 ) )

	# Unit force in the mid-wall
	Wb = a * p

	# Membrane stress at the corner
	SmemA = Wa / T

	# Membrane stress in the mid-wall
	SmemB = Wb / T

	# Membrane stress in the mid-wall
	Mb = ((a ** 2) * p)/(6 - B*(6-math.pi * math.sqrt(3))) * ( ((1-B) ** 3)/(3) - (B*(1-B)/(2*math.sqrt(3))) * (B*(7*math.pi - 12 * math.sqrt(3) ) - math.pi ))

	# Membrane stress in the corner
	Ma = ((a ** 2) * p) * ( ((1-B)/6) * (1-B*(7-4*math.sqrt(3))) ) - Mb
	# SAFETY AND ECONOMIC CHARACTERISTICS OF A 1000-MWe FAST SODIUM-COOLED REACTOR DESIGN. (1968). 

	# Corner-stress correction factor (for the specific corner radius/thickness)
	# SCohen, K.P.; O'Neill, G.L., Advan. Nucl. Sci. Technol., 4: 67-107
	K1 = 1.273

	# Hyperbolic stress in the corner
	ShypA = K1 * (6 * Ma) / (T ** 2)

	# Bending stress at the mid-wall
	SbendB = (6 * Mb) / (T ** 2)

	# Total corner stress
	StotA = SmemA + ShypA

	# Total mid-wall stress
	StotB = SmemB + SbendB

	# Creep-rate calculation at peak-stress location
	DuctProperties = nonfuelsolidproperties(material=Duct, temperature=CoolantInletTemperature, fastflux=PeakFastFlux, stress=StotB, dpa=maxDPA, porosity=1)

	# Creep-rate calculation at peak-stress location
	CreepRate = DuctProperties.creeprate

	# Total life-time creep
	Creep = (ResidenceTime * 24 * 3600 * CreepRate)/100

	# The creep-expanded flat-to-flat of the ducted assembly
	DuctedAssemblyFTFCreeped = DuctedAssemblyFTF * (1 + Creep/6)

	# The difference in inter-assembly gap due to creep
	CreepDiffGap = (0.5*(AssemblyHexagonFTF - DuctedAssemblyFTF)) - (0.5*(AssemblyHexagonFTF - DuctedAssemblyFTFCreeped))

	# Fractional swelling
	FracSwelling = DuctProperties.swelling

	# Outward swelling to decrease gap
	Swelling = FracSwelling * T / 2	

	# The required inter-assembly gap to achieve the EOL gapmargin
	InterAssemblyGap = 10*(Deflection + CreepDiffGap + Swelling + DuctGapMargin/10)

	# Components to inter-assembly gap in [mm]
	GapMarginPrint  = 10 * GapMargin
	DeflectionPrint = 10 * Deflection
	CreepPrint      = 10 * CreepDiffGap
	SwellingPrint   = 10 * Swelling

	return(DuctThickness, InterAssemblyGap,GapMarginPrint,DeflectionPrint,CreepPrint,SwellingPrint, MaxStress, StotB)		
