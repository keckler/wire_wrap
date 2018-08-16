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
#|      Last updated on: November 16th, 2013                                                                | 
#|----------------------------------------------------------------------------------------------------------|

## RUN NAME (results will be found in results/Name)
Name = "BnB"

################################################################################## //// ######## //// ######|
########    -- GENERAL INPUT SETTINGS --                                      #### //// ######## //// ######| 
################################################################################## //// ######## //// ######|  

## POWER
Power = 3500e6 # Total system thermal heating power [W]

## CORE COMPONENTS
Fuel     = "MetallicZr"  # UO2/Nitride/Carbide/MetalU/MetallucZr/MetallicMo/MetallicTh
Bond     = "Na"     # He/Na/Pb/LBE
Cladding = "HT9"     # D9/HT9/T91 (Wire assumed to be the same material as cladding)
Coolant  = "Na"     # Na/Pb/LBE
Duct     = "HT9"     # D9/HT9/T91

## COOLANT PROPERTIES
CoolantInletTemperature  = 355.0 + 273.15 # Coolant inlet temperature [K]
CoolantOutletTemperature = 534.0 + 273.15 #"C" # Set or calculated PEAK coolant outlet temperature [K or "C"]

## PRIMARY CYCLE FLOW CHARACTERISTICS
ThermalCenterElevation        = 2.15   # Elevation between the thermal center of the core and thermal center of the internal heat exchanger [m]
NonCorePressureDropMultiplier = 0.20   # Fraction of the total pressure drop in the primary system that is NOT in the core (recommended value = 0.2) [#]
PumpResistanceFraction        = 0.05   # Pump pressure drop fraction in natural circulation (recommended value = 0.05) [#]
          
## ASSEMBLY & PIN
Assemblies                   = 492      # Number of power-producing fuel assemblies [#]
InternalControlAssemblies    = 0       # Number of control-assemblies located inside the core [#]
FTF                          = 18.0     # Assembly inner flat-to-flat size [cm]
DuctThickness                = 3.50     # Duct/Wrapper wall thickness [mm or "C"]
InterAssemblyGap             = 2.00     # Gap betweeen assemblies per assembly [mm or "C"]
RelativeWirePitch            = 25       # Axial heigh of one 360-degree wire rotation around the pin given as: [Variable] * Rod Diameter [#, 8 < x < 50]
CTR                          = 0.05     # Cladding thickness ratio (cladding thickness / outer rod diameter) [#]
FissionGasVenting            = "on"     # Vent fission gases to coolant
SpacerType                   = "Wire"   # Wire/Grid/None   

## AXIAL COMPONENTS WITHIN ADOPT CALCULATION         
LowerEndCapLength            = 0.01      # Length of the lower end cap              [m]
LowerShieldLength            = 0.05      # Length of lower shielding within the rod [m]
LowerReflectorLength         = 0.00      # Length of lower reflector within the rod [m]
LowerGasPlenumLength         = 0.00      # Length of gas plenum below the core      [m]
LowerInsulatorPelletLength   = 0.00      # Length of the lower insulator pellet     [m]
FuelLength                   = 3.00      # Length of active fuel                    [m]
UpperInsulatorPelletLength   = 0.01      # Length of the upper insulator pellet     [m]
UpperGasPlenumLength         = 0.10      # Length of gas plenum above the core      [m]    
UpperReflectorLength         = 0.00      # Length of upper reflector within the rod [m]
UpperShieldLength            = 0.00      # Length of upper shielding within the rod [m]
UpperEndCapLength            = 0.01      # Length of the upper end cap              [m]

## AXIAL COMPONENTS NOT INCLUDED IN ADOPT CALCULATION 
LowerCoolantPlenaLength = 0.5   # Total axial length of the lower coolant plena structure [m]
IHXLength               = 3     # Total axial length of the internal head exhanger        [m]
IHXToTop                = 0.5   # Total axial length between the top of the IHX and the top of the vessel [m]

## RADIAL COMPONENTS NOT INCLUDED IN ADOPT CALCULATION
InternalRadialComponentWidth = 0.60 # Total width of the pumps or IHXs (whichever is the most wide) [m]
CoreBarrelThickness          = 0.04
PrimaryVesselThickness       = 0.06 # Thickness of the primary vessel [m]

## GENERAL FUEL DATA
FuelType         = "solid" #"annular" 
FuelSmearDensity = 75.0    # % of the cross-sectional area of the inside of the rod that is (fresh) fuel [%]
FTDF             = 1.00    # Fresh fuel density fraction of theoretical density (ref oxide: 0.95, metal = 1.00) [#]
Porosity         = 1-FTDF  # Fresh fuel porosity (recommended, Porosity = 1-FTDF), irradiated fuel porosity is calculated

## SPECIFIC METALLIC FUEL DATA
MetallicFuelNonActinideMassFraction = 0.06 # Fraction of metallic alloy fuel (MetallicZr or MetallicMo) that is the alloying element [#]
BondInfiltration = 0.4 # Fraction of porosity that is filled with liquid bond as fuel swells
  
## OPTIONAL SETTINGS (USUALLY NO NEED TO CHANGE)
MeVPerFission             = 200   # The average recoverable energy in MeV per fission (ref: 200 MeV), for use in cladding thickness calculations
GasAtomsPerFission        = 0.27  # The average number of gaseous atoms created per fission event
ColdFillGasPressure       = 200e3 # Pressure at 20 deg. C (101300 = 1 atm) [Pa]
FissionGasVentingPressure = 200e3

################################################################################## //// ######## //// ######|
########    -- INITIAL GUESSES --                                            ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    It's very important for calculation efficiency to provide good   ##### //// ######## //// ######|  
########    initial guesses. If ADOPT print-output shows large differences   ##### //// ######## //// ######|  
########    to the defined values here, considere cancelling the run to      ##### //// ######## //// ######|
########    define  better initial guess values!                             ##### //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

