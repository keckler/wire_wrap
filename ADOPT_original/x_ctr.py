import math
from x_prop import *

def ctrcalc(FuelLength, LowerGasPlenumLength, UpperGasPlenumLength, FuelSmearDensity, 
			Burnup, Fuel, MeVPerFission, FuelAverageDensity, ActinideMassFraction, GasAtomsPerFission,
			CoolantInletTemperature, CoolantOutletTemperature, Cladding, CladdingPeakDesignGasTemperature,
			GasReleaseFraction, PeakFCMIDesignPressure, CTR, YieldStrengthMargin, Bond, CladdingInnerRadius, 
			FreshFuelRadius, BondInfiltration, Porosity, PeakCladdingOuterWallTemperature, PeakCladdingInnerWallTemperature, 
			PeakFastFlux, HoopStressOP, ResidenceTime, CladdingCreepConstraint, Diameter, CTRx, CladdingCDFConstraint,
			FissionGasVenting, FissionGasVentingPressure, MetallicFuelNonActinideMassFraction, FTDF,MetallicFuelPlutoniumFraction,
			MetallicFuelUraniumFraction):

	########################################################################## //// ######## //// #######
	##### Estimate the porosity in the fuel if it is fully swollen radially    //// ######## //// #######
	########################################################################## //// ######## //// #######

	SwollenPorosity = 1-FuelSmearDensity/100

	########################################################################## //// ######## //// #######
	##### Get fuel properties                                                  //// ######## //// #######
	########################################################################## //// ######## //// #######

	FuelProperties = fuelproperties(material=Fuel, temperature=1, FTDF=FTDF, expansion="none", WU=MetallicFuelUraniumFraction, WPu=MetallicFuelPlutoniumFraction, Wzr=MetallicFuelNonActinideMassFraction, Burnup=Burnup,mode=1, indensity=1, intemperature=1)

	########################################################################## //// ######## //// #######
	##### Calculate the reduction in gas plenum length due to bond expulsion   //// ######## //// #######
	########################################################################## //// ######## //// #######

	if FuelProperties.fueltype == "Metallic" and Bond != "He" and FuelSmearDensity < 100:
	
		FuelArea             = math.pi * FreshFuelRadius ** 2
		InnerCladdingArea    = math.pi * CladdingInnerRadius ** 2
		PorosityVolume       = InnerCladdingArea * SwollenPorosity * FuelLength
		BondPorosityVolume   = BondInfiltration * PorosityVolume
		GapArea              = InnerCladdingArea - FuelArea
		GapVolume            = GapArea * FuelLength
		PlenumLengthDecrease = (GapVolume - BondPorosityVolume) / InnerCladdingArea

	else:

		PlenumLengthDecrease = 0

	EffectiveUpperGasPlenumLength = UpperGasPlenumLength - PlenumLengthDecrease

	########################################################################## //// ######## //// #######
	##### Define the volume of fuel relative to the volume available for gas   //// ######## //// #######
	########################################################################## //// ######## //// #######

	PlenumMultiplier = FuelSmearDensity * FuelLength / (LowerGasPlenumLength + EffectiveUpperGasPlenumLength) / 100

	########################################################################## //// ######## //// #######
	##### Estimate the average fission gas temperature                         //// ######## //// #######
	########################################################################## //// ######## //// #######

	OPPlenumTemperature = 30 + (UpperGasPlenumLength/(UpperGasPlenumLength + LowerGasPlenumLength)) * CoolantOutletTemperature + \
	                           (LowerGasPlenumLength/(UpperGasPlenumLength + LowerGasPlenumLength)) * CoolantInletTemperature

	########################################################################## //// ######## //// #######
	##### Define the temperature for yield stress evaluation                   //// ######## //// #######
	########################################################################## //// ######## //// #######

	if UpperGasPlenumLength > 0:
	
		YStemperatureOP = (CoolantOutletTemperature + 15)

	else: 

		YStemperatureOP = (CoolantInletTemperature + 15)

	########################################################################## //// ######## //// #######
	##### Apply conservative margins for fission gas temperature               //// ######## //// #######
	########################################################################## //// ######## //// #######

	if CladdingPeakDesignGasTemperature == "C":

		PlenumTemperature = OPPlenumTemperature
		YStemperature     = YStemperatureOP

	else:

		YStemperature     = CladdingPeakDesignGasTemperature
		PlenumTemperature = CladdingPeakDesignGasTemperature

	########################################################################## //// ######## //// #######
	##### Add conservative estimate of the relative release of fission gases   //// ######## //// #######
	########################################################################## //// ######## //// #######

	FuelGasReleaseFractionOP = FuelProperties.gasrelease

	if GasReleaseFraction == "C":

		FuelGasReleaseFraction = FuelGasReleaseFractionOP

	else:

		FuelGasReleaseFraction = GasReleaseFraction

	########################################################################## //// ######## //// #######
	##### Define values needed for fission gas pressure calculation            //// ######## //// #######
	########################################################################## //// ######## //// #######

	# Number of of molecules per kg-mol
	MoleculesPerKgMol = 6.023 * 1e26

	# 1 Megawatt-day in MeV
	MWdMeV = 5.3927 * 1e23

	# Number of fission events per MWd
	FissionsPerMWd = MWdMeV / MeVPerFission 

	# Pre-multiplier for n-equation
	PreF_n = FissionsPerMWd * GasAtomsPerFission / MoleculesPerKgMol

	# Pre-multiplier for a0-equation
	PreF_a0 = (8314 * 273 / 101300) * PreF_n

	# Pre-multiplier for pressure-equation
	PreF_P = PreF_a0 * (101300 / 273)

	########################################################################## //// ######## //// #######
	##### Calculate the plenum pressure due to fission gas                     //// ######## //// #######
	########################################################################## //// ######## //// #######

	if FissionGasVenting == "on":

		# Peak plenum pressure
		PlenumFissionGasPressure = FissionGasVentingPressure / 1e6
	
		# Plenum pressure at accepted operation
		PlenumFissionGasPressureOP = FissionGasVentingPressure / 1e6

	else:

		# Peak plenum pressure
		PlenumFissionGasPressure = PreF_P * ActinideMassFraction[0] * FuelAverageDensity * FuelGasReleaseFraction * Burnup * PlenumTemperature * PlenumMultiplier / 1e6
	
		# Plenum pressure at accepted operation
		PlenumFissionGasPressureOP = PreF_P * ActinideMassFraction[0] * FuelAverageDensity * FuelGasReleaseFractionOP * Burnup * OPPlenumTemperature * PlenumMultiplier / 1e6

	########################################################################## //// ######## //// #######
	##### Define the maximum (constraining) fission gas pressure               //// ######## //// #######
	########################################################################## //// ######## //// #######

	DesignPressure = max([PlenumFissionGasPressure, PeakFCMIDesignPressure])

	if PlenumFissionGasPressure > PeakFCMIDesignPressure:

		CladdingFactor = "Fission gas pressure"

	else:

		CladdingFactor = "FCMI"

	########################################################################## //// ######## //// #######
	##### Define the evaluation temperature for cladding creep                 //// ######## //// #######
	########################################################################## //// ######## //// #######

	CladEvalT = (PeakCladdingOuterWallTemperature + PeakCladdingInnerWallTemperature) / 2

	########################################################################## //// ######## //// #######
	##### Define cladding thermo-physical properties at operating temperature  //// ######## //// #######
	########################################################################## //// ######## //// #######

	CladdingProperties      = nonfuelsolidproperties(material=Cladding, temperature=CladEvalT, fastflux=1, stress=1, dpa=1, porosity=1)
	CladdingYieldStrengthOP = CladdingProperties.yieldstrength
	CladdingElasticModulus  = CladdingProperties.elasticmodulus
	CladdingPoissions       = CladdingProperties.poissons

	if CladdingYieldStrengthOP < 0:

		print(CladdingYieldStrengthOP)	

	########################################################################## //// ######## //// #######
	##### Define cladding thermo-physical properties at set temperature        //// ######## //// #######
	########################################################################## //// ######## //// #######

	CladdingPropertiesHT    = nonfuelsolidproperties(material=Cladding, temperature=YStemperature, fastflux=1, stress=1, dpa=1, porosity=1)
	CladdingYieldStrength   = CladdingPropertiesHT.yieldstrength

	if CladdingYieldStrength < 0:

		print(CladdingYieldStrength)	

	# Maximum allowable stress is [YieldStrengthMargin] times the Yield Strength (set in input)
	MaxStress = YieldStrengthMargin * CladdingYieldStrength

	# Finally, the CTR
	CladdingThicknessRatio = 2.5 * DesignPressure/ (5 * MaxStress + 2 * DesignPressure)

	# And cladding thickness
	CladdingThickness = CladdingThicknessRatio * Diameter

	# Burnup-steps to calculate integrated cladding creep
	Burnup1 = 100

	# Make a list of applicable fission gas-pressures by burnup
	GasPressureList = []
	
	for x in range(Burnup1):

		y = Burnup1/(x+1)
		GasPressureList.append(PlenumFissionGasPressureOP/(y))

	# Make a list of applicable hoop-stresses
	CreepHoopStressList = []

	# Make a list of applicable equivalent stresses
	EquivalentStressList = []

	# Assuming no external coolant pressure
	coolantpressure = 0

	for pressure in GasPressureList:

		# Thin-shell under internal pressure loading
		HoopStress = (pressure - coolantpressure) * (CladdingInnerRadius / CladdingThickness)

		# Equivalent stress by hydrostatic loading of a thing, cylindrical shell
		EquivalentStress = (math.sqrt(3)/2) * HoopStress

		CreepHoopStressList.append(HoopStress)
		EquivalentStressList.append(EquivalentStress)		

	# Make a list of applicable creep-rates
	CreepRateList = []

	# Rupture-time list
	RuptureTimeList = []

	for stress in EquivalentStressList:	

		CreepData = nonfuelsolidproperties(material=Cladding, temperature=CladEvalT, fastflux=PeakFastFlux, stress=stress, dpa=1, porosity=1)
		CreepRateList.append(CreepData.creeprate)
		RuptureTimeList.append(CreepData.rupturetime)

	# Calculate cumulative cladding creep
	Creep = 0

	for creeprate in CreepRateList:
	
		Creep += (ResidenceTime/Burnup1) * 24 * 3600 * creeprate

	# Calculate cumulative damage fraction
	CDF = 0

	for rtime in RuptureTimeList:

		CDF   += (ResidenceTime * 24)/rtime

	# Increase cladding thickness if creep is too large
	while Creep > CladdingCreepConstraint or CDF > CladdingCDFConstraint:

		if Creep > CladdingCreepConstraint:

			CladdingFactor = "Creep"

		elif CDF > CladdingCDFConstraint:

			CladdingFactor = "CDF"		

		# Make a list of applicable hoop-stresses
		CreepHoopStressList = []

		# Increase CTR
		CladdingThicknessRatio += 1e-4

		# Calculate cladding thickness from CTR
		CladdingThickness = CladdingThicknessRatio * Diameter
	
		for pressure in GasPressureList:
	
			CreepHoopStressList.append((CladdingInnerRadius + CladdingThickness/2) * pressure / CladdingThickness)
	
		# Make a list of applicable creep-rates
		CreepRateList = []

		# Rupture-time list
		RuptureTimeList = []

		for stress in EquivalentStressList:		
		
			CreepData = nonfuelsolidproperties(material=Cladding, temperature=CladEvalT, fastflux=PeakFastFlux, stress=stress, dpa=1, porosity=1)
			CreepRateList.append(CreepData.creeprate)
			RuptureTimeList.append(CreepData.rupturetime)

		# Calculate cumulative cladding creep
		Creep = 0

		for creeprate in CreepRateList:
		
			Creep += (ResidenceTime/Burnup1) * 24 * 3600 * creeprate	

		# Calculate cumulative damage fraction
		CDF = 0
	
		for rtime in RuptureTimeList:
	
			CDF   += (ResidenceTime * 24)/rtime

	CladdingCreep = Creep

	if CTRx != 1:

		CTR = CladdingThicknessRatio

	else:
	
		CladdingFactor = "Not calculated"

	return(PlenumFissionGasPressure, PeakFCMIDesignPressure, CTR, DesignPressure, PlenumFissionGasPressureOP, CladdingYieldStrength, GasReleaseFraction, 
		   FuelGasReleaseFractionOP, OPPlenumTemperature, PlenumTemperature, CladdingYieldStrengthOP, PlenumLengthDecrease, EffectiveUpperGasPlenumLength,
		   CladdingCreep, CladdingFactor, CDF, OPPlenumTemperature)

