# -*- coding: UTF-8 -*-
import math
from x_prop import *

def ft(PeakFuelRimTemperature, TemperaturePoints, TemperatureConvergence, GadoliniumContent, Burnup, FTDF, \
	   PeakPinPeakLinearPower, FuelLength, CosinePinAxialPowerPeaking, FuelRimAxialTemperature, Name, FreshFuelRadius,
	   TotalFuelPins, AxialTemperaturePoints, FissileFraction, Batches, ActinideMassFraction, PinAxialPowerPeaking, Fuel,
	   Porosity, mlabpath, MetallicFuelPlutoniumFraction, MetallicFuelNonActinideMassFraction, MetallicFuelUraniumFraction,
	   FuelType, CladdingInnerWallAxialTemperature, InnerFuelRadius, InnerFuelDiameter):
	
	# Initial guess for the average cladding inner wall temperature at the axial bottom of the rod
	AverageFuelTemperature = PeakFuelRimTemperature 
	
	# Start collecting guesses for the average cladding temperature (to determine average cladding conductivity)
	CollectAverageFuelTemperatures = [AverageFuelTemperature]
	
	# Empty list to define peak fuel temperature
	PeakFuelInnerTemperature = []
	
	# Empty list to define average fuel density
	FuelDensity = []

	# Collect centerline fuel temperatures
	FuelInnerAxialTemperature = {}

	# Collect centerline fuel temperatures for matplotlib
	FuelInnerAxialTemperatureZ2 = []

	# Start of iterative calculation of fuel mass
	FuelMass = 0

	# Start variable for outer cladding temperatures in MATLAB file
	cgf = open(mlabpath +  "/fuel_inner_temperature.m", 'a')
	cgf.write("fit = [")

	#print("-----------")

	# Do for all axial evaluation points
	for z in TemperaturePoints:
	
		# Initial value for counter to check conductivity convergence
		i = 0
	
		# Initial error for the temperature (since conductivity is not converged)
		InnerFuelTemperatureError = 1e6

		if FuelType != "annular" and FuelType != "Annular":

			AnnularMultiplier = 0

		else:

			AnnularMultiplier = 0

		# Run until temperatures match within the convergence criteria
		while InnerFuelTemperatureError > TemperatureConvergence:
	
			# Increase the trail counter by 1
			i += 1

			FuelProperties = fuelproperties(material=Fuel, temperature=AverageFuelTemperature, FTDF=FTDF, expansion="none", WU=MetallicFuelUraniumFraction, WPu=MetallicFuelPlutoniumFraction, Wzr=MetallicFuelNonActinideMassFraction, Burnup=Burnup, mode=1, indensity=1,intemperature=1)
			FuelConductivity = FuelProperties.conductivity

			if PinAxialPowerPeaking < (math.pi/2):

				# Calculate the radial temperature difference across the fuel at the specific axial level
				FuelTemperatureDelta = AnnularMultiplier + (PeakPinPeakLinearPower * ((1/(4 * math.pi * FuelConductivity))* math.cos(math.pi * z / (FuelLength * CosinePinAxialPowerPeaking))))
	
			else:

				FuelTemperatureDelta = (PeakPinPeakLinearPower / (4 * math.pi * FuelConductivity)) * (math.cos(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / (0.1e1 - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1))

			# Calculate the fuel centerline temperature at the specific axial level
			if FuelType != "annular" and FuelType != "Annular":

				FuelInnerTemperature = FuelRimAxialTemperature.get(z) + FuelTemperatureDelta
	
			else:

				FuelInnerTemperature = CladdingInnerWallAxialTemperature.get(z) + FuelTemperatureDelta

			# Calculate the fuel radial "average" temperature
			AverageFuelTemperature = (FuelInnerTemperature + FuelRimAxialTemperature.get(z)) / 2
	
			# Add the new average temperature guess
			CollectAverageFuelTemperatures.append(AverageFuelTemperature)
	
			# Calculate the difference between the previous guess for average temperature and the current
			InnerFuelTemperatureError = CollectAverageFuelTemperatures[i] - CollectAverageFuelTemperatures[i-1]
	
		# Collect axial fuel centerline temperature
		COW_Temperature = {z : FuelInnerTemperature}
	
		# Update fuel centerline temperature list
		PeakFuelInnerTemperature.append(FuelInnerTemperature)
	
		# Update fuel centerline temperature dictionary
		FuelInnerAxialTemperature.update(COW_Temperature)
	
		# Write data to MATLAB
		cgf.write("\n")
		cgf.write(str(FuelInnerTemperature-273.15) + ",")

		FuelInnerAxialTemperatureZ2.append(FuelInnerTemperature-273.15)

		FuelSectionDensity = FuelProperties.density
		FuelDensity.append(FuelSectionDensity)


	FuelAverageDensity = sum(FuelDensity) / AxialTemperaturePoints # g / cm^
	FuelVolume = TotalFuelPins * math.pi * ((FreshFuelRadius*100) ** 2) * (FuelLength*100) # cm^3
	FuelMass = FuelVolume * FuelAverageDensity / 1000 # kg

	CoreFissileMass  = 0
	CoreActinideMass = 0
	CoreFuelMass     = FuelMass

	for batch in range(Batches):
	
		CAM = (FuelMass/Batches) * ActinideMassFraction[batch]
		CFM = CAM * FissileFraction[batch]

		CoreActinideMass += CAM
		CoreFissileMass  += CFM

	# Define the peak cladding outer wall temperature
	PeakFuelInnerTemperature = max(PeakFuelInnerTemperature)
	
	# Figure out where axially the peak cladding outer wall temperature occurs
	for k,v in FuelInnerAxialTemperature.items():
		if v == PeakFuelInnerTemperature:
			PeakFuelInnerTemperateAxialPosition = k

	cgf.write("];")
	cgf.close()

	return(FuelInnerAxialTemperature, PeakFuelInnerTemperature, PeakFuelInnerTemperateAxialPosition, CoreFuelMass, CoreFissileMass, CoreActinideMass,
		   FuelInnerAxialTemperatureZ2, FuelAverageDensity)
