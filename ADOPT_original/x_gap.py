# -*- coding: UTF-8 -*-
from x_prop import *
import math

def gapt(PeakCladdingInnerWallTemperature, TemperaturePoints, TemperatureConvergence, PeakPinPeakLinearPower, \
	    GapOuterRadius, GapInnerRadius, FuelLength, CosinePinAxialPowerPeaking, CladdingInnerWallAxialTemperature, Name,
	    PinAxialPowerPeaking, mlabpath, Bond):

	#### Assumptions
	#### 1. Convective heat transfer is neglected (completely valid assumption - Source [1])
	#### 2. Neglection of near-surface effects for tight gap geometries
	
	# Lanning, D. D., & Hann, C. R. (1975). 
	# Review of methods applicable to the calculation of gap conductance in Zircaloy-clad UO2 fuel rods. 
	# doi:10.2172/4209005
	# 
	# When fuel is not contacting the cladding the thermal conduction is primarily throuqh the gas. 
	# When fuel does contact the cladding, 5 - 20% of the heat may flow through the contact points, 
	# depending on the contact pressure, the gas mix i n the gap, and the surface profiles. 
	# In no practical case however, does heat flow due to radiation exceed ~ 2 o%f the total.
	#
	# For gaps of 1e-3 cm or greater, hgas = kgas/gap-distance
	
	# Initial guess for the average cladding inner wall temperature at the axial bottom of the rod
	AverageGapTemperature = PeakCladdingInnerWallTemperature 
	
	# Start collecting guesses for the average cladding temperature (to determine average cladding conductivity)
	CollectAverageGapTemperatures = [AverageGapTemperature]
	
	PeakFuelRimTemperature    = []
	FuelRimAxialTemperature   = {}
	FuelRimAxialTemperatureZ2 = []
	
	# Start variable for outer cladding temperatures in MATLAB file
	cgi = open(mlabpath +  "/fuel_outer_temperature.m", 'a')
	cgi.write("git = [")
	
	# Do for all axial evaluation points
	for z in TemperaturePoints:
	
		# Initial value for counter to check conductivity convergence
		i = 0
	
		# Initial error for the temperature (since conductivity is not converged)
		GapTemperatureError = 1e6
	
		# Run until temperatures match within the convergence criteria
		while GapTemperatureError > TemperatureConvergence:
	
			# Increase the trail counter by 1
			i += 1

			BondProperties = nonsolids(material=Bond, temperature=AverageGapTemperature, pressure=1)
			GapConductivity = BondProperties.conductivity

			if PinAxialPowerPeaking < (math.pi/2):

				# Calculate the radial temperature difference across the cladding at the specific axial level
				GapTemperatureDelta = PeakPinPeakLinearPower * ( 1/(2 * math.pi * GapConductivity) * math.log(GapOuterRadius / GapInnerRadius) * math.cos(math.pi * z / (FuelLength * CosinePinAxialPowerPeaking)) )
	
			else:

				GapTemperatureDelta = PeakPinPeakLinearPower * ( 1/(2 * math.pi * GapConductivity) * math.log(GapOuterRadius / GapInnerRadius) * (math.cos(math.pi * z / CosinePinAxialPowerPeaking / FuelLength) - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)) / (0.1e1 - math.cos(math.pi / CosinePinAxialPowerPeaking / 0.2e1)))

			# Calculate the inner cladding wall temperature at the specific axial level
			FuelRimTemperature = CladdingInnerWallAxialTemperature.get(z) + GapTemperatureDelta
	
			# Calculate the cladding mid-wall temperature
			AverageGapTemperature = (FuelRimTemperature + CladdingInnerWallAxialTemperature.get(z)) / 2
	
			# Add the new mid-wall temperature guess
			CollectAverageGapTemperatures.append(AverageGapTemperature)
	
			# Calculate the difference between the previous guess for average temperature and the current
			GapTemperatureError = CollectAverageGapTemperatures[i] - CollectAverageGapTemperatures[i-1]
	
		# Collect axial cladding outer wall temperature
		COW_Temperature = {z : FuelRimTemperature}
	
		# Update cladding outer wall temperature dictionary
		PeakFuelRimTemperature.append(FuelRimTemperature)
	
		# Update cladding outer wall temperature dictionary
		FuelRimAxialTemperature.update(COW_Temperature)

		# Write data to MATLAB
		cgi.write("\n")
		cgi.write(str(FuelRimTemperature-273.15) + ",")

		FuelRimAxialTemperatureZ2.append(FuelRimTemperature-273.15)

	# Define the peak cladding outer wall temperature
	PeakFuelRimTemperature = max(PeakFuelRimTemperature)
	
	# Figure out where axially the peak cladding outer wall temperature occurs
	for k,v in FuelRimAxialTemperature.items():
		if v == PeakFuelRimTemperature:
			PeakFuelRimTemperateAxialPosition = k
	
	cgi.write("];")
	cgi.close()

	return(FuelRimAxialTemperature, PeakFuelRimTemperature,FuelRimAxialTemperatureZ2)
