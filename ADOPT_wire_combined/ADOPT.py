#! /usr/bin/env python3

#|----------------------------------------------------------------------------------------------------------|
#|##########################################################################################################|
#|                                        __                  __                                            | 
#|                                       /\ \      v.2.1.0   /\ \__              _____________________      |
#|      ------------              __     \_\ \    ___   _____\ \ ,_\            |                     |     |
#|      Assembly                /`__`\   /`_` \  / __`\/\ `__`\ \ \/            |   Includes EDIS     |     |
#|      Design                 /\ \L\.\_/\ \L\ \/\ \L\ \ \ \L\ \ \ \_           |   (Every Day I'm)   |     |
#|      and                    \ \__/.\_\ \___,_\ \____/\ \ ,__/\ \__\          |    Shuffling!)      |     |
#|      Optimization            \/__/\/_/\/__,_ /\/___/  \ \ \/  \/__/          |_____________________|     | 
#|      Tool                                              \ \_\                                             |
#|      ------------                  staffanq@gmail.com   \/_/                       Good luck!!           |
#|                                                                                                          | 
#|##########################################################################################################|
#|----------------------------------------------------------------------------------------------------------|
#|      Last updated on: November 23rd, 2013                                                                | 
#|----------------------------------------------------------------------------------------------------------| 

################################################################################################### //// ######## //// #######
##################### Import modules                ############################################### //// ######## //// #######
################################################################################################### //// ######## //// ####### 

import os
import math
import time

try:
   import cPickle as pickle
except:
   import pickle

################################################################################################### //// ######## //// #######
##################### Import settings               ############################################### //// ######## //// #######
################################################################################################### //// ######## //// ####### 

from ADOPT_settings     import *

################################################################################################### //// ######## //// #######
##################### Import functions and data     ############################################### //// ######## //// #######
################################################################################################### //// ######## //// ####### 

from x_coolant          import *
from x_pregeometry      import *
from x_axialpeak        import *
from x_geometry         import *
from x_postgeometry     import *
from x_coolantaxial     import *
from x_reynoldsinfo     import *
from x_claddingt        import *
from x_gap              import *
from x_fuelt            import *
from x_tplot            import *
from x_pressure         import *
from x_volfracs         import *
from x_printiteration   import *
from x_adjustment       import *
from x_isotopes         import *
from x_materials        import *
from x_materialcalc     import *
from x_radreflector     import *
from x_runserpent       import *
from x_radshield        import *
from x_plotassemblies   import *
from x_cleanup          import *
from x_collapseaxial    import *
from x_isotopevector    import *
from x_serpent          import *
from x_smfrd2           import *
from x_smfr_data        import *
from x_serpentdata      import *
from x_naturalcirc      import *
from x_decay            import * 
from x_duct             import *
from x_preoutputcomps   import *
from x_iguess           import *
from x_ctr              import *
from x_sysgeom          import *
from x_control          import *
from x_innernonfuel     import *
from x_smfrdm           import *
from x_smfrdm_react     import *
from x_smfrdmv          import *
from x_dpastuff         import *
from x_depmat           import *

if Plotting == "on":

	from x_mplots           import *

################################################################################################### //// ######## //// #######
##################### Create results folders        ############################################### //// ######## //// #######
################################################################################################### //// ######## //// ####### 

respath        = "results/" + Name
mlabpath       = respath + "/mlabplots"
serpplotpath   = respath + "/serpentplots"
serpfilepath   = respath + "/serpent"
runfilepath    = respath + "/runfiles"
matplotlibpath = respath + "/mplplots"

if not os.path.exists("results"):      os.makedirs("results")
if not os.path.exists(respath):        os.makedirs(respath)
if not os.path.exists(mlabpath):       os.makedirs(mlabpath)
if not os.path.exists(serpplotpath):   os.makedirs(serpplotpath)
if not os.path.exists(serpfilepath):   os.makedirs(serpfilepath)
if not os.path.exists(runfilepath):    os.makedirs(runfilepath)
if not os.path.exists(matplotlibpath): os.makedirs(matplotlibpath)

# Write neutronics file
Aneu = "results/" + Name + "/Neutronics.txt"

solq = open(Aneu, 'w')
solq.close()

solq = open("results/" + Name + "/SAS_Neutronics.txt", 'w')
solq.close()

################################################################################################### //// ######## //// #######
##################### Determine how many different fuels are used        ########################## //// ######## //// #######
################################################################################################### //// ######## //// ####### 

if AxialEnrichmentZoning == "on":

	TotalFuelMaterials = Batches * SerpentAxialZones

else:

	TotalFuelMaterials = Batches

################################################################################################### //// ######## //// #######
##################### Fix enriched non-fuel materials        ###################################### //// ######## //// #######
################################################################################################### //// ######## //// ####### 

materialsvector = [Fuel, Bond, Cladding, Coolant, Duct, ReflectorPinMaterial, ShieldPinMaterial]

if ShieldPinMaterial == "B4C" or AxialShieldPinMaterial == "B4C" or "B4C" in materialsvector:

	(IsotopeMassFractionList, IsotopeAtomicMassList, IsotopeAtomFractionList, ElementZTranslationList, ElementAtomicMassList) \
	= boron(B10Fraction, IsotopeMassFractionList, IsotopeAtomicMassList, IsotopeAtomFractionList, ElementZTranslationList, 
	ElementAtomicMassList)

################################################################################################### //// ######## //// #######
##################### Fuel isotopic information      ############################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

(NonActinideIsotopeAtomFractions, FissileIsotopeAtomFractions, FertileIsotopeAtomFractions, \
NonActinideIsotopeMassFractions, FissileIsotopeMassFractions, FertileIsotopeMassFractions, ActinideMassFraction) \
= fuelinfo(FissileFraction, Fissile, Fertile, Fuel, ElementAtomicMassList, IsotopeAtomFractionList, IsotopeAtomicMassList, \
Batches, MetallicFuelNonActinideMassFraction, TotalFuelMaterials)

################################################################################################### //// ######## //// #######
##################### Cladding isotopic information      ########################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

(CladdingIsotopeMassFractions, CladdingIsotopeAtomFractions, CladdingAverageAtomicMass) \
= cladding(Cladding, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, 
IsotopeMassFractionList, ElementAtomicMassList)

################################################################################################### //// ######## //// #######
##################### Duct isotopic information          ########################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

(DuctIsotopeMassFractions, DuctIsotopeAtomFractions, DuctAverageAtomicMass) \
= duct(Duct, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, \
ElementAtomicMassList)

################################################################################################### //// ######## //// #######
##################### Coolant isotopic information       ########################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

(CoolantIsotopeMassFractions, CoolantIsotopeAtomFractions, CoolantAverageAtomicMass) \
= coolantisotopes(Coolant, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, \
ElementAtomicMassList, Na, Pb, LBE)

################################################################################################### //// ######## //// #######
##################### Bond isotopic information       ############################################# //// ######## //// #######
################################################################################################### //// ######## //// #######

(BondIsotopeMassFractions, BondIsotopeAtomFractions, BondAverageAtomicMass) \
= bondisotopes(Bond, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, \
ElementAtomicMassList, Na, Pb, LBE, He)

################################################################################################### //// ######## //// #######
##################### Reflector isotopics            ############################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

(ReflectorIsotopeMassFractions, ReflectorIsotopeAtomFractions, ReflectorAverageAtomicMass) \
= reflectorisotopes(ReflectorPinMaterial, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, \
IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList)

################################################################################################### //// ######## //// #######
##################### Shield isotopics               ############################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

(ShieldIsotopeMassFractions, ShieldIsotopeAtomFractions, ShieldAverageAtomicMass) \
= shieldisotopes(ShieldPinMaterial, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, \
IsotopeMassFractionList, ElementAtomicMassList, B4C)

################################################################################################### //// ######## //// #######
##################### Coolant inlet properties       ############################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

CoolantInletHeatCapacity, CoolantInletDensity, CoolantInletDynamicViscosity, CoolantInletConductivity \
= CoolantInletProperties(Coolant, CoolantInletTemperature)

################################################################################################### //// ######## //// #######
#####################                                                                         ##### //// ######## //// #######
#####################  Iteratively find a a solution to match input                           ##### //// ######## //// #######
#####################                                                                         ##### //// ######## //// #######
################################################################################################### //// ######## //// #######

if SerpentRun == "on":
	RadialPowerPeakDifference = 1
else:
	RadialPowerPeakDifference = 1e-30

################################################################################################### //// ######## //// #######
##################### Converting power peaking factor ####################### axialpeak.py    ##### //// ######## //// #######
################################################################################################### //// ######## //// #######

CosinePinAxialPowerPeaking = axialpeaking(PinAxialPowerPeaking)

################################################################################################### //// ######## //// #######
##################### Initial conditions ########################################################## //// ######## //// #######
################################################################################################### //// ######## //// #######

BeforeAll = time.time()
AfterAll  = BeforeAll

# Serpent data initial values
SerpentRadialPowerPeaking = []
SerpentAxialPowerPeaking  = []
PowerPeakDifference       = 2 * PowerPeakConvergence
RadialPowerPeakDifference = 2 * PowerPeakConvergence
AxialPowerPeakDifference  = 2 * PowerPeakConvergence

MetallicFuelUraniumFraction = 1 - (MetallicFuelPlutoniumFraction + MetallicFuelNonActinideMassFraction)

MinKeff                   = 0
MaxKeff                   = 0
KeffErr                   = 0
BOCKeff                   = 0 
EOCKeff                   = 0
MinBeff                   = 1
MaxBeff                   = 1
BeffErr                   = 0
BOCBeff                   = 1 
EOCBeff                   = 1
VoidKeff                  = 0
KeffCycleSwing            = 0
KeffPeakSwing             = 0
VoidWorth                 = 0
zoneSC                    = 0
zoneSCC                   = 0
RadiusChange              = 0
GapMarginPrint            = 0
DeflectionPrint           = 0
CreepPrint                = 0
SwellingPrint             = 0
MaxStress                 = 0
StotB                     = 0

CoolantReactivityCoefficientPCM     = 0
CoolantReactivityCoefficientCents   = 0
FuelReactivityCoefficientPCM        = 0
FuelReactivityCoefficientCents      = 0
RadialReactivityCoefficientPCM      = 0
RadialReactivityCoefficientCents    = 0
FuelDopplerCoefficientPCM           = 0
FuelDopplerCoefficientCents         = 0
SeqCoolCoefficientsCents            = 0
SeqCoolCoefficientsPCM              = 0
RadialReactivityCoefficientCMPCM    = 0
RadialReactivityCoefficientCMCents  = 0
LowerPlenumCoolantDensityDifference = 0
UpperPlenumCoolantDensityDifference = 0
BelowCoreReactPerKG                 = 0
AboveCoreReactPerKG                 = 0
BelowCoreReactPCM                   = 0
BelowCoreReactCents                 = 0
AboveCoreReactPCM                   = 0
AboveCoreReactCents                 = 0
BelowCents                          = 0
AboveCents                          = 0
BelowPCM                            = 0
AbovePCM                            = 0

SeqFuelPerPCM = []
SeqFuelPerCent = []
SequentialBUCKeff      = []
SequentialBUCKeffError = []

PeakFluence               = PeakFlux * ResidenceTime * 3600 * 24
PeakFastFluence           = 0.6 * PeakFluence
AverageFlux               = PeakFlux / PinAxialPowerPeaking
maxDPAcell                = "n/a"

RadialPowerPeaks = [0]
AxialPowerPeaks  = [0]

SeqCoolCoefficientsPCM   = []
SeqCoolCoefficientsCents = []
SeqCoolPerKG             = []
SeqFuelPerKG             = []
SeqCladPerKG             = []

CladdingYieldStrength = 0
HoopStress            = 0
HoopStressOP          = 0
CoreMassFlowDecNat    = 0
NotAgain              = 0

if CTR == "C":
	DesignPressure = 0
	CTRx = 0
else:
	CTRx = 1

# Neutronic counter start
x = 0

sol = open("results/" + Name + "/RadialPowerPeaking.m", 'w')
sol.write("Radial = [ \n")
sol2 = open("results/" + Name + "/AxialPowerPeaking.m", 'w')
sol2.write("Axial = [ \n")

CorePressureDropConstraint = PressureDropConstraint
AverageCoolantVelocity0    = AverageCoolantVelocity

if DuctThickness == "C" or DuctThickness == "Calculated":

	DuctX = "C"

	DuctThickness    = DuctWallGuess
	InterAssemblyGap = IAGapGuess

else:

	DuctX = "S"


if CoolantOutletTemperature == "Calculated" or CoolantOutletTemperature == "C":

	CoolantOutletTemperature     = CladdingOuterTemperatureConstraint
	CoolantOutletTemperatureMode = "Calculated"

else:

	CoolantOutletTemperatureMode = "set"

i = 0

