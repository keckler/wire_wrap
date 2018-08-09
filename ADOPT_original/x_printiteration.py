# -*- coding: UTF-8 -*-

import math

def printiter(i, ChannelPressureDrop, InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity, \
			  CoolantOutletTemperature, PeakCladdingOuterWallTemperature, PeakFuelInnerTemperature, Pitch, Diameter, AssemblyPitch, \
			  RadialReflectorRows, RadialShieldRows, FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction, \
			  ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, PeakCladdingInnerWallTemperature, \
			  CalculatedPeakCoolantVelocity, CoolantVelocityConstraint, CorePressureDropConstraint, AverageCoolantVelocity, VelocityPrecision, \
			  CladdingOuterTemperatureConstraint, TemperatureConvergence, FuelTemperatureConstraint, PinsPerAssembly,CladdingInnerTemperatureConstraint,
			  FuelPinRows, ConvergedSolution, FreshFuelRadius, CladdingThickness, Before, After, AverageCoolantOutletTemperature, \
			  xpressuredrop, xflowvelocity,xfueltemp,xcladi,xclado, Name, CoreDiameter, SystemDiameter,x,BeforeAll,RadialPowerPeaking, \
			  RadialPowerPeakDifference, MinKeff, MaxKeff, SerpentDepletion, SerpentRun, CoreOuterRadius, ShieldOuterRadius, PeakFlux, AverageFlux,
			  maxDPA, maxDPAcell, Cladding, PeakFluence, PeakAssemblyMassFlow, CoolantInletTemperature, NaturalCirculation, NaturalCirculationThermalCenterElevation,
			  DecayHeatTime, InletPressureDrop, OutletPressureDrop, NonCorePressureDropMultiplier, DuctThickness, InterAssemblyGap, xfom1, Power,
			  CorePD, TotPD, CoreVolume, FTF, InnerAssemblySideLength, DuctedAssemblyFTF, DuctedAssemblySideLength,
			  AssemblyHexagonFTF, AssemblyHexagonSideLength, TotalFuelPins, TotalFuelLength, AveragePinPower, PeakPinPower, AveragePinAverageLinearPower,
			  AveragePinPeakLinearPower, PeakPinAverageLinearPower, PeakPinPeakLinearPower, SystemVolume, SystemHeight, FuelLength, VolumetricPowerDensity,
			  Assemblies, CoreFissileMass, CoreFuelMass, SpecificPower, SpecificFissilePower, CoreActinideMass, AverageChannelPressureDrop,
			  AverageInletPressureDrop, AverageOutletPressureDrop, AverageCorePD, FuelMassDensityGCC, CoolantMassDensityGCC, FuelAverageDensity, 
			  CoolantAverageDensity, PinAxialPowerPeaking, AxialPowerPeakDifference, GapMarginPrint,DeflectionPrint,CreepPrint,SwellingPrint, MaxStress, 
			  StotB, PeakFastFluence, BOCKeff, EOCKeff, KeffCycleSwing, KeffPeakSwing, KeffErr, PlenumFissionGasPressure, PeakFCMIDesignPressure, 
			  CTR, DesignPressure, PlenumFissionGasPressureOP, HoopStress, CladdingYieldStrength, TotalSystemHeight, TotalSystemDiameter,
			  GasReleaseFraction, FuelGasReleaseFractionOP, OPPlenumTemperature, PlenumTemperature, HoopStressOP, CladdingYieldStrengthOP,
			  PlenumLengthDecrease, EffectiveUpperGasPlenumLength, UpperGasPlenumLength, CladdingCreep, CladdingFactor, SerpentDPA, 
			  SingleInteriorChannelFlowArea, SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, SingleInteriorChannelHydraulicDiameter,
			  SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, SingleInteriorChannelWettedPerimeter, 
			  SingleEdgeChannelWettedPerimeter, SingleCornerChannelWettedPerimeter, InteriorChannelFrictionFactor,
			  EdgeChannelFrictionFactor, CornerChannelFrictionFactor, AverageInteriorChannelFrictionFactor, AverageEdgeChannelFrictionFactor, 
			  AverageCornerChannelFrictionFactor, DecNatInteriorChannelFrictionFactor, DecNatEdgeChannelFrictionFactor, DecNatCornerChannelFrictionFactor, 
			  BundleAverageBelowCoreReynolds, AverageBelowCoreInteriorReynolds, AverageBelowCoreEdgeReynolds, AverageBelowCoreCornerReynolds, 
			  BelowCoreInteriorReynolds, BelowCoreEdgeReynolds, BelowCoreCornerReynolds, BelowCoreDecNatInteriorReynolds, BelowCoreDecNatEdgeReynolds, 
			  BelowCoreDecNatCornerReynolds, InteriorDecNatChannelCoolantVelocity, EdgeDecNatChannelCoolantVelocity, CornerDecNatChannelCoolantVelocity,
			  InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly, FlowConvergence, FlowError, CDF, InternalControlAssemblies,
			  CoreMassFlow, VolumetricFlowRate, PumpingPower, BondMassDensityGCC, CladdingMassDensityGCC, DuctMassDensityGCC, CoreMassDensityGCC, 
			  AverageDuctDensity, AverageBondDensity, AverageCladdingDensity, BondMass, CladdingMass, DuctMass, CoolantMass, FuelMassFraction, 
			  CoolantMassFraction, BondMassFraction, CladdingMassFraction, DuctMassFraction, AverageDecNatCoolantVelocity,
			  AverageBundleAverageBelowCoreReynolds, BundleAverageDecNatBelowCoreReynolds, ChannelPressureDropDecNat, PeakAssemblyMassFlowDecNat,
			  InletDecNatPressureDrop, OutletDecNatPressureDrop, TotalPressureDropDecNat, PumpPressureDrop, AverageAssemblyPower, PeakAssemblyPower,
			  PeakAssemblyDecNatPower, AverageAssemblyDecNatPower, AssemblyFlowArea, AssemblyWettedPerimeter, BundleHydraulicDiameter,
			  AverageFuelDeltaT, AverageCoolantTemperatureRise):

	timediff = abs(After-Before)
	hourdiff = timediff / 3600
	mindiff  = timediff / 60
	secdiff  = timediff
	CPUTime  = "n/a"	
	
	if secdiff >= 1 and mindiff < 1:
	
		if int(round(secdiff)) == 1:
	
			S = "s"

		else:

			S = "s"
	
		CPUTime = str(int(round(secdiff))) + S
	
	if mindiff >= 1 and hourdiff < 1:
	
		mindiff = int(math.floor(mindiff))
		secdiff = secdiff - mindiff*60
	
		if int(round(secdiff)) == 1:
	
			S = "s"
	
		else: 
	
			S = "s"
	
		if int(round(mindiff)) == 1:
		
			M = "m"
	
		else:
	
			M = "m"	
	
		CPUTime = str(int(round(mindiff))) + M + " " + str(int(round(secdiff))) + S
	
	if hourdiff >= 1:
	
		hourdiff = int(math.floor(hourdiff))
		mindiff  = int(math.floor(mindiff - hourdiff*60))
		secdiff  = secdiff - hourdiff*3600 - mindiff*60
	
		if int(round(hourdiff)) == 1:
		
			H = "h"
		
		else: 
		
			H = "h"
	
		if int(round(mindiff)) == 1:
		
			M = "m"
		
		else: 
		
			M = "m"	
	
		if int(round(secdiff)) == 1:
	
			S = "s"
	
		else: 
	
			S = "s"
	
		CPUTime = str(int(round(hourdiff))) + H + " " + str(int(round(mindiff))) + M + " " + str(int(round(secdiff))) + S

	timediff = abs(After-BeforeAll)
	hourdiff = timediff / 3600
	mindiff  = timediff / 60
	secdiff  = timediff
	TOTTime  = "n/a"	
	
	if secdiff >= 1 and mindiff < 1:
	
		if int(round(secdiff)) == 1:
	
			S = "s"
	
		else: 
	
			S = "s"
	
		TOTTime = str(int(round(secdiff))) + S
	
	if mindiff >= 1 and hourdiff < 1:
	
		mindiff = int(math.floor(mindiff))
		secdiff = secdiff - mindiff*60
	
		if int(round(secdiff)) == 1:
	
			S = "s"
	
		else: 
	
			S = "s"
	
		if int(round(mindiff)) == 1:
		
			M = "m"
		
		else: 
		
			M = "m"	
	
		TOTTime = str(int(round(mindiff))) + M + " " + str(int(round(secdiff))) + S
	
	if hourdiff >= 1:
	
		hourdiff = int(math.floor(hourdiff))
		mindiff  = int(math.floor(mindiff - hourdiff*60))
		secdiff  = secdiff - hourdiff*3600 - mindiff*60
	
		if int(round(hourdiff)) == 1:
		
			H = "h"
		
		else: 
		
			H = "h"
	
		if int(round(mindiff)) == 1:
		
			M = "m"
		
		else: 
		
			M = "m"	
	
		if int(round(secdiff)) == 1:
	
			S = "s"
	
		else: 
	
			S = "s"
	
		TOTTime = str(int(round(hourdiff))) + H + " " + str(int(round(mindiff))) + M + " " + str(int(round(secdiff))) + S

	print("             __                  __         ")
	print("            /\ \      v.2.1.0   /\ \__      ")
	print("     __     \_\ \    ___   _____\ \ ,_\     ")
	print("   /`__`\   /`_` \  / __`\/\ `__`\ \ \/     ")
	print("  /\ \L\.\_/\ \L\ \/\ \L\ \ \ \L\ \ \ \_    ")
	print("  \ \__/.\_\ \___,_\ \____/\ \ ,__/\ \__\   ")
	print("   \/__/\/_/\/__,_ /\/___/  \ \ \/  \/__/   ")
	print("                             \ \_\          ")
	print("         staffanq@gmail.com   \/_/          ")
	print(" ")
	#print("  Core name:  " + str(Name))
	if SerpentRun == "on":
		print("  Neutronic iter.: " + str(x) +", TH iter. = " + str(i))
	else:
		print("  TH iter. = " + str(i))
	print("  TH time:  " + CPUTime + ", tot. time: " + TOTTime)

	if x >= 1:
		print("  Radial/axial power peaking: {0:02.3f}".format(RadialPowerPeaking) + "/{0:02.3f}".format(PinAxialPowerPeaking))
		print("  Rel. error, radial: {0:02.2%}".format(abs(RadialPowerPeakDifference)) + ", axial: {0:02.2%}".format(abs(AxialPowerPeakDifference)))
	else:
		print("  Radial/axial power peaking: {0:02.3f}".format(RadialPowerPeaking) + "/{0:02.3f}".format(PinAxialPowerPeaking))

	if FlowError < FlowConvergence:

		print("  Flow distribution is: Converged")

	else:

		print("  Flow distribution is: Not converged")
		
	print(" ")	
	print("----- FLOW ---------------------------------")
	print("  Peak ass. mass flow:      {0:02.2f}".format(PeakAssemblyMassFlow) + " kg/s")
	#print("  Nat. conv. flow frac.:    {0:02.1%}".format(NaturalCirculation))
	print("  Nat. circ FOM1:           {0:02.2f}".format(NaturalCirculationThermalCenterElevation) + " m (t={0:01.0f}".format(DecayHeatTime) + "s)")
	print("  Bundle pressure drop:     {0:02.1f}".format(ChannelPressureDrop/1e3) + " kPa")
	#print("  Inlet/outlet pres. drop:  {0:02.1f}".format(InletPressureDrop/1e3) + "/{0:02.1f}".format(OutletPressureDrop/1e3) + " kPa")
	print("  Core/total pressure drop: {0:02.1f}".format(CorePD) + "/{0:02.1f}".format(TotPD) + " kPa")
	print("  Ave/peak coolant vel.:    {0:02.3f}".format(AverageCoolantVelocity) + "/{0:02.3f}".format(EdgeChannelCoolantVelocity) + " m/s")	
	print(" ")	
	print("----- TEMPERATURE --------------------------")
	print("  Coolant inlet T:       {0:02.1f}".format(CoolantInletTemperature-273.15) + " deg. C")
	print("  Ave. coolant outlet T: {0:02.1f}".format(AverageCoolantOutletTemperature-273.15) + " deg. C")
	print("  Peak coolant outlet T: {0:02.1f}".format(CoolantOutletTemperature-273.15) + " deg. C")
	print("  Peak clad outer T:     {0:02.1f}".format(PeakCladdingOuterWallTemperature-273.15) + " deg. C")
	print("  Peak clad inner T:     {0:02.1f}".format(PeakCladdingInnerWallTemperature-273.15) + " deg. C")
	print("  Peak fuel T:           {0:02.1f}".format(PeakFuelInnerTemperature-273.15) + " deg. C")
	print(" ")		
	print("----- GEOMETRY -----------------------------")
	print("  Pins/assembly:   " + str(PinsPerAssembly))
	print("  P/D:             {0:02.5f}".format(Pitch/Diameter))
	print("  Rod diameter:    {0:02.4f}".format(Diameter*100)           + " cm")
	#print("  Rod pitch (mm):       {0:02.4f}".format(Pitch*1000))
	#print("  Fuel diameter (mm):   {0:02.4f}".format(FreshFuelRadius*2000))
	print("  Duct thickness:  {0:02.4f}".format(DuctThickness)          + " mm")
	print("  IA-gap:          {0:02.4f}".format(InterAssemblyGap)       + " mm")
	print("  Clad thickness:  {0:02.4f}".format(CladdingThickness*1000) + " mm")
	print("  Core diameter:   {0:02.2f}".format(CoreOuterRadius*200)    + " cm")
	print("  Vessel height:   {0:02.2f}".format(TotalSystemHeight)      + " m")
	print("  Vessel diameter: {0:02.2f}".format(TotalSystemDiameter)    + " m")
	print(" ")	
	print("----- VOLUME FRACTIONS ---------------------")
	print("  Fuel:           {0:02.2%}".format(FuelVolumeFraction))
	print("  Gap:            {0:02.2%}".format(GapVolumeFraction))	
	print("  Coolant:        {0:02.2%}".format(ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction))
	print("  Structure:      {0:02.2%}".format(CladdingVolumeFraction + DuctVolumeFraction + WireVolumeFraction))	

	#print("  Cladding:          {0:02.2%}".format(CladdingVolumeFraction))
	#print("  Wire:              {0:02.2%}".format(WireVolumeFraction))
	#print("  Active coolant:    {0:02.2%}".format(ActiveCoolantVolumeFraction))	
	#print("  Duct:              {0:02.2%}".format(DuctVolumeFraction))
	#print("  IA coolant:        {0:02.2%}".format(InterAssemblyVolumeFraction))	

	print(" ")	
	print("----- CONSTRAINTS --------------------------")
	print("  Peak flow velocity:  " + xflowvelocity)
	print("  Core pressure drop:  " + xpressuredrop)
	print("  Nat. circ FOM1:      " + xfom1)	
	print("  Peak outer clad T:   " + xclado)	
	print("  Peak inner clad T:   " + xcladi)		
	print("  Peak fuel T:         " + xfueltemp)

	if x > 0:

		if SerpentRun == "on":
	
			print(" ")
			print("----- From SERPENT --------------------------")
			#print("  Peak flux: {0:02.2f}".format(PeakFlux) + " (x 1e14 n/cm^2*s)")
			#print("  Peak fluence: {0:02.2f}".format(PeakFluence/1e8) + " (x 1e23 n/cm^2)")
	
			print("  Keff (BOC/EOC): {0:02.4f}".format(BOCKeff) + "/{0:02.4f}".format(EOCKeff)  + " (+/- {0:02.5f}".format(KeffErr) + ")")		
			print("  Keff (min/max): {0:02.4f}".format(MinKeff) + "/{0:02.4f}".format(MaxKeff)  + " (+/- {0:02.5f}".format(KeffErr) + ")")
			#print("  Keff BOC-EOC swing: {0:02.2%}".format(KeffCycleSwing))
			print("  Keff max-min swing: {0:02.2%}".format(KeffPeakSwing))
	
			if SerpentDPA == "on":
				print("  Peak fast fluence:  {0:02.2f}".format(PeakFastFluence/1e23) + " (x 1e23 n/cm^2)")	
				print("  Peak " + Cladding + " cycle DPA: {0:02.2f}".format(maxDPA) + " (" + maxDPAcell + ")")

	if ConvergedSolution == 1:

		sol = open("results/" + Name + "/CoreInfo.txt", 'w')

		sol.write("             __                  __         \n")
		sol.write("            /\ \      v.2.1.0   /\ \__      \n")
		sol.write("     __     \_\ \    ___   _____\ \ ,_\     \n")
		sol.write("   /`__`\   /`_` \  / __`\/\ `__`\ \ \/     \n")
		sol.write("  /\ \L\.\_/\ \L\ \/\ \L\ \ \ \L\ \ \ \_    \n")
		sol.write("  \ \__/.\_\ \___,_\ \____/\ \ ,__/\ \__\   \n")
		sol.write("   \/__/\/_/\/__,_ /\/___/  \ \ \/  \/__/   \n")
		sol.write("                             \ \_\          \n")
		sol.write("         staffanq@gmail.com   \/_/          \n")
		sol.write(" \n")
		sol.write("  Core name:  " + str(Name) + "\n")
		if SerpentRun == "on":
			sol.write("  Neutronic iter.: " + str(x) +", TH iter. = " + str(i) + "\n")
		else:
			sol.write("  TH iter. = " + str(i) + "\n")
		sol.write("  TH time:  " + CPUTime + ", tot. time: " + TOTTime + "\n")
		sol.write(" \n")	
		sol.write("----- POWER ---------------------------------------\n")
		sol.write("  Total thermal power:  {0:02.2f}".format(Power/1e6) + " MW \n")

		if x >= 1:
			sol.write("  Radial power peaking: {0:02.3f}".format(RadialPowerPeaking) + " (d: {0:02.2%}".format(abs(RadialPowerPeakDifference)) + ")\n")
		else:
			sol.write("  Radial power peaking: {0:02.3f}".format(RadialPowerPeaking) + "\n")

		sol.write(" \n")
		sol.write("----- POWER DENSITY -------------------------------\n")
		sol.write("  Core volumetric power density:  {0:02.2f}".format(VolumetricPowerDensity)           + " MW/m^3 \n")		
		sol.write("  Core-averaged linear power:     {0:02.2f}".format(AveragePinAverageLinearPower/1e3) + " kW/m   \n")
		sol.write("  Peak ax-averaged linear power:  {0:02.2f}".format(PeakPinAverageLinearPower/1e3)    + " kW/m   \n")
		sol.write("  Peak linear power:              {0:02.2f}".format(PeakPinPeakLinearPower/1e3)       + " kW/m   \n")
		sol.write("  Fuel specific power:            {0:02.2f}".format(SpecificPower)                    + " kW/kg  \n")
		sol.write("  BOC fissile specific power:     {0:02.2f}".format(SpecificFissilePower)             + " kW/kg  \n")
		sol.write(" \n")
		sol.write("----- PRIMARY LOOP FLOW CHARACTERISTICS -----------\n")
		sol.write("  Pressure drop:        {0:02.1f}".format(TotPD)              + " kPa   \n")
		sol.write("  Mass flow rate:       {0:02.1f}".format(CoreMassFlow)       + " kg/s  \n")
		sol.write("  Volumetric flow rate: {0:02.3f}".format(VolumetricFlowRate) + " m^3/s \n")
		sol.write("  Pumping power:        {0:02.3f}".format(PumpingPower)       + " MW    \n")
		sol.write(" \n")
		sol.write("----- PEAK-POWER ASSEMBLY INFO (full power) -------\n")
		sol.write("  Power:                      {0:02.2f}".format(PeakAssemblyPower/1e6) + " MW \n")		
		sol.write("  Mass flow:                  {0:02.2f}".format(PeakAssemblyMassFlow)           + " kg/s \n")
		sol.write("  Interior channel velocity:  {0:02.3f}".format(InteriorChannelCoolantVelocity) + " m/s  \n")	
		sol.write("  Edge channel velocity:      {0:02.3f}".format(EdgeChannelCoolantVelocity)     + " m/s  \n")	
		sol.write("  Corner channel velocity:    {0:02.3f}".format(CornerChannelCoolantVelocity)   + " m/s  \n")	
		sol.write("  Bundle pressure drop:       {0:02.1f}".format(ChannelPressureDrop/1e3)  + " kPa \n")
		sol.write("  Inlet pressure drop:        {0:02.1f}".format(InletPressureDrop/1e3)    + " kPa \n")
		sol.write("  Outlet pressure drop:       {0:02.1f}".format(OutletPressureDrop/1e3)   + " kPa \n")
		sol.write("  Assembly pressure drop:     {0:02.1f}".format(CorePD)                   + " kPa \n")
		sol.write(" \n")		
		sol.write("----- PEAK-POWER ASSEMBLY INFO (decay power) ------\n")
		sol.write("  Power:                       {0:02.2f}".format(PeakAssemblyDecNatPower/1e3) + " kW \n")	
		sol.write("  Mass flow:                   {0:02.2f}".format(PeakAssemblyMassFlowDecNat) + " kg/s \n")
		sol.write("  Interior channel velocity:   {0:02.3f}".format(InteriorDecNatChannelCoolantVelocity) + " m/s  \n")	
		sol.write("  Edge channel velocity:       {0:02.3f}".format(EdgeDecNatChannelCoolantVelocity)     + " m/s  \n")	
		sol.write("  Corner channel velocity:     {0:02.3f}".format(CornerDecNatChannelCoolantVelocity)   + " m/s  \n")	
		sol.write("  Bundle pressure drop:        {0:02.1f}".format(ChannelPressureDropDecNat)  + " Pa \n")
		sol.write("  Inlet pressure drop:         {0:02.1f}".format(InletDecNatPressureDrop)    + " Pa \n")
		sol.write("  Outlet pressure drop:        {0:02.1f}".format(OutletDecNatPressureDrop)   + " Pa \n")
		sol.write("  Pump pressure drop:          {0:02.1f}".format(PumpPressureDrop)           + " Pa \n")
		sol.write("  Assembly pressure drop:      {0:02.1f}".format(ChannelPressureDropDecNat+InletDecNatPressureDrop+OutletDecNatPressureDrop) + " Pa \n")
		sol.write("  Primary cycle pressure drop: {0:02.1f}".format(TotalPressureDropDecNat) + " Pa \n")
		sol.write(" \n")
		sol.write("----- AVERAGE-POWER ASSEMBLY INFO -----------------\n")
		sol.write("  Power:                      {0:02.2f}".format(AverageAssemblyPower/1e6) + " MW \n")			
		sol.write("  Mass flow:                  {0:02.2f}".format(PeakAssemblyMassFlow/RadialPowerPeaking)               + " kg/s \n")
		sol.write("  Interior channel velocity:  {0:02.3f}".format(InteriorChannelCoolantVelocity/RadialPowerPeaking) + " m/s  \n")	
		sol.write("  Edge channel velocity:      {0:02.3f}".format(EdgeChannelCoolantVelocity/RadialPowerPeaking)     + " m/s  \n")	
		sol.write("  Corner channel velocity:    {0:02.3f}".format(CornerChannelCoolantVelocity/RadialPowerPeaking)   + " m/s  \n")	
		sol.write("  Bundle pressure drop:       {0:02.1f}".format(AverageChannelPressureDrop/1e3)  + " kPa \n")				
		sol.write("  Inlet pressure drop:        {0:02.1f}".format(AverageInletPressureDrop/1e3)    + " kPa \n")
		sol.write("  Outlet pressure drop:       {0:02.1f}".format(AverageOutletPressureDrop/1e3)   + " kPa \n")
		sol.write("  Orificing pressure drop:    {0:02.1f}".format(CorePD-AverageCorePD)            + " kPa \n")
		sol.write("  Assembly pressure drop:     {0:02.1f}".format(CorePD)                          + " kPa \n")
		sol.write(" \n")
		sol.write("----- NATURAL CIRCULATION / DECAY HEAT REMOVAL-----\n")
		sol.write(" \n")
		sol.write("  Full-power nat. convection flow frac.: {0:02.1%}".format(NaturalCirculation) + "\n")
		sol.write(" \n")
		sol.write("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  *\n")			
		sol.write("  Thermal-center elevation needed for natural   \n")
		sol.write("  circulation decay heat removal: {0:02.2f}".format(NaturalCirculationThermalCenterElevation) + " m \n")
		sol.write("  (at t={0:01.0f}".format(DecayHeatTime) + "s after shutdown) \n")
		sol.write("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  *\n")	
		sol.write(" \n")	
		sol.write("----- TEMPERATURES --------------------------------\n")
		sol.write("  Coolant inlet T:         {0:02.1f}".format(CoolantInletTemperature-273.15) + " deg. C\n")
		sol.write("  Ave. coolant outlet T:   {0:02.1f}".format(AverageCoolantOutletTemperature-273.15) + " deg. C\n")
		sol.write("  Peak coolant outlet T:   {0:02.1f}".format(CoolantOutletTemperature-273.15) + " deg. C\n")
		sol.write("  Peak clad outer T:       {0:02.1f}".format(PeakCladdingOuterWallTemperature-273.15) + " deg. C\n")
		sol.write("  Peak clad inner T:       {0:02.1f}".format(PeakCladdingInnerWallTemperature-273.15) + " deg. C\n")
		sol.write("  Peak fuel T:             {0:02.1f}".format(PeakFuelInnerTemperature-273.15) + " deg. C\n")
		sol.write(" \n")		
		sol.write("----- ROD GEOMETRY --------------------------------\n")
		sol.write("  P/D:             {0:02.5f}".format(Pitch/Diameter)         +     "\n")
		sol.write("  Rod pitch:       {0:02.4f}".format(Pitch*100)              + " cm \n")		
		sol.write("  Rod diameter:    {0:02.4f}".format(Diameter*100)           + " cm \n")
		sol.write("  Fuel diameter:   {0:02.4f}".format(FreshFuelRadius*200)    + " cm \n")
		sol.write("  Clad thickness:  {0:02.4f}".format(CladdingThickness*1000) + " mm \n")
		sol.write(" \n")	
		sol.write("----- ASSEMBLY GEOMETRY --------------------------\n")
		sol.write("  Pins/assembly:                " + str(PinsPerAssembly)                         +     "\n")
		sol.write("  Duct thickness:               {0:02.3f}".format(DuctThickness)                 + " mm \n")
		sol.write("  Inter-assembly gap:           {0:02.3f}".format(InterAssemblyGap)              + " mm \n")
		sol.write("  Assembly pitch:               {0:02.2f}".format(AssemblyPitch)                 + " cm \n")
		sol.write("  Assembly inner flat-to-flat:  {0:02.2f}".format(InnerAssemblySideLength*2)     + " cm \n")			
		sol.write("  Ducted assembly flat-to-flat: {0:02.2f}".format(DuctedAssemblyFTF)             + " cm \n")	
		sol.write("  Ducted assembly side length:  {0:02.2f}".format(DuctedAssemblySideLength)      + " cm \n")	
		sol.write(" \n")	
		sol.write("----- DUCT SPECIFICS ----------------------------\n")
		sol.write("  Peak duct stress (corner):           {0:02.1f}".format(MaxStress)         + " MPa\n")		
		sol.write("  Peak duct stress (mid-wall):         {0:02.1f}".format(StotB)             + " MPa\n")	
		sol.write("  Duct thickness:                      {0:02.3f}".format(DuctThickness)     + " mm \n")
		sol.write("  Set EOL duct-gap margin:             {0:02.3f}".format(GapMarginPrint)    + " mm \n")
		sol.write("  Duct pressure-deflection:            {0:02.3f}".format(DeflectionPrint)   + " mm \n")		
		sol.write("  EOL duct-gap reduction by creep:     {0:02.3f}".format(CreepPrint)        + " mm \n")	
		sol.write("  EOL duct-gap reduction by swelling:  {0:02.3f}".format(SwellingPrint)     + " mm \n")
		sol.write("  Design inter-assembly gap:           {0:02.3f}".format(InterAssemblyGap)  + " mm \n")			
		sol.write(" \n")
		sol.write("----- CLADDING SPECIFICS ------------------------\n")

		if PlenumLengthDecrease > 0:

			sol.write("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - *  \n")
			sol.write("  System is using metallic fuel, liquid bond,        \n")		
			sol.write("  and a smear density less than 100%. As the fuel    \n")
			sol.write("  swells with burnup, it expels bond (that doesn't   \n")
			sol.write("  infiltrate fuel pores) to the plenum, reducing     \n")
			sol.write("  the effective volume for gas in the upper gas      \n")		
			sol.write("  plenum, which gives an effective length reduction  \n")
			sol.write("  of: {0:02.1f}".format((UpperGasPlenumLength-EffectiveUpperGasPlenumLength)*100) + " cm, from {0:02.1f}".format(UpperGasPlenumLength*100) + " cm to {0:02.1f}".format(EffectiveUpperGasPlenumLength*100) + " cm. \n")
			sol.write("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  * \n")				
			sol.write(" \n")

		sol.write("  Limiting factor for cladding: " + CladdingFactor + "\n")	
		sol.write(" \n")
		sol.write("  Cladding thickness ratio:     {0:02.4f}".format(CTR)                        +      "\n")
		sol.write("  Cladding thickness:           {0:02.4f}".format(CladdingThickness*1000)     + " mm  \n")					
		sol.write("  Cumulative life-time creep:   {0:02.2%}".format(CladdingCreep/100)          + "\n")
		sol.write("  Cumulative damage fraction:   {0:02.7f}".format(CDF)                        + "\n")
		sol.write(" \n")
		sol.write("  Exp. ave. plenum temperature:  {0:02.1f}".format(OPPlenumTemperature-273.15)   + " dec. C\n")
		sol.write("  Expected fission gas release:  {0:02.1%}".format(FuelGasReleaseFractionOP)   + "\n")	
		sol.write("  Expected fission gas pressure: {0:02.1f}".format(PlenumFissionGasPressureOP) + " MPa \n")	
		sol.write("  Expected FCMI pressure:        [n/a] \n")
		sol.write("  Expected clad. stress (yield): {0:02.1f}".format(HoopStressOP) + " MPa ({0:02.1f}".format(CladdingYieldStrengthOP) +" MPa)  \n")
		sol.write(" \n")
		sol.write("  Design plenum temperature:     {0:02.1f}".format(PlenumTemperature-273.15)   + " dec. C\n")		
		sol.write("  Design fission gas release:    {0:02.1%}".format(GasReleaseFraction)         + "\n")			
		sol.write("  Design fission gas pressure:   {0:02.1f}".format(PlenumFissionGasPressure)   + " MPa \n")	
		sol.write("  Design FCMI pressure:          {0:02.1f}".format(PeakFCMIDesignPressure)     + " MPa \n")
		sol.write("  Design-limiting pressure:      {0:02.1f}".format(DesignPressure)             + " MPa \n")	
		sol.write("  Design clad. stress (yield):   {0:02.1f}".format(HoopStress) + " MPa ({0:02.1f}".format(CladdingYieldStrength) +" MPa)  \n")
		sol.write(" \n")
		sol.write("----- CORE GEOMETRY ------------------------------\n")
		sol.write("  # of fuel assembles:    " + str(Assemblies)                                 +      "\n")
		sol.write("  # of control assembles: " + str(InternalControlAssemblies)                  +      "\n")
		sol.write("  # of fuel pins:         " + str(TotalFuelPins)                              +      "\n")
		sol.write("  Active core volume:     {0:02.2f}".format(CoreVolume)                       + " m^3 \n")
		sol.write("  Equiv. core diameter:   {0:02.2f}".format(CoreOuterRadius*200)              + " cm  \n")	
		sol.write("  Active core height:     {0:02.2f}".format(FuelLength * 100)                 + " cm  \n")	
		sol.write("  Core H/D ratio:         {0:02.2f}".format(FuelLength / (CoreOuterRadius*2)) + "     \n")
		sol.write("  Total fueled length:    {0:02.0f}".format(TotalFuelLength)                  + " m   \n")
		sol.write(" \n")	
		sol.write("----- SYSTEM GEOMETRY ----------------------------\n")
		sol.write("  Core-assembly height:     {0:02.2f}".format(SystemHeight*100) + " cm  \n")
		sol.write("  Approx. vessel height:    {0:02.2f}".format(TotalSystemHeight)   + " m   \n")
		sol.write("  Approx. vessel diameter:  {0:02.2f}".format(TotalSystemDiameter) + " m   \n")
		sol.write(" \n")		
		sol.write("----- VOLUME FRACTIONS ---------------------------\n")
		sol.write("  Fuel:              {0:02.2%}".format(FuelVolumeFraction)          + "\n")
		sol.write("  Gap:               {0:02.2%}".format(GapVolumeFraction)           + "\n")
		sol.write("  Cladding:          {0:02.2%}".format(CladdingVolumeFraction)      + "\n")
		sol.write("  Wire:              {0:02.2%}".format(WireVolumeFraction)          + "\n")
		sol.write("  Active coolant:    {0:02.2%}".format(ActiveCoolantVolumeFraction) + "\n")	
		sol.write("  Duct:              {0:02.2%}".format(DuctVolumeFraction)          + "\n")
		sol.write("  IA coolant:        {0:02.2%}".format(InterAssemblyVolumeFraction) + "\n")	
		sol.write(" \n")	
		sol.write("----- MASS FRACTIONS -----------------------------\n")
		sol.write("  Fuel:              {0:02.2%}".format(FuelMassFraction)     + "\n")
		sol.write("  Gap:               {0:02.2%}".format(BondMassFraction)     + "\n")
		sol.write("  Cladding+wire:     {0:02.2%}".format(CladdingMassFraction) + "\n")
		sol.write("  Active coolant:    {0:02.2%}".format(CoolantMassFraction)  + "\n")	
		sol.write("  Duct:              {0:02.2%}".format(DuctMassFraction)     + "\n")
		sol.write(" \n")	
		sol.write("----- MASSES --------(at BOC for fuel)------------\n")	
		sol.write("  Total fuel mass:    {0:02.0f}".format(CoreFuelMass)                  + " kg \n")			
		sol.write("  Actinides:          {0:02.0f}".format(CoreActinideMass)              + " kg \n")
		sol.write("  Fuel non-actinides: {0:02.0f}".format(CoreFuelMass-CoreActinideMass) + " kg \n")			
		sol.write("  Fissile material:   {0:02.0f}".format(CoreFissileMass)               + " kg \n")
		sol.write(" \n")	
		sol.write("  Bond:               {0:01.0f}".format(BondMass)                      + " kg \n")
		sol.write("  Cladding:           {0:02.0f}".format(CladdingMass)                  + " kg \n")
		sol.write("  Coolant:            {0:02.0f}".format(CoolantMass)                   + " kg \n")
		sol.write("  Duct:               {0:02.0f}".format(DuctMass)                      + " kg \n")
	
		TotalCoreMass = CoreFuelMass + BondMass + CladdingMass + CoolantMass + DuctMass

		sol.write("  Total core:         {0:02.0f}".format(TotalCoreMass)                 + " kg \n")

		sol.write(" \n")
		sol.write("----- CORE-AVERAGED (smeared) DENSITIES ----------\n")				
		sol.write("  Fuel:       {0:02.2f}".format(FuelMassDensityGCC)     + " g/cm^3 \n")
		sol.write("  Bond:       {0:02.1f}".format(BondMassDensityGCC)     + " g/cm^3 \n")		
		sol.write("  Cladding:   {0:02.2f}".format(CladdingMassDensityGCC) + " g/cm^3 \n")		
		sol.write("  Coolant:    {0:02.2f}".format(CoolantMassDensityGCC)  + " g/cm^3 \n")
		sol.write("  Duct:       {0:02.2f}".format(DuctMassDensityGCC)     + " g/cm^3 \n")	
		sol.write("  Core:       {0:02.2f}".format(CoreMassDensityGCC)     + " g/cm^3 \n")	
		sol.write(" \n")
		sol.write("----- AVERAGE COMPONENT DENSITIES ----------------\n")				
		sol.write("  Fuel:       {0:02.2f}".format(FuelAverageDensity)     + " g/cm^3 \n")
		sol.write("  Bond:       {0:02.1f}".format(AverageBondDensity)     + " g/cm^3 \n")
		sol.write("  Cladding:   {0:02.2f}".format(AverageCladdingDensity) + " g/cm^3 \n")
		sol.write("  Coolant:    {0:02.2f}".format(CoolantAverageDensity/1e3)  + " g/cm^3 \n")
		sol.write("  Duct:       {0:02.2f}".format(AverageDuctDensity)     + " g/cm^3 \n")
		sol.write(" \n")		
		sol.write("----- CONSTRAINTS --------------------------------\n")
		sol.write("  Peak flow velocity:  " + xflowvelocity  + "\n")
		sol.write("  Core pressure drop:  " + xpressuredrop  + "\n")
		sol.write("  Nat. circ FOM1:      " + xfom1          + "\n")	
		sol.write("  Peak outer clad T:   " + xclado         + "\n")	
		sol.write("  Peak inner clad T:   " + xcladi         + "\n")		
		sol.write("  Peak fuel T:         " + xfueltemp      + "\n")

		solth = open("results/" + Name + "/TH-details.txt", 'w')

		solth.write("----- THERMAL-HYDRAULIC DETAILS-------------------\n")
		solth.write(" \n")	
		solth.write("  Channels per assembly:       \n") 
		solth.write("  ---------------------------------  \n")	
		solth.write("  Interior:   " + str(InteriorChannelsPerAssembly) + " \n")
		solth.write("  Edge:       " + str(EdgeChannelsPerAssembly)     + " \n")
		solth.write("  Corner:     " + str(CornerChannelsPerAssembly)   + " \n")
		solth.write("  Total:      " + str(InteriorChannelsPerAssembly+EdgeChannelsPerAssembly+CornerChannelsPerAssembly) + "\n")		
		solth.write(" \n")
		solth.write("  Flow-area:       \n")
		solth.write("  ---------------------------------  \n")
		solth.write("  Interior:   {0:02.4f}".format(SingleInteriorChannelFlowArea*1e6) + " mm^2 \n")
		solth.write("  Edge:       {0:02.4f}".format(SingleEdgeChannelFlowArea*1e6)     + " mm^2 \n")
		solth.write("  Corner:     {0:02.4f}".format(SingleCornerChannelFlowArea*1e6)   + " mm^2 \n")
		solth.write("  Ass. total: {0:02.4f}".format(AssemblyFlowArea*(100**2))              + " cm^2 \n")
		solth.write(" \n")
		solth.write("  Hydraulic diameter:       \n")
		solth.write("  ------------------------------------------  \n")	
		solth.write("  Interior:   {0:02.4f}".format(SingleInteriorChannelHydraulicDiameter*1e3) + " mm \n")
		solth.write("  Edge:       {0:02.4f}".format(SingleEdgeChannelHydraulicDiameter*1e3)     + " mm \n")
		solth.write("  Corner:     {0:02.4f}".format(SingleCornerChannelHydraulicDiameter*1e3)   + " mm \n")
		solth.write("  Ass. total: {0:02.4f}".format(BundleHydraulicDiameter*1e3)                + " mm \n")		
		solth.write(" \n")
		solth.write("  Wetted perimeter per channel:       \n")
		solth.write("  ----------------------------------------  \n")
		solth.write("  Interior:   {0:02.4f}".format(SingleInteriorChannelWettedPerimeter*1e3) + " mm \n")
		solth.write("  Edge:       {0:02.4f}".format(SingleEdgeChannelWettedPerimeter*1e3)     + " mm \n")
		solth.write("  Corner:     {0:02.4f}".format(SingleCornerChannelWettedPerimeter*1e3)   + " mm \n")
		solth.write("  Ass. total: {0:02.4f}".format(AssemblyWettedPerimeter*100)              + " cm \n")
		solth.write(" \n")  
		solth.write("  Flow velocity in peak-power assembly at full power/flow:\n")
		solth.write("  ------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.4f}".format(InteriorChannelCoolantVelocity) + " m/s \n")
		solth.write("  Edge:       {0:02.4f}".format(EdgeChannelCoolantVelocity)     + " m/s \n")
		solth.write("  Corner:     {0:02.4f}".format(CornerChannelCoolantVelocity)   + " m/s \n")
		solth.write("  Average:    {0:02.4f}".format(AverageCoolantVelocity)         + " m/s \n")
		solth.write(" \n") 
		solth.write("  Flow velocity in average-power assembly at full power/flow:\n")
		solth.write("  ---------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.4f}".format(InteriorChannelCoolantVelocity/RadialPowerPeaking) + " m/s \n")
		solth.write("  Edge:       {0:02.4f}".format(EdgeChannelCoolantVelocity/RadialPowerPeaking)     + " m/s \n")
		solth.write("  Corner:     {0:02.4f}".format(CornerChannelCoolantVelocity/RadialPowerPeaking)   + " m/s \n")
		solth.write("  Average:    {0:02.4f}".format(AverageCoolantVelocity/RadialPowerPeaking)         + " m/s \n")
		solth.write(" \n") 
		solth.write("  Flow velocity in peak-power assembly at decay power and natural circulation flow:\n")
		solth.write("  -------------------------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.4f}".format(InteriorDecNatChannelCoolantVelocity) + " m/s \n")
		solth.write("  Edge:       {0:02.4f}".format(EdgeDecNatChannelCoolantVelocity)     + " m/s \n")
		solth.write("  Corner:     {0:02.4f}".format(CornerDecNatChannelCoolantVelocity)   + " m/s \n")
		solth.write("  Average:    {0:02.4f}".format(AverageDecNatCoolantVelocity)         + " m/s \n")
		solth.write(" \n") 
		solth.write("  Flow velocity in average-power assembly at decay power and natural circulation flow:\n")
		solth.write("  ----------------------------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.4f}".format(InteriorDecNatChannelCoolantVelocity/RadialPowerPeaking) + " m/s \n")
		solth.write("  Edge:       {0:02.4f}".format(EdgeDecNatChannelCoolantVelocity/RadialPowerPeaking)     + " m/s \n")
		solth.write("  Corner:     {0:02.4f}".format(CornerDecNatChannelCoolantVelocity/RadialPowerPeaking)   + " m/s \n")
		solth.write("  Average:    {0:02.4f}".format(AverageDecNatCoolantVelocity/RadialPowerPeaking)         + " m/s \n")
		solth.write(" \n") 
		solth.write("  Inlet Reynolds number in peak-power assembly at full power/flow: \n")
		solth.write("  ---------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.0f}".format(BelowCoreInteriorReynolds)       + " \n")
		solth.write("  Edge:       {0:02.0f}".format(BelowCoreEdgeReynolds)           + " \n")
		solth.write("  Corner:     {0:02.0f}".format(BelowCoreCornerReynolds)         + " \n")	
		solth.write("  Average:    {0:02.0f}".format(BundleAverageBelowCoreReynolds)  + " \n")
		solth.write(" \n")  
		solth.write("  Inlet Reynolds number in average-power assembly at full power/flow: \n")
		solth.write("  ------------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.0f}".format(AverageBelowCoreInteriorReynolds)      + " \n")
		solth.write("  Edge:       {0:02.0f}".format(AverageBelowCoreEdgeReynolds)          + " \n")
		solth.write("  Corner:     {0:02.0f}".format(AverageBelowCoreCornerReynolds)        + " \n")		
		solth.write("  Average:    {0:02.0f}".format(AverageBundleAverageBelowCoreReynolds) + " \n")	
		solth.write(" \n")  
		solth.write("  Inlet Reynolds number in peak-power assembly at decay power and natural circulation flow: \n")
		solth.write("  --------------------------------------------------------------------------------------------  \n") 	
		solth.write("  Interior:   {0:02.0f}".format(BelowCoreDecNatInteriorReynolds)      + " \n")
		solth.write("  Edge:       {0:02.0f}".format(BelowCoreDecNatEdgeReynolds)          + " \n")
		solth.write("  Corner:     {0:02.0f}".format(BelowCoreDecNatCornerReynolds)        + " \n")		
		solth.write("  Average:    {0:02.0f}".format(BundleAverageDecNatBelowCoreReynolds) + " \n")	
		solth.write(" \n")
		solth.write("  Friction coefficient at full power/flow in peak-power assembly: \n")
		solth.write("  --------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.5f}".format(InteriorChannelFrictionFactor) +  " \n")
		solth.write("  Edge:       {0:02.5f}".format(EdgeChannelFrictionFactor)     +  " \n")
		solth.write("  Corner:     {0:02.5f}".format(CornerChannelFrictionFactor)   +  " \n")
		solth.write(" \n")
		solth.write("  Friction coefficient at full power/flow in average-power assembly: \n")
		solth.write("  -----------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.5f}".format(AverageInteriorChannelFrictionFactor) +     " \n")
		solth.write("  Edge:       {0:02.5f}".format(AverageEdgeChannelFrictionFactor)     +     " \n")
		solth.write("  Corner:     {0:02.5f}".format(AverageCornerChannelFrictionFactor)   +     " \n")
		solth.write(" \n")
		solth.write("  Friction coefficient at decay power, natural circulation flow in peak-power assembly: \n")
		solth.write("  --------------------------------------------------------------------------------------------  \n")
		solth.write("  Interior:   {0:02.5f}".format(DecNatInteriorChannelFrictionFactor) +     " \n")
		solth.write("  Edge:       {0:02.5f}".format(DecNatEdgeChannelFrictionFactor)     +     " \n")
		solth.write("  Corner:     {0:02.5f}".format(DecNatCornerChannelFrictionFactor)   +     " \n")

