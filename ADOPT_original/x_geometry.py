import math

def innergeometry(FTF, FTF_Convergence, FuelPinRows, RelativeWirePitch, PeakPinPower, CoolantTemperatureRise,
				  CoolantInletDensity, InteriorChannelCoolantVelocity, CoolantInletHeatCapacity, AverageCoolantVelocity,
				  PinsPerAssembly, SpacerType):

	## ASSUMPTIONS
	## 1. Peak power location is cooled by an interior coolant channel
	## 2. Coolant thermo-physical properties are evaluated at the inlet temperature

	PD = 0.9999999999
	i  = 0

	#print("PEAK PIN POWER IN GEO")
	#print(PeakPinPower)

	while PD < 1:

		if i > 1:
			InteriorChannelCoolantVelocity = AverageCoolantVelocity * 1.3
		elif i > 2:
			InteriorChannelCoolantVelocity = InteriorChannelCoolantVelocity - 1e-2

		i += 1

		################################################################################################### //// ######## //// #######
		##################### Peak required coolant mass-flow area ######################################## //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		# The coolant area required for the peak power pin in the core
		MassFlowArea        = PeakPinPower / (CoolantTemperatureRise * CoolantInletDensity * InteriorChannelCoolantVelocity * CoolantInletHeatCapacity)

		# The coolant area required for half of the peak power pin in the core
		HalfPinMassFlowArea = MassFlowArea / 2

		# Initial guesses to find assembly geometry
		Convergence  = 1e30           # Initial guess for assembly flat-to-flat (m)
		Diameter     = 1e-5           # Initial guess for pin diameter (m)
		WireDiameter = Diameter/20    # Initital guess for wire diameter (m)
	
		# Iterate until the calculated inside flat-to-flat distance matches the set one
		while Convergence > FTF_Convergence:
	
			# Incrementally increase the fuel pin diameter
			Diameter += 1e-7
	
			# The axial length of one wire rotation
			WirePitch = RelativeWirePitch * Diameter
	
			# Cos-Theta
			if WireDiameter > Diameter:
				CT = 1
			else:
				CT = WirePitch * (WirePitch ** 2 + math.pi ** 2 * (Diameter + WireDiameter) ** 2) ** (-0.1e1 / 0.2e1)

			# Calculated the corresponding needed P/D to get the given mass flow area (as defined above)
			if SpacerType == "None":

				PD = math.sqrt(0.6e1 * math.sqrt(0.3e1) * math.pi * Diameter ** 2 + 0.6e1 * math.sqrt(0.3e1) * math.pi * WireDiameter ** 2 + 0.48e2 * math.sqrt(0.3e1) * HalfPinMassFlowArea) / Diameter / 0.6e1
				#PD = math.sqrt(0.6e1 * math.sqrt(0.3e1) * math.pi * Diameter ** 2 + 0.6e1 * math.sqrt(0.3e1) * math.pi * WireDiameter ** 2 + 0.48e2 * math.sqrt(0.3e1) * HalfPinMassFlowArea) / Diameter / 0.6e1

			elif SpacerType == "Wire":

				PD = math.sqrt(0.6e1) * math.sqrt(CT * math.sqrt(0.3e1) * (math.pi * Diameter ** 2 * CT + math.pi * WireDiameter ** 2 + 0.8e1 * HalfPinMassFlowArea * CT)) / CT / Diameter / 0.6e1
				#PD = math.sqrt(0.6e1) * math.sqrt(CT * math.sqrt(0.3e1) * (math.pi * Diameter ** 2 * CT + math.pi * WireDiameter ** 2 + 0.8e1 * HalfPinMassFlowArea * CT)) / CT / Diameter / 0.6e1

			# Calculated pin pitch given P/D and Diameter (m)
			Pitch = PD * Diameter

			# Calculate the wire diameter as defined as the distance between outer rims of adjacent pins
			WireDiameter = Pitch - Diameter
		
			# Make sure the wire-diameter value is reasonable, if not, set to zero (for now)
			if WireDiameter > Diameter:
				WireDiameter = 0

			# Calculate the resulting internal flat-to-flat distance
			FTF_Calculated = 100 * (math.sqrt(0.3e1) * FuelPinRows * (Diameter + WireDiameter) - Diameter + 2 * Pitch)
			#FTF_Calculated = 100 * (math.sqrt(0.3e1) * FuelPinRows * (Diameter + WireDiameter) - Diameter + 2 * Pitch)

			# Correctly set the wire-diameter again for the next iteration
			WireDiameter = Pitch - Diameter
		
			# Check for convergence
			Convergence = abs(FTF - FTF_Calculated)	

	if SpacerType != "Wire":

		WireDiameter = 0

	TotalFlowArea = (math.sqrt(3)/2) * (FTF/100) ** 2 - 271 * math.pi/4 * (Diameter ** 2 + WireDiameter ** 2)
	MassFlowArea = 2 * HalfPinMassFlowArea

	return(Diameter, Pitch, WireDiameter, MassFlowArea, InteriorChannelCoolantVelocity)

