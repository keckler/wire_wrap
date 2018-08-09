# -*- coding: UTF-8 -*-

import math
#from   pylab import *

def axialcoolant(MassFlowArea, InteriorChannelCoolantVelocity, CoolantInletDensity, FuelLength, AxialTemperaturePoints, \
	             CosinePinAxialPowerPeaking, CoolantInletHeatCapacity, SingleInteriorChannelHydraulicDiameter, \
	             BelowCoreChannelLength, CoolantInletTemperature, PeakPinPeakLinearPower, Pitch, Diameter, \
	             SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, EdgeChannelCoolantVelocity, \
	             CornerChannelCoolantVelocity, SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, EdgePinPeakLinearPower,
	             CornerPinPeakLinearPower, Name, Coolant, PinAxialPowerPeaking, mlabpath, RadialPowerPeaking,
	              SingleInteriorChannelFlowArea):

	#print("SingleInteriorChannelFlowArea")
	#print(SingleInteriorChannelFlowArea * 100 ** 2)
	#print("InteriorChannelCoolantVelocity")
	#print(InteriorChannelCoolantVelocity * 100)
	#print("CoolantInletDensity")
	#print(CoolantInletDensity)
	#print("CoolantInletHeatCapacity")
	#print(CoolantInletHeatCapacity)

	# The mass flow in the peak power channel of the core (which has the highest flow velocity)
	PeakChannelMassFlow = SingleInteriorChannelFlowArea * InteriorChannelCoolantVelocity * CoolantInletDensity

	#print("PeakChannelMassFlow")
	#print(PeakChannelMassFlow*1000)

	# Edge channel mass flow
	EdgeChannelMassFlow = SingleEdgeChannelFlowArea * EdgeChannelCoolantVelocity * CoolantInletDensity

	# Corner channel mass flow
	CornerChannelMassFlow = SingleCornerChannelFlowArea * CornerChannelCoolantVelocity * CoolantInletDensity

	# The mass flow in an interior channel of an assembly producing core-averaged assembly power
	AverageInteriorChannelMassFlow = MassFlowArea * InteriorChannelCoolantVelocity * CoolantInletDensity / RadialPowerPeaking

	# The mass flow in an edge channel of an assembly producing core-averaged assembly power
	AverageCornerChannelMassFlow = SingleCornerChannelFlowArea * CornerChannelCoolantVelocity * CoolantInletDensity / RadialPowerPeaking

	# The mass flow in a corner channel of an assembly producing core-averaged assembly power
	AverageCornerChannelMassFlow = SingleCornerChannelFlowArea * CornerChannelCoolantVelocity * CoolantInletDensity / RadialPowerPeaking
	
	# Empty list for collecting temperature evaluation points
	TemperaturePoints  = []
	TemperaturePointsZ = []
	
	# Create a file to plot the temperature distribution in Matlab
	ct    = open(mlabpath + "/coolant_temperature.m", 'w')
	cte   = open(mlabpath + "/coolant_edgechannel_temperature.m", 'w')
	ctc   = open(mlabpath + "/coolant_cornerchannel_temperature.m", 'w')
	cto   = open(mlabpath + "/cladding_outer_temperature.m", 'w')
	cti   = open(mlabpath + "/cladding_inner_temperature.m", 'w')
	cgi   = open(mlabpath + "/fuel_outer_temperature.m", 'w')
	cgf   = open(mlabpath + "/fuel_inner_temperature.m", 'w')
	pdrop = open(mlabpath + "/pressuredrop.m", 'w')
	
	# Write the z (axial) axis
	ct.write("z = [")
	cte.write("z = [")
	ctc.write("z = [")
	cto.write("z = [")
	cti.write("z = [")
	cgi.write("z = [")
	cgf.write("z = [")

	pdrop.write("corez = [")
	
	# Starting point for coolant temperature evaluation
	z = -FuelLength/2

	# Calculate until reaching the top of fuel (here, the axial mid-level of fuel is z = 0)
	while z < FuelLength/2 + FuelLength/AxialTemperaturePoints:
	
		# Rounding the number
		z = round(z,5)
	
		# Collect the evalution point to the list
		TemperaturePoints.append(z)
		TemperaturePointsZ.append(z + FuelLength/2)

		# Write the results to MATLAB
		ct.write("\n")
		ct.write(str(z) + ",")
		cte.write("\n")
		cte.write(str(z) + ",")
		ctc.write("\n")
		ctc.write(str(z) + ",")
		cto.write("\n")
		cto.write(str(z) + ",")
		cti.write("\n")
		cti.write(str(z) + ",")
		cgi.write("\n")
		cgi.write(str(z) + ",")
		cgf.write("\n")
		cgf.write(str(z) + ",")
		pdrop.write("\n")
		pdrop.write(str(z + FuelLength/2 + BelowCoreChannelLength) + ",")
	
		# Increment the evaluation point
		z += FuelLength/AxialTemperaturePoints


	# End the variables in the MATLAB files
	ct.write("];")
	ct.write("\n")

	cte.write("];")
	cte.write("\n")

	ctc.write("];")
	ctc.write("\n")
	
	cto.write("];")
	cto.write("\n")

	cti.write("];")
	cti.write("\n")
	cti.close()

	cgi.write("];")
	cgi.write("\n")
	cgi.close()

	cgf.write("];")
	cgf.write("\n")
	cgf.close()

	pdrop.write("];")
	pdrop.write("\n")
	pdrop.close()
	
	# Start variable for coolant temperatures in MATLAB file
	ct.write("cz = [")

	# Start variable for edge coolant temperatures in MATLAB file
	cte.write("cze = [")

	# Start variable for corner coolant temperatures in MATLAB file
	ctc.write("czc = [")
	
	# Start variable for outer cladding temperatures in MATLAB file
	cto.write("cot = [")
	
	# Create empty dictionaries for saving axial coolant information
	CoolantAxialTemperature                     = {}
	CoolantAxialEdgeTemperature                 = {}
	CoolantAxialEdgeHeatCapacity 				= {}
	CoolantAxialEdgeDensity 					= {}
	CoolantAxialEdgeDynamicViscosity		    = {}
	CoolantAxialEdgeConductivity 				= {}
	CoolantAxialEdgeKinematicViscosity 			= {}
	CoolantAxialCornerTemperature			    = {}
	CoolantAxialCornerHeatCapacity			    = {}
	CoolantAxialCornerDensity 					= {}
	CoolantAxialCornerDynamicViscosity		    = {}
	CoolantAxialCornerConductivity 				= {}
	CoolantAxialCornerKinematicViscosity		= {}
	CoolantAxialHeatCapacity                    = {}
	CoolantAxialDensity                         = {}
	CoolantAxialDynamicViscosity                = {}
	CoolantAxialConductivity                    = {}
	CoolantAxialKinematicViscosity              = {}
	CoolantAxialInteriorPeclet                  = {}
	CoolantAxialEdgePeclet                      = {}
	CoolantAxialCornerPeclet                    = {}
	CoolantAxialInteriorNusselt                 = {}
	CoolantAxialEdgeNusselt                     = {}
	CoolantAxialCornerNusselt                   = {}
	CoolantAxialInteriorHeatTransferCoefficient = {}
	CoolantAxialEdgeHeatTransferCoefficient     = {}
	CoolantAxialCornerHeatTransferCoefficient   = {}
	CoolantAxialInteriorReynolds                = {}
	CoolantAxialEdgeReynolds                    = {}
	CoolantAxialCornerReynolds                  = {}
	CoolantAxialAverageInteriorReynolds         = {}
	CoolantAxialAverageEdgeReynolds             = {}
	CoolantAxialAverageCornerReynolds           = {}

	# Create empty dictionary for saving axial outer cladding temperature
	CladdingOuterWallAxialTemperature   = {}
	PeakCladdingOuterWallTemperature    = []

	# Create lists for matplotlib
	CoolantTemperatureZ2 = []
	CoolantEdgeTemperatureZ2 = []
	CoolantEdgeHeatCapacityZ2 = []
	CoolantEdgeDensityZ2 = []
	CoolantEdgeDynamicViscosityZ2 = []
	CoolantEdgeConductivityZ2 = []
	CoolantEdgeKinematicViscosityZ2 = []
	CoolantCornerTemperatureZ2 = []
	CoolantCornerHeatCapacityZ2 = []
	CoolantCornerDensityZ2 = []
	CoolantCornerDynamicViscosityZ2 = []
	CoolantCornerConductivityZ2 = []
	CoolantCornerKinematicViscosityZ2 = []
	CoolantHeatCapacityZ2 = []
	CoolantDensityZ2 = []
	CoolantDynamicViscosityZ2 = []
	CoolantConductivityZ2 = []
	CoolantKinematicViscosityZ2 = []
	CoolantInteriorPecletZ2 = []
	CoolantEdgePecletZ2 = []
	CoolantCornerPecletZ2 = []
	CoolantInteriorNusseltZ2 = []
	CoolantEdgeNusseltZ2 = []
	CoolantCornerNusseltZ2 = []
	CoolantInteriorHeatTransferCoefficientZ2 = []
	CoolantEdgeHeatTransferCoefficientZ2 = []
	CoolantCornerHeatTransferCoefficientZ2 = []
	CoolantInteriorReynoldsZ2 = []
	CoolantEdgeReynoldsZ2 = []
	CoolantCornerReynoldsZ2 = []
	CladdingOuterWallTemperatureZ2 = []

	for z in TemperaturePoints:
		
		if PinAxialPowerPeaking < (math.pi/2):

			# Calculate coolant temperature at axial position z
			CoolantTemperatureZ       = CoolantInletTemperature + (PeakPinPeakLinearPower/2) * FuelLength * CosinePinAxialPowerPeaking * (math.sin(math.pi * z / FuelLength / CosinePinAxialPowerPeaking) + math.sin(math.pi / CosinePinAxialPowerPeaking / 2)) / PeakChannelMassFlow / CoolantInletHeatCapacity / math.pi

			# Calculate coolant temperature at axial position z
			CoolantEdgeTemperatureZ   = CoolantInletTemperature + (EdgePinPeakLinearPower/2) * FuelLength * CosinePinAxialPowerPeaking * (math.sin(math.pi * z / FuelLength / CosinePinAxialPowerPeaking) + math.sin(math.pi / CosinePinAxialPowerPeaking / 2)) / EdgeChannelMassFlow / CoolantInletHeatCapacity / math.pi
	
			# Calculate coolant temperature at axial position z
			CoolantCornerTemperatureZ = CoolantInletTemperature + (CornerPinPeakLinearPower/6) * FuelLength * CosinePinAxialPowerPeaking * (math.sin(math.pi * z / FuelLength / CosinePinAxialPowerPeaking) + math.sin(math.pi / CosinePinAxialPowerPeaking / 2)) / CornerChannelMassFlow / CoolantInletHeatCapacity / math.pi

		else:

			CoolantTemperatureZ       = CoolantInletTemperature + PeakPinPeakLinearPower * (-0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi / CosinePinAxialPowerPeaking / 0.2e1) + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * math.pi * FuelLength - 0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) + 0.2e1 * math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * z * math.pi) / (-0.1e1 + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / PeakChannelMassFlow / CoolantInletHeatCapacity / 0.2e1

			CoolantEdgeTemperatureZ   = CoolantInletTemperature + EdgePinPeakLinearPower * (-0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi / CosinePinAxialPowerPeaking / 0.2e1) + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * math.pi * FuelLength - 0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) + 0.2e1 * math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * z * math.pi) / (-0.1e1 + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / EdgeChannelMassFlow / CoolantInletHeatCapacity / 0.2e1

			CoolantCornerTemperatureZ = CoolantInletTemperature + CornerPinPeakLinearPower * (-0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi / CosinePinAxialPowerPeaking / 0.2e1) + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * math.pi * FuelLength - 0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) + 0.2e1 * math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * z * math.pi) / (-0.1e1 + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / CornerChannelMassFlow / CoolantInletHeatCapacity / 0.2e1

		if Coolant == "Pb":
	
			# Coolant heat capacity in J/kg-K
			CoolantHeatCapacity     = 0.1762e3 - 0.4926e-1 * CoolantTemperatureZ + 0.1544000000e-4 * CoolantTemperatureZ ** 2 - 0.1524e7 / CoolantTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantDensity          = 11441-1.2795 * CoolantTemperatureZ 
			
			# Coolant  dynamic visocity in Pa * s
			CoolantDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantTemperatureZ)
		
			# Coolant thermal conductivity in W/m*K
			CoolantConductivity     = 9.2 + 0.011 * CoolantTemperatureZ 
	
			#######################################################################################################
	
			# Coolant heat capacity in J/kg-K
			CoolantEdgeHeatCapacity     = 0.1762e3 - 0.4926e-1 * CoolantEdgeTemperatureZ + 0.1544000000e-4 * CoolantEdgeTemperatureZ ** 2 - 0.1524e7 / CoolantEdgeTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantEdgeDensity          = 11441-1.2795 * CoolantEdgeTemperatureZ 
			
			# Coolant  dynamic visocity in Pa * s
			CoolantEdgeDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantEdgeTemperatureZ)
		
			# Coolant thermal conductivity in W/m*K
			CoolantEdgeConductivity     = 9.2 + 0.011 * CoolantEdgeTemperatureZ 
	
			#######################################################################################################
	
			# Coolant heat capacity in J/kg-K
			CoolantCornerHeatCapacity     = 0.1762e3 - 0.4926e-1 * CoolantCornerTemperatureZ + 0.1544000000e-4 * CoolantCornerTemperatureZ ** 2 - 0.1524e7 / CoolantCornerTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantCornerDensity          = 11441-1.2795 * CoolantCornerTemperatureZ 
			
			# Coolant  dynamic visocity in Pa * s
			CoolantCornerDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantCornerTemperatureZ)
		
			# Coolant thermal conductivity in W/m*K
			CoolantCornerConductivity     = 9.2 + 0.011 * CoolantCornerTemperatureZ 


		elif Coolant == "Na":


			# Coolant heat capacity in J/kg-K
			CoolantHeatCapacity         = -3.001 * 1e6 * CoolantTemperatureZ ** (-2) + 1658 - 0.8479 * CoolantTemperatureZ + 4.454 * 1e-4 * CoolantTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantDensity              = 1014 - 0.235 * CoolantTemperatureZ
			
			# Dynamic visocity in Pa * s
			CoolantDynamicViscosity     = math.exp((556.835/CoolantTemperatureZ) - 0.3985 * math.log(CoolantTemperatureZ) - 6.4406)
			
			# Thermal conductivity in W/m*K
			CoolantConductivity         = 104 - 0.047 * CoolantTemperatureZ

			#######################################################################################################

			# Coolant heat capacity in J/kg-K
			CoolantEdgeHeatCapacity     = -3.001 * 1e6 * CoolantEdgeTemperatureZ ** (-2) + 1658 - 0.8479 * CoolantEdgeTemperatureZ + 4.454 * 1e-4 * CoolantEdgeTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantEdgeDensity          = 1014 - 0.235 * CoolantEdgeTemperatureZ
			
			# Dynamic visocity in Pa * s
			CoolantEdgeDynamicViscosity = math.exp((556.835/CoolantEdgeTemperatureZ) - 0.3985 * math.log(CoolantEdgeTemperatureZ) - 6.4406)
			
			# Thermal conductivity in W/m*K
			CoolantEdgeConductivity     = 104 - 0.047 * CoolantEdgeTemperatureZ

			#######################################################################################################

			# Coolant heat capacity in J/kg-K
			CoolantCornerHeatCapacity     = -3.001 * 1e6 * CoolantCornerTemperatureZ ** (-2) + 1658 - 0.8479 * CoolantCornerTemperatureZ + 4.454 * 1e-4 * CoolantCornerTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantCornerDensity          = 1014 - 0.235 * CoolantCornerTemperatureZ
			
			# Dynamic visocity in Pa * s
			CoolantCornerDynamicViscosity = math.exp((556.835/CoolantCornerTemperatureZ) - 0.3985 * math.log(CoolantCornerTemperatureZ) - 6.4406)
			
			# Thermal conductivity in W/m*K
			CoolantCornerConductivity     = 104 - 0.047 * CoolantCornerTemperatureZ


		elif Coolant == "LBE":

			#  coolant heat capacity in J/kg-K
			CoolantHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantTemperatureZ + 7.183 * 1e6 * CoolantTemperatureZ ** (-2)
			
			#  coolant density in kg/m^3
			CoolantDensity          = 10725 - 1.22 * CoolantTemperatureZ
			
			#  dynamic visocity in Pa * s
			CoolantDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantTemperatureZ)
			
			#  thermal conductivity in W/m*K
			CoolantConductivity     = 7.34 + 9.5 * 1e-3 * CoolantTemperatureZ

			#######################################################################################################

			#  coolant heat capacity in J/kg-K
			CoolantEdgeHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantEdgeTemperatureZ + 7.183 * 1e6 * CoolantEdgeTemperatureZ ** (-2)
			
			#  coolant density in kg/m^3
			CoolantEdgeDensity          = 10725 - 1.22 * CoolantEdgeTemperatureZ
			
			#  dynamic visocity in Pa * s
			CoolantEdgeDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantEdgeTemperatureZ)
			
			#  thermal conductivity in W/m*K
			CoolantEdgeConductivity     = 7.34 + 9.5 * 1e-3 * CoolantEdgeTemperatureZ

			#######################################################################################################

			#  coolant heat capacity in J/kg-K
			CoolantCornerHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantCornerTemperatureZ + 7.183 * 1e6 * CoolantCornerTemperatureZ ** (-2)
			
			#  coolant density in kg/m^3
			CoolantCornerDensity          = 10725 - 1.22 * CoolantCornerTemperatureZ
			
			#  dynamic visocity in Pa * s
			CoolantCornerDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantCornerTemperatureZ)
			
			#  thermal conductivity in W/m*K
			CoolantCornerConductivity     = 7.34 + 9.5 * 1e-3 * CoolantCornerTemperatureZ			

		##############################################################################################################################
		##############################################################################################################################
	
		# Coolant kinematic visocity in Pa * s / kg
		CoolantKinematicViscosity = CoolantDynamicViscosity / CoolantDensity

		# Coolant kinematic visocity in Pa * s / kg
		CoolantEdgeKinematicViscosity = CoolantEdgeDynamicViscosity / CoolantEdgeDensity

		# Coolant kinematic visocity in Pa * s / kg
		CoolantCornerKinematicViscosity = CoolantCornerDynamicViscosity / CoolantCornerDensity

		##############################################################################################################################	
		######## Channel Peclet numbers ##############################################################################################
		##############################################################################################################################

		# Coolant interior channel Peclet number
		CoolantInteriorPeclet = CoolantDensity * InteriorChannelCoolantVelocity * SingleInteriorChannelHydraulicDiameter / CoolantConductivity

		# Coolant edge channel Peclet number
		CoolantEdgePeclet     = CoolantEdgeDensity * EdgeChannelCoolantVelocity * SingleEdgeChannelHydraulicDiameter / CoolantEdgeConductivity
	
		# Coolant corner channel Peclet number
		CoolantCornerPeclet   = CoolantEdgeDensity * CornerChannelCoolantVelocity * SingleCornerChannelHydraulicDiameter / CoolantCornerConductivity

		##############################################################################################################################	
		######## Channel Nusselt numbers #############################################################################################
		##############################################################################################################################

		# Coolant interior channel Nusselt number
		CoolantInteriorNusselt = 0.047 * (1 - math.exp(-3.8 * Pitch / Diameter + 3.8)) * (CoolantInteriorPeclet ** 0.77 + 250)

		# Coolant edge channel Nusselt number
		CoolantEdgeNusselt     = 0.047 * (1 - math.exp(-3.8 * Pitch / Diameter + 3.8)) * (CoolantEdgePeclet     ** 0.77 + 250)

		# Coolant corner channel Nusselt number
		CoolantCornerNusselt   = 0.047 * (1 - math.exp(-3.8 * Pitch / Diameter + 3.8)) * (CoolantCornerPeclet   ** 0.77 + 250)
	
		##############################################################################################################################	
		######## Channel heat transfer coefficients ##################################################################################
		##############################################################################################################################

		# Coolant interior channel heat transfer coefficient (W/m^2)
		InteriorHeatTransferCoefficient = CoolantInteriorNusselt * CoolantConductivity       / SingleInteriorChannelHydraulicDiameter

		# Coolant edge channel heat transfer coefficient (W/m^2)
		EdgeHeatTransferCoefficient     = CoolantEdgeNusselt     * CoolantEdgeConductivity   / SingleEdgeChannelHydraulicDiameter

		# Coolant corner channel heat transfer coefficient (W/m^2)
		CornerHeatTransferCoefficient   = CoolantCornerNusselt   * CoolantCornerConductivity / SingleCornerChannelHydraulicDiameter
		
		##############################################################################################################################	
		######## Channel Reynolds numbers ############################################################################################
		##############################################################################################################################

		# Coolant interior channel Reynolds number
		CoolantInteriorReynolds = InteriorChannelCoolantVelocity * SingleInteriorChannelHydraulicDiameter / CoolantKinematicViscosity
	
		# Coolant edge channel Reynolds number
		CoolantEdgeReynolds     = EdgeChannelCoolantVelocity     * SingleEdgeChannelHydraulicDiameter     / CoolantEdgeKinematicViscosity

		# Coolant corner channel Reynolds number
		CoolantCornerReynolds   = CornerChannelCoolantVelocity   * SingleCornerChannelHydraulicDiameter   / CoolantCornerKinematicViscosity

		##############################################################################################################################	
		######## Average channel Reynolds numbers ####################################################################################
		##############################################################################################################################

		# Coolant interior channel Reynolds number
		AverageCoolantInteriorReynolds = InteriorChannelCoolantVelocity * SingleInteriorChannelHydraulicDiameter / CoolantKinematicViscosity / RadialPowerPeaking
	
		# Coolant edge channel Reynolds number
		AverageCoolantEdgeReynolds     = EdgeChannelCoolantVelocity     * SingleEdgeChannelHydraulicDiameter     / CoolantEdgeKinematicViscosity / RadialPowerPeaking

		# Coolant corner channel Reynolds number
		AverageCoolantCornerReynolds   = CornerChannelCoolantVelocity   * SingleCornerChannelHydraulicDiameter   / CoolantCornerKinematicViscosity / RadialPowerPeaking


		##############################################################################################################################	
		######## Collect axial information ###########################################################################################
		##############################################################################################################################

		# Collect axial position and temperature information
		CAT_Temperature          = {z : CoolantTemperatureZ}
	
		# Collect axial position and heat capacity
		CAT_HeatCapacity         = {z : CoolantHeatCapacity}	
	
		# Collect axial position and density
		CAT_Density              = {z : CoolantDensity}	
	
		# Collect axial position and dynamic viscosity
		CAT_DynamicViscosity     = {z : CoolantDynamicViscosity}	
	
		# Collect axial position and thermal conductivity
		CAT_Conductivity         = {z : CoolantConductivity}	
	 
		# Collect axial position and kinematic viscosity
		CAT_KinematicViscosity   = {z : CoolantKinematicViscosity}		

		# Collect axial position and temperature information
		CAT_EdgeTemperature          = {z : CoolantEdgeTemperatureZ}
	
		# Collect axial position and heat capacity
		CAT_EdgeHeatCapacity         = {z : CoolantEdgeHeatCapacity}	
	
		# Collect axial position and density
		CAT_EdgeDensity              = {z : CoolantEdgeDensity}	
	
		# Collect axial position and dynamic viscosity
		CAT_EdgeDynamicViscosity     = {z : CoolantEdgeDynamicViscosity}	
	
		# Collect axial position and thermal conductivity
		CAT_EdgeConductivity         = {z : CoolantEdgeConductivity}	
	 
		# Collect axial position and kinematic viscosity
		CAT_EdgeKinematicViscosity   = {z : CoolantEdgeKinematicViscosity}	
	
		# Collect axial position and temperature information
		CAT_CornerTemperature          = {z : CoolantCornerTemperatureZ}
	
		# Collect axial position and heat capacity
		CAT_CornerHeatCapacity         = {z : CoolantCornerHeatCapacity}	
	
		# Collect axial position and density
		CAT_CornerDensity              = {z : CoolantCornerDensity}	
	
		# Collect axial position and dynamic viscosity
		CAT_CornerDynamicViscosity     = {z : CoolantCornerDynamicViscosity}	
	
		# Collect axial position and thermal conductivity
		CAT_CornerConductivity         = {z : CoolantCornerConductivity}	
	 
		# Collect axial position and kinematic viscosity
		CAT_CornerKinematicViscosity   = {z : CoolantCornerKinematicViscosity}	

		# Collect interior channel axial position and peclet number
		CAT_InteriorPeclet       = {z : CoolantInteriorPeclet}

		# Collect edge channel axial position and peclet number
		CAT_EdgePeclet           = {z : CoolantEdgePeclet}

		# Collect corner channel axial position and peclet number
		CAT_CornerPeclet         = {z : CoolantCornerPeclet}

		# Collect interior channel axial position and nusselt number
		CAT_InteriorNusselt      = {z : CoolantInteriorNusselt}

		# Collect edge channel axial position and nusselt number
		CAT_EdgeNusselt          = {z : CoolantEdgeNusselt}

		# Collect corner channel axial position and nusselt number
		CAT_CornerNusselt        = {z : CoolantCornerNusselt}
	
		# Collect interior channel axial position and heat transfer coefficient
		CAT_InteriorHeatTransfer = {z : InteriorHeatTransferCoefficient}

		# Collect edge channel axial position and heat transfer coefficient
		CAT_EdgeHeatTransfer     = {z : EdgeHeatTransferCoefficient}

		# Collect corner channel axial position and heat transfer coefficient
		CAT_CornerHeatTransfer   = {z : CornerHeatTransferCoefficient}
	
		# Collect interior channel axial position and renolds numbers
		CAT_InteriorReynolds     = {z : CoolantInteriorReynolds}

		# Collect edge channel axial position and renolds numbers
		CAT_EdgeReynolds         = {z : CoolantEdgeReynolds}

		# Collect corner channel axial position and renolds numbers
		CAT_CornerReynolds       = {z : CoolantCornerReynolds}

		# Collect interior channel axial position and renolds numbers
		CAT_AverageInteriorReynolds = {z : AverageCoolantInteriorReynolds}

		# Collect edge channel axial position and renolds numbers
		CAT_AverageEdgeReynolds     = {z : AverageCoolantEdgeReynolds}

		# Collect corner channel axial position and renolds numbers
		CAT_AverageCornerReynolds   = {z : AverageCoolantCornerReynolds}
	
		# Update the dictionary with the information
		CoolantAxialTemperature.update(CAT_Temperature)
		CoolantAxialHeatCapacity.update(CAT_HeatCapacity)
		CoolantAxialDensity.update(CAT_Density)
		CoolantAxialDynamicViscosity.update(CAT_DynamicViscosity)
		CoolantAxialConductivity.update(CAT_Conductivity)
		CoolantAxialKinematicViscosity.update(CAT_KinematicViscosity)

		CoolantAxialEdgeTemperature.update(CAT_EdgeTemperature)
		CoolantAxialEdgeHeatCapacity.update(CAT_EdgeHeatCapacity)
		CoolantAxialEdgeDensity.update(CAT_EdgeDensity)
		CoolantAxialEdgeDynamicViscosity.update(CAT_EdgeDynamicViscosity)
		CoolantAxialEdgeConductivity.update(CAT_EdgeConductivity)
		CoolantAxialEdgeKinematicViscosity.update(CAT_EdgeKinematicViscosity)		

		CoolantAxialCornerTemperature.update(CAT_CornerTemperature)
		CoolantAxialCornerHeatCapacity.update(CAT_CornerHeatCapacity)
		CoolantAxialCornerDensity.update(CAT_CornerDensity)
		CoolantAxialCornerDynamicViscosity.update(CAT_CornerDynamicViscosity)
		CoolantAxialCornerConductivity.update(CAT_CornerConductivity)
		CoolantAxialCornerKinematicViscosity.update(CAT_CornerKinematicViscosity)		

		CoolantAxialInteriorPeclet.update(CAT_InteriorPeclet)
		CoolantAxialEdgePeclet.update(CAT_EdgePeclet)
		CoolantAxialCornerPeclet.update(CAT_CornerPeclet)

		CoolantAxialInteriorNusselt.update(CAT_InteriorNusselt)
		CoolantAxialEdgeNusselt.update(CAT_EdgeNusselt)
		CoolantAxialCornerNusselt.update(CAT_CornerNusselt)

		CoolantAxialInteriorHeatTransferCoefficient.update(CAT_InteriorHeatTransfer)
		CoolantAxialEdgeHeatTransferCoefficient.update(CAT_EdgeHeatTransfer)
		CoolantAxialCornerHeatTransferCoefficient.update(CAT_CornerHeatTransfer)

		CoolantAxialInteriorReynolds.update(CAT_InteriorReynolds)
		CoolantAxialEdgeReynolds.update(CAT_EdgeReynolds)
		CoolantAxialCornerReynolds.update(CAT_CornerReynolds)
	
		CoolantAxialAverageInteriorReynolds.update(CAT_AverageInteriorReynolds)
		CoolantAxialAverageEdgeReynolds.update(CAT_AverageEdgeReynolds)
		CoolantAxialAverageCornerReynolds.update(CAT_AverageCornerReynolds)

		# Write the temperature data to MATLAB file
		ct.write("\n")
		ct.write(str(CoolantTemperatureZ-273.15) + ",")
	
		# Write the temperature data to MATLAB file
		cte.write("\n")
		cte.write(str(CoolantEdgeTemperatureZ-273.15) + ",")

		# Write the temperature data to MATLAB file
		ctc.write("\n")
		ctc.write(str(CoolantCornerTemperatureZ-273.15) + ",")

		if PinAxialPowerPeaking < (math.pi/2):

			# Outer wall cladding temperature calculation in the interior channel
			CladdingOuterWallTemperature = CoolantTemperatureZ + (PeakPinPeakLinearPower / (math.pi * Diameter * InteriorHeatTransferCoefficient)) * math.cos(math.pi * z / (FuelLength * CosinePinAxialPowerPeaking))
	
		else:

			CladdingOuterWallTemperature = CoolantTemperatureZ  + PeakPinPeakLinearPower * (math.cos(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / (0.1e1 - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / (Diameter/2) / InteriorHeatTransferCoefficient / 0.2e1;

		# Collect axial cladding outer wall temperature
		COW_Temperature = {z : CladdingOuterWallTemperature}
	
		# Update cladding outer wall temperature dictionary
		CladdingOuterWallAxialTemperature.update(COW_Temperature)
	
		# Collect data to estimate the peak cladding outer wall temperature
		PeakCladdingOuterWallTemperature.append(CladdingOuterWallTemperature.real)
	
		# Write data to MATLAB
		cto.write("\n")
		cto.write(str(CladdingOuterWallTemperature-273.15) + ",")

		## Gather things for matplotlib
		CoolantTemperatureZ2.append(CoolantTemperatureZ-273.15)
		CoolantEdgeTemperatureZ2.append(CoolantEdgeTemperatureZ-273.15)
		CoolantCornerTemperatureZ2.append(CoolantCornerTemperatureZ-273.15)

		CladdingOuterWallTemperatureZ2.append(CladdingOuterWallTemperature-273.15)	

		CoolantHeatCapacityZ2.append(CoolantHeatCapacity)
		CoolantEdgeHeatCapacityZ2.append(CoolantEdgeHeatCapacity)
		CoolantCornerHeatCapacityZ2.append(CoolantHeatCapacity)	

		CoolantDensityZ2.append(CoolantDensity)
		CoolantEdgeDensityZ2.append(CoolantEdgeDensity)
		CoolantCornerDensityZ2.append(CoolantCornerDensity)

		CoolantDynamicViscosityZ2.append(CoolantDynamicViscosity)
		CoolantEdgeDynamicViscosityZ2.append(CoolantDynamicViscosity)
		CoolantCornerDynamicViscosityZ2.append(CoolantCornerDynamicViscosity)

		CoolantConductivityZ2.append(CoolantConductivity)
		CoolantEdgeConductivityZ2.append(CoolantEdgeConductivity)
		CoolantCornerConductivityZ2.append(CoolantCornerConductivity)		

		CoolantKinematicViscosityZ2.append(CoolantKinematicViscosity)
		CoolantEdgeKinematicViscosityZ2.append(CoolantEdgeKinematicViscosity)
		CoolantCornerKinematicViscosityZ2.append(CoolantCornerKinematicViscosity)

		CoolantInteriorPecletZ2.append(CoolantInteriorPeclet)
		CoolantEdgePecletZ2.append(CoolantEdgePeclet)
		CoolantCornerPecletZ2.append(CoolantCornerPeclet)

		CoolantInteriorNusseltZ2.append(CoolantInteriorNusselt)
		CoolantEdgeNusseltZ2.append(CoolantEdgeNusselt)
		CoolantCornerNusseltZ2.append(CoolantCornerNusselt)

		CoolantInteriorHeatTransferCoefficientZ2.append(InteriorHeatTransferCoefficient)
		CoolantEdgeHeatTransferCoefficientZ2.append(EdgeHeatTransferCoefficient)
		CoolantCornerHeatTransferCoefficientZ2.append(CornerHeatTransferCoefficient)

		CoolantInteriorReynoldsZ2.append(CoolantInteriorReynolds)
		CoolantEdgeReynoldsZ2.append(CoolantEdgeReynolds)
		CoolantCornerReynoldsZ2.append(CoolantCornerReynolds)
	
	# Define the peak cladding outer wall temperature
	PeakCladdingOuterWallTemperature = max(PeakCladdingOuterWallTemperature)
	
	# Figure out where axially the peak cladding outer wall temperature occurs
	for k,v in CladdingOuterWallAxialTemperature.items():
		if v == PeakCladdingOuterWallTemperature:
			PeakCladdingOuterWallTemperateAxialPosition = k
	
	# Close the variable, add plotting, and close files
	ct.write("];")
	ct.close()

	cte.write("];")
	cte.close()
	
	ctc.write("];")
	ctc.close()

	cto.write("];")
	cto.close()

	EdgeChannelOutletTemperature  = CoolantEdgeTemperatureZ
	CornerChannelOutletTemperature = CoolantCornerTemperatureZ


	return(TemperaturePoints, CoolantAxialTemperature, CoolantAxialHeatCapacity, CoolantAxialDensity, CoolantAxialDynamicViscosity, \
		   CoolantAxialConductivity, CoolantAxialKinematicViscosity, CoolantAxialInteriorPeclet, CoolantAxialEdgePeclet, \
		   CoolantAxialCornerPeclet, CoolantAxialInteriorNusselt, CoolantAxialEdgeNusselt, CoolantAxialCornerNusselt, \
		   CoolantAxialInteriorHeatTransferCoefficient, CoolantAxialEdgeHeatTransferCoefficient, CoolantAxialCornerHeatTransferCoefficient, \
		   CoolantAxialInteriorReynolds, CoolantAxialEdgeReynolds, CoolantAxialCornerReynolds, CladdingOuterWallAxialTemperature, \
		   PeakCladdingOuterWallTemperature, CoolantAxialEdgeTemperature, CoolantAxialEdgeHeatCapacity,CoolantAxialEdgeDensity, \
		   CoolantAxialEdgeDynamicViscosity,CoolantAxialEdgeConductivity,CoolantAxialEdgeKinematicViscosity,CoolantAxialCornerTemperature, \
		   CoolantAxialCornerHeatCapacity,CoolantAxialCornerDensity, CoolantAxialCornerDynamicViscosity, CoolantAxialCornerConductivity, \
		   CoolantAxialCornerKinematicViscosity,EdgeChannelOutletTemperature,CornerChannelOutletTemperature, CoolantTemperatureZ2,
		   CoolantEdgeTemperatureZ2,CoolantEdgeHeatCapacityZ2,CoolantEdgeDensityZ2,CoolantEdgeDynamicViscosityZ2,CoolantEdgeConductivityZ2,
		   CoolantEdgeKinematicViscosityZ2,CoolantCornerTemperatureZ2,CoolantCornerHeatCapacityZ2,CoolantCornerDensityZ2,
		   CoolantCornerDynamicViscosityZ2,CoolantCornerConductivityZ2,CoolantCornerKinematicViscosityZ2, CoolantHeatCapacityZ2,
		   CoolantDensityZ2,CoolantDynamicViscosityZ2,CoolantConductivityZ2,CoolantKinematicViscosityZ2, CoolantInteriorPecletZ2,
		   CoolantEdgePecletZ2,CoolantCornerPecletZ2,CoolantInteriorNusseltZ2,CoolantEdgeNusseltZ2,CoolantCornerNusseltZ2,
		   CoolantInteriorHeatTransferCoefficientZ2,CoolantEdgeHeatTransferCoefficientZ2,CoolantCornerHeatTransferCoefficientZ2,
		   CoolantInteriorReynoldsZ2,CoolantEdgeReynoldsZ2,CoolantCornerReynoldsZ2,CladdingOuterWallTemperatureZ2, 
		   TemperaturePointsZ, CoolantAxialAverageCornerReynolds, CoolantAxialAverageInteriorReynolds, CoolantAxialAverageEdgeReynolds,
		   PeakChannelMassFlow, EdgeChannelMassFlow, CornerChannelMassFlow)



def decnataxialcoolant(MassFlowArea, DecayHeatRemovalFlowVelocity, CoolantInletDensity, FuelLength, AxialTemperaturePoints, \
	                   CosinePinAxialPowerPeaking, CoolantInletHeatCapacity, SingleInteriorChannelHydraulicDiameter, \
	                   BelowCoreChannelLength, CoolantInletTemperature, PeakPinPeakLinearPower, Pitch, Diameter, \
	                   SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, EdgeChannelDecNatCoolantVelocity, \
	                   CornerChannelDecNatCoolantVelocity, SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, EdgePinPeakLinearPower,
	                   CornerPinPeakLinearPower, Name, Coolant, PinAxialPowerPeaking, mlabpath):

	InteriorChannelCoolantVelocity = DecayHeatRemovalFlowVelocity
	EdgeChannelCoolantVelocity = EdgeChannelDecNatCoolantVelocity
	CornerChannelCoolantVelocity = CornerChannelDecNatCoolantVelocity

	# The mass flow in the peak power channel of the core (which has the highest flow velocity)
	PeakChannelMassFlow = MassFlowArea * DecayHeatRemovalFlowVelocity * CoolantInletDensity

	# Edge channel mass flow
	EdgeChannelMassFlow = SingleEdgeChannelFlowArea * EdgeChannelDecNatCoolantVelocity * CoolantInletDensity

	# Corner channel mass flow
	CornerChannelMassFlow = SingleCornerChannelFlowArea * CornerChannelDecNatCoolantVelocity * CoolantInletDensity
	
	# Starting point for coolant temperature evaluation
	z = -FuelLength/2
	
	# Empty list for collecting temperature evaluation points
	TemperaturePoints  = []
	TemperaturePointsZ = []
		
	# Calculate until reaching the top of fuel (here, the axial mid-level of fuel is z = 0)
	while z < FuelLength/2 + FuelLength/AxialTemperaturePoints:
	
		# Rounding the number
		z = round(z,5)
	
		# Collect the evalution point to the list
		TemperaturePoints.append(z)
		TemperaturePointsZ.append(z + FuelLength/2)
	
		# Increment the evaluation point
		z += FuelLength/AxialTemperaturePoints
	
	# Create empty dictionaries for saving axial coolant information
	CoolantDecNatAxialInteriorPeclet                  = {}
	CoolantDecNatAxialEdgePeclet                      = {}
	CoolantDecNatAxialCornerPeclet                    = {}
	CoolantDecNatAxialInteriorNusselt                 = {}
	CoolantDecNatAxialEdgeNusselt                     = {}
	CoolantDecNatAxialCornerNusselt                   = {}
	CoolantDecNatAxialInteriorHeatTransferCoefficient = {}
	CoolantDecNatAxialEdgeHeatTransferCoefficient     = {}
	CoolantDecNatAxialCornerHeatTransferCoefficient   = {}
	CoolantDecNatAxialInteriorReynolds                = {}
	CoolantDecNatAxialEdgeReynolds                    = {}
	CoolantDecNatAxialCornerReynolds                  = {}

	# Create empty dictionary for saving axial outer cladding temperature
	CladdingOuterWallAxialTemperature   = {}
	PeakCladdingOuterWallTemperature    = []

	# Create lists for matplotlib
	CoolantDecNatInteriorPecletZ2 = []
	CoolantDecNatEdgePecletZ2 = []
	CoolantDecNatCornerPecletZ2 = []
	CoolantDecNatInteriorNusseltZ2 = []
	CoolantDecNatEdgeNusseltZ2 = []
	CoolantDecNatCornerNusseltZ2 = []
	CoolantDecNatInteriorHeatTransferCoefficientZ2 = []
	CoolantDecNatEdgeHeatTransferCoefficientZ2 = []
	CoolantDecNatCornerHeatTransferCoefficientZ2 = []
	CoolantDecNatInteriorReynoldsZ2 = []
	CoolantDecNatEdgeReynoldsZ2 = []
	CoolantDecNatCornerReynoldsZ2 = []
	CladdingDecNatOuterWallTemperatureZ2 = []

	for z in TemperaturePoints:
		
		if PinAxialPowerPeaking < (math.pi/2):

			# Calculate coolant temperature at axial position z
			CoolantTemperatureZ       = CoolantInletTemperature + PeakPinPeakLinearPower * FuelLength * CosinePinAxialPowerPeaking * (math.sin(math.pi * z / FuelLength / CosinePinAxialPowerPeaking) + math.sin(math.pi / CosinePinAxialPowerPeaking / 2)) / PeakChannelMassFlow / CoolantInletHeatCapacity / math.pi;
	
			# Calculate coolant temperature at axial position z
			CoolantEdgeTemperatureZ   = CoolantInletTemperature + EdgePinPeakLinearPower * FuelLength * CosinePinAxialPowerPeaking * (math.sin(math.pi * z / FuelLength / CosinePinAxialPowerPeaking) + math.sin(math.pi / CosinePinAxialPowerPeaking / 2)) / EdgeChannelMassFlow / CoolantInletHeatCapacity / math.pi;
	
			# Calculate coolant temperature at axial position z
			CoolantCornerTemperatureZ = CoolantInletTemperature + (CornerPinPeakLinearPower/3) * FuelLength * CosinePinAxialPowerPeaking * (math.sin(math.pi * z / FuelLength / CosinePinAxialPowerPeaking) + math.sin(math.pi / CosinePinAxialPowerPeaking / 2)) / CornerChannelMassFlow / CoolantInletHeatCapacity / math.pi;

		else:

			CoolantTemperatureZ       = CoolantInletTemperature + PeakPinPeakLinearPower * (-0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi / CosinePinAxialPowerPeaking / 0.2e1) + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * math.pi * FuelLength - 0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) + 0.2e1 * math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * z * math.pi) / (-0.1e1 + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / PeakChannelMassFlow / CoolantInletHeatCapacity / 0.2e1

			CoolantEdgeTemperatureZ   = CoolantInletTemperature + EdgePinPeakLinearPower * (-0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi / CosinePinAxialPowerPeaking / 0.2e1) + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * math.pi * FuelLength - 0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) + 0.2e1 * math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * z * math.pi) / (-0.1e1 + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / EdgeChannelMassFlow / CoolantInletHeatCapacity / 0.2e1

			CoolantCornerTemperatureZ = CoolantInletTemperature + CornerPinPeakLinearPower * (-0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi / CosinePinAxialPowerPeaking / 0.2e1) + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * math.pi * FuelLength - 0.2e1 * CosinePinAxialPowerPeaking * FuelLength * math.sin(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) + 0.2e1 * math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1) * z * math.pi) / (-0.1e1 + math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / math.pi / CornerChannelMassFlow / CoolantInletHeatCapacity / 0.2e1

		if Coolant == "Pb":
	
			# Coolant heat capacity in J/kg-K
			CoolantHeatCapacity     = 0.1762e3 - 0.4926e-1 * CoolantTemperatureZ + 0.1544000000e-4 * CoolantTemperatureZ ** 2 - 0.1524e7 / CoolantTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantDensity          = 11441-1.2795 * CoolantTemperatureZ 
			
			# Coolant  dynamic visocity in Pa * s
			CoolantDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantTemperatureZ)
		
			# Coolant thermal conductivity in W/m*K
			CoolantConductivity     = 9.2 + 0.011 * CoolantTemperatureZ 
	
			#######################################################################################################
	
			# Coolant heat capacity in J/kg-K
			CoolantEdgeHeatCapacity     = 0.1762e3 - 0.4926e-1 * CoolantEdgeTemperatureZ + 0.1544000000e-4 * CoolantEdgeTemperatureZ ** 2 - 0.1524e7 / CoolantEdgeTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantEdgeDensity          = 11441-1.2795 * CoolantEdgeTemperatureZ 
			
			# Coolant  dynamic visocity in Pa * s
			CoolantEdgeDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantEdgeTemperatureZ)
		
			# Coolant thermal conductivity in W/m*K
			CoolantEdgeConductivity     = 9.2 + 0.011 * CoolantEdgeTemperatureZ 
	
			#######################################################################################################
	
			# Coolant heat capacity in J/kg-K
			CoolantCornerHeatCapacity     = 0.1762e3 - 0.4926e-1 * CoolantCornerTemperatureZ + 0.1544000000e-4 * CoolantCornerTemperatureZ ** 2 - 0.1524e7 / CoolantCornerTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantCornerDensity          = 11441-1.2795 * CoolantCornerTemperatureZ 
			
			# Coolant  dynamic visocity in Pa * s
			CoolantCornerDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantCornerTemperatureZ)
		
			# Coolant thermal conductivity in W/m*K
			CoolantCornerConductivity     = 9.2 + 0.011 * CoolantCornerTemperatureZ 


		elif Coolant == "Na":


			# Coolant heat capacity in J/kg-K
			CoolantHeatCapacity         = -3.001 * 1e6 * CoolantTemperatureZ ** (-2) + 1658 - 0.8479 * CoolantTemperatureZ + 4.454 * 1e-4 * CoolantTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantDensity              = 1014 - 0.235 * CoolantTemperatureZ
			
			# Dynamic visocity in Pa * s
			CoolantDynamicViscosity     = math.exp((556.835/CoolantTemperatureZ) - 0.3985 * math.log(CoolantTemperatureZ) - 6.4406)
			
			# Thermal conductivity in W/m*K
			CoolantConductivity         = 104 - 0.047 * CoolantTemperatureZ

			#######################################################################################################

			# Coolant heat capacity in J/kg-K
			CoolantEdgeHeatCapacity     = -3.001 * 1e6 * CoolantEdgeTemperatureZ ** (-2) + 1658 - 0.8479 * CoolantEdgeTemperatureZ + 4.454 * 1e-4 * CoolantEdgeTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantEdgeDensity          = 1014 - 0.235 * CoolantEdgeTemperatureZ
			
			# Dynamic visocity in Pa * s
			CoolantEdgeDynamicViscosity = math.exp((556.835/CoolantEdgeTemperatureZ) - 0.3985 * math.log(CoolantEdgeTemperatureZ) - 6.4406)
			
			# Thermal conductivity in W/m*K
			CoolantEdgeConductivity     = 104 - 0.047 * CoolantEdgeTemperatureZ

			#######################################################################################################

			# Coolant heat capacity in J/kg-K
			CoolantCornerHeatCapacity     = -3.001 * 1e6 * CoolantCornerTemperatureZ ** (-2) + 1658 - 0.8479 * CoolantCornerTemperatureZ + 4.454 * 1e-4 * CoolantCornerTemperatureZ ** 2
			
			# Coolant density in kg/m^3
			CoolantCornerDensity          = 1014 - 0.235 * CoolantCornerTemperatureZ
			
			# Dynamic visocity in Pa * s
			CoolantCornerDynamicViscosity = math.exp((556.835/CoolantCornerTemperatureZ) - 0.3985 * math.log(CoolantCornerTemperatureZ) - 6.4406)
			
			# Thermal conductivity in W/m*K
			CoolantCornerConductivity     = 104 - 0.047 * CoolantCornerTemperatureZ


		elif Coolant == "LBE":

			#  coolant heat capacity in J/kg-K
			CoolantHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantTemperatureZ + 7.183 * 1e6 * CoolantTemperatureZ ** (-2)
			
			#  coolant density in kg/m^3
			CoolantDensity          = 10725 - 1.22 * CoolantTemperatureZ
			
			#  dynamic visocity in Pa * s
			CoolantDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantTemperatureZ)
			
			#  thermal conductivity in W/m*K
			CoolantConductivity     = 7.34 + 9.5 * 1e-3 * CoolantTemperatureZ

			#######################################################################################################

			#  coolant heat capacity in J/kg-K
			CoolantEdgeHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantEdgeTemperatureZ + 7.183 * 1e6 * CoolantEdgeTemperatureZ ** (-2)
			
			#  coolant density in kg/m^3
			CoolantEdgeDensity          = 10725 - 1.22 * CoolantEdgeTemperatureZ
			
			#  dynamic visocity in Pa * s
			CoolantEdgeDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantEdgeTemperatureZ)
			
			#  thermal conductivity in W/m*K
			CoolantEdgeConductivity     = 7.34 + 9.5 * 1e-3 * CoolantEdgeTemperatureZ

			#######################################################################################################

			#  coolant heat capacity in J/kg-K
			CoolantCornerHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantCornerTemperatureZ + 7.183 * 1e6 * CoolantCornerTemperatureZ ** (-2)
			
			#  coolant density in kg/m^3
			CoolantCornerDensity          = 10725 - 1.22 * CoolantCornerTemperatureZ
			
			#  dynamic visocity in Pa * s
			CoolantCornerDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantCornerTemperatureZ)
			
			#  thermal conductivity in W/m*K
			CoolantCornerConductivity     = 7.34 + 9.5 * 1e-3 * CoolantCornerTemperatureZ			

		##############################################################################################################################
		##############################################################################################################################
	
		# Coolant kinematic visocity in Pa * s / kg
		CoolantKinematicViscosity = CoolantDynamicViscosity / CoolantDensity

		# Coolant kinematic visocity in Pa * s / kg
		CoolantEdgeKinematicViscosity = CoolantEdgeDynamicViscosity / CoolantEdgeDensity

		# Coolant kinematic visocity in Pa * s / kg
		CoolantCornerKinematicViscosity = CoolantCornerDynamicViscosity / CoolantCornerDensity

		##############################################################################################################################	
		######## Channel Peclet numbers ##############################################################################################
		##############################################################################################################################

		# Coolant interior channel Peclet number
		CoolantInteriorPeclet = CoolantDensity * InteriorChannelCoolantVelocity * SingleInteriorChannelHydraulicDiameter / CoolantConductivity

		# Coolant edge channel Peclet number
		CoolantEdgePeclet     = CoolantEdgeDensity * EdgeChannelCoolantVelocity     * SingleEdgeChannelHydraulicDiameter     / CoolantEdgeConductivity
	
		# Coolant corner channel Peclet number
		CoolantCornerPeclet   = CoolantEdgeDensity * CornerChannelCoolantVelocity   * SingleCornerChannelHydraulicDiameter   / CoolantCornerConductivity

		##############################################################################################################################	
		######## Channel Nusselt numbers #############################################################################################
		##############################################################################################################################

		# Coolant interior channel Nusselt number
		CoolantInteriorNusselt = 0.047 * (1 - math.exp(-3.8 * Pitch / Diameter + 3.8)) * (abs(CoolantInteriorPeclet) ** 0.77 + 250)

		# Coolant edge channel Nusselt number
		CoolantEdgeNusselt     = 0.047 * (1 - math.exp(-3.8 * Pitch / Diameter + 3.8)) * (abs(CoolantEdgePeclet)   ** 0.77 + 250)

		# Coolant corner channel Nusselt number
		CoolantCornerNusselt   = 0.047 * (1 - math.exp(-3.8 * Pitch / Diameter + 3.8)) * (abs(CoolantCornerPeclet) ** 0.77 + 250)
	
		##############################################################################################################################	
		######## Channel heat transfer coefficients ##################################################################################
		##############################################################################################################################

		# Coolant interior channel heat transfer coefficient (W/m^2)
		InteriorHeatTransferCoefficient = CoolantInteriorNusselt * CoolantConductivity       / SingleInteriorChannelHydraulicDiameter

		# Coolant edge channel heat transfer coefficient (W/m^2)
		EdgeHeatTransferCoefficient     = CoolantEdgeNusselt     * CoolantEdgeConductivity   / SingleEdgeChannelHydraulicDiameter

		# Coolant corner channel heat transfer coefficient (W/m^2)
		CornerHeatTransferCoefficient   = CoolantCornerNusselt   * CoolantCornerConductivity / SingleCornerChannelHydraulicDiameter
		
		##############################################################################################################################	
		######## Channel Reynolds numbers ############################################################################################
		##############################################################################################################################

		# Coolant interior channel Reynolds number
		CoolantInteriorReynolds = InteriorChannelCoolantVelocity * SingleInteriorChannelHydraulicDiameter / CoolantKinematicViscosity
	
		# Coolant edge channel Reynolds number
		CoolantEdgeReynolds     = EdgeChannelCoolantVelocity     * SingleEdgeChannelHydraulicDiameter     / CoolantEdgeKinematicViscosity

		# Coolant corner channel Reynolds number
		CoolantCornerReynolds   = CornerChannelCoolantVelocity   * SingleCornerChannelHydraulicDiameter   / CoolantCornerKinematicViscosity

		##############################################################################################################################	
		######## Collect axial information ###########################################################################################
		##############################################################################################################################

		# Collect interior channel axial position and peclet number
		CAT_InteriorPeclet       = {z : CoolantInteriorPeclet}

		# Collect edge channel axial position and peclet number
		CAT_EdgePeclet           = {z : CoolantEdgePeclet}

		# Collect corner channel axial position and peclet number
		CAT_CornerPeclet         = {z : CoolantCornerPeclet}

		# Collect interior channel axial position and nusselt number
		CAT_InteriorNusselt      = {z : CoolantInteriorNusselt}

		# Collect edge channel axial position and nusselt number
		CAT_EdgeNusselt          = {z : CoolantEdgeNusselt}

		# Collect corner channel axial position and nusselt number
		CAT_CornerNusselt        = {z : CoolantCornerNusselt}
	
		# Collect interior channel axial position and heat transfer coefficient
		CAT_InteriorHeatTransfer = {z : InteriorHeatTransferCoefficient}

		# Collect edge channel axial position and heat transfer coefficient
		CAT_EdgeHeatTransfer     = {z : EdgeHeatTransferCoefficient}

		# Collect corner channel axial position and heat transfer coefficient
		CAT_CornerHeatTransfer   = {z : CornerHeatTransferCoefficient}
	
		# Collect interior channel axial position and renolds numbers
		CAT_InteriorReynolds     = {z : CoolantInteriorReynolds}

		# Collect edge channel axial position and renolds numbers
		CAT_EdgeReynolds         = {z : CoolantEdgeReynolds}

		# Collect corner channel axial position and renolds numbers
		CAT_CornerReynolds       = {z : CoolantCornerReynolds}
	
		# Update the dictionary with the information
		CoolantDecNatAxialInteriorPeclet.update(CAT_InteriorPeclet)
		CoolantDecNatAxialEdgePeclet.update(CAT_EdgePeclet)
		CoolantDecNatAxialCornerPeclet.update(CAT_CornerPeclet)
		CoolantDecNatAxialInteriorNusselt.update(CAT_InteriorNusselt)
		CoolantDecNatAxialEdgeNusselt.update(CAT_EdgeNusselt)
		CoolantDecNatAxialCornerNusselt.update(CAT_CornerNusselt)
		CoolantDecNatAxialInteriorHeatTransferCoefficient.update(CAT_InteriorHeatTransfer)
		CoolantDecNatAxialEdgeHeatTransferCoefficient.update(CAT_EdgeHeatTransfer)
		CoolantDecNatAxialCornerHeatTransferCoefficient.update(CAT_CornerHeatTransfer)
		CoolantDecNatAxialInteriorReynolds.update(CAT_InteriorReynolds)
		CoolantDecNatAxialEdgeReynolds.update(CAT_EdgeReynolds)
		CoolantDecNatAxialCornerReynolds.update(CAT_CornerReynolds)

		CoolantDecNatInteriorPecletZ2.append(CoolantInteriorPeclet)
		CoolantDecNatEdgePecletZ2.append(CoolantEdgePeclet)
		CoolantDecNatCornerPecletZ2.append(CoolantCornerPeclet)
		CoolantDecNatInteriorNusseltZ2.append(CoolantInteriorNusselt)
		CoolantDecNatEdgeNusseltZ2.append(CoolantEdgeNusselt)
		CoolantDecNatCornerNusseltZ2.append(CoolantCornerNusselt)
		CoolantDecNatInteriorHeatTransferCoefficientZ2.append(InteriorHeatTransferCoefficient)
		CoolantDecNatEdgeHeatTransferCoefficientZ2.append(EdgeHeatTransferCoefficient)
		CoolantDecNatCornerHeatTransferCoefficientZ2.append(CornerHeatTransferCoefficient)
		CoolantDecNatInteriorReynoldsZ2.append(CoolantInteriorReynolds)
		CoolantDecNatEdgeReynoldsZ2.append(CoolantEdgeReynolds)
		CoolantDecNatCornerReynoldsZ2.append(CoolantCornerReynolds)

	return(CoolantDecNatAxialInteriorReynolds, CoolantDecNatAxialEdgeReynolds, CoolantDecNatAxialCornerReynolds)