## FLOW VELOCITY GUESS
## Note! The initial guess for coolant flow velocity is EXTREMELY important.
## A 100% safe guess is to set it equal to the flow velocity constraint value, but such settings may lead
## to very long computational time as flow-related constraint might be violated. A good guess for coolant 
## velocity can be found rather quickly by trial and error, this is highly recommended!

AverageCoolantVelocity = 11.3 # [m/s]

## ASSEMBLY SOLVER INITIAL GUESS (values will be updated even without running Serpent)
DuctWallGuess = 2.0 # Guess for Duct/Wrapper wall thickness [mm]
IAGapGuess    = 1.5 # Guess for initial gap betweeen assemblies per assembly [mm]

## VALUES THAT WILL NOT BE UPDATED UNLESS SERPENT RESULTS ARE AVAILABLE
Burnup                             = 100             # Est. average discharge burnup [GWd/MT]
PinAxialPowerPeaking               = 1.50            # The axial power peaking along the peak-power pin (qmax/qave)
RadialPowerPeaking                 = 2.20           # The radial (axially averaged) power peaking across the core
SerpentRadialPowerPeakingCorrector = 1.000 # Corrector for the inability of Serpent to calculate continouous power distribution [DO NOT CHANGE]
PeakFlux                           = 1.00e15         # Guess for the peak core flux
PeakFastFlux                       = 0.6 * PeakFlux  # Guess for the peak core fast flux
maxDPA                             = 200
MetallicFuelPlutoniumFraction      = 0.10            # Estimated peak plutonium fraction in MetallicZr fuel [#]
								                	 # (for use in conductivity and density calc., this guess
								                	 #  will NOT be used to define the fuel composition in SERPENT) 

################################################################################## //// ######## //// ######|
########    -- CONSTRAINTS --                                                ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    It's very important for calculation efficiency to provide good   ##### //// ######## //// ######|  
########    initial guesses. If ADOPT print-output shows large differences   ##### //// ######## //// ######|  
########    to the defined values here, considere cancelling the run to      ##### //// ######## //// ######|
########    define  better initial guess values!                             ##### //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

## FLOW CONSTRAINTS
PressureDropConstraint               = 1.00e6 # Total primary cycle pressure drop constraint [Pa]
MassFlowConstraint                   = 1e6   # Maximum coolant mass flow rate [kg/s]
CoolantVelocityConstraint            = 12    # Peak coolant axial velocity [m/s]
NaturalCirculationFOM1Constraint     = 1000#ThermalCenterElevation # Maximum thermal center elevation for decay heat removal by natural circulation [m]
DecayHeatTime                        = 0.0 # Time after shutdown that natural circulation decay heat removal capacity is analyzed for (recommended value = 0.0) [s]

## TEMPERATURE CONSTRAINTS
CoolantTemperatureConstraint         = 550.0  + 273.15  # Maximum coolant temperature [K]
CladdingOuterTemperatureConstraint   = 600.0  + 273.15  # Maximum cladding outer wall temperature [K]
CladdingMidWallTemperatureConstraint = 625.0  + 273.15  # Maximum cladding mid-wall temperature [K]
CladdingInnerTemperatureConstraint   = 650.0  + 273.15  # Peak cladding temperature [K]
FuelTemperatureConstraint            = 1000.0 + 273.15  # Peak centerline fuel temperature [K]

## STRUCTURAL CONSTRAINTS
MinimumPinRows                       = 7       # Minimum rows of fuel pins (6 = 127 pins, 7 = 169 pins etc.) [#]
YieldStrengthMargin                  = 1/(3/2) # Maximum allowable duct and cladding stress as a fraction of yield stress [#]
DuctGapMargin                        = 0.1    # Gap between adjacent duct walls at end of life [mm]

# CLADDING CONSTRAINING FACTORS
CladdingCreepConstraint              = 1             # Maximum allowable life-time cladding creep [%]
CladdingCDFConstraint                = 0.5           # Cumulative cladding damage fraction [#]
CladdingMinimumThickness             = 0.4          # Minimum cladding thickess [mm]
CladdingPeakDesignGasTemperature     = 550 + 273.15  # Maximum fission gas temperature applicable for cladding thickness analysis ["C" or set to a temperature]
GasReleaseFraction                   = 1.00          # Fraction of fission gas produced that is released to the plenum ["C" or value 0 < x < 100]
PeakFCMIDesignPressure               = 10.0          # Peak pressure [MPa]

################################################################################## //// ######## //// ######|
########    -- CORE-MODEL INPUT SETTINGS --                                  ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    These settings are required for ADOPT to make a SERPENT model    ##### //// ######## //// ######|  
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

## CORE FUEL DISTRIBUTION
## The variable "Batches" refer to the number of radial core zones that will be modeled.
## This value does not need to correspond to the number of actual batches that are shuffled in the system.
## A single-batch system (no shuffling) can be modeled by setting a ficticious >1 value for Batches, which
## enables burnup-dependent results radially in the core. The vectors defining the fraction of fissile
## material in each radial region ("FissileFraction"), the type of fissile material ("Fissile") and the type
## of fertile material ("Fissile") must be of the same length as the defined number of batches ("Batches").

## EXAMPLE Small Modular Fast Reactor (turn EDIS off!)
## Creates a core with three radial enrichment zones that flattens power distribution 
##

x8   = 0.080
x85  = 0.085 
x105 = 0.105
x115 = 0.115
x145 = 0.145
x15  = 0.150
x18  = 0.180

Batches               = 12
AxialEnrichmentZoning = "off"

#FissileFraction       = [ x18, x8, x18 ]

# Starting from the radial center batch at the bottom
# AXIAL          == HORIZONTAL
# RADIAL (BATCH) == VERTICAL

x = 0.25/100

