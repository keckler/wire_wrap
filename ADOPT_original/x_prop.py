# -*- coding: UTF-8 -*-
import math

## Calculate the density of the steel in the grid plate
#if LowerGridPlateSteel == "T91":

#	SteelDensity = 7.7425 - 0.0003289 * CoolantInletTemperature

#elif LowerGridPlateSteel == "HT9":
#
#	SteelDensity = 7.874 - 3.23 * 1e-4 * CoolantInletTemperature

#elif LowerGridPlateSteel == "D9":
#
#	## TAKEN FROM SS316 ##
#	SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantInletTemperature - 3.894 * 1e-8 * CoolantInletTemperature ** 2

#elif LowerGridPlateSteel == "SS316":
#
#	# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
#	SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantInletTemperature - 3.894 * 1e-8 * CoolantInletTemperature ** 2

#elif LowerGridPlateSteel == "SS304":
#
#	# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
#	SteelDensity = 7.984 - 2.651 * 1e-4 * CoolantInletTemperature - 1.158*1e-7 * CoolantInletTemperature ** 2


# A PRELIMINARY APPROACH TO THE EXTENSION OF THE TRANSURANUS CODE TO 
# THE FUEL ROD PERFORMANCE ANALYSIS OF HLM-COOLED NUCLEAR REACTORS
# L. LUZZI, P. BOTAZZOLI, M. DEVITA, V. DI MARCELLO, G. PASTORE
#
# CladdingYieldStrength   = 833.2 - 2.357 * YStemperature + 4.362 * 1e-3 * YStemperature ** 2 - 2.795 * 1e-6 * YStemperature ** 3
# CladdingYieldStrengthOP = 833.2 - 2.357 * YStemperatureOP + 4.362 * 1e-3 * YStemperatureOP ** 2 - 2.795 * 1e-6 * YStemperatureOP ** 3
# CladdingElasticModulus  = 2.261 * 1e5 - 15.61 * CladEvalT - 5.991 * 1e-2 * CladEvalT ** 2
# 
# # TAKEN FROM HT9
# CladdingPoissions       = 0.3	

#if Cladding == "T91":

#	SerpentCladdingDensity = 7.7425 - 0.0003289 * Temperature

#	if CladdingTemperaturePerturbation == "Void" or CladdingTemperaturePerturbation == "void":

#		SerpentPerturbedCladdingDensity = 1e-30

#	else:

#		SerpentPerturbedCladdingDensity = 7.7425 - 0.0003289 * (Temperature + CladdingTemperaturePerturbation)

#elif Cladding == "HT9":
#
#	SerpentCladdingDensity = 7.874 - 3.23 * 1e-4 * Temperature
#	
#	if CladdingTemperaturePerturbation == "Void" or CladdingTemperaturePerturbation == "void":

#		SerpentPerturbedCladdingDensity = 1e-30

#	else:

#		SerpentPerturbedCladdingDensity = 7.874 - 3.23 * 1e-4 * (Temperature + CladdingTemperaturePerturbation)


#elif Cladding == "D9":

#	## TAKEN FROM SS316 ##
#	SerpentCladdingDensity = 8.804 - 4.209 * 1e-4 * Temperature - 3.894 * 1e-8 * Temperature ** 2
#	
#	if CladdingTemperaturePerturbation == "Void" or CladdingTemperaturePerturbation == "void":

#		SerpentPerturbedCladdingDensity = 1e-30

#	else:

#		SerpentPerturbedCladdingDensity = 8.804 - 4.209 * 1e-4 * (Temperature + CladdingTemperaturePerturbation) - 3.894 * 1e-8 * (Temperature + CladdingTemperaturePerturbation) ** 2

#elif Cladding == "SS316":

#	# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
#	SerpentCladdingDensity =  8.804 - 4.209 * 1e-4 * Temperature - 3.894 * 1e-8 * Temperature ** 2

#	if CladdingTemperaturePerturbation == "Void" or CladdingTemperaturePerturbation == "void":

#		SerpentPerturbedCladdingDensity = 1e-30

#	else:

#		SerpentPerturbedCladdingDensity = 8.804 - 4.209 * 1e-4 * (Temperature + CladdingTemperaturePerturbation) - 3.894 * 1e-8 * (Temperature + CladdingTemperaturePerturbation) ** 2

#elif Cladding == "SS304":