while abs(PowerPeakDifference) > PowerPeakConvergence:

	EdgePinPowerPeaking   = RadialPowerPeaking
	CornerPinPowerPeaking = RadialPowerPeaking

	if NotAgain == 0:

		# Load initial guess for TH parameters
		(AverageCoolantVelocity, FuelPinRows, CoolantOutletTemperature) \
		= THinitialguess(CoolantVelocityConstraint, MinimumPinRows, CladdingOuterTemperatureConstraint, 
		CoolantOutletTemperatureMode, CoolantOutletTemperature, AverageCoolantVelocity0, CoolantTemperatureConstraint)
	
		# Set all initial velocities to the peak allowed coolant velocity
		InteriorChannelCoolantVelocity           = 1.0 * AverageCoolantVelocity
		EdgeChannelCoolantVelocity               = 1.0 * AverageCoolantVelocity
		CornerChannelCoolantVelocity             = 1.0 * AverageCoolantVelocity
		CalculatedPeakCoolantVelocity            = 2 * CoolantVelocityConstraint
		TotalPressureDrop                        = 2 * CorePressureDropConstraint
		PeakCladdingOuterWallTemperature         = 2 * CladdingOuterTemperatureConstraint
		PeakCladdingInnerWallTemperature         = 2 * CladdingInnerTemperatureConstraint
		PeakFuelInnerTemperature                 = 2 * FuelTemperatureConstraint
		NaturalCirculationThermalCenterElevation = 2 * NaturalCirculationFOM1Constraint
		FlowError                                = 2 * FlowConvergence

	ix = 0

	ConvergedSolution = 0
	Before = time.time()
	After  = Before
	FlowCheck = []

	while CalculatedPeakCoolantVelocity > CoolantVelocityConstraint or TotalPressureDrop > CorePressureDropConstraint or PeakCladdingOuterWallTemperature > CladdingOuterTemperatureConstraint or PeakFuelInnerTemperature > FuelTemperatureConstraint or NaturalCirculationThermalCenterElevation > NaturalCirculationFOM1Constraint or FlowError > FlowConvergence or i < MinimumIterations:

		if SerpentRun != "on" or PowerCorrection != "on":

			RadialPowerPeakDifference = 1e-30
			AxialPowerPeakDifference  = 1e-30
			PowerPeakDifference       = 1e-30

		################################################################################################### //// ######## //// #######
		##################### Power, mass flow and temperatures      ###################################### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		CoolantTemperatureRise    =  CoolantOutletTemperature - CoolantInletTemperature
		CoolantAverageTemperature = (CoolantOutletTemperature + CoolantInletTemperature) / 2

		AverageAssemblyPower      = Power / Assemblies
		PeakAssemblyPower         = AverageAssemblyPower * RadialPowerPeaking

		if ix > 1:
		
			CoreMassFlowDecNat         = Power * DecayHeat / (CoolantInletHeatCapacity * AverageCoolantTemperatureRise)
			AssemblyMassFlowDecNat     = CoreMassFlowDecNat / Assemblies
			PeakAssemblyMassFlowDecNat = AssemblyMassFlowDecNat * RadialPowerPeaking
			PeakAssemblyDecNatPower    = PeakAssemblyPower * DecayHeat
			AverageAssemblyDecNatPower = AverageAssemblyPower * DecayHeat

		################################################################################################### //// ######## //// #######
		##################### Coolant average properties       ############################################ //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(CoolantAverageHeatCapacity, CoolantAverageDensity, CoolantAverageDynamicViscosity, CoolantAverageConductivity) \
		= CoolantAverageProperties(Coolant, CoolantAverageTemperature)
		
		################################################################################################### //// ######## //// #######
		##################### Coolant outlet properties       ############################################# //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(CoolantOutletHeatCapacity, CoolantOutletDensity, CoolantOutletDynamicViscosity, CoolantOutletConductivity) \
		= CoolantOutletProperties(Coolant, CoolantOutletTemperature)

		if i > 2:

			################################################################################################### //// ######## //// #######
			##################### Pre-calculate results for print              ################################ //// ######## //// #######
			################################################################################################### //// ######## //// #######

			(CorePD, TotPD, CoreVolume, SystemVolume, SystemHeight, VolumetricPowerDensity, SpecificPower, SpecificFissilePower, AverageCorePD,
			FuelMassDensityGCC, CoolantMassDensityGCC, BondMassDensityGCC, CladdingMassDensityGCC, DuctMassDensityGCC, CoreMassDensityGCC,
			BondMass, CladdingMass, DuctMass, CoolantMass, FuelMass, FuelMassFraction, CoolantMassFraction, BondMassFraction, CladdingMassFraction,
			DuctMassFraction) \
			= preoutput(InletPressureDrop, OutletPressureDrop, ChannelPressureDrop, NonCorePressureDropMultiplier,
	        CoreOuterRadius, AssemblyPitch, RadialReflectorRows, RadialShieldRows, FuelLength, SystemDiameter,
	        BelowCoreChannelLength, AboveCoreChannelLength, Power, CoreFissileMass, CoreFuelMass,
	        FuelVolumeFraction, FuelAverageDensity, CoolantAverageDensity, ActiveCoolantVolumeFraction,
	        InterAssemblyVolumeFraction, AverageInletPressureDrop, AverageOutletPressureDrop, AverageChannelPressureDrop,
	        AverageBondDensity, AverageDuctDensity, AverageCladdingDensity, GapVolumeFraction, CladdingVolumeFraction, DuctVolumeFraction)

			################################################################################################### //// ######## //// #######
			##################### Print information to terminal                ################################ //// ######## //// #######
			################################################################################################### //// ######## //// #######

			printiter(i, ChannelPressureDrop, InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity, \
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
			AverageFuelDeltaT, AverageCoolantTemperatureRise)

		i += 1
		ix += 1
	

		################################################################################################### //// ######## //// #######
		##################### Pin information                ############################################## //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(PinsPerAssembly,TotalFuelPins,TotalFuelLength,AveragePinPower,PeakPinPower,AveragePinAverageLinearPower, \
		AveragePinPeakLinearPower,PeakPinAverageLinearPower,PeakPinPeakLinearPower, EdgePinAverageLinearPower, \
		EdgePinPeakLinearPower, CornerPinAverageLinearPower, CornerPinPeakLinearPower, EdgePinPower, CornerPinPower) \
		= pininformation(FuelPinRows,Assemblies,FuelLength,Power,RadialPowerPeaking,PinAxialPowerPeaking, EdgePinPowerPeaking, \
		CornerPinPowerPeaking)

		################################################################################################### //// ######## //// #######
		##################### Assembly information           ############################################## //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(InnerAssemblySideLength,DuctedAssemblyFTF,DuctedAssemblySideLength,AssemblyHexagonFTF, \
		AssemblyHexagonSideLength, AssemblyPitch, TotalAssemblyArea, InnerAssemblyArea, \
		DuctedAssemblyArea, TotalAssemblyArea, CoreDiameter, SystemDiameter, TotalCoreArea) \
		= assemblyinformation(FTF,DuctThickness,InterAssemblyGap, RadialReflectorRows, RadialShieldRows, Assemblies)

		################################################################################################### //// ######## //// #######
		##################### Define general serpent geometry             ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(SerpentCoreRadius, CellVolume, ReflectorOuterRadius, ReflectorVolume, CoreOuterRadius, 
		ShieldOuterRadius, ShieldVolume, SystemOuterRadius)	\
		= serpentcoregeometry(Batches, TotalAssemblyArea, SerpentAxialZones, FuelLength, Assemblies, 
		AssemblyPitch, RadialReflectorRows, RadialShieldRows, SerpentOutsideDistance, InternalControlAssemblies)

		################################################################################################### //// ######## //// #######
		##################### Radial reflector assemblies     ####################### radreflector.py ##### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(ReflectorPinOuterRadius, ReflectorPinInnerRadius, ReflectorPinPitch, ReflectorPinSlugRadius) \
		= radialreflector(ReflectorPinMaterial, ReflectorPinVolumeFraction, InnerAssemblyArea, ReflectorPinsPerAssembly, \
		FTF, ReflectorSlugSmearDensity,ReflectorSlugCTR)
		
		################################################################################################### //// ######## //// #######
		##################### Radial shield assemblies     ########################## radshield.py    ##### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius) \
		= shieldreflector(ShieldPinMaterial, ShieldPinVolumeFraction, InnerAssemblyArea, ShieldPinsPerAssembly, FTF, \
		ShieldSlugSmearDensity, ShieldSlugCTR)
	
		################################################################################################### //// ######## //// #######
		##################### General subchannel information ############################################## //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(InteriorChannelsPerAssembly,EdgeChannelsPerAssembly,CornerChannelsPerAssembly,CoreInteriorChannels, \
		CoreEdgeChannels,CoreCornerChannels,CoreTotalChannels,BelowCoreChannelLength, AboveCoreChannelLength, \
		ChannelsPerAssembly) \
		= geomsubchannels(FuelPinRows, Assemblies, LowerEndCapLength, LowerShieldLength, LowerReflectorLength, LowerGasPlenumLength, \
        LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength, UpperGasPlenumLength, UpperReflectorLength, \
		UpperShieldLength, UpperEndCapLength)

		################################################################################################### //// ######## //// #######
		##################### Geometric calculation ################################ geometry.py       #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		#print("PeakPinPower")
		#print(PeakPinPower)

		(Diameter, Pitch, WireDiameter, MassFlowArea, InteriorChannelCoolantVelocity) = innergeometry(FTF, FTF_Convergence, FuelPinRows, RelativeWirePitch, 
		PeakPinPower, CoolantTemperatureRise, CoolantInletDensity, InteriorChannelCoolantVelocity, CoolantInletHeatCapacity,
		AverageCoolantVelocity, PinsPerAssembly, SpacerType)

		################################################################################################### //// ######## //// #######
		##################### Cladding thickness calculation           #################################### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		if ix > 1:

			(PlenumFissionGasPressure, PeakFCMIDesignPressure, CTR, DesignPressure, PlenumFissionGasPressureOP, CladdingYieldStrength, GasReleaseFraction, 
		    FuelGasReleaseFractionOP, OPPlenumTemperature, PlenumTemperature, CladdingYieldStrengthOP, PlenumLengthDecrease, EffectiveUpperGasPlenumLength,
		    CladdingCreep, CladdingFactor, CDF, OPPlenumTemperature) \
			= ctrcalc(FuelLength, LowerGasPlenumLength, UpperGasPlenumLength, FuelSmearDensity, 
			Burnup, Fuel, MeVPerFission, FuelAverageDensity, ActinideMassFraction, GasAtomsPerFission,
			CoolantInletTemperature, CoolantOutletTemperature, Cladding, CladdingPeakDesignGasTemperature,
			GasReleaseFraction, PeakFCMIDesignPressure, CTR, YieldStrengthMargin, Bond, CladdingInnerRadius, 
			FreshFuelRadius, BondInfiltration, Porosity, PeakCladdingOuterWallTemperature, PeakCladdingInnerWallTemperature, 
			PeakFastFlux, HoopStressOP, ResidenceTime, CladdingCreepConstraint, Diameter, CTRx, CladdingCDFConstraint,
			FissionGasVenting, FissionGasVentingPressure, MetallicFuelNonActinideMassFraction, FTDF,MetallicFuelPlutoniumFraction,
			MetallicFuelUraniumFraction) 
	
			HoopStress   = (CladdingInnerRadius + CladdingThickness/2) * DesignPressure / CladdingThickness
			HoopStressOP = (CladdingInnerRadius + CladdingThickness/2) * PlenumFissionGasPressureOP / CladdingThickness

		################################################################################################### //// ######## //// #######
		##################### Fuel rod information ################################# postgeometry.py   #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(CladdingThickness, CladdingOuterDiameter, CladdingOuterRadius, CladdingInnerDiameter, CladdingInnerRadius, \
		FreshFuelDiameter, FreshFuelRadius, GapInnerDiameter, GapInnerRadius, GapOuterDiameter, GapOuterRadius, WirePitch,
		InnerFuelRadius, InnerFuelDiameter) \
		= rodinfo(CTR, Diameter, CladdingMinimumThickness, FuelSmearDensity, RelativeWirePitch, i)

		################################################################################################### //// ######## //// #######
		##################### Specific subchannel information ###################### postgeometry.py   #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(BareSingleInteriorChannelFlowArea, SingleInteriorChannelFlowArea, BareSingleEdgeChannelFlowArea, SingleEdgeChannelFlowArea, \
		BareSingleCornerChannelFlowArea, SingleCornerChannelFlowArea, BareSingleInteriorChannelWettedPerimeter, \
		SingleInteriorChannelWettedPerimeter, BareSingleEdgeChannelWettedPerimeter, SingleEdgeChannelWettedPerimeter, \
		BareSingleCornerChannelWettedPerimeter, SingleCornerChannelWettedPerimeter, BareSingleInteriorChannelHydraulicDiameter, \
		SingleInteriorChannelHydraulicDiameter, BareSingleEdgeChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, \
		BareSingleCornerChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, SingleInteriorChannelProjectedWireArea, \
		SingleEdgeChannelProjectedWireArea, SingleCornerChannelProjectedWireArea, S1, S2, S3, SingleAverageHydraulicDiameter, \
		AssemblyFlowArea, AssemblyWettedPerimeter, BundleHydraulicDiameter) \
		= flowinfo(Pitch, Diameter, WireDiameter, WirePitch, InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, \
		CornerChannelsPerAssembly, FTF, PinsPerAssembly)

		################################################################################################### //// ######## //// #######
		##################### Volume fraction ################################### volfracs.py          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
	
		(FuelVolumeFraction,GapVolumeFraction,CladdingVolumeFraction,ActiveCoolantVolumeFraction, DuctVolumeFraction, \
		InterAssemblyVolumeFraction,WireVolumeFraction, EquivalentCladdingRadius) \
		= volumefraction(FTF, Pitch, Diameter, PinsPerAssembly, FreshFuelRadius, CladdingThickness, GapOuterRadius, TotalAssemblyArea, \
		AssemblyFlowArea, GapInnerRadius, InnerAssemblyArea, DuctedAssemblyArea, InternalControlAssemblies, Assemblies)
	
		################################################################################################### //// ######## //// #######
		##################### Coolant axial information ############################ coolantaxial.py   #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(TemperaturePoints, CoolantAxialTemperature, CoolantAxialHeatCapacity, CoolantAxialDensity, CoolantAxialDynamicViscosity, \
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
		CoolantInteriorReynoldsZ2,CoolantEdgeReynoldsZ2,CoolantCornerReynoldsZ2,CladdingOuterWallTemperatureZ2, TemperaturePointsZ,
		CoolantAxialAverageCornerReynolds, CoolantAxialAverageInteriorReynolds, CoolantAxialAverageEdgeReynolds,
		PeakChannelMassFlow, EdgeChannelMassFlow, CornerChannelMassFlow) \
		= axialcoolant(MassFlowArea, InteriorChannelCoolantVelocity, CoolantInletDensity, FuelLength, AxialTemperaturePoints, \
		CosinePinAxialPowerPeaking, CoolantInletHeatCapacity, SingleInteriorChannelHydraulicDiameter, \
		BelowCoreChannelLength, CoolantInletTemperature, PeakPinPeakLinearPower, Pitch, Diameter, \
		SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, EdgeChannelCoolantVelocity, \
		CornerChannelCoolantVelocity, SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, EdgePinPeakLinearPower, \
		CornerPinPeakLinearPower, Name, Coolant, PinAxialPowerPeaking, mlabpath, RadialPowerPeaking,  SingleInteriorChannelFlowArea)

		################################################################################################### //// ######## //// #######
		##################### Set Reynolds information ############################# reynoldsinfo.py  ##### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(LowerReynoldsValidityRange, UpperReynoldsValidityRange, LaminarReynolds, TurbulentReynolds, \
		BelowCoreInteriorReynolds, BelowCoreEdgeReynolds, BelowCoreCornerReynolds, AboveCoreInteriorReynolds, \
		AboveCoreEdgeReynolds, AboveCoreCornerReynolds, BundleAverageBelowCoreReynolds, FlowRegime) \
		= reyinf(Pitch, Diameter, CoolantAxialInteriorReynolds, CoolantAxialEdgeReynolds, CoolantAxialCornerReynolds, FuelLength, \
		InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly)

		################################################################################################### //// ######## //// #######
		##################### Set average-assembly Reynolds information ############ reynoldsinfo.py  ##### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(AverageBelowCoreInteriorReynolds, AverageBelowCoreEdgeReynolds, AverageBelowCoreCornerReynolds, AverageAboveCoreInteriorReynolds, \
		AverageAboveCoreEdgeReynolds, AverageAboveCoreCornerReynolds, AverageBundleAverageBelowCoreReynolds) \
		= averagereyinf(Pitch, Diameter, CoolantAxialAverageInteriorReynolds, CoolantAxialAverageEdgeReynolds, CoolantAxialAverageCornerReynolds, FuelLength, \
	    InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly, RadialPowerPeaking)	
		
		################################################################################################### //// ######## //// #######
		##################### Flow distribution #################################### pressuredrop.py   #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity, CalculatedPeakCoolantVelocity, \
		Cf1, Cf2, Cf3, X1, X2, X3, BundleAverageBelowCoreReynolds) \
		= flowsplit(BareSingleInteriorChannelFlowArea,SingleInteriorChannelFlowArea,BareSingleInteriorChannelWettedPerimeter, \
		SingleInteriorChannelWettedPerimeter,BareSingleInteriorChannelHydraulicDiameter, \
		SingleInteriorChannelHydraulicDiameter,BelowCoreInteriorReynolds,LaminarReynolds, Pitch, Diameter, \
		BelowCoreChannelLength, AverageCoolantVelocity, CoolantInletDensity, SingleInteriorChannelProjectedWireArea, \
		WireDiameter, WirePitch, BundleAverageBelowCoreReynolds, RelativeWirePitch,  SingleEdgeChannelProjectedWireArea, \
		BareSingleEdgeChannelFlowArea, SingleCornerChannelProjectedWireArea, BareSingleCornerChannelFlowArea, \
		SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, S1, S2, S3, SingleAverageHydraulicDiameter, \
		SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, InteriorChannelsPerAssembly, \
		EdgeChannelsPerAssembly, CornerChannelsPerAssembly, ChannelsPerAssembly)
	
		################################################################################################### //// ######## //// #######
		##################### Pressure drop in peak-power assembly         ######### pressuredrop.py   #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(ChannelPressureDrop, InteriorChannelFrictionFactor, EdgeChannelFrictionFactor, CornerChannelFrictionFactor) \
		= channelpressuredrop(Cf1,Cf2,Cf3,InteriorChannelCoolantVelocity,EdgeChannelCoolantVelocity,CornerChannelCoolantVelocity, \
		BelowCoreInteriorReynolds, BelowCoreEdgeReynolds, BelowCoreCornerReynolds, CoolantAxialInteriorReynolds, \
		CoolantAxialEdgeReynolds, CoolantAxialCornerReynolds, FuelLength, BelowCoreChannelLength, AboveCoreChannelLength, \
		FlowRegime, TemperaturePoints, CoolantAxialDensity, CoolantAxialKinematicViscosity, CoolantInletDensity, \
		SingleInteriorChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter)

		(InletPressureDrop, OutletPressureDrop) = \
		inletoutletpressuredrop(CoolantInletDensity, AverageCoolantVelocity, BundleAverageBelowCoreReynolds)

		################################################################################################### //// ######## //// #######
		##################### Pressure drop in average-power assembly         ############################# pressuredrop.py   #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(AverageChannelPressureDrop, AverageInteriorChannelFrictionFactor, AverageEdgeChannelFrictionFactor, AverageCornerChannelFrictionFactor) \
		= averagechannelpressuredrop(Cf1,Cf2,Cf3,InteriorChannelCoolantVelocity,EdgeChannelCoolantVelocity,CornerChannelCoolantVelocity, AverageBelowCoreInteriorReynolds,
	    AverageBelowCoreEdgeReynolds, AverageBelowCoreCornerReynolds, CoolantAxialAverageInteriorReynolds, CoolantAxialAverageEdgeReynolds, CoolantAxialAverageCornerReynolds,
	    FuelLength, BelowCoreChannelLength, AboveCoreChannelLength, FlowRegime, TemperaturePoints, CoolantAxialDensity, CoolantAxialKinematicViscosity, \
	    CoolantInletDensity,SingleInteriorChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, RadialPowerPeaking)

		(AverageInletPressureDrop, AverageOutletPressureDrop) \
		= averageinletoutletpressuredrop(CoolantInletDensity, AverageCoolantVelocity, AverageBundleAverageBelowCoreReynolds, RadialPowerPeaking)

		################################################################################################### //// ######## //// #######
		##################### Inner cladding wall temperature ###################### claddingt.py     ##### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(CladdingInnerWallAxialTemperature, PeakCladdingInnerWallTemperature, PeakCladdingInnerWallTemperateAxialPosition,
		 CladdingInnerWallTemperatureZ2) \
		= innercladdingt(PeakCladdingOuterWallTemperature, TemperaturePoints, TemperatureConvergence, PeakPinPeakLinearPower, \
		CladdingOuterRadius, CladdingInnerRadius, FuelLength, CosinePinAxialPowerPeaking, CladdingOuterWallAxialTemperature, Name, \
		PinAxialPowerPeaking, Cladding, mlabpath)
		
		################################################################################################### //// ######## //// #######
		##################### Outer fuel temperature ############################### gap.py           ##### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(FuelRimAxialTemperature, PeakFuelRimTemperature, FuelRimAxialTemperatureZ2) \
		= gapt(PeakCladdingInnerWallTemperature, TemperaturePoints, TemperatureConvergence, PeakPinPeakLinearPower, \
		GapOuterRadius, GapInnerRadius, FuelLength, CosinePinAxialPowerPeaking, CladdingInnerWallAxialTemperature, Name, \
		PinAxialPowerPeaking, mlabpath, Bond)
		
		################################################################################################### //// ######## //// #######
		##################### Inner fuel temperature ############################### fuelt.py          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		GadoliniumContent = 0 

		(FuelInnerAxialTemperature, PeakFuelInnerTemperature, PeakFuelInnerTemperateAxialPosition, CoreFuelMass, \
		CoreFissileMass, CoreActinideMass, FuelInnerAxialTemperatureZ2, FuelAverageDensity) \
		= ft(PeakFuelRimTemperature, TemperaturePoints, TemperatureConvergence, GadoliniumContent, Burnup, FTDF, \
		PeakPinPeakLinearPower, FuelLength, CosinePinAxialPowerPeaking, FuelRimAxialTemperature, Name, FreshFuelRadius, \
		TotalFuelPins, AxialTemperaturePoints, FissileFraction, Batches, ActinideMassFraction, PinAxialPowerPeaking, \
		Fuel, Porosity, mlabpath, MetallicFuelPlutoniumFraction, MetallicFuelNonActinideMassFraction, MetallicFuelUraniumFraction,
		FuelType, CladdingInnerWallAxialTemperature, InnerFuelRadius, InnerFuelDiameter)
	
		################################################################################################### //// ######## //// #######
		##################### Burnup estimation ########################################################### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		AverageBurnup = Power * ResidenceTime / CoreActinideMass / 1e6
		PeakBurnup    = AverageBurnup * PinAxialPowerPeaking

		################################################################################################### //// ######## //// #######
		##################### Average coolant outlet temperature ########################################## //// ######## //// #######
		################################################################################################### //// ######## //// #######

		PeakAssemblyMassFlow = CoolantInletDensity * SingleInteriorChannelFlowArea * InteriorChannelCoolantVelocity * InteriorChannelsPerAssembly + \
							   CoolantInletDensity * SingleEdgeChannelFlowArea     * EdgeChannelCoolantVelocity     * EdgeChannelsPerAssembly     + \
							   CoolantInletDensity * SingleCornerChannelFlowArea   * CornerChannelCoolantVelocity   * CornerChannelsPerAssembly

		AverageAssemblyMassFlow = PeakAssemblyMassFlow / RadialPowerPeaking
		AverageCoolantOutletTemperature = (AssemblyFlowArea * CoolantInletDensity * AverageCoolantVelocity * CoolantInletHeatCapacity * CoolantInletTemperature + PeakAssemblyPower)/(AssemblyFlowArea * CoolantInletDensity * AverageCoolantVelocity * CoolantInletHeatCapacity)		   
		AverageCoolantTemperatureRise = AverageCoolantOutletTemperature - CoolantInletTemperature

		CoreMassFlow              = Power / (CoolantInletHeatCapacity * AverageCoolantTemperatureRise)
		VolumetricFlowRate        = CoreMassFlow / CoolantInletDensity
		PumpingPower              = VolumetricFlowRate * TotalPressureDrop / 1e6

		After = time.time()	

		################################################################################################### //// ######## //// #######
		##################### Collapse temperature data to serpent points ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature,
		SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature,
		SerpentAxialCoolantDensity, SerpentAxialIAGapDensity, SerpentAxialCladdingDensity,
		SerpentAxialDuctDensity, SerpentAxialBondDensity, SerpentAxialFuelDensity,
		SerpentTemperaturePoints, SerpentAxialReflectorDensity, SerpentAxialShieldDensity, AverageBondDensity, 
		AverageDuctDensity, AverageCladdingDensity, SerpentPerturbedAxialCoolantDensity, SerpentPerturbedAxialFuelDensity,
		FuelAverageTemperature, AverageFuelDeltaT, SerpentPerturbedAxialCladdingDensity, AverageFuelDensity, FreeExpansionDensity,
		PerturbedAverageFuelDensity) = \
		collapsetoserpent(CoolantAxialTemperature, CoolantAxialEdgeTemperature, CoolantAxialCornerTemperature,
		InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly,
		ChannelsPerAssembly, TemperaturePoints, FuelLength, SerpentAxialZones,CladdingOuterWallAxialTemperature, 
		CladdingInnerWallAxialTemperature, FuelRimAxialTemperature, FuelInnerAxialTemperature, AxialTemperaturePoints,
		Coolant, Fuel, Cladding, Duct, Bond, ColdFillGasPressure, ReflectorPinMaterial, ShieldPinMaterial,
		MetallicFuelPlutoniumFraction, MetallicFuelNonActinideMassFraction, SingleInteriorChannelFlowArea, SingleEdgeChannelFlowArea, 
		SingleCornerChannelFlowArea, AssemblyFlowArea, FTDF, ShieldPinPorosity, CoolantTemperaturePerturbation, 
		DuctTemperaturePerturbation, CladdingTemperaturePerturbation, FuelTemperaturePerturbation, MetallicFuelUraniumFraction, Burnup, FuelExpansion,
		FreshFuelRadius, CladdingInnerRadius)

		################################################################################################### //// ######## //// #######
		##################### Passive decay heat removal     ############################################## //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(DecayHeat, DecayHeatRemovalFlowVelocity) = decayheatflow(Pitch, Diameter, MassFlowArea, CycleTime, PeakPinPower, CoolantInletDensity, 
		CoolantTemperatureRise, CoolantInletHeatCapacity, DecayHeatTime)		

		EdgeChannelDecNatCoolantVelocity   = DecayHeatRemovalFlowVelocity
		CornerChannelDecNatCoolantVelocity = DecayHeatRemovalFlowVelocity
		AverageDecNatCoolantVelocity       = DecayHeatRemovalFlowVelocity

		(CoolantDecNatAxialInteriorReynolds, CoolantDecNatAxialEdgeReynolds, CoolantDecNatAxialCornerReynolds) = \
		decnataxialcoolant(MassFlowArea, DecayHeatRemovalFlowVelocity, CoolantInletDensity, FuelLength, AxialTemperaturePoints, \
	    CosinePinAxialPowerPeaking, CoolantInletHeatCapacity, SingleInteriorChannelHydraulicDiameter, \
	    BelowCoreChannelLength, CoolantInletTemperature, PeakPinPeakLinearPower, Pitch, Diameter, \
	    SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, EdgeChannelDecNatCoolantVelocity, \
	    CornerChannelDecNatCoolantVelocity, SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, EdgePinPeakLinearPower,
	    CornerPinPeakLinearPower, Name, Coolant, PinAxialPowerPeaking, mlabpath)

		(BelowCoreDecNatInteriorReynolds, BelowCoreDecNatEdgeReynolds, BelowCoreDecNatCornerReynolds, AboveCoreDecNatInteriorReynolds, \
		AboveCoreDecNatEdgeReynolds, AboveCoreDecNatCornerReynolds, BundleAverageDecNatBelowCoreReynolds, FlowRegimeDecNat) = \
		decnatreyinf(Pitch, Diameter, CoolantDecNatAxialInteriorReynolds, CoolantDecNatAxialEdgeReynolds, CoolantDecNatAxialCornerReynolds, FuelLength, \
	    InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly)

		(InteriorDecNatChannelCoolantVelocity, EdgeDecNatChannelCoolantVelocity, CornerDecNatChannelCoolantVelocity,
		Cf1DecNat, Cf2DecNat, Cf3DecNat, X1DecNat, X2DecNat, X3DecNat, InteriorIntermittancyFactor, EdgeIntermittancyFactor,   
		CornerIntermittancyFactor, Cf1t, Cf2t, Cf3t, Cf1l, Cf2l, Cf3l)	 = \
		decnatflowsplit(BareSingleInteriorChannelFlowArea,SingleInteriorChannelFlowArea,BareSingleInteriorChannelWettedPerimeter,
        SingleInteriorChannelWettedPerimeter,BareSingleInteriorChannelHydraulicDiameter,
        SingleInteriorChannelHydraulicDiameter,BelowCoreDecNatInteriorReynolds,LaminarReynolds, Pitch, Diameter,
        BelowCoreChannelLength, AverageDecNatCoolantVelocity, CoolantInletDensity, SingleInteriorChannelProjectedWireArea,
        WireDiameter, WirePitch, BundleAverageDecNatBelowCoreReynolds, RelativeWirePitch,  SingleEdgeChannelProjectedWireArea, 
        BareSingleEdgeChannelFlowArea, SingleCornerChannelProjectedWireArea, BareSingleCornerChannelFlowArea, 
        SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, S1, S2, S3, SingleAverageHydraulicDiameter,
        SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, InteriorChannelsPerAssembly,
		EdgeChannelsPerAssembly, CornerChannelsPerAssembly, ChannelsPerAssembly, FlowRegimeDecNat, TurbulentReynolds,
		BelowCoreDecNatEdgeReynolds, BelowCoreDecNatCornerReynolds, BundleHydraulicDiameter)		

		(ChannelPressureDropDecNat, DecNatInteriorChannelFrictionFactor, DecNatEdgeChannelFrictionFactor, DecNatCornerChannelFrictionFactor) = \
		decnatchannelpressuredrop(Cf1DecNat,Cf2DecNat,Cf3DecNat,InteriorDecNatChannelCoolantVelocity,EdgeDecNatChannelCoolantVelocity,CornerDecNatChannelCoolantVelocity, BelowCoreDecNatInteriorReynolds,
	    BelowCoreDecNatEdgeReynolds, BelowCoreDecNatCornerReynolds, CoolantDecNatAxialInteriorReynolds, CoolantDecNatAxialEdgeReynolds, CoolantDecNatAxialCornerReynolds,
	    FuelLength, BelowCoreChannelLength, AboveCoreChannelLength, FlowRegimeDecNat, TemperaturePoints, CoolantAxialDensity, CoolantAxialKinematicViscosity, \
	    CoolantInletDensity,SingleInteriorChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, InteriorIntermittancyFactor, EdgeIntermittancyFactor,    
		CornerIntermittancyFactor, Cf1t, Cf2t, Cf3t, Cf1l, Cf2l, Cf3l)

		(InletDecNatPressureDrop, OutletDecNatPressureDrop) = \
		decnatinletoutletpressuredrop(CoolantInletDensity, AverageDecNatCoolantVelocity, BundleAverageDecNatBelowCoreReynolds)

		(NaturalCirculationThermalCenterElevation, TotalPressureDropDecNat, PumpPressureDrop) = \
		decaynaturalcirculation(Coolant, ChannelPressureDropDecNat, NonCorePressureDropMultiplier, AverageCoolantOutletTemperature, 
		CoolantInletTemperature, CoolantInletDensity, ThermalCenterElevation, CoolantOutletDensity, CycleTime, Power, DecayHeat, PumpResistanceFraction,
		InletDecNatPressureDrop, OutletDecNatPressureDrop)

		################################################################################################### //// ######## //// #######
		##################### Full-power natural circulation      ######################################### //// ######## //// #######
		################################################################################################### //// ######## //// #######
	
		(NaturalCirculation) \
		= naturalcirculation(Coolant, ChannelPressureDrop, NonCorePressureDropMultiplier, AverageCoolantOutletTemperature, 
		CoolantInletTemperature, CoolantInletDensity, ThermalCenterElevation, CoolantOutletDensity, CycleTime, Power, 
		InletPressureDrop, OutletPressureDrop)

		################################################################################################### //// ######## //// #######
		##################### Duct deformation analysis           ######################################### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		TotalPressureDrop = (ChannelPressureDrop + InletPressureDrop + OutletPressureDrop) * (1 + NonCorePressureDropMultiplier)

		if DuctX == "C":

			(DuctThickness, InterAssemblyGap,GapMarginPrint,DeflectionPrint,CreepPrint,SwellingPrint, MaxStress, StotB) \
			 = ductdeform(TotalPressureDrop, DuctedAssemblySideLength, Duct, CoolantInletTemperature, 
			PeakFastFlux, ResidenceTime, AssemblyPitch, YieldStrengthMargin, DuctGapMargin, DuctedAssemblyArea, 
			DuctedAssemblyFTF, AssemblyHexagonFTF, maxDPA)

		################################################################################################### //// ######## //// #######
		##################### Total system approx. size           ######################################### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(TotalSystemHeight, TotalSystemDiameter) \
		= systemgeometry(LowerCoolantPlenaLength, BelowCoreChannelLength, FuelLength, AboveCoreChannelLength, IHXLength, IHXToTop, 
		ThermalCenterElevation, InternalRadialComponentWidth, CoreDiameter, SystemDiameter, PrimaryVesselThickness)

		################################################################################################### //// ######## //// #######
		##################### Calculate flow distribution convergence           ########################### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		FlowCheck.append(InteriorChannelCoolantVelocity)

		if ix > 1:

			FlowError = abs((FlowCheck[ix-1] - FlowCheck[ix-2])/FlowCheck[ix-2])

		################################################################################################### //// ######## //// #######
		##################### Adjust values                  #################### x_adjustment.py      #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
	
		TotalPressureDrop = (ChannelPressureDrop + InletPressureDrop + OutletPressureDrop) * (1 + NonCorePressureDropMultiplier)

		(FuelPinRows, AverageCoolantVelocity, CoolantOutletTemperature,xpressuredrop, xflowvelocity,xfueltemp,xcladi,xclado, xfom1) = \
		adjust(CalculatedPeakCoolantVelocity, CoolantVelocityConstraint, CorePressureDropConstraint, AverageCoolantVelocity, \
		VelocityPrecision, CladdingOuterTemperatureConstraint, TemperatureConvergence, FuelTemperatureConstraint, \
		CladdingInnerTemperatureConstraint, PeakCladdingInnerWallTemperature, PeakCladdingOuterWallTemperature, \
		PeakFuelInnerTemperature, CoolantOutletTemperature, FuelPinRows, ChannelPressureDrop, CoolantOutletTemperatureMode,
		TotalPressureDrop, NaturalCirculationThermalCenterElevation, NaturalCirculationFOM1Constraint)		


	################################################################################################### //// ######## //// #######
	##################### Temperatures plotting ################################ tplot.py          #### //// ######## //// #######
	################################################################################################### //// ######## //// #######
	
	tempplot(FuelLength, Name, mlabpath)
	
	if SerpentCoreType == "SMFR":

		ActiveZoneArea = Assemblies * (3 * math.sqrt(3) / 2) * ((AssemblyHexagonSideLength/100) ** 2) # m^2
		ActiveZoneVolume = ActiveZoneArea * FuelLength / SerpentAxialZones
		FuelZoneVolume = ActiveZoneVolume * FuelVolumeFraction
		CoolantZoneVolume = ActiveZoneVolume * (ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction)
		CladZoneVolume = ActiveZoneVolume * CladdingVolumeFraction

		FuelZoneMass = FuelZoneVolume * SerpentAxialFuelDensity[0] * 1000
		CoolantZoneMass = CoolantZoneVolume * SerpentAxialCoolantDensity[0] * 1000
		CladZoneMass    = CladZoneVolume * SerpentAxialCladdingDensity[0] * 1000

		#print("ActiveZoneArea")
		#print(ActiveZoneArea)
		#print("TotalCoreArea")
		#print(TotalCoreArea)
		#print("SerpentAxialZones")
		#print(SerpentAxialZones)
		#print("FuelZoneMass")
		#print(FuelZoneMass)
		#print("CoolantZoneMass")
		#print(CoolantZoneMass)
		#print("CladZoneMass")
		#print(CladZoneMass) 

		#FuelPert = (SerpentAxialFuelDensity[0]) * 1000 * FuelVolumeFraction * ActiveZoneVolume
		#print(FuelPert)

		################################################################################################### //// ######## //// #######
		##################### Create Control assemblies ########################### x_control.py       #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, ControlInnerSideLength, 
		ControlOuterSideLength) = control(FTF, DuctThickness, BUControlDuctGap, BUControlPinsPerAssembly, BUControlAreaFraction,
		BUControlSmearDensity, BUControlCTR)

		################################################################################################### //// ######## //// #######
		##################### Create SCRAM assemblies ############################# x_control.py       #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius, \
		ScramInnerSideLength, ScramOuterSideLength) = scram(FTF, DuctThickness, ScramDuctGap, ScramPinsPerAssembly, ScramAreaFraction,
		ScramSmearDensity, ScramCTR)

		################################################################################################### //// ######## //// #######
		##################### Calculate radius of inner reflector and shield ###### x_innernonfuel.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		AxialShieldPinRadius    = innershieldradius(CladdingInnerRadius, AxialShieldSlugSmearDensity)
		AxialReflectorPinRadius = innerreflectorradius(CladdingInnerRadius, AxialReflectorSlugSmearDensity)

		################################################################################################### //// ######## //// #######
		##################### Define the grid-plate cell material            ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(GridPlateCellDensity, GridPlateMassFractions) = gridplate(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
		IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, LowerGridPlateSteel, LowerGridPlateSteelFraction, 
		CoolantInletTemperature, CoolantInletDensity, Pb, LBE, Na, Coolant)

		################################################################################################### //// ######## //// #######
		##################### Define coolant-perturbed grid-plate cell material  ## x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(GridPlateCellDensity_perturbed, GridPlateMassFractions_perturbed) = gridplate_perturbed(T91, D9, HT9, ElementZTranslationList, 
		IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, LowerGridPlateSteel, 
		LowerGridPlateSteelFraction, CoolantInletTemperature, CoolantInletDensity, Pb, LBE, Na, Coolant, CoolantTemperaturePerturbation)

		################################################################################################### //// ######## //// #######
		##################### Define the barrel material                     ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(BarrelMassFractions, BarrelDensity) = barrel(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	    IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, CoreBarrelSteel, CoolantAverageTemperature)

		################################################################################################### //// ######## //// #######
		##################### Define the insulator material                  ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(InsulatorMassFractions, LowerInsulatorDensity, UpperInsulatorDensity) = insulator(T91, D9, HT9, ElementZTranslationList, 
		IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, InsulatorMaterial, 
		CoolantAverageTemperature, ZrO2)

		################################################################################################### //// ######## //// #######
		##################### Define the end cap material                    ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(EndCapMassFractions, LowerEndCapDensity, UpperEndCapDensity) = lowerendcap(T91, D9, HT9, ElementZTranslationList, 
		IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, EndCapMaterial, 
		CoolantInletTemperature, CoolantOutletTemperature)

		################################################################################################### //// ######## //// #######
		##################### Define inner reflector material                ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(LowerInnerAxialReflectorDensity, UpperInnerAxialReflectorDensity, InnerReflectorMassFractions) = insidereflector(T91, D9, 
		HT9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	    AxialReflectorPinMaterial, CoolantAverageTemperature, CoolantOutletTemperature)

		################################################################################################### //// ######## //// #######
		##################### Define inner shield material                   ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(LowerInnerAxialShieldDensity, UpperInnerAxialShieldDensity, InnerShieldMassFractions) = insideshield(T91, D9, HT9, B4C, 
		ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
		AxialShieldPinMaterial, CoolantAverageTemperature, CoolantOutletTemperature)

		############################################################################################9####### //// ######## //// #######
		##################### Define bottom plate material                   ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		BottomPlateMassFractions, BottomPlateCellDensity = bottomplate(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
		IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, BottomPlateSteel, CoolantInletTemperature)

		################################################################################################### //// ######## //// #######
		##################### Make BU-control material                       ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(BUControlMassFractions, BUControlDensity) = bucontrolabs(T91, D9, HT9, B4C, ElementZTranslationList, IsotopeAtomFractionList, 
		IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, BUControlAbsorber, CoolantAverageTemperature, 
		CoolantOutletTemperature, BUControlB10Fraction)

		################################################################################################### //// ######## //// #######
		##################### Make SCRAM material                            ###### x_materialcalc.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		(ScramMassFractions, ScramDensity) = scramabs(T91, D9, HT9, B4C, ElementZTranslationList, IsotopeAtomFractionList, 
		IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, ScramAbsorber, CoolantAverageTemperature, 
		CoolantOutletTemperature, ScramB10Fraction)

		################################################################################################### //// ######## //// #######
		##################### Define component colors                              ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		(FuelColor, InsulatorColor, ShieldColor, SteelColor, HotCoolant, MediumCoolant, ColdCoolant, GasColor,
  		GridPlateColor, BarrelColor, InsulatorColor, EndCapColor, AxialReflectorColor, AxialShieldColor, BottomPlateColor, 
  		CoolantGradient20, FuelGradient20, DuctColor, FuelColor, BondColor, CladdingColor, ReflectorColor, BuControlAbsorberColor,
  		ScramAbsorberColor, PerturbedColor) = colors()

		################################################################################################### //// ######## //// #######
		##################### Make the grid-plate cell material                    ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makegridplate(Name, CoolantInletTemperature, GridPlateCellDensity, GridPlateMassFractions, GridPlateColor,
		LowerGridPlateSteelFraction, LowerGridPlateSteel, Coolant)

		################################################################################################### //// ######## //// #######
		##################### Make cold coolant material                           ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makebelowcorecoolant(Name, CoolantIsotopeMassFractions, CoolantInletDensity, CoolantInletTemperature, ColdCoolant,
		Coolant)

		################################################################################################### //// ######## //// #######
		##################### Make inlet plenum coolant material                   ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makelowerplenumcoolant(Name, CoolantIsotopeMassFractions, CoolantInletDensity, CoolantInletTemperature, ColdCoolant,
		Coolant)

		################################################################################################### //// ######## //// #######
		##################### Make in-core coolant material                        ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makecorecoolant(Name, CoolantIsotopeMassFractions, Coolant, SerpentAxialCoolantDensity, SerpentAxialCoolantTemperature,
		SerpentAxialZones, CoolantGradient20)

		################################################################################################### //// ######## //// #######
		##################### Make upper plenum coolant material                   ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeupperplenumcoolant(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, CoolantOutletTemperature, HotCoolant,
		Coolant)

		################################################################################################### //// ######## //// #######
		##################### Make high-temperature in-core coolant material ###### x_smfrdm_react.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		if CoolantReactivityCoefficient == "on":

			makecorecoolant_react(Name, CoolantIsotopeMassFractions, Coolant, SerpentAxialCoolantDensity, SerpentAxialCoolantTemperature,
			SerpentAxialZones, CoolantGradient20, SerpentPerturbedAxialCoolantDensity, CoolantTemperaturePerturbation)

		RelColDensDiff = []

		if SequentialAxialInCoreCoolantReactivity == "on":

			# Make perturbed inlet plenum coolant
			LowerPlenumCoolantDensityDifference = makelowerplenumcoolant_voided(Name, CoolantIsotopeMassFractions, CoolantInletDensity, 
			CoolantInletTemperature, ColdCoolant, Coolant, PerturbedColor, CoolantTemperaturePerturbation)

			# Make perturbed grid plate coolant material
			makegridplate_perturbed(Name, CoolantInletTemperature, GridPlateCellDensity_perturbed, GridPlateMassFractions_perturbed, GridPlateColor,
			LowerGridPlateSteelFraction, LowerGridPlateSteel, Coolant, CoolantTemperaturePerturbation, PerturbedColor)

			for zone in range(SerpentAxialZones):

				RelativeCoolantDensityDifference = makecorecoolant_seqV(Name, CoolantIsotopeMassFractions, Coolant, 
				SerpentAxialCoolantTemperature, SerpentAxialZones, CoolantGradient20, SerpentPerturbedAxialCoolantDensity, 
				CoolantTemperaturePerturbation, zone, SerpentAxialCoolantDensity, PerturbedColor)

				RelColDensDiff.append(RelativeCoolantDensityDifference)

				makecorecoolant_seqR(Name, CoolantIsotopeMassFractions, Coolant, SerpentAxialCoolantDensity, SerpentAxialCoolantTemperature,
				SerpentAxialZones, CoolantGradient20, CoolantTemperaturePerturbation, zone)

			# Make perturbed outlet plenum coolant
			UpperPlenumCoolantDensityDifference = makeupperplenumcoolant_voided(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, CoolantOutletTemperature, HotCoolant,
			Coolant, PerturbedColor, CoolantTemperaturePerturbation)

		################################################################################################### //// ######## //// #######
		##################### Make hot coolant material                           ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeabovecorecoolant(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, AverageCoolantOutletTemperature, HotCoolant,
		Coolant)

		if CoolantReactivityCoefficient == "on":

			makeabovecorecoolant_react(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, AverageCoolantOutletTemperature, HotCoolant,
			Coolant, CoolantTemperaturePerturbation)

		################################################################################################### //// ######## //// #######
		##################### Make in-core duct material                           ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makecoreduct(Name, DuctIsotopeMassFractions, Duct, SerpentAxialDuctDensity, SerpentAxialDuctTemperature,
		SerpentAxialZones, DuctColor)

		################################################################################################### //// ######## //// #######
		##################### Make in-core cladding material                       ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makecorecladding(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
		SerpentAxialZones, CladdingColor, Batches)

		################################################################################################### //// ######## //// #######
		##################### Make below-core cladding material                    ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makebelowcorecladding(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
		SerpentAxialZones, CladdingColor)

		################################################################################################### //// ######## //// #######
		##################### Make hot cladding material                           ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeabovecorecladding(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
		SerpentAxialZones, CladdingColor)

		################################################################################################### //// ######## //// #######
		##################### Make in-core bond material                          ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makecorebond(Name, BondIsotopeMassFractions, Bond, SerpentAxialBondDensity, SerpentAxialBondTemperature,
		SerpentAxialZones, BondColor)

		################################################################################################### //// ######## //// #######
		##################### Make feed-fuel material                              ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		#makefuel(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
		#SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
		#FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20, SerpentDepletion, FuelColor)

		if FuelReactivityCoefficient == "on":

			makefuel_react(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
			SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
			FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
			SerpentDepletion, FuelColor, SerpentPerturbedAxialFuelDensity, FuelTemperaturePerturbation, FuelAverageDensity, WhereInCycle)

		#if FuelDopplerCoefficient == "on":
		#	makefuel_doppler(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
		#	SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
		#	FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
		#	SerpentDepletion, FuelColor, SerpentPerturbedAxialFuelDensity, DopplerTemperaturePerturbation)

		RelFuelDensDiff = []

		if SequentialAxialFuelReactivity == "on":

			for zone in range(SerpentAxialZones):

				mi = open(Name + "_material_fuel_perturbed_axial_" + str(zone+1), 'w')
				mi.close()

				RelativeFuelDensityDifference = makefuel_seqV(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
				SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
				FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
				SerpentDepletion, FuelColor, SerpentPerturbedAxialFuelDensity, FuelTemperaturePerturbation, zone, TotalFuelPins, 
				FreshFuelRadius, FuelLength, TotalFuelLength, PerturbedColor, FuelAverageDensity)

				#print(RelativeFuelDensityDifference)

				RelFuelDensDiff.append(RelativeFuelDensityDifference)

				mi = open(Name + "_material_fuel_reference_axial_" + str(zone+1), 'w')
				mi.close()
				
				makefuel_seqR(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
				SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
				FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
				SerpentDepletion, FuelColor, SerpentPerturbedAxialFuelDensity, FuelTemperaturePerturbation, zone, FuelAverageDensity)

		RelCladDensDiff = []

		if SequentialAxialCladReactivity == "on":

			for zone in range(SerpentAxialZones):

				RelativeCladdingDensityDifference = makecorecladding_seqV(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
			    SerpentAxialZones, CladdingColor, zone, SerpentPerturbedAxialCladdingDensity, CladdingTemperaturePerturbation,
			    CladdingOuterRadius, CladdingInnerRadius, TotalFuelLength, PerturbedColor)

				RelCladDensDiff.append(RelativeCladdingDensityDifference)

				makecorecladding_seqR(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
			    SerpentAxialZones, CladdingColor, zone, SerpentPerturbedAxialCladdingDensity, CladdingTemperaturePerturbation)

		################################################################################################### //// ######## //// #######
		##################### Make feed-fuel material that cannot be depleted      ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makefuelnb(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
		SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
		FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
		SerpentDepletion, FuelColor, FuelAverageDensity, AxialEnrichmentZoning, TotalFuelMaterials)

		################################################################################################### //// ######## //// #######
		##################### Make core barrel material                            ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makecorebarrel(Name, CoreBarrelSteel, CoolantAverageTemperature, D9, HT9, T91, BarrelMassFractions, BarrelDensity, 
		BarrelColor)	

		################################################################################################### //// ######## //// #######
		##################### Make radial reflector pin material                   ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeradialreflector(Name, ReflectorIsotopeMassFractions, ReflectorPinMaterial, SerpentAxialReflectorDensity, 
		SerpentAxialDuctTemperature, SerpentAxialZones, ReflectorColor)

		################################################################################################### //// ######## //// #######
		##################### Make radial shield pin material                      ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeradialshield(Name, ShieldIsotopeMassFractions, ShieldPinMaterial, SerpentAxialShieldDensity, 
		SerpentAxialDuctTemperature, SerpentAxialZones, ShieldColor)

		################################################################################################### //// ######## //// #######
		##################### Make lower insulator pellet material                 ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makelowerinsulator(Name, CoolantInletTemperature, LowerInsulatorDensity, InsulatorColor, InsulatorMaterial, 
		InsulatorMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make upper insulator pellet material                 ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeupperinsulator(Name, CoolantOutletTemperature, UpperInsulatorDensity, InsulatorColor, InsulatorMaterial,
		InsulatorMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make lower end cap material                          ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makelowerendcap(Name, CoolantInletTemperature, LowerEndCapDensity, EndCapColor, EndCapMaterial, EndCapMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make upper end cap material                          ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeupperendcap(Name, CoolantOutletTemperature, UpperEndCapDensity, EndCapColor, EndCapMaterial, EndCapMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make lower inner reflector material                  ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makelowerinnerreflector(Name, CoolantInletTemperature, LowerInnerAxialReflectorDensity, AxialReflectorColor, 
		AxialReflectorPinMaterial, InnerReflectorMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make upper inner reflector material                  ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeupperinnerreflector(Name, CoolantOutletTemperature, UpperInnerAxialReflectorDensity, AxialReflectorColor, 
		AxialReflectorPinMaterial, InnerReflectorMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make lower inner shield material                     ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makelowerinnershield(Name, CoolantInletTemperature, LowerInnerAxialShieldDensity, AxialShieldColor, 
		AxialShieldPinMaterial, InnerShieldMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make upper inner shield material                     ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makeupperinnershield(Name, CoolantOutletTemperature, UpperInnerAxialShieldDensity, AxialShieldColor, 
		AxialShieldPinMaterial, InnerShieldMassFractions)

		################################################################################################### //// ######## //// #######
		##################### Make bottom plate material                           ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makebottomplate(Name, CoolantInletTemperature, BottomPlateCellDensity, BottomPlateMassFractions, BottomPlateColor,
		BottomPlateSteel)

		################################################################################################### //// ######## //// #######
		##################### Make bu-control material                            ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makebucontrolabsorber(Name, CoolantAverageTemperature, BUControlMassFractions, BUControlDensity, BUControlAbsorber,
		BuControlAbsorberColor, BUControlB10Fraction)

		################################################################################################### //// ######## //// #######
		##################### Make scram material                                  ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		makescramabsorber(Name, CoolantAverageTemperature, ScramMassFractions, ScramDensity, ScramAbsorber, ScramAbsorberColor, 
		ScramB10Fraction)
		
		################################################################################################### //// ######## //// #######
		##################### Make system gas material                             ###### x_smfrdm.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		systemgas(Name)

		################################################################################################### //// ######## //// #######
		##################### Define MOC and EOC material from previous depletions ###### x_depmat.py  #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		MOCBUmatNumber = int(round(((SerpentDepletionSteps+1)/2),0))

		MOCBUmatFile   = NameOfReferenceData + "_geometry_reference.bumat" + str(MOCBUmatNumber)
		EOCBUmatNumber = SerpentDepletionSteps
		EOCBUmatFile   = NameOfReferenceData + "_geometry_reference.bumat" + str(EOCBUmatNumber)

		fixdepfuel(MOCBUmatFile, EOCBUmatFile, Name, SerpentPerturbedAxialFuelDensity, SerpentAxialFuelDensity, FuelAverageDensity)

		################################################################################################### //// ######## //// #######
		##################### Create SMFR Serpent model ########################### x_smfrd.py         #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		WhereSMFRD = "Reference"

		AA = "results/" + Name + "/CoreInfo_dpa.txt"
		a = open(AA, 'w')
		a.close()

		InnerLowerGridPlateVolume = LowerGridPlateHeight * math.pi * (5 ** 2)

		if LowerGridDPA == "on" or CladdingDPA == "on":

			energydetector(Name, LowerGridDPA, InnerLowerGridPlateVolume, CladdingDPA, SerpentAxialZones)

		(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, 
		CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch, 
		Name, InnerAssemblySideLength, DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
		ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
		SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
		UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
		ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
		ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
		LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
		BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
		SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
		SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
		SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
		zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
		SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
		SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		################################################################################################### //// ######## //// #######
		##################### Create BU-control insertion at BOC model  ################### x_smfrd.py #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		if BUControlInsertionSimulation == "on":

			WhereSMFRD = "BUControlInsertion"			

			for zoneSC in range(SerpentAxialZones):

				(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, 
				CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
				DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
				ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
				SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
				UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
				ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        		LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        		ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        		ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
				ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
				LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
				BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
				SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
				SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
				SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
				zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
				SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
				SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		################################################################################################### //// ######## //// #######
		##################### Create SCRAM-control insertion at BOC model  ################ x_smfrd.py #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		if SequentialScramRodInsertion == "on":

			WhereSMFRD = "SequentialScramRodInsertion"			

			for zoneSC in range(SerpentAxialZones+1):

				(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, 
				CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
				DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
				ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
				SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
				UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
				ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        		LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        		ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        		ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
				ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
				LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
				BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
				SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
				SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
				SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
				zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
				SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
				SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		################################################################################################### //// ######## //// #######
		##################### Create coolant-density-perturbed model  ##################### x_smfrd.py #### //// ######## //// #######
		################################################################################################### //// ######## //// #######

		if CoolantReactivityCoefficient == "on":

			WhereSMFRD = "CoolantReactivity"			

			(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
			DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
			ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
			SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
			UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
			ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        	LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        	ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        	ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
			ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
			LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
			BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
			SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
			SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
			SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
			zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
			SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
			SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)
	
		if FuelReactivityCoefficient == "on":

			WhereSMFRD = "FuelReactivity"			

			(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
			DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
			ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
			SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
			UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
			ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        	LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        	ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        	ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
			ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
			LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
			BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
			SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
			SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
			SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
			zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
			SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
			SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		if RadialExpansionCoefficient == "on":

			WhereSMFRD = "RadialExpansion"			

			(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
			DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
			ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
			SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
			UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
			ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        	LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        	ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        	ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
			ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
			LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
			BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
			SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
			SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
			SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
			zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
			SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
			SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		if FuelDopplerCoefficient == "on":

			WhereSMFRD = "FuelDoppler"			

			(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
			DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
			ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
			SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
			UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
			ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        	LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        	ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        	ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
			ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
			LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
			BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
			SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
			SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
			SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
			zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
			SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
			SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		if SequentialAxialInCoreCoolantReactivity == "on":

			WhereSMFRD = "LowerCoolantReactivity"			

			(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
			DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
			ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
			SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
			UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
			ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
			LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
			ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
			ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
			ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
			LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
			BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
			SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
			SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
			SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
			zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
			SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
			SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

			WhereSMFRD = "SequentialCoolant"

			for zoneSC in range(SerpentAxialZones):			

				(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
				DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
				ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
				SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
				UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
				ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        		LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        		ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        		ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
				ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
				LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
				BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
				SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
				SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
				SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
				zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
				SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
				SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

			WhereSMFRD = "UpperCoolantReactivity"			

			(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
			DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
			ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
			SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
			UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
			ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
			LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
			ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
			ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
			ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
			LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
			BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
			SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
			SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
			SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
			zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
			SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
			SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		if SequentialAxialFuelReactivity == "on":

			WhereSMFRD = "SequentialFuel"

			for zoneSC in range(SerpentAxialZones):			

				(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
				DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
				ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
				SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
				UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
				ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        		LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        		ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        		ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
				ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
				LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
				BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
				SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
				SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
				SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
				zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
				SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
				SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		if SequentialAxialCladReactivity == "on":

			WhereSMFRD = "SequentialClad"

			for zoneSC in range(SerpentAxialZones):			

				(CoreLatticeIDs, CoreBarrelRadius0, FuelStep0, RadiusChange, FueledRadius, GridPlateVolume, InletPlenumVolume) = smfrd2(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, AssemblyPitch,Name, InnerAssemblySideLength,
				DuctedAssemblySideLength, CoreActinideMass, Power, ReflectorPinOuterRadius, ReflectorPinInnerRadius, 
				ReflectorPinPitch, ReflectorPinSlugRadius, ReflectorPinsPerAssembly, EquivalentCladdingRadius, SerpentSMFRPlotting,
				SerpentDepletion, LowerEndCapLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength,
				UpperGasPlenumLength, UpperEndCapLength, ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius,
				ShieldPinsPerAssembly, SerpentDPA, Assemblies, SerpentAxialZones, PinsPerAssembly, InternalRadialComponentWidth,
        		LowerCoolantPlenaLength, IHXLength, IHXToTop, PrimaryVesselThickness, ThermalCenterElevation, CoreBarrelThickness,
        		ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius, BUControlPinsPerAssembly, ControlInnerSideLength, 
        		ControlOuterSideLength, ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
				ScramInnerSideLength, ScramOuterSideLength, ScramPinsPerAssembly, AxialShieldPinRadius, AxialReflectorPinRadius, 
				LowerShieldLength, LowerReflectorLength, UpperShieldLength, UpperReflectorLength, LowerGridPlateHeight, InletPlenumHeight,
				BottomPlateHeight, BottomSupportStructureHeight, SerpentDepletionType, SerpentDepletionSteps, SerpentDepletionPCC, SerpentDepletionEnd, 
				SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles,
				SerpentInventory, CoreMap, CoreBarrelRadius, CoreLatticeElements, AssemblyHexagonSideLength, WhereSMFRD, FuelTemperaturePerturbation,
				SerpentAxialFuelTemperature, Fuel, FuelExpansion, FuelAverageTemperature, RadialExpansionTemperaturePerturbation, LowerGridPlateSteel,
				zoneSC, RadialReflectorRows, RadialShieldRows, RadiusChange, CoolantInletTemperature, Batches, FreeExpansionDensity, SerpentAxialFuelDensity, 
				SerpentPerturbedAxialFuelDensity, AverageFuelDensity, PerturbedAverageFuelDensity, LowerGridDPA, SerpentDepletionAccuracy, WhereInCycle, CladdingDPA,
				SequentialScramRodInsertion, FuelType, InnerFuelRadius, PlotPixels)

		if SerpentRun == "on" and ReferenceRun == "on":	

			X = 0
			filename = Name + "_geometry_reference_res.m"

			if UseExistingReferenceRun != "on" and UseExistingReferenceRun != "ON":

				################################################################################################### //// ######## //// #######
				##################### Run SMFR Serpent reference model #################### x_runserpent.py    #### //// ######## //// #######
				################################################################################################### //// ######## //// #######
	
				Where = "SMFRiteration"
				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
	
			################################################################################################### //// ######## //// #######
			##################### Gather SMFR data  ################################### x_smfr_data.py     #### //// ######## //// #######
			################################################################################################### //// ######## //// #######

			if os.path.exists(filename) == True and os.path.isfile(filename) == True: X = 1

			if X == 1:

				(RadialPowerPeaking, MaxKeff, MinKeff, BOCKeff, EOCKeff, KeffCycleSwing, KeffPeakSwing, MaxBeff, MinBeff, BOCBeff, EOCBeff, 
				KeffErr, BeffErr) = smfrdata(Name, SerpentDepletionSteps, SerpentDepletion, CoreLatticeIDs)

			if LowerGridDPA == "on":

				Where = "LowerGridDPA"
				calculatepa(Name, Where, InnerLowerGridPlateVolume, CycleTime, LowerGridPlateSteel, CladdingDPA, Cladding, FuelLength,
				SerpentAxialZones, CladdingOuterRadius, CladdingInnerRadius, PinsPerAssembly,x)

			if CladdingDPA == "on":

				Where = "CladdingDPA"
				calculatepa(Name, Where, InnerLowerGridPlateVolume, CycleTime, LowerGridPlateSteel, CladdingDPA, Cladding, FuelLength,
				SerpentAxialZones, CladdingOuterRadius, CladdingInnerRadius, PinsPerAssembly,x)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR Serpent coolant coeff model ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		if SerpentRun == "on" and CoolantReactivityCoefficient == "on":

			Where = "SMFR_coolantcoeff"
			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)

		resfile = "" + Name +  "_geometry_coolantreactivity_res.m"
		(CoolantPerturbationKeff, CoolantPerturbationKeffErr) = getcoeff(resfile)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR Serpent fuel coeff model    ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		if SerpentRun == "on" and FuelReactivityCoefficient == "on":

			Where = "SMFR_fuelcoeff"
			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)

		resfile = "" + Name +  "_geometry_fuelreactivity_res.m"
		(FuelPerturbationKeff, FuelPerturbationKeffErr) = getcoeff(resfile)
	
		################################################################################################### //// ######## //// #######
		##################### Run SMFR Serpent rad. exp. model     ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		if SerpentRun == "on" and RadialExpansionCoefficient == "on":

			Where = "SMFR_radexp"
			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)

		resfile = "" + Name +  "_geometry_radialexpansion_res.m"
		(RadialPerturbationKeff, RadialPerturbationKeffErr) = getcoeff(resfile)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR Serpent fuel doppler model  ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		if SerpentRun == "on" and FuelDopplerCoefficient == "on":

			Where = "SMFR_doppler"
			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)

		resfile = "" + Name +  "_geometry_fueldoppler_res.m"
		(DopplerPerturbationKeff, DopplerPerturbationKeffErr) = getcoeff(resfile)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR BU-control insertion        ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		SequentialBUCKeff      = []
		SequentialBUCKeffError = []

		if SerpentRun == "on" and BUControlInsertionSimulation == "on":

			Where = "SMFR_BUC"

			for zoneSCC in range(SerpentAxialZones):

				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
				resfile = "" + Name +  "_geometry_BUC_ax" + str(zoneSCC+1) + "_res.m"

				(SeqBUCKeff, SeqBUCKeffErr) = getcoeff(resfile)

				SequentialBUCKeff.append(SeqBUCKeff)
				SequentialBUCKeffError.append(SeqBUCKeffErr)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR SCRAM-control insertion        ############# x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		SequentialSCRAMKeff      = []
		SequentialSCRAMKeffError = []

		if SerpentRun == "on" and SequentialScramRodInsertion == "on":

			Where = "SequentialScramRodInsertion"

			for zoneSCC in range(SerpentAxialZones+1):

				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
				resfile = "" + Name +  "_geometry_SCRAM_ax" + str(zoneSCC+1) + "_res.m"

				(SeqSCRAMKeff, SeqSCRAMKeffErr) = getcoeff(resfile)

				SequentialSCRAMKeff.append(SeqSCRAMKeff)
				SequentialSCRAMKeffError.append(SeqSCRAMKeffErr)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR sequential coolant react    ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		SequentialCoolantKeff      = []
		SequentialCoolantKeffError = []
		LowSeqCKeff    = 1
		LowSeqCKeffErr = 0
		UpSeqCKeff     = 1
		UpSeqCKeffErr  = 0		

		if SerpentRun == "on" and SequentialAxialInCoreCoolantReactivity == "on":

			Where = "SMFR_lowseqcool"

			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
			resfile = "" + Name +  "_geometry_lowcoolantreactivity_res.m"	

			(LowSeqCKeff, LowSeqCKeffErr) = getcoeff(resfile)

			Where = "SMFR_seqcool"

			for zoneSCC in range(SerpentAxialZones):

				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
				resfile = "" + Name +  "_geometry_seqcool_ax" + str(zoneSCC+1) + "_res.m"

				(SeqCKeff, SeqCKeffErr) = getcoeff(resfile)

				SequentialCoolantKeff.append(SeqCKeff)
				SequentialCoolantKeffError.append(SeqCKeffErr)

			Where = "SMFR_upseqcool"

			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
			resfile = "" + Name +  "_geometry_upcoolantreactivity_res.m"
			(UpSeqCKeff, UpSeqCKeffErr) = getcoeff(resfile)	

		################################################################################################### //// ######## //// #######
		##################### Run SMFR sequential fuel react       ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		SequentialFuelKeff      = []
		SequentialFuelKeffError = []

		if SerpentRun == "on" and SequentialAxialFuelReactivity == "on":

			Where = "SMFR_seqfuel"

			for zoneSCC in range(SerpentAxialZones):

				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
				resfile = "" + Name +  "_geometry_seqfuel_ax" + str(zoneSCC+1) + "_res.m"

				(SeqFKeff, SeqFKeffErr) = getcoeff(resfile)

				SequentialFuelKeff.append(SeqFKeff)
				SequentialFuelKeffError.append(SeqFKeffErr)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR sequential clad react       ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######				

		SequentialCladKeff      = []
		SequentialCladKeffError = []

		if SerpentRun == "on" and SequentialAxialCladReactivity == "on":

			Where = "SMFR_seqclad"

			for zoneSCC in range(SerpentAxialZones):

				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
				resfile = "" + Name +  "_geometry_seqclad_ax" + str(zoneSCC+1) + "_res.m"

				(SeqClKeff, SeqClKeffErr) = getcoeff(resfile)

				SequentialCladKeff.append(SeqClKeff)
				SequentialCladKeffError.append(SeqClKeffErr)

		################################################################################################### //// ######## //// #######
		##################### Run SMFR Serpent voided model        ################ x_runserpent.py    #### //// ######## //// #######
		################################################################################################### //// ######## //// #######	

		if SerpentRun == "on" and TotalVoidCalculation == "on":

			Where = "SMFR_totalvoid"
			runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)
			
		resfile = "" + Name +  "_geometry_totvoid_res.m"
		(VoidKeff, VoidKeffErr) = getresvoid(resfile)
	
	else:

		################################################################################################### //// ######## //// #######
		##################### Plotting colors  ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		outsidergb     = " 242 242 242 "
		outershieldrgb = " 133 37 37 "
		innershieldrgb = " 133 37 37 "
		outerreflrgb   = " 153 145 145 "
		innerreflrgb   = " 222 213 213 "
		gasrgb         = " 196 225 242"
		
		################################################################################################### //// ######## //// #######
		##################### Define core cell names for serpent          ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		CellNames = corecellnames(Batches, SerpentAxialZones)
		
		################################################################################################### //// ######## //// #######
		##################### Create non-fuel materials file              ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		open(Name + "_nonfuel", 'w')
		
		################################################################################################### //// ######## //// #######
		##################### Print below core coolant for serpent        ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
			
		belowcorecoolant(CoolantIsotopeMassFractions, SerpentAxialCoolantDensity, Coolant, Name, ShieldOuterRadius, serpfilepath,
		SerpentAxialCoolantTemperature, outsidergb)
		
		if LowerShieldLength > 0:
		
			################################################################################################### //// ######## //// #######
			##################### Print lower shield for serpent              ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			lowershield(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
			ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
			CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
			CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
			SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
			SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
			SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
			serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, LowerShieldLength,
			CoreOuterRadius, Cladding, Coolant, Duct, ShieldPinMaterial, SerpentAxialShieldDensity,
			ShieldIsotopeMassFractions, innershieldrgb)
		
		if LowerReflectorLength > 0:
		
			################################################################################################### //// ######## //// #######
			##################### Print lower reflector for serpent           ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			lowerreflector(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
			ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
			CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
			CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
			SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
			SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
			SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
			serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, LowerReflectorLength,
			CoreOuterRadius, Cladding, Coolant, Duct, ReflectorPinMaterial, SerpentAxialReflectorDensity,
			ReflectorIsotopeMassFractions, innerreflrgb)
		
		if LowerGasPlenumLength > 0:
		
			################################################################################################### //// ######## //// #######
			##################### Print lower gas plenum for serpent          ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			lowergasplenum(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
			ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
			CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
			CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
			SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
			SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
			SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
			serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, LowerGasPlenumLength,
			CoreOuterRadius, Cladding, Coolant, Duct, gasrgb)
		
		BelowCoreSerpentLength = LowerShieldLength + LowerReflectorLength + LowerGasPlenumLength	
		
		if BelowCoreSerpentLength > 0:
		
			################################################################################################### //// ######## //// #######
			##################### Print below-core radial reflector serpent   ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			belowcorerefl(ReflectorPinVolumeFraction, ReflectorPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
			DuctIsotopeMassFractions, ReflectorIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
			SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
			SerpentAxialReflectorDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialDuctTemperature, serpfilepath, Name, ReflectorVolume, CoreOuterRadius,
			ReflectorOuterRadius, FuelLength, ReflectorPinOuterRadius, ReflectorPinPitch, BelowCoreSerpentLength, outerreflrgb)
			
			################################################################################################### //// ######## //// #######
			##################### Print below-core radial shield serpent      ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			belowcoreradialshield(ShieldPinVolumeFraction, ShieldPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
			DuctIsotopeMassFractions, ShieldIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
			SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
			SerpentAxialShieldDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialDuctTemperature, serpfilepath, Name, CoreOuterRadius, ShieldOuterRadius, FuelLength, 
			ShieldPinOuterRadius, ShieldPinPitch, ShieldVolume, ReflectorOuterRadius, BelowCoreSerpentLength, outershieldrgb)
		
		AboveCoreSerpentLength = UpperShieldLength + UpperReflectorLength + UpperGasPlenumLength	
		
		if AboveCoreSerpentLength > 0:
		
			################################################################################################### //// ######## //// #######
			##################### Print above-core radial reflector serpent   ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			abovecorerefl(ReflectorPinVolumeFraction, ReflectorPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
			DuctIsotopeMassFractions, ReflectorIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
			SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
			SerpentAxialReflectorDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialDuctTemperature, serpfilepath, Name, ReflectorVolume, CoreOuterRadius,
			ReflectorOuterRadius, FuelLength, ReflectorPinOuterRadius, ReflectorPinPitch, AboveCoreSerpentLength,
			SerpentTemperaturePoints, outerreflrgb)
		
			################################################################################################### //// ######## //// #######
			##################### Print above-core radial shield serpent      ###################          #### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			abovecoreradialshield(ShieldPinVolumeFraction, ShieldPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
			DuctIsotopeMassFractions, ShieldIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
			SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
			SerpentAxialShieldDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialDuctTemperature, serpfilepath, Name, CoreOuterRadius, ShieldOuterRadius, FuelLength, 
			ShieldPinOuterRadius, ShieldPinPitch, ShieldVolume, ReflectorOuterRadius, AboveCoreSerpentLength,
			SerpentTemperaturePoints, outershieldrgb)
		
		################################################################################################### //// ######## //// #######
		##################### Print core materials for serpent            ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		coreisotopes(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
		ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
		NonActinideIsotopeAtomFractions, FissileIsotopeAtomFractions, FertileIsotopeAtomFractions,
		NonActinideIsotopeMassFractions, FissileIsotopeMassFractions, FertileIsotopeMassFractions, 
		ActinideMassFraction,CladdingIsotopeMassFractions, CladdingIsotopeAtomFractions, 
		CladdingAverageAtomicMass, DuctIsotopeMassFractions, DuctIsotopeAtomFractions,
		CoolantIsotopeMassFractions, CoolantIsotopeAtomFractions, BondIsotopeMassFractions,
		BondIsotopeAtomFractions, SerpentAxialCoolantDensity, SerpentAxialIAGapDensity, 
		SerpentAxialCladdingDensity, SerpentAxialDuctDensity, SerpentAxialBondDensity, 
		SerpentAxialFuelDensity, SerpentAxialZones, Batches, SerpentAxialIAGapTemperature, 
		SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, SerpentAxialCladdingTemperature, 
		SerpentAxialBondTemperature, SerpentAxialFuelTemperature, serpfilepath, Name, 
		Fissile, Fertile, Fuel, Cladding, Bond, Coolant, Duct, CellNames, FissileFraction, CellVolume,
		SerpentTemperaturePoints, FuelLength, SerpentCoreRadius, SerpentDepletion, EDIS)
		
		################################################################################################### //// ######## //// #######
		##################### Print reflector materials for serpent       ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		reflectorserpent(ReflectorPinVolumeFraction, ReflectorPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
		DuctIsotopeMassFractions, ReflectorIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
		SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
		SerpentAxialReflectorDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
		SerpentAxialDuctTemperature, serpfilepath, Name, ReflectorVolume, CoreOuterRadius, ReflectorOuterRadius,
		FuelLength, ReflectorPinOuterRadius, ReflectorPinPitch, outerreflrgb)
		
		################################################################################################### //// ######## //// #######
		##################### Print shield materials for serpent          ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		shieldserpent(ShieldPinVolumeFraction, ShieldPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
		DuctIsotopeMassFractions, ShieldIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
		SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
		SerpentAxialShieldDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
		SerpentAxialDuctTemperature, serpfilepath, Name, CoreOuterRadius,
		ShieldOuterRadius, FuelLength, ShieldPinOuterRadius, ShieldPinPitch, ShieldVolume, ReflectorOuterRadius, outershieldrgb)
		
		################################################################################################### //// ######## //// #######
		##################### Print radial outside coolant for serpent    ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		outsidecorecoolant(CoolantIsotopeMassFractions, SerpentAxialCoolantDensity, Coolant, 
		Name, ShieldOuterRadius, serpfilepath, SerpentAxialCoolantTemperature,
		SerpentTemperaturePoints, SystemOuterRadius, CoolantAverageTemperature, outsidergb)
		
		if UpperGasPlenumLength > 0:
		
			uppergasplenum(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
			ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
			CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
			CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
			SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
			SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
			SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
			serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, UpperGasPlenumLength,
			CoreOuterRadius, Cladding, Coolant, Duct, SerpentTemperaturePoints, gasrgb)
		
		if UpperReflectorLength > 0:
		
			upperreflector(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
			ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
			CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
			CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
			SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
			SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
			SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
			serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, UpperReflectorLength,
			CoreOuterRadius, Cladding, Coolant, Duct, ReflectorPinMaterial, SerpentAxialReflectorDensity,
			ReflectorIsotopeMassFractions, SerpentTemperaturePoints, innerreflrgb)
		
		if UpperShieldLength > 0:
		
			uppershield(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
			ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
			CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
			CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
			SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
			SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
			SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
			SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
			serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, UpperShieldLength,
			CoreOuterRadius, Cladding, Coolant, Duct, ShieldPinMaterial, SerpentAxialShieldDensity,
			ShieldIsotopeMassFractions, SerpentTemperaturePoints, innershieldrgb)	
		
		################################################################################################### //// ######## //// #######
		##################### Print above core coolant for serpent        ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
			
		abovecorecoolant(CoolantIsotopeMassFractions, SerpentAxialCoolantDensity, Coolant, 
		Name, SystemOuterRadius, serpfilepath, SerpentAxialCoolantTemperature,
		SerpentTemperaturePoints, outsidergb)	
		
		################################################################################################### //// ######## //// #######
		##################### Produce main serpent input file             ###################          #### //// ######## //// #######
		################################################################################################### //// ######## //// #######
		
		serpentinput(SerpentCoreRadius, Batches, SerpentAxialZones, CellNames, serpfilepath, Name, 
		LowerEndCapLength, LowerShieldLength, LowerReflectorLength, LowerGasPlenumLength, 
		LowerInsulatorPelletLength, FuelLength,  UpperInsulatorPelletLength, UpperGasPlenumLength,  
		UpperReflectorLength, UpperShieldLength, UpperEndCapLength, ReflectorOuterRadius, ShieldOuterRadius,
		SerpentOutsideDistance, SystemOuterRadius, RadialShieldRows, RadialReflectorRows, BelowCoreSerpentLength,
		AboveCoreSerpentLength, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles, SerpentCylPlotting, 
		SerpentDepletion, SerpentDepletionSteps, SerpentDepletionType, SerpentDepletionEnd, SerpentInventory, Power,
		SerpentDepletionPCC, SerpentDPA, SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, EDIS)

		resfile   = Name + "_res.m"
		depfile   = Name + "_dep.m"

		if SerpentRun == "on":
		
			printiter(i, ChannelPressureDrop, InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity, \
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
			AverageFuelDeltaT, AverageCoolantTemperatureRise)
			
			Where = "runcyl"
	
			if EDIS != "on":
	
				runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones)	

		if SerpentRun == "on" or GetNeutronData == "on":
	
			if SerpentVersion == 2:
		
				RadialPowerPeaks = []
				AxialPowerPeaks  = []
	
				for step in range(SerpentDepletionSteps+1):
		
					detfile   = Name + "_det" + str(step) + ".m"
		
					if os.path.exists(detfile): 
			
						(RadialPowerPeaking, PinAxialPowerPeaking) = powers2(detfile, CellNames, Batches, Power, SerpentAxialZones, SerpentCoreRadius, Plotting, matplotlibpath, step, x)
						(PeakFlux, PeakFluence) = flux2(detfile, CellNames, Batches, SerpentAxialZones, CellVolume, ResidenceTime)
		
						RadialPowerPeaks.append(RadialPowerPeaking)
						AxialPowerPeaks.append(PinAxialPowerPeaking)
	
						RadialPowerPeaking = max(RadialPowerPeaks)

						if max(AxialPowerPeaks) < 1.56:

							PinAxialPowerPeaking = max(AxialPowerPeaks)

						else:

							PinAxialPowerPeaking = 1.56

	
				if os.path.exists(resfile): 				
					(MaxKeff, MinKeff, BOCKeff, EOCKeff, MaxBeff, MinBeff, BOCBeff, EOCBeff, KeffCycleSwing, KeffPeakSwing, KeffErr, BeffErr) = getres(resfile, SerpentDepletion, Plotting, depfile, SerpentDepletionSteps, x, matplotlibpath)			
	
				if SerpentDPA == "on":
			
					detfile   = Name + "_det0.m"
	
					if os.path.exists(detfile): 
						(SumFluenceZone, SumFluxZone, SumFastFluxZone, SumFastFluenceZone, DPAcollect, maxDPA, maxDPAcell, PeakFastFluence) = getdet(detfile, CellNames, CellVolume, CycleTime, Cladding)
	
		sol.write(str(RadialPowerPeaking) + " ")
		sol2.write(str(PinAxialPowerPeaking) + " ")
	
	RadialPowerPeaking = SerpentRadialPowerPeakingCorrector * RadialPowerPeaking
	SerpentRadialPowerPeaking.append(RadialPowerPeaking)
	SerpentAxialPowerPeaking.append(PinAxialPowerPeaking)

	DifVals = len(SerpentRadialPowerPeaking)

	if DifVals > 1 and SerpentRun == "on":
	
		RadialPowerPeakDifference = abs((SerpentRadialPowerPeaking[x] - SerpentRadialPowerPeaking[x-1]) / (SerpentRadialPowerPeaking[x]))
		AxialPowerPeakDifference  = abs((SerpentAxialPowerPeaking[x]  - SerpentAxialPowerPeaking[x-1])  / (SerpentAxialPowerPeaking[x]))
		PowerPeakDifference       = max([RadialPowerPeakDifference, AxialPowerPeakDifference])

	VoidWorth = (VoidKeff-BOCKeff)/BOCBeff

	if SerpentCoreType != "Cyl":

		if SerpentRun == "on":
	
			if CoolantReactivityCoefficient == "on":
			
				CoolantReactivityCoefficientPCM   = (CoolantPerturbationKeff - BOCKeff) * 1e5 / CoolantTemperaturePerturbation
				CoolantReactivityCoefficientCents =  100 * (CoolantPerturbationKeff - BOCKeff) / BOCBeff / CoolantTemperaturePerturbation
			
			if FuelReactivityCoefficient == "on":
			
				FuelReactivityCoefficientPCM   = (FuelPerturbationKeff - BOCKeff) * 1e5 / FuelTemperaturePerturbation
				FuelReactivityCoefficientCents =  100 * (FuelPerturbationKeff - BOCKeff) / BOCBeff / FuelTemperaturePerturbation
			
			if RadialExpansionCoefficient == "on":
			
				RadialReactivityCoefficientPCM     =  (RadialPerturbationKeff - BOCKeff) * 1e5 / RadialExpansionTemperaturePerturbation
				RadialReactivityCoefficientCents   =  100 * (RadialPerturbationKeff - BOCKeff) / BOCBeff / RadialExpansionTemperaturePerturbation
				RadialReactivityCoefficientCMPCM   =  (RadialPerturbationKeff - BOCKeff) * 1e5 / RadiusChange
				RadialReactivityCoefficientCMCents =  100 * (RadialPerturbationKeff - BOCKeff) / BOCBeff / RadiusChange
		
			if FuelDopplerCoefficient == "on":
			
				FuelDopplerCoefficientPCM   = -abs((DopplerPerturbationKeff - BOCKeff) * 1e5 / DopplerTemperaturePerturbation)
				FuelDopplerCoefficientCents = -abs(100 * (DopplerPerturbationKeff - BOCKeff) / BOCBeff / DopplerTemperaturePerturbation)
		
			(ColMassDiff, FuelMassDiff, CladMassDiff, BelowMassDiff, AboveMassDiff) = SMFRmasses(SerpentPerturbedAxialFuelDensity, FuelStep0, CoreBarrelRadius0, FuelVolumeFraction, GapVolumeFraction, DuctVolumeFraction, 
			InterAssemblyVolumeFraction, ActiveCoolantVolumeFraction, CladdingVolumeFraction, WireVolumeFraction, RelColDensDiff, SerpentAxialZones, FuelLength,
			RelFuelDensDiff, Name, SerpentAxialCoolantDensity, SerpentPerturbedAxialCoolantDensity, SerpentAxialFuelDensity, RelCladDensDiff, SerpentAxialCladdingDensity, 
			SerpentPerturbedAxialCladdingDensity, FueledRadius, SequentialAxialFuelReactivity, SequentialAxialCladReactivity, SequentialAxialInCoreCoolantReactivity,
			AssemblyHexagonSideLength, Assemblies, GridPlateVolume, InletPlenumVolume, LowerGridPlateSteelFraction, LowerEndCapLength, LowerShieldLength,
			LowerReflectorLength, LowerGasPlenumLength, LowerInsulatorPelletLength, UpperEndCapLength, UpperShieldLength, UpperReflectorLength, UpperGasPlenumLength, UpperInsulatorPelletLength,
			GridPlateCellDensity, GridPlateCellDensity_perturbed, LowerPlenumCoolantDensityDifference, UpperPlenumCoolantDensityDifference)
	
	#if SerpentRunOverRide == "on":

	SerpentRun == "on"

	if SerpentRun == "on":

		if SequentialAxialInCoreCoolantReactivity == "on":

			if CoolantTemperaturePerturbation == "void" or CoolantTemperaturePerturbation == "Void":

				BelowCoreReactPerKG = 1e5 * (LowSeqCKeff - BOCKeff)/(BelowMassDiff)
				AboveCoreReactPerKG = 1e5 * (UpSeqCKeff - BOCKeff)/(AboveMassDiff)

				BelowCents = 100 * (LowSeqCKeff - BOCKeff) / BOCBeff

				AboveCents = 100 * (UpSeqCKeff - BOCKeff) / BOCBeff
				BelowPCM   = 1e5 * (LowSeqCKeff - BOCKeff)
				AbovePCM   = 1e5 * (UpSeqCKeff - BOCKeff) 


			else:

				BelowCoreReactPCM   = 1e5 * (LowSeqCKeff - BOCKeff)/CoolantTemperaturePerturbation
				BelowCoreReactCents = 100 * (LowSeqCKeff - BOCKeff)/BOCBeff
				AboveCoreReactPCM   = 1e5 * (UpSeqCKeff - BOCKeff)/CoolantTemperaturePerturbation			
				AboveCoreReactCents = 100 * (UpSeqCKeff - BOCKeff)/BOCBeff

			for val in range(len(SequentialCoolantKeff)):
	
				SeqCoolPerKGs = 1e5 * (SequentialCoolantKeff[val]-BOCKeff)/ColMassDiff[val]
				SeqCoolPerKG.append(SeqCoolPerKGs)
	
				if CoolantTemperaturePerturbation == "void" or CoolantTemperaturePerturbation == "Void":
	
					SeqCoolCoefficientPCM   = (SequentialCoolantKeff[val] - BOCKeff) * 1e5
					SeqCoolCoefficientCents =  100 * (SequentialCoolantKeff[val] - BOCKeff) / BOCBeff
	
				else:
	
					SeqCoolCoefficientPCM   = (SequentialCoolantKeff[val] - BOCKeff) * 1e5 / CoolantTemperaturePerturbation
					SeqCoolCoefficientCents =  100 * (SequentialCoolantKeff[val] - BOCKeff) / BOCBeff /  CoolantTemperaturePerturbation
	
				SeqCoolCoefficientsPCM.append(SeqCoolCoefficientPCM)
				SeqCoolCoefficientsCents.append(SeqCoolCoefficientCents)

		if SequentialAxialFuelReactivity == "on":
	
			for val in range(len(SequentialFuelKeff)):

				SeqFuelPerKGs = 1e5 * (SequentialFuelKeff[val]-BOCKeff)/FuelMassDiff[val]
				SeqFuelPerKG.append(SeqFuelPerKGs)

				if FuelTemperaturePerturbation != "void" and FuelTemperaturePerturbation != "VOID":

					SeqFuelPerPCMs  = 1e5 * (SequentialFuelKeff[val]-BOCKeff)/FuelTemperaturePerturbation
					SeqFuelPerCents = 100 * (SequentialFuelKeff[val]-BOCKeff)/BOCBeff/FuelTemperaturePerturbation

				else:

					SeqFuelPerPCMs  = 1e5 * (SequentialFuelKeff[val]-BOCKeff)
					SeqFuelPerCents = 100 * (SequentialFuelKeff[val]-BOCKeff)/BOCBeff

				SeqFuelPerPCM.append(SeqFuelPerPCMs)
				SeqFuelPerCent.append(SeqFuelPerCents)

		if SequentialAxialCladReactivity == "on":
	
			for val in range(len(SequentialCladKeff)):

				SeqCladPerKGs = 1e5 * (SequentialCladKeff[val]-BOCKeff)/CladMassDiff[val]
				SeqCladPerKG.append(SeqCladPerKGs)
	
	x += 1	