FissileFraction       = [x, x, x,
						 x, x, x,
						 x, x, x,
					 	 x, x, x,
						 x, x, x,
						 x, x, x,
						 x, x, x,
						 x, x, x,
						 x, x, x,
						 x, x, x,
						 x, x, x,
						 x, x, x];

#FissileFraction       = [ 0.145,  0.12  , 0.08  , 0.08  , 0.12   , 0.145,
#						  0.155 , 0.13  , 0.10  , 0.10  , 0.13   , 0.155,
#						  0.175 , 0.16  , 0.145 , 0.145 , 0.16   , 0.175] # Fraction of fissile material loaded in each radial batch (first value is radial center)

Fissile       = ["U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235",
				 "U235","U235","U235"] # Fissile fuel component (U233/U235/TRU-SMFR/TRU-51-5/TRU-51-10/TRU-33-30)] 

Fertile       = ["U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238",
				 "U238","U238","U238"]  # Fertile fuel component (U238/Th/DU/NU)]

## FUEL CYCLE INFORMATION
CycleTime       = 730 * 1.0        # Cycle time in [days]
ResidenceTime   = CycleTime #* Batches  # Total time the fuel assembly stays in the core (in a shuffled system: ResidenceTime = Batches * CycleTime) [days]

## AXIAL SHIELD DEFINITION
AxialShieldPinMaterial         = "B4C"  # D9/HT9/T91/B4C
AxialShieldSlugSmearDensity    = 0.99   # Area fraction of the fuel rod that is shield pin [#]

## AXIAL REFLECTOR DEFINITION
AxialReflectorPinMaterial      = "D9"  # D9/HT9/T91
AxialReflectorSlugSmearDensity = 0.99   # Area fraction of the fuel rod that is reflection pin [#]

## RADIAL REFLECTOR DEFINITION
RadialReflectorRows         = 1         # Number of rows of radial reflectors outside of the active core [#]
ReflectorPinsPerAssembly    = 37        # Number of reflector pins per radial reflector assembly [#]
ReflectorPinMaterial        = "D9"     # D9/HT9/T91
ReflectorPinVolumeFraction  = 0.40      # Volume fraction of the radial reflector assembly that consists of reflector pin material [#]
ReflectorPinType            = "Layered" # Layered = Uses reflector pin, gap and cladding. Solid = Single reflector piece (no gap or cladding)
ReflectorSlugSmearDensity   = 0.85      # Area fraction of the reflector pin that is reflector material [ONLY for layered reflector pins] [#]
ReflectorSlugCTR            = 0.05      # Reflector pin cladding thickness ratio [ONLY for layered reflector pins] [#]

## RADIAL SHIELD DEFINITION
RadialShieldRows         = 1            # Number of rows of radial shield outside of the active core or (if applicable) radial reflectors [#]
ShieldPinsPerAssembly    = 19           # Number of shield pins per radial reflector assembly [#]
ShieldPinMaterial        = "B4C"        # D9/HT9/T91/B4C
ShieldPinPorosity        = 0.10
ShieldPinVolumeFraction  = 0.60         # Volume fraction of the radial reflector assembly that consists of reflector pin material [#]
ShieldPinType            = "Layered"    # Layered = Uses shield pin, gap and cladding. Solid = Single shield piece (no gap or cladding)
B10Fraction              = 0.90         # The boron enrichment for B4C shield pins [#]
ShieldSlugSmearDensity   = 0.85         # Area fraction of the shield pin that is shield material [ONLY for layered shield pins] [#]
ShieldSlugCTR            = 0.05         # Shield pin cladding thickness ratio [ONLY for layered shield pins] [#]

## BURNUP CONTROL ASSEMBLY DEFINITION
BUControlDuctGap         = 5 # mm
BUControlPinsPerAssembly = 19
BUControlAreaFraction    = 0.85
BUControlAbsorber        = "B4C"
BUControlB10Fraction     = 0.199
BUControlSmearDensity    = 0.95
BUControlCTR             = 0.05

## SCRAM ASSEMBLY DEFINITION
ScramDuctGap         = 5 # mm
ScramPinsPerAssembly = 7
ScramAreaFraction    = 0.85
ScramAbsorber        = "B4C"
ScramB10Fraction     = 0.90
ScramSmearDensity    = 0.99
ScramCTR             = 0.05

################################################################################## //// ######## //// ######|
########    -- SEPRENT RUN-SETTINGS --                                       ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    These settings are for ADOPT-SERPENT and does not affect the     ##### //// ######## //// ######|  
########    EDIS-SERPENT settings which are given seperately                 ##### //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

## ACTIVATE SERPENT NEUTRON TRANSPORT
SerpentRun               = "off"      # Run Serpent neutron transport ["on"/"off"]

## SERPENT SIMULATION-TYPE SETTINGS
SerpentCoreType          = "Cyl"     # "Cyl"  = Conventional cylindrical homogenized model (RECOMMENDED)
									  # "SMFR" = Small detailed geometry model -- USE WITH CAUTION

## SERPENT MODEL OPTUONS
SerpentAxialZones      = 9    # Number of axial zones in the Serpent model [#]
SerpentOutsideDistance = 100  # Distance of coolant modeled outside of the core assembly (in all directions) [cm]

## VERSION OF SERPENT TO RUN (only 1 and 2)
SerpentVersion = 2 # Version of Serpent to run [1 or 2]

## PARALLELIZATION SETTINGS
SerpentParallelization = "off" # Run Serpent in parallell ["off" / "mpi" / "openmp"]
SerpentNodes           = 1    # Number of nodes to run 

## NEUTRON HISTORIES
SerpentCylNeutrons       = 200   # Number of neutrons [#]
SerpentCylActiveCycles   = 10    # Number of active (stored) cycles [#]
SerpentCylInactiveCycles = 20     # Number of inactive (not stored) cycles [#]