#	# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
#	SerpentCladdingDensity = 7.984 - 2.651 * 1e-4 * Temperature - 1.158*1e-7 * Temperature ** 2

#	if CladdingTemperaturePerturbation == "Void" or CladdingTemperaturePerturbation == "void":

#		SerpentPerturbedCladdingDensity = 1e-30

#	else:

#		SerpentPerturbedCladdingDensity = 7.984 - 2.651 * 1e-4 * (Temperature + CladdingTemperaturePerturbation) - 1.158*1e-7 * (Temperature + CladdingTemperaturePerturbation) ** 2


class nonsolids(object):

	def __init__(self, material, temperature, pressure):

		self.material        = material
		self.temperature     = temperature
		self.pressure        = pressure

		if self.material == "Pb":

			self.density = (11441-1.2795 * self.temperature)/1000
			self.conductivity = 9.2 + 0.011 * self.temperature

		if self.material == "LBE":

			self.density = (10725 - 1.22 * self.temperature)/1000
			self.conductivity = 7.34 + 9.5 * 1e-3 * self.temperature

		if self.material == "Na":

			self.density = (1014 - 0.235 * self.temperature)/1000
			self.conductivity = 104 - 0.047 * self.temperature

		if self.material == "He":

			R   = 8.3144621
			AHe = 4.0026032

			self.density = (self.pressure * self.temperature / 273.15) / R / self.temperature * AHe / 1e6

			# Vargaftik, N. B., & Yakush, L. V. (n.d.). 
			# Temperature dependence of thermal conductivity of helium. 
			# Journal of engineering physics, 32(5), 530–532

			self.conductivity = 0.0476 + 0.3620e-3 * self.temperature - 0.618e-7 * self.temperature ** 2 + 0.718e-11 * self.temperature ** 3