def reactivityout(x, Name, SequentialAxialInCoreCoolantReactivity, SeqCoolCoefficientsPCM, SeqCoolCoefficientsCents,
			  CoolantTemperaturePerturbation, SeqCoolPerKG, SeqFuelPerKG, SequentialAxialFuelReactivity, SequentialAxialCladReactivity, SeqCladPerKG,
			  RadialReactivityCoefficientCMPCM, RadialReactivityCoefficientCMCents, SequentialBUCKeff, SequentialBUCKeffError, BUControlInsertionSimulation,
			  BelowCoreReactPerKG, AboveCoreReactPerKG, BelowCoreReactPCM, BelowCoreReactCents, AboveCoreReactPCM, AboveCoreReactCents, BelowCents, AboveCents, BelowPCM, AbovePCM,
			  VoidWorth, CoolantReactivityCoefficient, CoolantReactivityCoefficientPCM, CoolantReactivityCoefficientCents,
			  FuelReactivityCoefficient, FuelReactivityCoefficientPCM, FuelReactivityCoefficientCents, TotalVoidCalculation, RadialReactivityCoefficientCents,
			  RadialReactivityCoefficientPCM, RadialExpansionCoefficient, FuelDopplerCoefficient, FuelDopplerCoefficientCents, FuelDopplerCoefficientPCM, BOCBeff, EOCBeff, 
			  MinBeff, MaxBeff, BeffErr, BOCKeff, EOCKeff, KeffErr, MinKeff, MaxKeff, SerpentDepletion, PeakFlux, PeakFluence, PeakFastFluence, maxDPA, maxDPAcell, Cladding, 
			  SerpentDPA, KeffCycleSwing, KeffPeakSwing, SeqFuelPerPCM, SeqFuelPerCent, FuelTemperaturePerturbation, SerpentRun, AverageFuelDeltaT, AverageCoolantTemperatureRise,
			  AverageCoolantOutletTemperature):

	if x > 0:

		solq = open("results/" + Name + "/Neutronics.txt", 'w')
	
		solq.write("\n")
		solq.write("----- Multiplication -----------------------------\n")
		solq.write("  Keff (BOC/EOC):     {0:02.4f}".format(BOCKeff) + "/{0:02.4f}".format(EOCKeff)  + " (+/- {0:02.5f}".format(KeffErr) + ")\n")			
		solq.write("  Keff (min/max):     {0:02.4f}".format(MinKeff) + "/{0:02.4f}".format(MaxKeff)  + " (+/- {0:02.5f}".format(KeffErr) + ")\n")	
		
		if SerpentDepletion == "on":
	
			solq.write("  Keff BOC-EOC swing: {0:02.2%}".format(KeffCycleSwing)                          + "\n")
			solq.write("  Keff max-min swing: {0:02.2%}".format(KeffPeakSwing)                           + "\n")
	
		solq.write("\n")
		solq.write("----- Delayed neutron fraction  ------------------\n")
		solq.write("  Beff (BOC/EOC):     {0:02.0f}".format(BOCBeff*1e5) + "/{0:02.0f}".format(EOCBeff*1e5)  + " pcm (+/- {0:02.1f}".format(BeffErr*BOCBeff*1e5) + " pcm)\n")
		solq.write("  Beff (min/max):     {0:02.0f}".format(MinBeff*1e5) + "/{0:02.0f}".format(MaxBeff*1e5)  + " pcm (+/- {0:02.1f}".format(BeffErr*BOCBeff*1e5) + " pcm)\n")	
		solq.write("\n")
		solq.write("----- Flux and fluence ---------------------------\n")
		solq.write("  Peak flux:          {0:02.2f}".format(PeakFlux/1e14) + " (x 1e14 n/cm^2*s)\n")
		solq.write("  Peak fluence:       {0:02.2f}".format(PeakFluence/1e23) + " (x 1e23 n/cm^2)\n")	
		
		if SerpentDPA == "on":
	
			solq.write("  Peak fast fluence:  {0:02.2f}".format(PeakFastFluence/1e23) + " (x 1e23 n/cm^2, E > 0.1 MeV)\n")	
			solq.write("  Peak " + Cladding + " cycle DPA: {0:02.2f}".format(maxDPA) + " (" + maxDPAcell + ")\n")
	
		solq.write("\n")	
	
		if TotalVoidCalculation == "on":	
	
			solq.write("----- Void ---------------------------\n")
			solq.write("  Total coolant void worth: {0:02.2f}".format(VoidWorth) + "$\n")
			solq.write("\n")
	
		if SequentialAxialInCoreCoolantReactivity == "on":
	
			if CoolantTemperaturePerturbation == "void" or CoolantTemperaturePerturbation == "Void":

				solq.write("----- Sequential axial coolant void worth \n")
				solq.write("\n")
				solq.write("  Below the core: {0:02.2f}".format(BelowCents) + " cents ({0:02.2f}".format(BelowPCM) + " pcm) \n")
	
				for x in range(len(SeqCoolCoefficientsCents)):
		
					solq.write("  In-core axial zone " + str(x+1) + "/" + str(len(SeqCoolCoefficientsCents)) + ": {0:02.2f}".format(SeqCoolCoefficientsCents[x]) + " cents  ({0:02.2f}".format(SeqCoolCoefficientsPCM[x]) + " pcm) \n")

				solq.write("  Above the core: {0:02.2f}".format(AboveCents) + " cents ({0:02.2f}".format(AbovePCM) + " pcm) \n")
				solq.write("\n")
	
			else:
	
				solq.write("----- Sequential axial coolant reactivity feedback \n")
				solq.write("\n")
				solq.write("  Below the core: {0:02.2f}".format(BelowCoreReactCents) + " c/K ({0:02.2f}".format(BelowCoreReactPCM) + " pcm/K) \n")
		
				for x in range(len(SeqCoolCoefficientsCents)):
		
					solq.write("  Axial zone " + str(x+1) + "/" + str(len(SeqCoolCoefficientsCents)) + ": {0:02.2f}".format(SeqCoolCoefficientsCents[x]) + " c/K  ({0:02.2f}".format(SeqCoolCoefficientsPCM[x]) + " pcm/K) \n")
	
				solq.write("  Above the core: {0:02.2f}".format(AboveCoreReactCents) + " c/K ({0:02.2f}".format(AboveCoreReactPCM) + " pcm/K) \n")
				solq.write("\n")
	
			solq.write("----- Sequential SAS-type axial coolant worth \n")
			solq.write("\n")
	
			solq.write("  Below the core: {0:02.2f}".format(BelowCoreReactPerKG) + " pcm/kg \n")
	
			for x in range(len(SeqCoolCoefficientsCents)):
				
				solq.write("  Axial zone " + str(x+1) + "/" + str(len(SeqCoolCoefficientsCents)) + ": {0:02.2f}".format(SeqCoolPerKG[x]) + " pcm/kg \n")
		
			solq.write("  Above the core: {0:02.2f}".format(AboveCoreReactPerKG) + " pcm/kg \n")
			solq.write("\n")
	
		if SequentialAxialFuelReactivity == "on":

			if FuelTemperaturePerturbation == "void" or FuelTemperaturePerturbation == "Void":

				solq.write("----- Sequential axial fuel void worth \n")
				solq.write("\n")

				for x in range(len(SeqFuelPerCent)):
	
					solq.write("  In-core axial zone " + str(x+1) + "/" + str(len(SeqFuelPerCent)) + ": {0:02.2f}".format(SeqFuelPerCent[x]) + " cents  ({0:02.2f}".format(SeqFuelPerPCM[x]) + " pcm) \n")
				
			else:
	
				solq.write("----- Sequential axial fuel reactivity feedback \n")
				solq.write("\n")

				for x in range(len(SeqFuelPerCent)):
			
					solq.write("In-core axial zone " + str(x+1) + "/" + str(len(SeqFuelPerCent)) + ": {0:02.2f}".format(SeqFuelPerCent[x]) + " cents/K  ({0:02.2f}".format(SeqFuelPerPCM[x]) + " pcm/K) \n")
	
				solq.write("\n")

			solq.write("----- Sequential SAS-type axial fuel worth \n")
			solq.write("\n")
		
			for x in range(len(SeqFuelPerKG)):
		
				solq.write("  Axial zone " + str(x+1) + "/" + str(len(SeqFuelPerKG)) + ": {0:02.2f}".format(SeqFuelPerKG[x]) + " pcm/kg \n")
			
			solq.write("\n")
	
		if SequentialAxialCladReactivity == "on":
	
			solq.write("----- Sequential SAS-type axial cladding worth \n")
			solq.write("\n")
		
			for x in range(len(SeqCladPerKG)):
		
				solq.write("  Axial zone " + str(x+1) + "/" + str(len(SeqCladPerKG)) + ": {0:02.2f}".format(SeqCladPerKG[x]) + " pcm/kg \n")
			
	
		if CoolantReactivityCoefficient == "on":
	
			solq.write("----- Feedback -----------------------\n")
			solq.write("  Coolant reactivity coefficient (alpha_c): {0:02.2f}".format(CoolantReactivityCoefficientCents) + " c/K  ({0:02.2f}".format(CoolantReactivityCoefficientPCM) + " pcm/K) \n")
	
		if FuelReactivityCoefficient == "on":
	
			solq.write("  Fuel reactivity coefficient    (alpha_f): {0:02.2f}".format(FuelReactivityCoefficientCents) + " c/K  ({0:02.2f}".format(FuelReactivityCoefficientPCM) + " pcm/K) \n")
	
		if RadialExpansionCoefficient == "on":
	
			solq.write("  Radial expansion coefficient   (alpha_r): {0:02.2f}".format(RadialReactivityCoefficientCents) + " c/K  ({0:02.2f}".format(RadialReactivityCoefficientPCM) + " pcm/K) \n")
			solq.write("                                 (alpha_r): {0:02.2f}".format(RadialReactivityCoefficientCMCents) + " c/cm  ({0:02.2f}".format(RadialReactivityCoefficientCMPCM) + " pcm/cm) \n")
	
		if FuelDopplerCoefficient == "on":
	
			solq.write("  Fuel Doppler coefficient       (alpha_d): {0:02.2f}".format(FuelDopplerCoefficientCents) + " c/K  ({0:02.2f}".format(FuelDopplerCoefficientPCM) + " pcm/K) \n")					
	
		if CoolantReactivityCoefficient == "on" and FuelDopplerCoefficient == "on" and RadialExpansionCoefficient == "on" and FuelReactivityCoefficient == "on" and SerpentRun =="on":
	
			solq.write("\n")
			solq.write("----- Quasi-static reactivity balance\n")	
			solq.write("\n")	
			solq.write("  Average fuel delta-T:     {0:02.2f}".format(AverageFuelDeltaT)             + " deg. C \n")
			solq.write("  Coolant temperature rise: {0:02.2f}".format(AverageCoolantTemperatureRise) + " deg. C \n")
			solq.write("\n")
	
			DefA = (FuelDopplerCoefficientCents + FuelReactivityCoefficientCents) * AverageFuelDeltaT
	
			solq.write("  A = {0:02.2f}".format(DefA) + "\n")		
	
			DefB = (FuelDopplerCoefficientCents + FuelReactivityCoefficientCents + CoolantReactivityCoefficientCents + 2 * RadialReactivityCoefficientCents) * AverageCoolantTemperatureRise / 2
	
			solq.write("  B = {0:02.2f}".format(DefB) + "\n")	
	
			DefC = (FuelDopplerCoefficientCents + FuelReactivityCoefficientCents + CoolantReactivityCoefficientCents + RadialReactivityCoefficientCents)
	
			solq.write("  C = {0:02.2f}".format(DefC) + "\n")	
	
			solq.write("\n")
	
			solq.write("  A/B:       {0:02.2f}".format(DefA/DefB) + "\n")
	
			solq.write("  C * dTC/B: {0:02.2f}".format(AverageCoolantTemperatureRise * DefC/DefB) + "\n")
	
			solq.write("\n")
	
			solq.write("----- Asymptote coolant outlet temperature:\n")
			solq.write("\n")	
	
			ULOFOUT = AverageCoolantOutletTemperature + (DefA/DefB) * AverageCoolantTemperatureRise
	
			solq.write("  ULOF:  {0:02.2f}".format(ULOFOUT) + " deg. C\n")
	
			ULOHSOUT = AverageCoolantOutletTemperature + (DefA+DefB)/DefC - AverageCoolantTemperatureRise
	
			solq.write("  ULOHS: {0:02.2f}".format(ULOHSOUT) + " deg. C\n")
	
		if BUControlInsertionSimulation == "on":
		
			solq.write("----- BU-control withdrawal reactivity  ----------------\n")
	
			for x in range(len(SequentialBUCKeff)):
	
				solq.write("Withdrawal: " + str((100*(x+1))/len(SequentialBUCKeff)) + "%, k_eff = {0:02.4f}".format(SequentialBUCKeff[x]) + " (+/- {0:02.1f}".format(SequentialBUCKeffError[x]*1e5) + " pcm)\n")
	
		