## DEPLETION SETTINGS
SerpentDepletion         = "off"      # Run depletion calculations ["on"/"off"]
SerpentDepletionSteps    = 4       # Number of depletions steps [#]
SerpentDepletionType     = "Days"    # ["Days" or "Burnup"]po
SerpentDepletionEnd      = CycleTime # Total number of days of depletion [#]
SerpentDepletionPCC      = "off"      # Predictor/corrector activated for depletion ["on"/"off"]
SerpentInventory         = ["act", "fp", "ng", "U-235","U-238","Pu-239","Pu-240",'Pu-241'] # Isotopes to track ["92238", "94239" etc.]
SerpentDepletionAccuracy = "coarse" #"nofp" #"coarse" #"medium"  # ["coarse","medium","fine"]

## ACTIVATE DPA-CALCULATION (increases computational time!) 
SerpentDPA               = "off"      # Calculate the peak cycle cladding DPA level ["on"/"off"]

## GET PREVIOUS NEUTRON DATA WITHOUT RUNNING SERPENT
GetNeutronData           = "on"

# XS-DATA PATH
#SerpentACElibpath = "/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7u_MP.xsdata"
#SerpentDEClibpath = "/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.dec"
#SerpentNFYlibpath = "/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.nfy"

# OLD PATH
#SerpentACElibpath = "/Users/SQ/Documents/XSdata/Serpent/sss_endfb7u.xsdata"
#SerpentDEClibpath = "/Users/SQ/Documents/XSdata/Serpent/sss_endfb7.dec"
#SerpentNFYlibpath = "/Users/SQ/Documents/XSdata/Serpent/sss_endfb7.nfy"

# TUTORIAL XS-DATA PATH
#SerpentACElibpath = "/mnt/scratch/serpent-tutorial/endfb7/sss_endfb7u.xsdata"
#SerpentDEClibpath = "/mnt/scratch/serpent-tutorial/endfb7/sss_endfb7.dec"
#SerpentNFYlibpath = "/mnt/scratch/serpent-tutorial/endfb7/sss_endfb7.nfy"

# BERKELIUM XS-DATA PATH /usr/local/SERPENT/xsdata/endfb7
#SerpentACElibpath =  "/usr/local/SERPENT/xsdata/endfb7/sss_endfb7u.xsdata"
#SerpentDEClibpath =  "/usr/local/SERPENT/xsdata/endfb7/sss_endfb7.dec"
#SerpentNFYlibpath =  "/usr/local/SERPENT/xsdata/endfb7/sss_endfb7.nfy"

# SAVIO XS-DATA PATH
SerpentACElibpath = "/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7u.xsdata"
SerpentDEClibpath = "/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.dec"
SerpentNFYlibpath = "/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy"

# UPPSALA XS-DATA PATH
#SerpentACElibpath =  "/TMC/TENDL2012/ACE//sss_endfb7u.xsdata"
#SerpentDEClibpath =  "/TMC/TENDL2012//sss_endfb7.dec"
#SerpentNFYlibpath =  "/TMC/TENDL2012//sss_endfb7.nfy"


################################################################################## //// ######## //// ######|
########    -- SEPRENT REACTIVITY FEEDBACK CALCULATIONS --                   ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|

ReferenceRun            = "on"
UseExistingReferenceRun = "off"
NameOfReferenceData     = "REF_REACTS"#"Depletion"

WhereInCycle = "BOC" # ["BOC", "MOC", "EOC"], EOC and MOC only works if there is already depleted fuel data!!

BUControlInsertionSimulation = "off" # ["on"/"off"]
SequentialScramRodInsertion  = "off"  # ["on"/"off"]
TotalScramRodInsertion       = "off" # ["on"/"off"]

SequentialAxialInCoreCoolantReactivity = "off" # ["on"/"off"]
SequentialAxialFuelReactivity          = "off" # ["on"/"off"]
SequentialAxialCladReactivity          = "off"  # ["on"/"off"]

RadialExpansionCoefficient    = "off"
CoolantReactivityCoefficient  = "off"  # Calculate the CORE coolant density reactivity coefficient [on/off]
FuelReactivityCoefficient     = "off"  # Calculate the fuel axial expansion reactivity coefficient [on/off]
FuelDopplerCoefficient        = "off"  # Calculate the fuel Doppler coefficient ["on"/"off"]

CladdingReactivityCoefficient = "off"  # Calculate the cladding density reactivity coefficient [on/off]
BondReactivityCoefficient     = "off"  # Calculate the bond density reactivity coefficient [on/off]
DuctReactivityCoefficient     = "off"  # Calculate the duct density reactivity coefficient [on/off]

FuelTemperaturePerturbation            = 2000 #"void" #"void" # Temperature difference to calculate fuel reactivity coefficient     [K]
CoolantTemperaturePerturbation         = 2000 #"void"#"void" #1000 # Temperature difference to calculate coolant reactivity coefficient  [K]
CladdingTemperaturePerturbation        = 2000 #"void" # Temperature difference to calculate cladding reactivity coefficient [K]

RadialExpansionTemperaturePerturbation = 2000
BondTemperaturePerturbation            = 600 # Temperature difference to calculate bond reactivity coefficient [K]
DuctTemperaturePerturbation            = 600 # Temperature difference to calculate duct reactivity coefficient [K]

TotalVoidCalculation                   = "off" # ["on"/"off"]

# Tweaking settings   
FuelExpansion = "axial" # Directions in which the fuel is allowed to expand ["axial","radial","all","none"]
DopplerTemperaturePerturbation = 900 # DO NOT CHANGE
SerpentRunOverRide = "on"

################################################################################## //// ######## //// ######|
########    -- DPA CALCULATIONS --                                           ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|

LowerGridDPA = "off"
CladdingDPA  = "off"

################################################################################## //// ######## //// ######|
########    -- DYNAMICS/TRANSIENT CALCULATIONS --                            ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|

RunDynamics = "off"

# Run settings
PumpCoastDown   = 5 # Seconds for 1/2 of coolant pressure from pumps
BreakAtPeak     = True # Break if peak temperature has been identified
PlotOutput      = False # Continously plot temperatures