sol.write("];")
sol2.write("];")
sol.close()
sol2.close()


if RunDynamics == "on" and SequentialAxialInCoreCoolantReactivity == "on" and SequentialAxialFuelReactivity == "on": 

	################################################################################################### //// ######## //// #######
	##################### CARL DYNAMICS                    ################### x_carl.py           #### //// ######## //// #######
	################################################################################################### //// ######## //// #######
	
	import x_dynamics
	
	PowerPerPin      = PeakPinAverageLinearPower * FuelLength            # Watt per pin
	FuelVolumePerPin = math.pi * (FuelLength * 100) * (FreshFuelRadius*100) ** 2   # cm^3
	
	CarlPowerPerCM3       = PowerPerPin / FuelVolumePerPin # WATT PER CM^3 FUEL

	#print("CarlPowerPerCM3")
	#print("{0:02.3f}".format(CarlPowerPerCM3) + " W/cm^3-fuel")

	CarlFlowArea          = 2 * SingleInteriorChannelFlowArea * 100 ** 2 # Flow area cm^2

	#print("CarlFlowArea")
	#print("{0:02.3f}".format(CarlFlowArea) + " cm^2")

	CarlHydraulicDiameter = SingleInteriorChannelHydraulicDiameter * 100

	#print("CarlHydraulicDiameter")
	#print("{0:02.3f}".format(CarlHydraulicDiameter) + " cm")

	CarlCoolantInlet      = CoolantInletTemperature

	#print("CarlCoolantInlet")
	#print("{0:02.3f}".format(CoolantInletTemperature) + " K")

	CarlFlowVelocity      = InteriorChannelCoolantVelocity * 100

	#print("CarlFlowVelocity")
	#print(CarlFlowVelocity)

	CarlFuelRadius        = FreshFuelRadius * 100

	#print("CarlFuelRadius")
	#print(CarlFuelRadius)

	CarlFuelLength        = FuelLength * 100

	#print("CarlFuelLength")
	#print(CarlFuelLength)

	CarlCladdingThickness = CladdingThickness * 100

	#print("CarlCladdingThickness")
	#print(CarlCladdingThickness)

	CarlGapThickness      = (CladdingInnerDiameter*100 - FreshFuelRadius*200)

	#print("CarlGapThickness")
	#print(CarlGapThickness)

	CarlIHX               = ThermalCenterElevation

	#print("CarlIHX")
	#print(CarlIHX)

	CarlPressureDrop      = TotalPressureDrop	

	#print("CarlPressureDrop")
	#print(CarlPressureDrop)

	CarlFuel              = Fuel
	CarlBond              = Bond

	pcm = 1e-5

	CarlCoolantCoefficients = -1.30*pcm
	CarlFuelCoefficients = -0.3*pcm

	CarlFuelCoefficients = []
	CarlCoolantCoefficients = []
	
	for z in range(SerpentAxialZones):
	
		CarlCoolantCoefficients.append(pcm * (RadialReactivityCoefficientPCM/SerpentAxialZones + SeqCoolCoefficientsPCM[z]))
	
		DopplerDefault = SeqFuelPerPCM[z]/3
	
		CarlFuelCoefficients.append(pcm * (DopplerDefault + SeqFuelPerPCM[z]))
	
	# RUN

	print("")
	print("- Running ULOF transient")
	
	ulof = x_dynamics.ULOF(h_rod = CarlFuelLength, r_rod = CarlFuelRadius, P0 = CarlPowerPerCM3, v0 = CarlFlowVelocity, nr=RadialResolution, nz=AxialResolution, 
		                   T_in = CarlCoolantInlet, aD = CarlFuelCoefficients, aC = CarlCoolantCoefficients, z_IHX = CarlIHX, dt = TimeStep,
		                   refine = TimeRefinement, bond = x_dynamics.Na, A_flow = CarlFlowArea, d_h = CarlHydraulicDiameter, axial_peaking = PinAxialPowerPeaking)
	
	ulof.fuel       = x_dynamics.Zr_alloy
	ulof.coolant    = x_dynamics.Na
	ulof.dp_0       = CarlPressureDrop
	ulof.p_over_d   = Pitch/Diameter
	ulof.coast_down = PumpCoastDown
	ulof.dr_gap     = CarlGapThickness
	ulof.dr_clad    = CarlCladdingThickness
	
	outfile = 'test.txt'

	ulof.setup()
	ulof.run(break_at_peak=BreakAtPeak, do_plot=PlotOutput, outfile=outfile, t_stop=MaximumTime)
	#ulof.run(break_at_peak=True, do_plot=False)

	PeakULOFTemperature = max(ulof.T_out-273)

	print(" - Peak ULOF coolant temperature: {0:02.1f}".format(PeakULOFTemperature) + " deg. C")

