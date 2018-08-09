import math

def CoolantInletProperties(Coolant, CoolantInletTemperature):

	if Coolant == "Pb":

		# Inlet coolant heat capacity in J/kg-K
		CoolantInletHeatCapacity     = 0.1762e3 - 0.4926e-1 *CoolantInletTemperature + 0.1544000000e-4 *CoolantInletTemperature ** 2 - 0.1524e7 /CoolantInletTemperature ** 2
		
		# Inlet coolant density in kg/m^3
		CoolantInletDensity          = 11441-1.2795 * CoolantInletTemperature 
		
		# Inlet dynamic visocity in Pa * s
		CoolantInletDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantInletTemperature )
		
		# Inlet thermal conductivity in W/m*K
		CoolantInletConductivity     = 9.2 + 0.011 * CoolantInletTemperature 

	elif Coolant == "Na":
	
		# Inlet coolant heat capacity in J/kg-K
		CoolantInletHeatCapacity     = -3.001 * 1e6 * CoolantInletTemperature ** (-2) + 1658 - 0.8479 * CoolantInletTemperature + 4.454 * 1e-4 * CoolantInletTemperature ** 2
		
		# Inlet coolant density in kg/m^3
		CoolantInletDensity          = 1014 - 0.235 * CoolantInletTemperature
		
		# Inlet dynamic visocity in Pa * s
		CoolantInletDynamicViscosity = math.exp((556.835/CoolantInletTemperature) - 0.3985 * math.log(CoolantInletTemperature) - 6.4406)
		
		# Inlet thermal conductivity in W/m*K
		CoolantInletConductivity     = 104 - 0.047 * CoolantInletTemperature

	elif Coolant == "LBE":

		# Inlet coolant heat capacity in J/kg-K
		CoolantInletHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantInletTemperature + 7.183 * 1e6 * CoolantInletTemperature ** (-2)
		
		# Inlet coolant density in kg/m^3
		CoolantInletDensity          = 10725 - 1.22 * CoolantInletTemperature
		
		# Inlet dynamic visocity in Pa * s
		CoolantInletDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantInletTemperature)
		
		# Inlet thermal conductivity in W/m*K
		CoolantInletConductivity     = 7.34 + 9.5 * 1e-3 * CoolantInletTemperature

	return(CoolantInletHeatCapacity, CoolantInletDensity, CoolantInletDynamicViscosity, CoolantInletConductivity)

def CoolantAverageProperties(Coolant, CoolantAverageTemperature):

	if Coolant == "Pb":

		# Average coolant heat capacity in J/kg-K
		CoolantAverageHeatCapacity     = 0.1762e3 - 0.4926e-1 *CoolantAverageTemperature + 0.1544000000e-4 *CoolantAverageTemperature ** 2 - 0.1524e7 /CoolantAverageTemperature ** 2
		
		# Average coolant density in kg/m^3
		CoolantAverageDensity          = 11441-1.2795 * CoolantAverageTemperature 
		
		# Average dynamic visocity in Pa * s
		CoolantAverageDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantAverageTemperature )
		
		# Average thermal conductivity in W/m*K
		CoolantAverageConductivity     = 9.2 + 0.011 * CoolantAverageTemperature 

	elif Coolant == "Na":
	
		# Average coolant heat capacity in J/kg-K
		CoolantAverageHeatCapacity     = -3.001 * 1e6 * CoolantAverageTemperature ** (-2) + 1658 - 0.8479 * CoolantAverageTemperature + 4.454 * 1e-4 * CoolantAverageTemperature ** 2
		
		# Average coolant density in kg/m^3
		CoolantAverageDensity          = 1014 - 0.235 * CoolantAverageTemperature
		
		# Average dynamic visocity in Pa * s
		CoolantAverageDynamicViscosity = math.exp((556.835/CoolantAverageTemperature) - 0.3985 * math.log(CoolantAverageTemperature) - 6.4406)
		
		# Average thermal conductivity in W/m*K
		CoolantAverageConductivity     = 104 - 0.047 * CoolantAverageTemperature

	elif Coolant == "LBE":

		# Average coolant heat capacity in J/kg-K
		CoolantAverageHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantAverageTemperature + 7.183 * 1e6 * CoolantAverageTemperature ** (-2)
		
		# Average coolant density in kg/m^3
		CoolantAverageDensity          = 10725 - 1.22 * CoolantAverageTemperature
		
		# Average dynamic visocity in Pa * s
		CoolantAverageDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantAverageTemperature)
		
		# Average thermal conductivity in W/m*K
		CoolantAverageConductivity     = 7.34 + 9.5 * 1e-3 * CoolantAverageTemperature
	
	return(CoolantAverageHeatCapacity, CoolantAverageDensity, CoolantAverageDynamicViscosity, CoolantAverageConductivity)

def CoolantOutletProperties(Coolant, CoolantOutletTemperature):

	if Coolant == "Pb":

		# Outlet coolant heat capacity in J/kg-K
		CoolantOutletHeatCapacity     = 0.1762e3 - 0.4926e-1 *CoolantOutletTemperature + 0.1544000000e-4 *CoolantOutletTemperature ** 2 - 0.1524e7 /CoolantOutletTemperature ** 2
		
		# Outlet coolant density in kg/m^3
		CoolantOutletDensity          = 11441-1.2795 * CoolantOutletTemperature 
		
		# Outlet dynamic visocity in Pa * s
		CoolantOutletDynamicViscosity = 4.55 * 1e-4 * math.exp(1069/CoolantOutletTemperature )
		
		# Outlet thermal conductivity in W/m*K
		CoolantOutletConductivity     = 9.2 + 0.011 * CoolantOutletTemperature 

	elif Coolant == "Na":
	
		# Outlet coolant heat capacity in J/kg-K
		CoolantOutletHeatCapacity     = -3.001 * 1e6 * (CoolantOutletTemperature ** (-2)) + 1658 - 0.8479 * CoolantOutletTemperature + 4.454 * 1e-4 * (CoolantOutletTemperature ** 2)
		
		# Outlet coolant density in kg/m^3
		CoolantOutletDensity          = 1014 - 0.235 * CoolantOutletTemperature
		
		# Outlet dynamic visocity in Pa * s
		CoolantOutletDynamicViscosity = math.exp((556.835/CoolantOutletTemperature) - 0.3985 * math.log(CoolantOutletTemperature) - 6.4406)
		
		# Outlet thermal conductivity in W/m*K
		CoolantOutletConductivity     = 104 - 0.047 * CoolantOutletTemperature

	elif Coolant == "LBE":

		# Outlet coolant heat capacity in J/kg-K
		CoolantOutletHeatCapacity     = 118.2 + 5.934 * 1e-3 * CoolantOutletTemperature + 7.183 * 1e6 * CoolantOutletTemperature ** (-2)
		
		# Outlet coolant density in kg/m^3
		CoolantOutletDensity          = 10725 - 1.22 * CoolantOutletTemperature
		
		# Outlet dynamic visocity in Pa * s
		CoolantOutletDynamicViscosity = 4.456 * 1e-4 * math.exp(780/CoolantOutletTemperature)
		
		# Outlet thermal conductivity in W/m*K
		CoolantOutletConductivity     = 7.34 + 9.5 * 1e-3 * CoolantOutletTemperature
	
	return(CoolantOutletHeatCapacity, CoolantOutletDensity, CoolantOutletDynamicViscosity, CoolantOutletConductivity)