class nonfuelsolidproperties(object):

	def __init__(self, material, temperature, fastflux, stress, dpa, porosity):

		self.material        = material
		self.porosity        = porosity
		self.temperature     = temperature
		self.fastflux        = fastflux
		self.stress          = stress
		self.dpa             = dpa
		self.roomtemperature = 273 + 20
		self.warning         = ""
		self.datasource      = "KAERI"

		if self.temperature < 355+273:

			self.temperature = 355+273

		########################################################################## //// ######## //// #######
		##### HT9 Steel                                                            //// ######## //// #######
		########################################################################## //// ######## //// #######

		if self.material == "HT9":
			
			# HT9 room temperature (20 deg. C = 298K) density reference:
			# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)

			self.roomtemperaturedensity = 7.75 # [g/cm^3]

			# HT9 Poisson's ratio reference:
			# Sofu, T., & Kramer, J. M. (2012). FPIN2: Pre-Failure Metal Fuel Pin Behavior Model, 1–92.

			self.poissons = 0.3

			# HT9 shear modulus reference:
			# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)
	
			self.shearmodulus = 1.043 * 1e5 - 53.78 * self.temperature
			self.shearmodulusminimumtemperature = 273
			self.shearmodulusmaximumtemperature = 1073

			if self.datasource == "ANL":

				# HT9 thermal expansion coefficient reference:
				# Cahalan, J. E., Dunn, F. E., Herzog, J. P., White, A. M., & Wigeland, R. A. (2012). 
				# Reactor Point Kinetics, Decay Heat, and Reactivity Feedback. Argonne National Laboratory, 1–64.
	
				self.averagelinearthermalexpansioncoefficient = 1.62307 * 1e-6 + 2.84714 * 1e-8  * self.temperature - 1.65103 * 1e-11 * self.temperature ** 2 # [1/K]

				# HT9 elastic modulus reference:
				# Sofu, T., & Kramer, J. M. (2012). FPIN2: Pre-Failure Metal Fuel Pin Behavior Model, 1–92.
	
				self.elasticmodulus = 2.12 * 1e5 * (1.144 - 4.856 * 1e-4 * self.temperature)
				self.elasticmodulusminimumtemperature = 293
				self.elasticmodulusmaximumtemperature = 1100

			elif self.datasource == "KAERI":

				# HT9 thermal expansion coefficient (alpha) reference:
				# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)

				self.averagelinearthermalexpansioncoefficient = (-2.191*1e-5 + 5.678 * 1e-6 * self.temperature + 8.111 * 1e-9 * self.temperature ** 2 - 2.576 * 1e-12 * self.temperature ** 3) / (self.temperature - 282.265) # [1/K]

				# HT9 elastic modulus reference:
				# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)
	
				self.elasticmodulus = 2.425 * 1e5 - 102.9 * self.temperature
				self.elasticmodulusminimumtemperature = 273
				self.elasticmodulusmaximumtemperature = 1073

			# HT9 yield strength reference:
			# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)

			self.yieldstrength = 742.48 - 1.4319 * self.temperature + 2.4885 * 1e-3 * self.temperature ** 2 - 1.79203 * 1e-6 * self.temperature ** 3

			#self.yieldstrength = 500.49712 - 0.47358 * self.temperature #+ 0.00102 * self.temperature ** 2 - 1.79203 * 1e-6 * self.temperature ** 3

			#if self.yieldstrength < 0:
			#	print(self.temperature)
			#	print(self.yieldstrength)

			self.yieldstrengthminimumtemperature = 293
			self.yieldstrengthmaximumtemperature = 1059

			# HT9 ultimate tensile strength reference:
			# S. Shikakura et. al, “Development of High-Strength Ferritic/Martensitic Steel for FBR Core Materials (in Japanese), 
			# Journal of the Atomic Energy Society of Japan / Atomic Energy So- ciety of Japan, vol 33 (12), pp. 1157-1170 (1991)

			self.ultimatetensilestrength = 1018 - 0.8911 * self.temperature + 0.0002593 * self.temperature ** 2 + 1.723 * 1e-6 * self.temperature ** 3 - 2.151 * 1e-9 * self.temperature ** 4
			self.ultimatetensilestrengthminimumtemperature = 298
			self.ultimatetensilestrengthmaximumtemperature = 823

			# HT9 relative thermal expansion (L/L0) reference:
			# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)
	
			self.relativethermalexpansion = -2.191 * 1e-3 + 5.678 * 1e-6 * self.temperature + 8.111 * 1e-9 * self.temperature ** 2 - 2.576 * 1e-12 * self.temperature ** 3
			self.relativethermalexpansionminimumtemperature = 273
			self.relativethermalexpansionmaximumtemperature = 1073

			# HT9 thermal conductivity reference:
			# Leibowitz, L., & Blomquist, R. A. (1988). 
			# Thermal conductivity and thermal expansion of stainless steels D9 and HT9. 
			# International Journal of Thermophysics, 9(5), 873–883. doi:10.1007/BF00503252

			if self.temperature <= 1030:

				self.conductivity = 17.622 + 2.428 * 1e-2 * self.temperature - 1.696 * 1e-5 * (self.temperature ** 2)

			else:

				self.conductivity = 12.027 + 1.218 * 1e-2 * self.temperature

			# HT9 density calculated from free thermal expansion
			self.density = self.roomtemperaturedensity / ((1 + self.relativethermalexpansion) ** 3)

			# HT9 irradiation enhanced creep
			# “Metallic Fuel Design Development”, Technical Report (In Korean) KAERI/RR-1887/98 (1998)
			self.creeprate = (1/100) * ((-2.9 + 9.5*1e-3 * (self.temperature - 273))*1e-26 * self.fastflux * (self.stress ** 1.3) \
							 + 1.743 * 1e18 * ((self.stress / self.elasticmodulus) ** 2.3) * math.exp(-36739/self.temperature))

			# HT9 rupture time
			# S.J. Zinkle (2002), Structural Materials Development for MFE and IFE, 
			# Oak Ridge National Laboratory FESAC Development Path Strategic Planning Meeting October 28 2002

			self.rupturetime = (math.exp(-0.2302585093e1 * (0.3537e4 * math.log(self.stress) - 0.45385e5 + 0.30e2 * self.temperature) / self.temperature))

			# Swelling (HT9 KALIMER PAPER)
			self.swelling = (0.6/100) * self.dpa

		########################################################################## //// ######## //// #######
		##### D9 Steel                                                             //// ######## //// #######
		########################################################################## //// ######## //// #######

		if self.material == "D9":

			# D9 room temperature (20 deg. C = 298K) density reference:
			# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976 (correlation taken from SS-316)

			self.roomtemperaturedensity = 8.804 - 4.209 * 1e-4 * self.roomtemperature - 3.894 * 1e-8 * self.roomtemperature ** 2

			# D9 Poisson's ratio reference:
			# Sofu, T., & Kramer, J. M. (2012). FPIN2: Pre-Failure Metal Fuel Pin Behavior Model, 1–92.

			self.poissons = 0.3

			# D9 shear modulus reference: NONE
	
			self.shearmodulus = 0
			self.shearmodulusminimumtemperature = 273
			self.shearmodulusmaximumtemperature = 1073

			# D9 elastic modulus reference:
			# Cahalan, J. E., Dunn, F. E., Herzog, J. P., White, A. M., & Wigeland, R. A. (2012). 
			# Reactor Point Kinetics, Decay Heat, and Reactivity Feedback. Argonne National Laboratory, 1–64.
	
			self.elasticmodulus = 2.261 * 1e5 - 72.29 * self.temperature
			self.elasticmodulusminimumtemperature = 293
			self.elasticmodulusmaximumtemperature = 1100

			# D9 yield strength reference:
			# K. G. Samuel, S. K. Ray, G. Sasikala, Dynamic strain ageing in prior cold worked 15Cr– 15Ni titanium modified stainless steel (Alloy D9). 
			# Journal of Nuclear Materials, vol 355 (1-3), pp. 30–37, doi:10.1016/j.jnucmat.2006.03.016 (2006)

			self.yieldstrength = 598 + 0.9393 * self.temperature - 0.003854 * self.temperature ** 2 + 5.219 * 1e-6 * self.temperature ** 3 - 2.391 * 1e-9 * self.temperature ** 4
			self.yieldstrengthminimumtemperature = 300
			self.yieldstrengthmaximumtemperature = 1050

			# D9 ultimate tensile strength reference:
			# K. G. Samuel, S. K. Ray, G. Sasikala, Dynamic strain ageing in prior cold worked 15Cr– 15Ni titanium modified stainless steel (Alloy D9). 
			# Journal of Nuclear Materials, vol 355 (1-3), pp. 30–37, doi:10.1016/j.jnucmat.2006.03.016 (2006)

			self.ultimatetensilestrength = 1111 - 2.22 * self.temperature + 0.003652 * self.temperature ** 2 - 2.099 * 1e-6 * self.temperature ** 3
			self.ultimatetensilestrengthminimumtemperature = 300
			self.ultimatetensilestrengthmaximumtemperature = 1050

			# D9 relative thermal expansion (L/L0) reference:
			# Leibowitz, L., & Blomquist, R. A. (1988). 
			# Thermal conductivity and thermal expansion of stainless steels D9 and HT9. 
			# International Journal of Thermophysics, 9(5), 873–883. doi:10.1007/BF00503252
	
			self.relativethermalexpansion = (-0.4247 + 1.282 * 1e-3 * self.temperature + 7.362 * 1e-7 * self.temperature ** 2 - 2.069 * 1e-10 * self.temperature ** 3)/100
			self.relativethermalexpansionminimumtemperature = 293
			self.relativethermalexpansionmaximumtemperature = 1300

			# D9 thermal expansion coefficient reference:
			# Cahalan, J. E., Dunn, F. E., Herzog, J. P., White, A. M., & Wigeland, R. A. (2012). 
			# Reactor Point Kinetics, Decay Heat, and Reactivity Feedback. Argonne National Laboratory, 1–64.
	
			self.averagelinearthermalexpansioncoefficient = self.relativethermalexpansion / (self.temperature-self.roomtemperature) # [1/K]

			# D9 thermal conductivity reference:
			# Leibowitz, L., & Blomquist, R. A. (1988). 
			# Thermal conductivity and thermal expansion of stainless steels D9 and HT9. 
			# International Journal of Thermophysics, 9(5), 873–883. doi:10.1007/BF00503252

			if self.temperature <= 1030:

				self.conductivity = 7.598 + 2.391 * 1e-2 * self.temperature - 8.899 * 1e-6 * self.temperature ** 2

			else:

				self.conductivity = 7.260 + 0.01509 * self.temperature						

			# D9 density correlation taken from SS-316
			# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976			
			self.density = 8.804 - 4.209 * 1e-4 * self.temperature - 3.894 * 1e-8 * self.temperature ** 2

			self.creeprate = (0.2630000000e-33 * self.stress ** 0.1063e2 * math.exp(-0.225000e6 / 0.4157e4 / self.temperature))

			self.rupturetime = math.exp(-0.1920000000e-6 * (-0.2917581946e12 + 0.2218294362e11 * math.log(self.stress) + 0.1619005144e9 * self.temperature) / self.temperature)

			# Swelling (HT9 KALIMER PAPER)
			self.swelling = (0.6/100) * self.dpa

		########################################################################## //// ######## //// #######
		##### B4C absorber                                                         //// ######## //// #######
		########################################################################## //// ######## //// #######

		if self.material == "B4C":

			self.density = (1-self.porosity) * (2.52 / (0.9948748015e0 + 0.1719000000e-4 * self.temperature))