################################################################################################### //// ######## //// #######
##################### Print converged solution to file ################### x_printiteration.py #### //// ######## //// #######
################################################################################################### //// ######## //// #######

After = time.time()
ConvergedSolution = 1

printiter(i, ChannelPressureDrop, InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity, \
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
AverageFuelDeltaT, AverageCoolantTemperatureRise)

reactivityout(x, Name, SequentialAxialInCoreCoolantReactivity, SeqCoolCoefficientsPCM, SeqCoolCoefficientsCents,
CoolantTemperaturePerturbation, SeqCoolPerKG, SeqFuelPerKG, SequentialAxialFuelReactivity, SequentialAxialCladReactivity, SeqCladPerKG,
RadialReactivityCoefficientCMPCM, RadialReactivityCoefficientCMCents, SequentialBUCKeff, SequentialBUCKeffError, BUControlInsertionSimulation,
BelowCoreReactPerKG, AboveCoreReactPerKG, BelowCoreReactPCM, BelowCoreReactCents, AboveCoreReactPCM, AboveCoreReactCents, BelowCents, AboveCents, BelowPCM, AbovePCM,
VoidWorth, CoolantReactivityCoefficient, CoolantReactivityCoefficientPCM, CoolantReactivityCoefficientCents,
FuelReactivityCoefficient, FuelReactivityCoefficientPCM, FuelReactivityCoefficientCents, TotalVoidCalculation, RadialReactivityCoefficientCents,
RadialReactivityCoefficientPCM, RadialExpansionCoefficient, FuelDopplerCoefficient, FuelDopplerCoefficientCents, FuelDopplerCoefficientPCM, BOCBeff, 
EOCBeff, MinBeff, MaxBeff, BeffErr, BOCKeff, EOCKeff, KeffErr, MinKeff, MaxKeff, SerpentDepletion, PeakFlux, PeakFluence, PeakFastFluence, maxDPA, 
maxDPAcell, Cladding, SerpentDPA, KeffCycleSwing, KeffPeakSwing, SeqFuelPerPCM, SeqFuelPerCent, FuelTemperaturePerturbation, SerpentRun, AverageFuelDeltaT, AverageCoolantTemperatureRise,
AverageCoolantOutletTemperature)