# Accuracy settings
RadialResolution = 10  # Radial mesh
AxialResolution  = 51  # Axial mesh
TimeStep         = 1   # Seconds, for point-kinetics solver
TimeRefinement   = 10  # [x]/Timestep, for TH solver
MaximumTime      = 500 # Time at which calculation is stopped

################################################################################## //// ######## //// ######|
########    -- SERPENT SMFR-SETTINGS --                                      ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    These settings only apply if <SerpentCoreType = "SMFR"> on line  ##### //// ######## //// ######|  
########    234. Using the SMFR-settings can be difficult, check your input  ##### //// ######## //// ######|
########    file and plot your geometry before use!!                         ##### //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

CoreBarrelSteel             = "D9"
InsulatorMaterial           = "ZrO2"
EndCapMaterial              = "D9"
LowerGridPlateSteel         = "D9"
BottomPlateSteel            = "D9"
BottomSupportStructureSteel = "D9"

LowerGridPlateHeight = 10         # The axial height of the lower grid plate [cm]
LowerGridPlateSteelFraction = 0.3 # Fraction of the smeared lower grid plate volume that is steel

InletPlenumHeight            = 15
BottomPlateHeight            = 10
BottomSupportStructureHeight = 15

CoreLatticeElements = 19
CoreBarrelRadius = "C" #81 # ["C" or value]

## DEFINTIONS

## 0 == Empty
## 1-5, Fuel types 1-5
## 6 == Radial reflector
## 7 == Radial shield
## 8 == Burnup Control Element
## 9 == Ducted empty assembly
## 10 == SCRAM control element
## 11 == Core radial restraint system

x = 11
y = 10