class fuelproperties(object):

	def __init__(self, material, temperature, FTDF, expansion, WU, WPu, Wzr, Burnup, mode, indensity, intemperature):

		self.material        = material
		self.temperature     = temperature
		self.temperatureC    = temperature - 273
		self.temperaturediff = temperature - 273
		self.FTDF            = FTDF
		self.expansion       = expansion
		self.WU              = WU
		self.WPu             = WPu
		self.WZr             = Wzr
		self.burnup          = Burnup
		self.warning         = ""
		self.burnupatom      = Burnup * 9.5 / 100
		self.mode            = mode
		self.indensity       = indensity
		self.intemperature   = intemperature

		########################################################################## //// ######## //// #######
		##### Uranium dioxide (UO2)                                                //// ######## //// #######
		########################################################################## //// ######## //// #######

		if self.material == "UO2":

			self.fueltype = "NonMetallic"

			# UO2 room temperature (20 deg. C = 298K) density reference:
			# Fink, J. K. (2000). Thermophysical properties of uranium dioxide. 
			# Journal of Nuclear Materials, 279(1), 1–18. doi:10.1016/S0022-3115(99)00273-1

			self.roomtemperaturedensity = 10.963 # [g/cm^3]

			self.meltingpoint = 3120	
			
			# UO2 thermal conductivity
			# MATPRO-11, Loeb porosity correction not used

			# UO2 conductivity 95% dense:
			# Fink, J. K. (2000). Thermophysical properties of uranium dioxide. 
			# Journal of Nuclear Materials, 279(1), 1–18. doi:10.1016/S0022-3115(99)00273-1			

			t = self.temperature / 1000
			self.conductivity = 100 / (6.548 + 25.533 * t) + (6400/t ** (5/2)) * math.exp(-16.35/t)

			# UO2 emissitivity
			# MATPRO-11

			if self.temperature < 1000:

				self.emissitivity = 0.8707

			elif self.temperature >= 1000 and self.temperature <= 2050:

				self.emissitivity = 1.311 - 4.404 * 1e-4 * self.temperature

			else:

				self.emissitivity = 0.4083

			# UO2 relative thermal expansion (L/L0) reference:
			# MATPRO-11
	
			self.relativethermalexpansion = -4.972 * 1e-4 + 7.107 * 1e-6 * self.temperatureC + 2.581 * 1e-9 * (self.temperatureC ** 2) + 1.140 * 1e-13 * (self.temperatureC ** 3)
			self.relativethermalexpansionminimumtemperature = 273
			self.relativethermalexpansionmaximumtemperature = self.meltingpoint

			# UO2 elastic modulus reference:
			# MATPRO-11		

			self.elasticmodulus = 2.334 * 1e5 * (1 - 2.752 * (1-self.FTDF))*(1 - 1.0915 * 1e-4 * self.temperature)

			# UO2 poisson reference:
			# MATPRO-11

			self.poisson = 0.316

			# UO2 relative thermal expansion (L/L0) reference:
			# Fink, J. K. (2000). Thermophysical properties of uranium dioxide. 
			# Journal of Nuclear Materials, 279(1), 1–18. doi:10.1016/S0022-3115(99)00273-1

			if self.temperature <= 923:

				self.relativethermalexpansion = (9.973*1e-1 + 9.082 * 1e-6 * self.temperature - 2.705 * 1e-10 * (self.temperature ** 2) + 4.391 * 1e-13 * (self.temperature ** 3)) -1
				self.aolr =  (9.973*1e-1 + 9.082 * 1e-6 * self.intemperature - 2.705 * 1e-10 * (self.intemperature ** 2) + 4.391 * 1e-13 * (self.intemperature ** 3))-1

			else:

				self.relativethermalexpansion = (9.9672*1e-1 + 1.179 * 1e-5 * self.temperature - 2.429 * 1e-9 * (self.temperature ** 2) + 1.219 * 1e-12 * (self.temperature ** 3)) -1
				self.aolr = (9.9672*1e-1 + 1.179 * 1e-5 * self.intemperature - 2.429 * 1e-9 * (self.intemperature ** 2) + 1.219 * 1e-12 * (self.intemperature ** 3)) -1

			#print("T")
			#print(self.temperature)
			#print("DL")
			#print(self.relativethermalexpansion)	

			# UO2 average thermal expansion coefficient (alpha) reference:
			# Fink, J. K. (2000). Thermophysical properties of uranium dioxide. 
			# Journal of Nuclear Materials, 279(1), 1–18. doi:10.1016/S0022-3115(99)00273-1

			if self.temperature <= 923:

				self.averagelinearthermalexpansioncoefficient = 9.828 * 1e-6 - 6.930 * 1e-10 * self.temperature + 1.330 * 1e-12 * (self.temperature ** 2) - 1.757 * 1e-17 * (self.temperature ** 3)
	
			else:

				self.averagelinearthermalexpansioncoefficient = 1.1833 * 1e-5 - 5.013 * 1e-9 * self.temperature + 3.756 * 1e-12 * (self.temperature ** 2) - 6.125 * 1e-17 * (self.temperature ** 3)
		
			if self.burnupatom < 7.8:
			
				self.gasrelease = 0.06214 * self.burnupatom + 0.3654
			
			else:
			
				self.gasrelease = 0.85


			if self.mode == "perturbation" and self.expansion == "axial" or self.expansion == "Axial" or self.expansion == "AXIAL":

				self.density = self.indensity / (1 + (self.relativethermalexpansion-self.aolr))
	
			elif self.mode == "perturbation" and self.expansion == "radial" or self.expansion == "Radial" or self.expansion == "RADIAL":
	
				self.density = self.indensity / ((1 + (self.relativethermalexpansion-self.aolr)) ** 2)
	
			elif self.mode == "perturbation" and self.expansion != "axial" and self.expansion != "Axial" and self.expansion != "AXIAL" and self.expansion != "radial" and self.expansion != "Radial" and self.expansion != "RADIAL":

				self.density = self.indensity / ((1 +(self.relativethermalexpansion-self.aolr)) ** 3)	

			else:
	
				self.density = self.roomtemperaturedensity / ((1 + self.relativethermalexpansion) ** 3)	

			self.density = self.density * self.FTDF				
		
		########################################################################## //// ######## //// #######
		##### Uranium-Zirconium and Uranium-Plutonium-Zirconium                    //// ######## //// #######
		########################################################################## //// ######## //// #######

		if self.material == "MetallicZr":

			self.fueltype = "Metallic"

			self.meltingpoint = 1060+273

			A = self.WU*19070
			B = self.WPu*19750
			C = self.WZr*6570
			D = A+B+C
			E = D/1000

			# Metallic-Zr room temperature (20 deg. C = 298K) density reference:
			self.roomtemperaturedensity = E #(1/1000) * ((self.WU*19070) + (self.WPu*19750) + (self.WZr*6570)) # [g/cm^3]	

			# Metallic-Zr relative thermal expansion (L/L0) reference:
			# Sofu, T., & Kramer, J. M. (2012). FPIN2: Pre-Failure Metal Fuel Pin Behavior Model, 1–92.

			if self.WPu == 0:

				if self.temperature <= 900:
	
					self.relativethermalexpansion = 1.695*1e-5 * (self.temperature - 293)
					self.aolr = 1.695*1e-5 * (self.intemperature - 293)
		
				elif self.temperature > 900 and self.temperature < 1000:
	
					self.relativethermalexpansion = 0.0103 + 7 * 1e-5 * (self.temperature - 900)
					self.aolr = 0.0103 + 7 * 1e-5 * (self.intemperature - 900)
	
				else:
	
					self.relativethermalexpansion = 0.0173 + 2.12 * 1e-5 * (self.temperature - 1000)
					self.aolr = 0.0173 + 2.12 * 1e-5 * (self.intemperature - 1000)				

			else:

				if self.temperature <= 864:
	
					self.relativethermalexpansion = 1.67*1e-5 * (self.temperature - 293)
					self.aolr =  1.67*1e-5 * (self.intemperature - 293)
		
				elif self.temperature > 864 and self.temperature < 950:
	
					self.relativethermalexpansion = 0.0095 + 6.7 * 1e-5 * (self.temperature - 864)
					self.aolr = 0.0095 + 6.7 * 1e-5 * (self.intemperature - 864)
	
				else:
	
					self.relativethermalexpansion = 0.0153 + 2.12 * 1e-5 * (self.temperature - 950)
					self.aolr = 0.0153 + 2.12 * 1e-5 * (self.intemperature - 950)

			self.relativethermalexpansionminimumtemperature = 273
			self.relativethermalexpansionmaximumtemperature = self.meltingpoint

			# Metallic Zr thermal conductivity
			# Kalimullah. (2012). SSCOMP: Pre-Transient Characterization of Metallic Fuel Pins, 1–186.

			AM_Pu = 239
			AM_U  = 238
			AM_Zr = 91.22

			M_Pu = self.WPu / AM_Pu
			M_U  = self.WU  / AM_U
			M_Zr = self.WZr / AM_Zr

			M_Fuel = M_Pu + M_U + M_Zr

			Ap = M_Pu / M_Fuel
			Az = M_Zr / M_Fuel
			Au = M_U  / M_Fuel

			Ku   = 0.22173  + 1.8562 * 1e-4 * self.temperature + 1.3278 * 1e-7 * (self.temperature ** 2)
			Ku50 = 0.074766 + 1.6738 * 1e-4 * self.temperature + 1.1599 * 1e-7 * (self.temperature ** 2)

			Kuz = Ku + ( 2 * Az / (Au + Az) ) * (Ku50 - Ku)

			if Ap > 0.16:

				C  = (0.89079 - 1.6757 * Az) - self.temperature * (1.7437 * 1e-3 - 4.0008 * 1e-3 * Az) + (self.temperature ** 2) * (1.9608 * 1e-6 - 3.1043 * 1e-6 * Az)

			else:

				C = 0.63477 - 1.4980 * 1e-3 * self.temperature + 1.8878 * 1e-6 * (self.temperature ** 2)

			Kuzpu = Kuz - C * Ap

			FIMABurnup = self.burnup / 9.5

			if FIMABurnup < 2:

				MPorosity = 0.135 * FIMABurnup
				FuelConductivity = Kuzpu * ((1-MPorosity) / (1 + 1.7 * MPorosity))

			elif FIMABurnup >= 2 and FIMABurnup < 5:

				FuelConductivity = Kuzpu * (0.5 + 0.0667 * (FIMABurnup-2))

			else:
			
				FuelConductivity = Kuzpu * 0.7	

			self.conductivity = 100 * FuelConductivity

			if self.burnup < 0.8:
		
				self.gasrelease = 0
		
			else:
		
				self.gasrelease = 0.8 * (1 - math.exp(-0.556 * self.burnupatom))

			self.averagelinearthermalexpansioncoefficient = self.relativethermalexpansion / (self.temperature - 293) # [1/K]

			Change = 1 * (1 + self.relativethermalexpansion)
			NominalVolume = math.pi * 1 ** 2 * 1
			HVolumeChange = (math.pi * 1 ** 2 * Change) / NominalVolume
			RVolumeChange = (math.pi * (Change) ** 2 * 1) / NominalVolume
			VVolumeChange = (math.pi * (Change) ** 2 * Change) / NominalVolume

			# Metallic-Zr density from thermal expansion

			if self.mode == "perturbation" and self.expansion == "axial" or self.expansion == "Axial" or self.expansion == "AXIAL":

				self.density = self.indensity / (1 + (self.relativethermalexpansion-self.aolr))
	
			elif self.mode == "perturbation" and self.expansion == "radial" or self.expansion == "Radial" or self.expansion == "RADIAL":
	
				self.density = self.indensity / ((1 + (self.relativethermalexpansion-self.aolr)) ** 2)
	
			elif self.mode == "perturbation" and self.expansion != "axial" and self.expansion != "Axial" and self.expansion != "AXIAL" and self.expansion != "radial" and self.expansion != "Radial" and self.expansion != "RADIAL":

				self.density = self.indensity / ((1 +(self.relativethermalexpansion-self.aolr)) ** 3)	

			else:

				self.density = self.roomtemperaturedensity / ((1 + self.relativethermalexpansion) ** 3)	