if SerpentCylPlotting == "on":

	print("SERPENT -- Plotting cylindrical cell model")

	Where = "CylinderPlot"
	runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC)
	

if Plotting == "on":

	print("ADOPT -- Plotting")

	mplotting(CoolantTemperatureZ2, CoolantEdgeTemperatureZ2,CoolantEdgeHeatCapacityZ2,CoolantEdgeDensityZ2,
	CoolantEdgeDynamicViscosityZ2, CoolantEdgeConductivityZ2, CoolantEdgeKinematicViscosityZ2,CoolantCornerTemperatureZ2,
	CoolantCornerHeatCapacityZ2,CoolantCornerDensityZ2, CoolantCornerDynamicViscosityZ2,CoolantCornerConductivityZ2,
	CoolantCornerKinematicViscosityZ2, CoolantHeatCapacityZ2, CoolantDensityZ2,CoolantDynamicViscosityZ2,CoolantConductivityZ2,
	CoolantKinematicViscosityZ2, CoolantInteriorPecletZ2, CoolantEdgePecletZ2,CoolantCornerPecletZ2,CoolantInteriorNusseltZ2,
	CoolantEdgeNusseltZ2,CoolantCornerNusseltZ2, CoolantInteriorHeatTransferCoefficientZ2,CoolantEdgeHeatTransferCoefficientZ2,
	CoolantCornerHeatTransferCoefficientZ2, CoolantInteriorReynoldsZ2,CoolantEdgeReynoldsZ2,CoolantCornerReynoldsZ2,
	CladdingOuterWallTemperatureZ2, matplotlibpath, FuelLength, TemperaturePointsZ, FuelInnerAxialTemperatureZ2,
	FuelRimAxialTemperatureZ2, CladdingInnerWallTemperatureZ2, PeakFuelInnerTemperature, PeakFuelInnerTemperateAxialPosition)