CoreMap = [ \
		 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		   0,0,0,0,0,0,0,0,0,0,x,x,x,x,x,x,0,0,0,
            0,0,0,0,0,0,0,0,x,x,7,7,7,7,7,x,x,0,0,
             0,0,0,0,0,0,0,x,7,7,6,6,6,6,7,7,x,0,0,
              0,0,0,0,0,0,x,7,6,6,3,3,3,6,6,7,x,0,0,
               0,0,0,0,0,x,7,6,3,2,2,2,2,3,6,7,x,0,0,
                0,0,0,0,x,7,6,3,2,y,1,y,2,3,6,7,x,0,0,
                 0,0,0,x,7,6,3,2,1,1,1,1,2,3,6,7,x,0,0,
                  0,0,0,x,7,6,2,y,1,y,1,y,2,6,7,x,0,0,0,
                   0,0,x,7,6,3,2,1,1,1,1,2,3,6,7,x,0,0,0,
                    0,0,x,7,6,3,2,y,1,y,2,3,6,7,x,0,0,0,0,
                     0,0,x,7,6,3,2,2,2,2,3,6,7,x,0,0,0,0,0,
                      0,0,x,7,6,6,3,3,3,6,6,7,x,0,0,0,0,0,0,
                       0,0,x,7,7,6,6,6,6,7,7,x,0,0,0,0,0,0,0,
                        0,0,x,x,7,7,7,7,7,x,x,0,0,0,0,0,0,0,0,
                         0,0,0,x,x,x,x,x,x,0,0,0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                           0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#CoreMap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,11,11,11,11,11,0,0,
#             0,0,0,0,0,0,11,11,7,7,7,7,11,11,0,
#              0,0,0,0,0,11,7,6,6,6,6,6,7,11,0,
#               0,0,0,0,11,7,6,9,9,9,9,6,7,11,0,
#                0,0,0,11,7,6,9,3,3,3,9,6,7,11,0,
#                 0,0,11,7,6,9,3,2,2,3,9,6,7,11,0,
#                  0,0,11,6,9,3,2,1,2,3,9,6,11,0,0,
#                   0,11,7,6,9,3,2,2,3,9,6,7,11,0,0,
#                    0,11,7,6,9,3,3,3,9,6,7,11,0,0,0,
#                     0,11,7,6,9,9,9,9,6,7,11,0,0,0,0,
#                      0,11,7,6,6,6,6,6,7,11,0,0,0,0,0,
#                       0,11,11,7,7,7,7,11,11,0,0,0,0,0,0,
#                        0,0,11,11,11,11,11,0,0,0,0,0,0,0,0,
#                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                         

#CoreMap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,11,11,11,11,11,0,0,
#             0,0,0,0,0,0,11,11,7,7,7,7,11,11,0,
#              0,0,0,0,0,11,7,6,6,6,6,6,7,11,0,
#               0,0,0,0,11,7,6,3,3,3,3,6,7,11,0,
#                0,0,0,11,7,6,3,9,2,9,3,6,7,11,0,
#                 0,0,11,7,6,3,2,1,1,2,3,6,7,11,0,
#                  0,0,11,6,3,9,1,9,1,9,3,6,11,0,0,
#                   0,11,7,6,3,2,1,1,2,3,6,7,11,0,0,
#                    0,11,7,6,3,9,2,9,3,6,7,11,0,0,0,
#                     0,11,7,6,3,3,3,3,6,7,11,0,0,0,0,
#                      0,11,7,6,6,6,6,6,7,11,0,0,0,0,0,
#                       0,11,11,7,7,7,7,11,11,0,0,0,0,0,0,
#                        0,0,11,11,11,11,11,0,0,0,0,0,0,0,0,
#                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

################################################################################## //// ######## //// ######|
########    -- EDIS RUN-SETTINGS --                                          ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    EDIS is a shuffling tool for Serpent. It will move material      ##### //// ######## //// ######|  
########    around in the core using a scheme specified by "shufflescheme".  ##### //// ######## //// ######|
########    Activating EDIS automatically de-activates all ADOPT-SERPENT     ##### //// ######## //// ######|
########    settings.                                                        ##### //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    Make sure the under "CORE FUEL DISTRIBUTION" (line 154-157)      ##### //// ######## //// ######|
########    match the settings for "schufflescheme" (!!)                     ##### //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

## ACTIVATE EDIS RUN 
EDIS = "on" # "on"/"off"

## SHUFFLING PATH -- (Example: 16-15-14-13-12-1-5-11-2-6-10-9-3-4-8-7)

# 3D-SWR-1

#shufflescheme = \
#{'Batch8Axial3':'Batch8Axial1','Batch8Axial1':'Batch8Axial2',  # 8 Outer radial batch axial shuffle
# 'Batch8Axial2':'Batch7Axial3','Batch7Axial3':'Batch7Axial1','Batch7Axial1':'Batch7Axial2',  # 7
# 'Batch7Axial2':'Batch1Axial3','Batch1Axial3':'Batch1Axial1','Batch1Axial1':'Batch1Axial2',  # 1
# 'Batch1Axial2':'Batch6Axial3','Batch6Axial3':'Batch6Axial1','Batch6Axial1':'Batch6Axial2',  # 6
# 'Batch6Axial2':'Batch2Axial3','Batch2Axial3':'Batch2Axial1','Batch2Axial1':'Batch2Axial2',  # 2
# 'Batch2Axial2':'Batch5Axial3','Batch5Axial3':'Batch5Axial1','Batch5Axial1':'Batch5Axial2',  # 5
# 'Batch5Axial2':'Batch3Axial3','Batch3Axial3':'Batch3Axial1','Batch3Axial1':'Batch3Axial2',  # 3
# 'Batch3Axial2':'Batch4Axial3','Batch4Axial3':'Batch4Axial1','Batch4Axial1':'Batch4Axial2'}  # 4

# 3D-SWR-2

#shufflescheme = \
#{'Batch8Axial3':'Batch8Axial1','Batch8Axial1':'Batch8Axial2',  # 8 Outer radial batch axial shuffle
# 'Batch8Axial2':'Batch7Axial3','Batch7Axial3':'Batch7Axial1','Batch7Axial1':'Batch7Axial2',  # 7
# 'Batch7Axial2':'Batch6Axial3','Batch6Axial3':'Batch6Axial1','Batch6Axial1':'Batch6Axial2',  # 6
# 'Batch6Axial2':'Batch1Axial3','Batch1Axial3':'Batch1Axial1','Batch1Axial1':'Batch1Axial2',  # 1
# 'Batch1Axial2':'Batch5Axial3','Batch5Axial3':'Batch5Axial1','Batch5Axial1':'Batch5Axial2',  # 5
# 'Batch5Axial2':'Batch2Axial3','Batch2Axial3':'Batch2Axial1','Batch2Axial1':'Batch2Axial2',  # 2
# 'Batch2Axial2':'Batch4Axial3','Batch4Axial3':'Batch4Axial1','Batch4Axial1':'Batch4Axial2',  # 4
# 'Batch4Axial2':'Batch3Axial3','Batch3Axial3':'Batch3Axial1','Batch3Axial1':'Batch3Axial2'}  # 3

# 3D-SWR-3 (From Florent) 12-11-10-9-8-1-7-6-2-3-4-5

#shufflescheme = \
#{'Batch12Axial3':'Batch12Axial1','Batch12Axial1':'Batch12Axial2',                                 # 12
# 'Batch12Axial2':'Batch11Axial3','Batch11Axial3':'Batch11Axial1','Batch11Axial1':'Batch11Axial2', # 11
# 'Batch11Axial2':'Batch10Axial3','Batch10Axial3':'Batch10Axial1','Batch10Axial1':'Batch10Axial2', # 10
# 'Batch10Axial2':'Batch9Axial3','Batch9Axial3':'Batch9Axial1','Batch9Axial1':'Batch9Axial2',      # 9
# 'Batch9Axial2':'Batch8Axial3','Batch8Axial3':'Batch8Axial1','Batch8Axial1':'Batch8Axial2',       # 8
# 'Batch8Axial2':'Batch1Axial3','Batch1Axial3':'Batch1Axial1','Batch1Axial1':'Batch1Axial2',       # 1
# 'Batch1Axial2':'Batch7Axial3','Batch7Axial3':'Batch7Axial1','Batch7Axial1':'Batch7Axial2',       # 7
# 'Batch7Axial2':'Batch6Axial3','Batch6Axial3':'Batch6Axial1','Batch6Axial1':'Batch6Axial2',       # 6
# 'Batch6Axial2':'Batch2Axial3','Batch2Axial3':'Batch2Axial1','Batch2Axial1':'Batch2Axial2',       # 2
# 'Batch2Axial2':'Batch3Axial3','Batch3Axial3':'Batch3Axial1','Batch3Axial1':'Batch3Axial2',       # 3
# 'Batch3Axial2':'Batch4Axial3','Batch4Axial3':'Batch4Axial1','Batch4Axial1':'Batch4Axial2',       # 4
# 'Batch4Axial2':'Batch5Axial3','Batch5Axial3':'Batch5Axial1','Batch5Axial1':'Batch5Axial2'}       # 5

# 2D-SWR-3 (From Florent) 12-11-10-9-8-1-7-6-2-3-4-5

shufflescheme = \
{'Batch12Axial1':'Batch11Axial1','Batch11Axial1':'Batch10Axial1','Batch10Axial1':'Batch9Axial1','Batch9Axial1':'Batch8Axial1','Batch8Axial1':'Batch1Axial1','Batch1Axial1':'Batch7Axial1','Batch7Axial1':'Batch6Axial1','Batch6Axial1':'Batch2Axial1','Batch2Axial1':'Batch3Axial1','Batch3Axial1':'Batch4Axial1','Batch4Axial1':'Batch5Axial1',
 'Batch12Axial2':'Batch11Axial2','Batch11Axial2':'Batch10Axial2','Batch10Axial2':'Batch9Axial2','Batch9Axial2':'Batch8Axial2','Batch8Axial2':'Batch1Axial2','Batch1Axial2':'Batch7Axial2','Batch7Axial2':'Batch6Axial2','Batch6Axial2':'Batch2Axial2','Batch2Axial2':'Batch3Axial2','Batch3Axial2':'Batch4Axial2','Batch4Axial2':'Batch5Axial2',
 'Batch12Axial3':'Batch11Axial3','Batch11Axial3':'Batch10Axial3','Batch10Axial3':'Batch9Axial3','Batch9Axial3':'Batch8Axial3','Batch8Axial3':'Batch1Axial3','Batch1Axial3':'Batch7Axial3','Batch7Axial3':'Batch6Axial3','Batch6Axial3':'Batch2Axial3','Batch2Axial3':'Batch3Axial3','Batch3Axial3':'Batch4Axial3','Batch4Axial3':'Batch5Axial3',      
 'Batch12Axial4':'Batch11Axial4','Batch11Axial4':'Batch10Axial4','Batch10Axial4':'Batch9Axial4','Batch9Axial4':'Batch8Axial4','Batch8Axial4':'Batch1Axial4','Batch1Axial4':'Batch7Axial4','Batch7Axial4':'Batch6Axial4','Batch6Axial4':'Batch2Axial4','Batch2Axial4':'Batch3Axial4','Batch3Axial4':'Batch4Axial4','Batch4Axial4':'Batch5Axial4',       
 'Batch12Axial5':'Batch11Axial5','Batch11Axial5':'Batch10Axial5','Batch10Axial5':'Batch9Axial5','Batch9Axial5':'Batch8Axial5','Batch8Axial5':'Batch1Axial5','Batch1Axial5':'Batch7Axial5','Batch7Axial5':'Batch6Axial5','Batch6Axial5':'Batch2Axial5','Batch2Axial5':'Batch3Axial5','Batch3Axial5':'Batch4Axial5','Batch4Axial5':'Batch5Axial5',      
 'Batch12Axial6':'Batch11Axial6','Batch11Axial6':'Batch10Axial6','Batch10Axial6':'Batch9Axial6','Batch9Axial6':'Batch8Axial6','Batch8Axial6':'Batch1Axial6','Batch1Axial6':'Batch7Axial6','Batch7Axial6':'Batch6Axial6','Batch6Axial6':'Batch2Axial6','Batch2Axial6':'Batch3Axial6','Batch3Axial6':'Batch4Axial6','Batch4Axial6':'Batch5Axial6',
 'Batch12Axial7':'Batch11Axial7','Batch11Axial7':'Batch10Axial7','Batch10Axial7':'Batch9Axial7','Batch9Axial7':'Batch8Axial7','Batch8Axial7':'Batch1Axial7','Batch1Axial7':'Batch7Axial7','Batch7Axial7':'Batch6Axial7','Batch6Axial7':'Batch2Axial7','Batch2Axial7':'Batch3Axial7','Batch3Axial7':'Batch4Axial7','Batch4Axial7':'Batch5Axial7',
 'Batch12Axial8':'Batch11Axial8','Batch11Axial8':'Batch10Axial8','Batch10Axial8':'Batch9Axial8','Batch9Axial8':'Batch8Axial8','Batch8Axial8':'Batch1Axial8','Batch1Axial8':'Batch7Axial8','Batch7Axial8':'Batch6Axial8','Batch6Axial8':'Batch2Axial8','Batch2Axial8':'Batch3Axial8','Batch3Axial8':'Batch4Axial8','Batch4Axial8':'Batch5Axial8',      
 'Batch12Axial9':'Batch11Axial9','Batch11Axial9':'Batch10Axial9','Batch10Axial9':'Batch9Axial9','Batch9Axial9':'Batch8Axial9','Batch8Axial9':'Batch1Axial9','Batch1Axial9':'Batch7Axial9','Batch7Axial9':'Batch6Axial9','Batch6Axial9':'Batch2Axial9','Batch2Axial9':'Batch3Axial9','Batch3Axial9':'Batch4Axial9','Batch4Axial9':'Batch5Axial9'}

# shufflescheme = \
# {'Batch3Axial3':'Batch3Axial1','Batch3Axial1':'Batch3Axial2',                                     # 3
#  'Batch3Axial2':'Batch2Axial3','Batch2Axial3':'Batch2Axial1','Batch2Axial1':'Batch2Axial2',       # 2
#  'Batch2Axial2':'Batch1Axial3','Batch1Axial3':'Batch1Axial1','Batch1Axial1':'Batch1Axial2'}       # 1

# 3D-SWR Out-to-in

#shufflescheme = \
#{'Batch16Axial3':'Batch16Axial1','Batch16Axial1':'Batch16Axial2',                                 # 16
# 'Batch16Axial2':'Batch15Axial3','Batch15Axial3':'Batch15Axial1','Batch15Axial1':'Batch15Axial2', # 15
# 'Batch15Axial2':'Batch14Axial3','Batch14Axial3':'Batch14Axial1','Batch14Axial1':'Batch14Axial2', # 14
# 'Batch14Axial2':'Batch13Axial3','Batch13Axial3':'Batch13Axial1','Batch13Axial1':'Batch13Axial2', # 13
# 'Batch13Axial2':'Batch12Axial3','Batch12Axial3':'Batch12Axial1','Batch12Axial1':'Batch12Axial2', # 12
# 'Batch12Axial2':'Batch11Axial3','Batch11Axial3':'Batch11Axial1','Batch11Axial1':'Batch11Axial2', # 11
# 'Batch11Axial2':'Batch10Axial3','Batch10Axial3':'Batch10Axial1','Batch10Axial1':'Batch10Axial2', # 10
# 'Batch10Axial2':'Batch9Axial3','Batch9Axial3':'Batch9Axial1','Batch9Axial1':'Batch9Axial2',      # 9
# 'Batch9Axial2':'Batch8Axial3','Batch8Axial3':'Batch8Axial1','Batch8Axial1':'Batch8Axial2',       # 8
# 'Batch8Axial2':'Batch7Axial3','Batch7Axial3':'Batch7Axial1','Batch7Axial1':'Batch7Axial2',       # 7
# 'Batch7Axial2':'Batch6Axial3','Batch6Axial3':'Batch6Axial1','Batch6Axial1':'Batch6Axial2',       # 6
# 'Batch6Axial2':'Batch5Axial3','Batch5Axial3':'Batch5Axial1','Batch5Axial1':'Batch5Axial2',       # 5
# 'Batch5Axial2':'Batch4Axial3','Batch4Axial3':'Batch4Axial1','Batch4Axial1':'Batch4Axial2',       # 4
# 'Batch4Axial2':'Batch3Axial3','Batch3Axial3':'Batch3Axial1','Batch3Axial1':'Batch3Axial2',       # 3
# 'Batch3Axial2':'Batch2Axial3','Batch2Axial3':'Batch2Axial1','Batch2Axial1':'Batch2Axial2',       # 2
# 'Batch2Axial2':'Batch1Axial3','Batch1Axial3':'Batch1Axial1','Batch1Axial1':'Batch1Axial2'}       # 1

## CYCLE SETTINGS
eqcycle_busteps         = 3          # The number of burnup-steps within each eq. cycle
eqcycle_shufflingoutage = 1          # Days the reactor is shutdown for shuffling operations

## EDIS STAGE-1 NEUTRON HISTORY SETTINGS
stage1_neutrons       = 2000          # Number of neutrons per cycle
stage1_activecycles   = 420           # Number of cycles stored
stage1_inactivecycles = 30            # Number of cycles discarded
stage1_iterations     = 40            # Maximum number of iterations in STAGE-1 (recommended: x > Batches)

## EDIS STAGE-2 NEUTRON HISTORY SETTINGS
stage2_neutrons       = 5000         # Number of neutrons per cycle
stage2_activecycles   = 520          # Number of cycles stored
stage2_inactivecycles = 30           # Number of cycles discarded

# EDIS-SERPENT PARALELLIZATION
mpi          = "off"   # Run EDIS-Serpent in parallel MPI-mode
nodes        = 1       # The number of nodes if running in MPI-mode

## DPA SETTINGS
DPA        = "off" # ["on" / "off"]
Material   = "HT9" # Material for which DPA is calculated

## CRITICAL CYCLE SEARCH SETTINGS
criticality        = "on"    # Attempts to find a critical cycle by changing the cycle length ("on" or "off")
eqcycle_kefftarget = 1.03    # The target keff for criticality search (almost always 1.00 + x)

## EDIS CONVERGENCE SETTINGS
keff_convergence = 0.005        # The relative difference in IMP_KEFF between two subsequent serpent runs
mat_convergence  = 0.01         # The relative difference in atomic density between two subsequent serpent runs
iter_convergence = 6 * Batches  # Maximum amount of iterations before breaking eq. cycle search
isotope_checks   = ["U-238"]    # Isotopes to check for material convergence
initialmaxdiff   = 1            # The maximum difference between in k_eff between as given with your initial guess
				                # for cycle time and your target k_keff (recommended value = 10-20% = 0.1-0.2)
printconvergence = 1            # Print material convergence data

## INFERRED SETTINGS (mostly given by previous input, but can be adjusted for EDIS)
eqcycle_days    = CycleTime  # The number of days between shuffling operations
eqcycle_batches = Batches #* SerpentAxialZones   # The number of batches to be shuffled
filename        = Name
version         = SerpentVersion
AxialZones      = SerpentAxialZones
sss1filename    = "sss"   # The registered name for the Serpent 1 exectuable
sss2filename    = "sss2"  # The registered name for the Serpent 2 exectuable

################################################################################## //// ######## //// ######|
########    -- OUTPUT OPTIONS --                                             ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|

## ADOPT PLOTTING SETTINGS
Plotting = "off" # Plots temperatures and coolant properties using MATPLOTLIB ["on/off"]

## SERPENT PLOTTING SETTINGS
SerpentCylPlotting   = "off"  # Plot the cylindrical model using Serpent ["on"/"off"]
SerpentPlotting      = "off"  # Plot fuel, reflector and shield assembly geometry using Serpent ["on"/"off"]
SerpentSMFRPlotting  = "on"  # Plot the SMFR model using Serpent ["on"/"off"]
PlotPixels = 15000

################################################################################## //// ######## //// ######|
########    -- CONVERGENCE CRITERIA --                                       ##### //// ######## //// ######|
################################################################################## //// ######## //// ######|
########                                                                     ##### //// ######## //// ######|
########    These settings strongly affect the calculation time!             ##### //// ######## //// ######|  
########                                                                     ##### //// ######## //// ######|
################################################################################## //// ######## //// ######| 

## ADOPT INNER CONVERGENCE
FTF_Convergence         = 1e-4    # Convergence for the distance, inner flat-to-flat of the assembly [cm]
FlowConvergence         = 1e-5    # Relative convergence criteria for the flow distribution [#]
TemperatureConvergence  = 0.05    # Temperature error in Kelvin for the convergence of conductivities [K]
AxialTemperaturePoints  = 500    # Number of axial points that calculations are made at (recommended: 100-1000) [#]
VelocityPrecision       = 1e-3    # Velocity adjustments (recommended: 0.01 - 0.001) [m/s]
MinimumIterations       = 5       # Minimum number of ADOPT solver iterations (recommended > 5)

## SERPENT CONVERGENCE
PowerCorrection      = "off" # Choose whether to find a converged power distribution or not ["on" / "off"]
PowerPeakConvergence = 0.01 # Relative convergence criteria for the radial and axial power peaking factors [#]
