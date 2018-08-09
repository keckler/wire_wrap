import math
from x_prop import *

def innercladdingt(PeakCladdingOuterWallTemperature, TemperaturePoints, TemperatureConvergence, PeakPinPeakLinearPower, \
	               CladdingOuterRadius, CladdingInnerRadius, FuelLength, CosinePinAxialPowerPeaking, CladdingOuterWallAxialTemperature,
	               Name, PinAxialPowerPeaking, Cladding, mlabpath):

	####  ASSUMPTIONS
	####  1. Cladding delta-T is determined by the cladding mid-wall conductivity at each axial point,
	####     thus, conductivity temperature dependence is assumed to be linear in the temperature span 
	####     radially across the cladding
	
	# Initial guess for the average cladding inner wall temperature at the axial bottom of the rod
	AverageCladdingTemperature  = PeakCladdingOuterWallTemperature 
	
	# Start collecting guesses for the average cladding temperature (to determine average cladding conductivity)
	CollectAverageCladdingTemperatures = [AverageCladdingTemperature]
	
	# Start variable for outer cladding temperatures in MATLAB file
	cti = open(mlabpath + "/cladding_inner_temperature.m", 'a')
	cti.write("cit = [")
	
	# Collect inner wall axial temperature
	CladdingInnerWallAxialTemperature = {}

	# Empty list to define peak inner wall temperature
	PeakCladdingInnerWallTemperature    = []

	# Plotting-style inner wall temperature list
	CladdingInnerWallTemperatureZ2 = []
	
	# Do for all axial evaluation points
	for z in TemperaturePoints:
	
		# Initial value for counter to check conductivity convergence
		i = 0
	
		# Initial error for the temperature (since conductivity is not converged)
		CladdingTemperatureError = 1e6
	
		# Run until temperatures match within the convergence criteria
		while CladdingTemperatureError > TemperatureConvergence:
	
			# Increase the trail counter by 1
			i += 1

			CladdingProperty = nonfuelsolidproperties(material=Cladding, temperature=AverageCladdingTemperature, fastflux=1, stress=1, dpa=1, porosity=1)
			CladdingConductivity = CladdingProperty.conductivity

			if PinAxialPowerPeaking < (math.pi/2):

				# Calculate the radial temperature difference across the cladding at the specific axial level
				CladdingTemperatureDelta = PeakPinPeakLinearPower * ( 1/(2 * math.pi * CladdingConductivity) * math.log(CladdingOuterRadius / CladdingInnerRadius) * math.cos(math.pi * z / (FuelLength * CosinePinAxialPowerPeaking)) )
		
			else:

				CladdingTemperatureDelta = PeakPinPeakLinearPower * ( 1/(2 * math.pi * CladdingConductivity) * math.log(CladdingOuterRadius / CladdingInnerRadius) * (math.cos(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / (0.1e1 - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)))

			# Calculate the inner cladding wall temperature at the specific axial level
			CladdingInnerWallTemperature = CladdingOuterWallAxialTemperature.get(z) + CladdingTemperatureDelta.real
	
			# Write data to MATLAB
			cti.write("\n")
			cti.write(str(CladdingInnerWallTemperature-273.15) + ",")

			# Write for matplotlib plotting
			CladdingInnerWallTemperatureZ2.append(CladdingInnerWallTemperature-273.15)
	
			# Calculate the cladding mid-wall temperature
			AverageCladdingTemperature = (CladdingOuterWallAxialTemperature.get(z) + CladdingInnerWallTemperature) / 2
	
			# Add the new mid-wall temperature guess
			CollectAverageCladdingTemperatures.append(AverageCladdingTemperature)
	
			# Calculate the difference between the previous guess for average temperature and the current
			CladdingTemperatureError = CollectAverageCladdingTemperatures[i] - CollectAverageCladdingTemperatures[i-1]
	
		PeakCladdingInnerWallTemperature.append(CladdingInnerWallTemperature.real)
	
		# Collect axial cladding outer wall temperature
		COW_Temperature = {z : CladdingInnerWallTemperature.real}
	
		# Update cladding outer wall temperature dictionary
		CladdingInnerWallAxialTemperature.update(COW_Temperature)
	
	# Define the peak cladding outer wall temperature
	PeakCladdingInnerWallTemperature = max(PeakCladdingInnerWallTemperature)

	# Figure out where axially the peak cladding outer wall temperature occurs
	for k,v in CladdingInnerWallAxialTemperature.items():
		if v == PeakCladdingInnerWallTemperature:
			PeakCladdingInnerWallTemperateAxialPosition = k
	
	cti.write("];")
	cti.close()

	return(CladdingInnerWallAxialTemperature, PeakCladdingInnerWallTemperature, PeakCladdingInnerWallTemperateAxialPosition, 
		   CladdingInnerWallTemperatureZ2)
	