################################################################################################### //// ######## //// #######
##################### Plot assemblies                             ###################          #### //// ######## //// #######
################################################################################################### //// ######## //// #######

if SerpentPlotting == "on":

	Where = "AssemblyPlotting"

	fname = plota(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, InnerAssemblySideLength, 
	DuctedAssemblySideLength, Name, AssemblyHexagonSideLength, PinsPerAssembly)
	
	runserpent_single(fname, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where)
	
	radname = plotr(ReflectorPinOuterRadius, ReflectorPinInnerRadius, ReflectorPinPitch, ReflectorPinSlugRadius, 
	InnerAssemblySideLength, DuctedAssemblySideLength, Name, AssemblyHexagonSideLength, PinsPerAssembly, 
	ReflectorPinsPerAssembly)
	
	runserpent_single(radname, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where)
	
	shname = plotsh(ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius, InnerAssemblySideLength, 
	DuctedAssemblySideLength, Name, AssemblyHexagonSideLength, PinsPerAssembly, ShieldPinsPerAssembly)
	
	runserpent_single(shname, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where)
	
	cleanplota(fname, serpplotpath)
	cleanplotr(radname, serpplotpath)
	cleanplotsh(shname, serpplotpath)

picklepath = respath + "/save.p"

Stuff = \
[Name, Power, Batches, CycleTime, FissileFraction, Fissile, Fertile, Fuel, Bond, Cladding, Duct, CoolantInletTemperature,
CoolantOutletTemperature, Assemblies, FTF, DuctThickness, InterAssemblyGap, RelativeWirePitch, CTR, ColdFillGasPressure, 
LowerEndCapLength, LowerShieldLength, LowerReflectorLength, LowerGasPlenumLength, LowerInsulatorPelletLength, FuelLength,
UpperInsulatorPelletLength, UpperGasPlenumLength, UpperReflectorLength, UpperShieldLength, UpperEndCapLength, RadialReflectorRows,
RadialShieldRows, FuelSmearDensity, GadoliniumContent, Burnup, FTDF, Porosity, MetallicFuelNonActinideMassFraction, 
MetallicFuelPlutoniumFraction, ReflectorPinsPerAssembly, ReflectorPinMaterial, ReflectorPinVolumeFraction, ReflectorPinType,
ReflectorSlugSmearDensity, ReflectorSlugCTR, ShieldPinsPerAssembly, ShieldPinMaterial, ShieldPinVolumeFraction, ShieldPinType,
B10Fraction, ShieldSlugSmearDensity, ShieldSlugCTR, Plotting, CoolantTemperatureConstraint, CladdingOuterTemperatureConstraint,
CladdingMidWallTemperatureConstraint, CladdingInnerTemperatureConstraint, FuelTemperatureConstraint, CoolantVelocityConstraint,
MassFlowConstraint, CladdingMinimumThickness, CorePressureDropConstraint, MinimumPinRows, FTF_Convergence, TemperatureConvergence,
AxialTemperaturePoints, VelocityPrecision, SerpentCoreType, SerpentVersion, SerpentPlotting, SerpentRun, SerpentCylNeutrons,
SerpentCylActiveCycles, SerpentCylInactiveCycles, SerpentCylPlotting, SerpentDepletion, SerpentDepletionSteps, SerpentDepletionType,
SerpentDepletionEnd, SerpentDepletionPCC, SerpentInventory, SerpentSMFRPlotting, SerpentDPA, SerpentAxialZones, SerpentOutsideDistance]

f = open(picklepath, 'wb')
for obj in Stuff:
    pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()

lren = len(Stuff)

f = open(picklepath, 'rb')
loaded_objects = []
for i in range(lren-1):
    loaded_objects.append(pickle.load(f))
f.close()

#|----------------------------------------------------------------------------------------------------------|
#|##########################################################################################################|
#|      ________  _______   ______   ______                                                                 | 
#|     /        |/       \ /      | /      \                                                                |
#|     $$$$$$$$/ $$$$$$$  |$$$$$$/ /$$$$$$  |                                                               |
#|     $$ |__    $$ |  $$ |  $$ |  $$ \__$$/        A Serpent shuffling and equilibrium-cycle tool!         |
#|     $$    |   $$ |  $$ |  $$ |  $$      \                                                                |
#|     $$$$$/    $$ |  $$ |  $$ |   $$$$$$  |                                                               |
#|     $$ |_____ $$ |__$$ | _$$ |_ /  \__$$ |                                                               |
#|     $$       |$$    $$/ / $$   |$$    $$/                                                                |
#|     $$$$$$$$/ $$$$$$$/  $$$$$$/  $$$$$$/              Good luck!!                                        |
#|                                                                                                          | 
#|##########################################################################################################|
#|----------------------------------------------------------------------------------------------------------|
#|      Last updated on: November 16th, 2013                                                                | 
#|----------------------------------------------------------------------------------------------------------|                                                                    

if EDIS == "on":

	############################################################################## //// ######## //// #######
	##################### Import EDIS functions                       ############ //// ######## //// #######
	############################################################################## //// ######## //// #######

	from x_edis_func      import *
	from x_edis_dpa       import *
	import time

	# Initial values and empty lists
	KEFF_LIST    = []
	KEFFSD_LIST  = []
	Materialinfo = {}
	diffy        = []
	
	# Make folders to put stuff
	edispath       = "results/" + Name + "/EDIS"
	orgfilespath   = "results/" + Name + "/EDIS" + "/edis_0_originalfiles"
	medfilespath   = "results/" + Name + "/EDIS" + "/edis_1_intermediate"
	finalfilespath = "results/" + Name + "/EDIS" + "/edis_2_finalfiles"
	dpapath        = "results/" + Name + "/EDIS" + "/edis_3_dpafiles"
	resultspath    = "results/" + Name + "/EDIS" + "/edis_x_output"

	if not os.path.exists(edispath): os.makedirs(edispath)
	if not os.path.exists(orgfilespath): os.makedirs(orgfilespath)
	if not os.path.exists(medfilespath): os.makedirs(medfilespath)
	if not os.path.exists(finalfilespath): os.makedirs(finalfilespath)
	if not os.path.exists(resultspath): os.makedirs(resultspath)
	
	# Set initial errors of material and multiplication
	materr   = 100 * mat_convergence
	keff_max = 100 * keff_convergence
	
	# Make sure iterations is an integer
	stage1_iterations= int(round(stage1_iterations))
	stage2_iterations= int(round(iter_convergence))
	
	# Delete old EDIS output files
	delete_edisfiles(resultspath)
	
	# Check that all input is in the correct data format
	filename, version, mpi, nodes, keff_convergence, mat_convergence, iter_convergence, isotope_checks, criticality, eqcycle_days, eqcycle_busteps = checkinputtypes(filename, version, mpi, nodes, keff_convergence, mat_convergence, iter_convergence, isotope_checks, criticality, eqcycle_days, eqcycle_busteps, resultspath)
	
	# Check if the Serpent input file exists
	filename = checkinputfile(filename, resultspath)
	
	# Save the original file-name as given by the user
	orgfilename = filename
	
	# Check for source normalization
	findpowernorm(filename, resultspath)
	
	# Create the STAGE-1 files
	s1file = makeinput_stage1(filename, stage1_neutrons, stage1_activecycles, stage1_inactivecycles)
	
	# Check if and where burnable materials exist
	matnames, numberofburnables = findburnables(s1file, resultspath)
	
	# Check if materials printing is activated
	findprintm(s1file, resultspath)
	
	# Check for depletion
	add_depletion(s1file, eqcycle_days, eqcycle_busteps, resultspath)
	
	# Add nuclide inventory
	setinventory(s1file, isotope_checks, version, resultspath)
	
	# Check the shuffling scheme
	IN, OUT, shuffledmats = checkshuffle(shufflescheme, resultspath)
	
	# Find and define the burnable volume volumes
	VOLUMES = findvolume(s1file, matnames, IN, shuffledmats, resultspath)
	
	# Print notes about Stage 1
	stage1notes(resultspath)
	
	# Define the current stage number as 1
	stage = 1
	
	# Tell the shuffle function we are not yet in criticality search mode
	critty = 0
	
	# Define that convergence has not been achieved
	converged = 0
	
	# See if DPA was run
	ranit = 0
	
	# Start of the process
	Start1 = time.time()
	
	# Start the clock on STAGE-1
	BeforeS1 = time.time()
	
	for iteration in range(stage1_iterations):
	
		where = "stage1"
		Before = time.time()
	
		# If convergence is achieved, break the iteration
		if keff_max < keff_convergence and materr < mat_convergence:
	
			# Stop clock on first converged
			secondconverged = time.time()
			converged = 1
	
			# Calculate the time of the Serpent run
			convtime = timediffcalc(BeforeS1, secondconverged)
	
			# Collect the first run data
			lenkef = len(KEFF_LIST)
			keff0 = KEFF_LIST[lenkef-1]
			keff0min = min(keff0)
			keff0max = max(keff0)
	
			convergednotes(convtime, keff0min, keff0max, eqcycle_kefftarget, eqcycle_days, eqcycle_batches, where, medfilespath, finalfilespath, resultspath, Name)
	
			# Shuffle materials
			shuffle(s1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
			
			if version == 2:
				BurnupFIMA = fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version)
	
			# BU-stuff
			if version == 2:
				bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged)
			else:
				bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days, eqcycle_busteps,resultspath)		
	
			if DPA == "on":
		
				if not os.path.exists(dpapath): os.makedirs(dpapath)
			
				filex = makedpafiles(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles, matnames, where)
			
				# Run neutron transport and depletion
				if mpi == "off":
					runserpent_single(filex,1,sss1filename,sss2filename)
				else:
					runserpent_mpi(filex,1,nodes,sss1filename,sss2filename)
			
				calcdpa(Material, AxialZones, eqcycle_batches, filex, shufflescheme, matnames, eqcycle_busteps, eqcycle_days, VOLUMES, version, where, medfilespath, finalfilespath)
	
			break
	
		# Run neutron transport and depletion
		if mpi == "off":
			runserpent_single(s1file,version,sss1filename,sss2filename)
		else:
			runserpent_mpi(s1file,version,nodes,sss1filename,sss2filename)
	
		After = time.time()
	
		# Calculate the time of the Serpent run
		serptime = timediffcalc(Before, After)
	
		# Read the multiplication factor results
		KEFF_LIST, KEFFSD_LIST, BOEC_KEFFp, EOEC_KEFFp, SWINGp = read_results(s1file, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where, resultspath)
	
		# Read the material composition results
		Materialinfo = checkmaterials(s1file, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath)
	
		# Check material convergence
		if iteration+1 > 50: #eqcycle_batches:
			keff_max = definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath)
			materr = materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath)
	
		# Shuffle materials
		shuffle(s1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
	
	AfterS1 = time.time()
	
	# Calculate the time of the Serpent run
	S1time = timediffcalc(BeforeS1, AfterS1)
	
	# ---------------------------------------------- #
	# STAGE-1 is now finished, moving on to STAGE-2  #
	# ---------------------------------------------- #
	
	if converged != 1:
	
		# Define the current stage number as 2
		stage = 2
		
		# Create the STAGE-1 files
		s2file = makeinput_stage2(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles)
	
		# Print notes about Stage 1
		stage2notes(S1time, resultspath)
	
		for x in range(stage2_iterations):
		
			where = "stage2"
			iteration = x + stage1_iterations
		
			# If convergence is achieved, break the iteration
			if keff_max < keff_convergence and materr < mat_convergence:
		
				# Stop clock on first converged
				secondconverged = time.time()
				converged = 1
		
				# Calculate the time of the Serpent run
				convtime = timediffcalc(BeforeS1, secondconverged)
		
				# Collect the first run data
				lenkef = len(KEFF_LIST)
				keff0 = KEFF_LIST[lenkef-1]
				keff0min = min(keff0)
				keff0max = max(keff0)
		
				convergednotes(convtime, keff0min, keff0max, eqcycle_kefftarget, eqcycle_days, eqcycle_batches, where, medfilespath, finalfilespath, resultspath)
		
				# Shuffle materials
				shuffle(s2file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
				
				if version == 2:
					BurnupFIMA = fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version)
		
				# BU-stuff
				if version == 2:
					bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged)
				else:
					bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days, eqcycle_busteps,resultspath)
				
				if DPA == "on":
			
					if not os.path.exists(dpapath): os.makedirs(dpapath)
				
					filex = makedpafiles(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles, matnames, where)
				
					# Run neutron transport and depletion
					if mpi == "off":
						runserpent_single(filex,1,sss1filename,sss2filename)
					else:
						runserpent_mpi(filex,1,nodes,sss1filename,sss2filename)
				
					calcdpa(Material, AxialZones, eqcycle_batches, filex, shufflescheme, matnames, eqcycle_busteps, eqcycle_days, VOLUMES, version, where, medfilespath, finalfilespath)
		
				break
		
			Before = time.time()
		
			# Run neutron transport and depletion
			if mpi == "off":
				runserpent_single(s2file,version,sss1filename,sss2filename)
			else:
				runserpent_mpi(s2file,version,nodes,sss1filename,sss2filename)
		
			After = time.time()
		
			# Calculate the time of the Serpent run
			serptime = timediffcalc(Before, After)
		
			# Read the multiplication factor results
			KEFF_LIST, KEFFSD_LIST, BOEC_KEFFp, EOEC_KEFFp, SWINGp = read_results(s1file, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where, resultspath)
		
			# Read the material composition results
			Materialinfo = checkmaterials(s1file, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath)
	
			# Check material convergence
			keff_max = definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath)
			materr = materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath)
		
			# Shuffle materials
			shuffle(s1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
	
	if converged != 1:
	
		serp = open(resultspath + "/EDIS_error.txt", 'a', encoding='utf-8')
	
		A = "The system did not reach target convergence within the alloted iterations"
		B = "Either improve statistics or increase the allowed number of STAGE-2 iterations!"
	
		serp.write(A)
		serp.write("\n")
		serp.write(B)
		serp.write("\n")
		serp.close()
	
		import sys
		sys.exit("Error occured, check EDIS_error.txt")
	
	# Collect the first run data
	lenkef = len(KEFF_LIST)
	keff0 = KEFF_LIST[lenkef-1]
	keff0min = min(keff0)
	keff0max = max(keff0)
	
	# Protect from crazy initial guess
	difforg = abs((keff0min - eqcycle_kefftarget)/eqcycle_kefftarget)
	
	if difforg > initialmaxdiff:
	
		serp = open(resultspath + "/EDIS_error.txt", 'a', encoding='utf-8')
	
		A = "Your initial guess at eq. cycle time yield an error of more than {0:02.2%}".format(difforg) + " for k_eff"
		B = "This is larger than the maximum allowed by your settings ({0:02.2%}".format(initialmaxdiff) + ")"
		C = "I recommend restarting this entire run with a new value guessed by you that will give a cycle closer to your target."
	
		serp.write(A)
		serp.write("\n")
		serp.write(B)
		serp.write("\n")
		serp.write(C)
		serp.write("\n")
		serp.close()
	
		import sys
		sys.exit("Error occured, check EDIS_error.txt")
	
	if criticality == "on":
	
		# Reset errors to high values
		materr   = 100 * mat_convergence
		keff_max = 100 * keff_convergence
	
		# Initial values and empty lists
		KEFF_LIST   = []
		KEFFSD_LIST = []
		Materialinfo = {}
	
		# Set keff1 to an initial value
		keff1 = keff0
	
		# Set initial values
		criticalitytries = 0
		eqcycle_days1    = 0
		stage            = 1
		converged        = 0
	
		# Figure out the second cycle time
		eqcycle_days1 = runcriticality(eqcycle_busteps, eqcycle_days, keff0, keff1, criticalitytries, eqcycle_kefftarget, eqcycle_days1,resultspath)
	
		# Make a new cycle file with the new burnup time
		s1file = makeinput_critcycle1(orgfilename, eqcycle_days1, eqcycle_busteps)	
	
		# Telling the shuffle function we are in criticality searching mode
		critty = 1
	
		BeforeS1 = time.time()
	
		for iteration in range(stage1_iterations):
		
			where = "lin1"
			Before = time.time()
	
			# If convergence is achieved, break the iteration
			if keff_max < keff_convergence and materr < mat_convergence:
		
				# Stop clock on first converged
				secondconverged = time.time()
				converged = 1
		
				# Calculate the time of the Serpent run
				convtime = timediffcalc(BeforeS1, secondconverged)
		
				# Collect the first run data
				lenkef = len(KEFF_LIST)
				keff1 = KEFF_LIST[lenkef-1]
				keff1min = min(keff1)
				keff1max = max(keff1)
		
				convergednotes(convtime, keff1min, keff1max, eqcycle_kefftarget, eqcycle_days1, eqcycle_batches, where, medfilespath, finalfilespath, resultspath)
		
				# Shuffle materials
				shuffle(s1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
				
				if version == 2:
					BurnupFIMA = fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version)
		
				# BU-stuff
				if version == 2:
					bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days1, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged)
				else:
					bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days1, eqcycle_busteps,resultspath)
	
				if DPA == "on":
			
					if not os.path.exists(dpapath): os.makedirs(dpapath)
				
					filex = makedpafiles(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles, matnames, where)
				
					# Run neutron transport and depletion
					if mpi == "off":
						runserpent_single(filex,1,sss1filename,sss2filename)
					else:
						runserpent_mpi(filex,1,nodes,sss1filename,sss2filename)
				
					calcdpa(Material, AxialZones, eqcycle_batches, filex, shufflescheme, matnames, eqcycle_busteps, eqcycle_days1, VOLUMES, version, where, medfilespath, finalfilespath)
		
				break
	
			# Run neutron transport and depletion
			if mpi == "off":
				runserpent_single(s1file,version,sss1filename,sss2filename)
			else:
				runserpent_mpi(s1file,version,nodes,sss1filename,sss2filename)
		
			After = time.time()
		
			# Calculate the time of the Serpent run
			serptime = timediffcalc(Before, After)
	
			# Read the multiplication factor results
			read_results(s1file, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where,resultspath)
		
			# Read the material composition results
			Materialinfo = checkmaterials(s1file, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath)
	
			# Check material convergence
			if iteration+1 > 2:
				keff_max = definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath)
				materr = materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath)
		
			# Shuffle materials
			shuffle(s1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
	
		AfterS1 = time.time()
		S1time = timediffcalc(BeforeS1, AfterS1)
	
		# ---------------------------------------------- #
		# STAGE-1 is now finished, moving on to STAGE-2  #
		# ---------------------------------------------- #
		
		if converged != 1:
	
			# Print notes about Stage 1
			stage2notes(S1time,resultspath)
			
			# Define the current stage number as 2
			stage = 2
			
			# Create the STAGE-1 files
			s2file = makeinput_critcycle2(orgfilename, eqcycle_days1, eqcycle_busteps, stage2_neutrons, stage2_activecycles, stage2_inactivecycles)	
		
			BeforeS2 = time.time()
	
			for x in range(stage2_iterations):
			
				where = "lin2"
				iteration = x + stage1_iterations
			
				# If convergence is achieved, break the iteration
				if keff_max < keff_convergence and materr < mat_convergence:
			
					# Stop clock on first converged
					secondconverged = time.time()
		
					converged = 1
		
					# Calculate the time of the Serpent run
					convtime = timediffcalc(BeforeS1, secondconverged)
			
					# Collect the first run data
					lenkef = len(KEFF_LIST)
					keff1 = KEFF_LIST[lenkef-1]
					keff1min = min(keff1)
					keff1max = max(keff1)
			
					convergednotes(convtime, keff1min, keff1max, eqcycle_kefftarget, eqcycle_days1, eqcycle_batches, where, medfilespath, finalfilespath, resultspath)
			
					# Shuffle materials
					shuffle(s2file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
					
					if version == 2:
						BurnupFIMA = fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version)
			
					# BU-stuff
					if version == 2:
						bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days1, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged)
					else:
						bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days1, eqcycle_busteps,resultspath)
	
					if DPA == "on":
				
						if not os.path.exists(dpapath): os.makedirs(dpapath)
					
						filex = makedpafiles(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles, matnames, where)
					
						# Run neutron transport and depletion
						if mpi == "off":
							runserpent_single(filex,1,sss1filename,sss2filename)
						else:
							runserpent_mpi(filex,1,nodes,sss1filename,sss2filename)
					
						calcdpa(Material, AxialZones, eqcycle_batches, filex, shufflescheme, matnames, eqcycle_busteps, eqcycle_days1, VOLUMES, version, where, medfilespath, finalfilespath)
		
					break
			
				Before = time.time()
		
				# Run neutron transport and depletion
				if mpi == "off":
					runserpent_single(s2file,version,sss1filename,sss2filename)
				else:
					runserpent_mpi(s2file,version,nodes,sss1filename,sss2filename)
			
				After = time.time()
			
				# Calculate the time of the Serpent run
				serptime = timediffcalc(Before, After)
		
				# Read the multiplication factor results
				read_results(s2file, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where,resultspath)
			
				# Read the material composition results
				Materialinfo = checkmaterials(s2file, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath)
		
				# Check material convergence
				keff_max = definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath)
				materr = materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath)
			
				# Shuffle materials
				shuffle(s2file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
	
		if converged != 1:
	
			serp = open(resultspath + "/EDIS_error.txt", 'a', encoding='utf-8')
		
			A = "The system did not reach target convergence within the alloted iterations"
			B = "Either improve statistics or increase the allowed number of STAGE-2 iterations!"
		
			serp.write(A)
			serp.write("\n")
			serp.write(B)
			serp.write("\n")
			serp.close()
	
			import sys
			sys.exit("Error occured, check EDIS_error.txt")
	
		# Gather data from last run
		lenkef = len(KEFF_LIST)
		keff1 = KEFF_LIST[lenkef-1]
		keff1min = min(keff1)
	
		# Set initial values
		criticalitytries = 1
		stage            = 1
		converged        = 0
	
		# Initial values and empty lists
		KEFF_LIST   = []
		KEFFSD_LIST = []
		Materialinfo = {}
	
		# Reset errors to high values
		materr   = 100 * mat_convergence
		keff_max = 100 * keff_convergence
	
		# Figure out critical equilibrium cycle days
		eqcycle_days2 = runcriticality(eqcycle_busteps, eqcycle_days, keff0, keff1, criticalitytries, eqcycle_kefftarget, eqcycle_days1,resultspath)
	
		# Print info for the next run
		precriticalnotes(keff0min, keff1min, eqcycle_days, eqcycle_days1, eqcycle_days2, resultspath)
	
		# Make a new cycle file with the new burnup time
		eq1file = makeinput_eqcycle1(orgfilename, eqcycle_days2, eqcycle_busteps)	
	
		# Telling the shuffle function we are in criticality searching mode
		critty = 2
	
		BeforeS1 = time.time()
	
		for iteration in range(stage1_iterations):
	
			where = "eq1"
			Before = time.time()
	
			if keff_max < keff_convergence and materr < mat_convergence:
			
				# Stop clock on first converged
				linconverged = time.time()
		
				converged = 1	
		
				# Calculate the time of the Serpent run
				convtime = timediffcalc(BeforeS1, linconverged)
			
				# Collect the first run data
				lenkef = len(KEFF_LIST)
				keff2 = KEFF_LIST[lenkef-1]
				keff2min = min(keff2)
				keff2max = max(keff2)
			
				convergednotes(convtime, keff2min, keff2max, eqcycle_kefftarget, eqcycle_days2, eqcycle_batches, where, medfilespath, finalfilespath, resultspath)
				
				# Shuffle materials
				shuffle(eq1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
				
				if version == 2:
					BurnupFIMA = fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version)
			
				# BU-stuff
				if version == 2:
					bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days2, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged)
				else:
					bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days2, eqcycle_busteps,resultspath)
	
				if DPA == "on":
				
					if not os.path.exists(dpapath): os.makedirs(dpapath)
				
					filex = makedpafiles(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles, matnames, where)
				
					# Run neutron transport and depletion
					if mpi == "off":
						runserpent_single(filex,1,sss1filename,sss2filename)
					else:
						runserpent_mpi(filex,1,nodes,sss1filename,sss2filename)
				
					calcdpa(Material, AxialZones, eqcycle_batches, filex, shufflescheme, matnames, eqcycle_busteps, eqcycle_days2, VOLUMES, version, where, medfilespath, finalfilespath)
		
				break
		
			# Run neutron transport and depletion
			if mpi == "off":
				runserpent_single(eq1file,version,sss1filename,sss2filename)
			else:
				runserpent_mpi(eq1file,version,nodes,sss1filename,sss2filename)
	
			After = time.time()
		
			# Calculate the time of the Serpent run
			serptime = timediffcalc(Before, After)
		
			# Read the multiplication factor results
			read_results(eq1file, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where,resultspath)
		
			# Read the material composition results
			Materialinfo = checkmaterials(eq1file, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath)
		
			# Check material convergence
			if iteration+1 > 2:
				keff_max = definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath)
				materr = materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath)
		
			# Shuffle materials
			shuffle(eq1file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
	
		AfterS1 = time.time()
		S1time = timediffcalc(BeforeS1, AfterS1)
	
		# ---------------------------------------------- #
		# STAGE-1 is now finished, moving on to STAGE-2  #
		# ---------------------------------------------- #
		
		if converged != 1:
	
			BeforeS2 = time.time()
			
			# Print notes about Stage 1
			stage2notes(S1time,resultspath)
			
			# Define the current stage number as 2
			stage = 2
			
			# Create the STAGE-1 files
			eq2file = makeinput_eqcycle2(orgfilename, eqcycle_days2, eqcycle_busteps, stage2_neutrons, stage2_activecycles, stage2_inactivecycles)	
		
			for x in range(stage2_iterations):
		
				where = "eq2"
				iteration = x + stage1_iterations
			
				# If convergence is achieved, break the iteration
				if keff_max < keff_convergence and materr < mat_convergence:
			
					# Stop clock on first converged
					linconverged = time.time()
		
					converged = 1	
		
					# Calculate the time of the Serpent run
					convtime = timediffcalc(BeforeS2, linconverged)
			
					# Collect the first run data
					lenkef = len(KEFF_LIST)
					keff2 = KEFF_LIST[lenkef-1]
					keff2min = min(keff2)
					keff2max = max(keff2)
			
					convergednotes(convtime, keff2min, keff2max, eqcycle_kefftarget, eqcycle_days2, eqcycle_batches, where, medfilespath, finalfilespath, resultspath)
					
					# Shuffle materials
					shuffle(eq2file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
					
					if version == 2:
						BurnupFIMA = fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version)
			
					# BU-stuff
					if version == 2:
						bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days2, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged)
					else:
						bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days2, eqcycle_busteps,resultspath)
	
					if DPA == "on":
				
						if not os.path.exists(dpapath): os.makedirs(dpapath)
					
						filex = makedpafiles(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles, matnames, where)
					
						# Run neutron transport and depletion
						if mpi == "off":
							runserpent_single(filex,1,sss1filename,sss2filename)
						else:
							runserpent_mpi(filex,1,nodes,sss1filename,sss2filename)
					
						calcdpa(Material, AxialZones, eqcycle_batches, filex, shufflescheme, matnames, eqcycle_busteps, eqcycle_days2, VOLUMES, version, where, medfilespath, finalfilespath)
		
					break
			
				Before = time.time()
		
				# Run neutron transport and depletion
				if mpi == "off":
					runserpent_single(eq2file,version,sss1filename,sss2filename)
				else:
					runserpent_mpi(eq2file,version,nodes,sss1filename,sss2filename)
		
				After = time.time()
			
				# Calculate the time of the Serpent run
				serptime = timediffcalc(Before, After)
			
				# Read the multiplication factor results
				read_results(eq2file, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where,resultspath)
			
				# Read the material composition results
				Materialinfo = checkmaterials(s2file, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath)
		
				# Check material convergence
				keff_max = definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath)
				materr = materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath)
			
				# Shuffle materials
				shuffle(eq2file, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version)
	
		# Gather data from last run
		lenkef = len(KEFF_LIST)
		keff2 = KEFF_LIST[lenkef-1]
		keff2min = min(keff2)
	
		End1 = time.time()
	
	else:
	
		End1 = time.time()
	
	if converged != 1:
	
		serp = open(resultspath + "/EDIS_error.txt", 'a', encoding='utf-8')
	
		A = "The system did not reach target convergence within the alloted iterations"
		B = "Either improve statistics or increase the allowed number of STAGE-2 iterations!"
	
		serp.write(A)
		serp.write("\n")
		serp.write(B)
		serp.write("\n")
		serp.close()
	
		import sys
		sys.exit("Error occured, check EDIS_error.txt")
	
	EqTime = timediffcalc(Start1, End1)
	
	finishednotes(EqTime, resultspath)
	
	if DPA == "on":
	
		cleandpa(orgfilename, dpapath)
		
	else:
	
		cleanupfiles(orgfilename, eqcycle_busteps, orgfilespath, medfilespath, finalfilespath, resultspath)	
	
	e_new   = "serpent_output.txt"
	if os.path.exists(e_new) == True:
		os.remove(e_new)
	
#cleanserpentfiles(Name, serpfilepath)
cleancylplot(Name, serpfilepath)

copyrunfiles(runfilepath, AverageCoolantVelocity, CoolantOutletTemperature, PinAxialPowerPeaking, RadialPowerPeaking)

