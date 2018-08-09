import math

def pininformation(FuelPinRows,Assemblies,FuelLength,Power,RadialPowerPeaking,PinAxialPowerPeaking, EdgePinPowerPeaking, CornerPinPowerPeaking):

	# Total number of fuel pins per assembly (#)
	PinsPerAssembly = 3*(FuelPinRows+1)*(FuelPinRows)+1
	
	# Total number of fuel pins in the core (#)
	TotalFuelPins   = Assemblies * PinsPerAssembly
	
	# Total length of fuel in the entire core (m)
	TotalFuelLength = TotalFuelPins * FuelLength
	
	# Total volume-integrated power produced by an average core pin (W)
	AveragePinPower = Power / TotalFuelPins  
	
	#print(RadialPowerPeaking)

	# Total volume-integrated power produced by the peak pin in the core (W)
	PeakPinPower    = RadialPowerPeaking * Power / TotalFuelPins  

	#print("CALC PEAK")
	#print(PeakPinPower)

	# Volume-integrated power produced by an edge pin in peak power assembly in the core (W)
	EdgePinPower    = EdgePinPowerPeaking * Power / TotalFuelPins

	# Volume-integrated power produced by a corner pin in peak power assembly in the core (W)
	CornerPinPower  = CornerPinPowerPeaking * Power / TotalFuelPins	
	
	# Average linear power in the core in W/m
	AveragePinAverageLinearPower = Power/TotalFuelLength 
	
	# Peak axial linear power of an average power pin in the core in W/m
	AveragePinPeakLinearPower    = Power * PinAxialPowerPeaking / TotalFuelLength
	
	# Axially averaged linear power of the peak power pin in the core in W/m
	PeakPinAverageLinearPower    = Power * RadialPowerPeaking / TotalFuelLength

	# Axially averaged linear power of an edge pin in peak power assembly in the core W/m
	EdgePinAverageLinearPower    = Power * EdgePinPowerPeaking / TotalFuelLength

	# Axially averaged linear power of a corner pin in peak power assembly in the core W/m
	CornerPinAverageLinearPower  = Power * CornerPinPowerPeaking / TotalFuelLength
	
	# Peak linear power of the peak power pin in the core in W/m
	PeakPinPeakLinearPower       = Power * RadialPowerPeaking * PinAxialPowerPeaking / TotalFuelLength

	# Peak linear power of an edge pin in peak power assembly in the core W/m
	EdgePinPeakLinearPower       = Power * EdgePinPowerPeaking * PinAxialPowerPeaking / TotalFuelLength

	# Peak linear power of an edge pin in peak power assembly in the core W/m
	CornerPinPeakLinearPower     = Power * CornerPinPowerPeaking * PinAxialPowerPeaking / TotalFuelLength

	return(PinsPerAssembly,TotalFuelPins,TotalFuelLength,AveragePinPower,PeakPinPower,AveragePinAverageLinearPower, \
		   AveragePinPeakLinearPower,PeakPinAverageLinearPower,PeakPinPeakLinearPower, EdgePinAverageLinearPower, \
		   EdgePinPeakLinearPower, CornerPinAverageLinearPower, CornerPinPeakLinearPower, EdgePinPower, CornerPinPower)

def assemblyinformation(FTF,DuctThickness,InterAssemblyGap, RadialReflectorRows, RadialShieldRows, Assemblies):
	
	# The hexagon side length of the assembly inner duct/wrapper wall
	InnerAssemblySideLength = FTF/math.sqrt(3)
	
	# The flat-to-flat distance between to outside duct/wrapper walls
	DuctedAssemblyFTF = FTF + 2 * DuctThickness/10
	
	# The hexagon side length of the outside duct wall
	DuctedAssemblySideLength = DuctedAssemblyFTF/math.sqrt(3)
	
	# The flat-to-flat distance of the ducted fuel assembly + the interassembly gap (per assembly)
	AssemblyHexagonFTF = DuctedAssemblyFTF + 2 * InterAssemblyGap/10
	
	# The hexagonal side length of a unit fuel assembly + interassembly gap (per assembly)
	AssemblyHexagonSideLength = AssemblyHexagonFTF/math.sqrt(3)
	
	# The distance between the centers of two adjacent fuel assemblies
	AssemblyPitch = AssemblyHexagonSideLength * 2	

	InnerAssemblyArea = (math.sqrt(3) / 2) * ((FTF/100) ** 2)

	DuctedAssemblyArea = (math.sqrt(3) / 2) * ((DuctedAssemblyFTF/100) ** 2)

	TotalAssemblyArea = (math.sqrt(3) / 2) * ((AssemblyHexagonFTF/100) ** 2)

	TotalCoreArea = Assemblies * TotalAssemblyArea

	CoreDiameter = 2 * math.sqrt(math.pi * TotalCoreArea) / math.pi

	SystemDiameter = CoreDiameter + (AssemblyPitch/100) * (2*RadialReflectorRows + 2*RadialShieldRows)

	return(InnerAssemblySideLength,DuctedAssemblyFTF,DuctedAssemblySideLength,AssemblyHexagonFTF, \
		   AssemblyHexagonSideLength, AssemblyPitch, TotalAssemblyArea, InnerAssemblyArea, \
		   DuctedAssemblyArea, TotalAssemblyArea, CoreDiameter, SystemDiameter, TotalCoreArea)

def geomsubchannels(FuelPinRows, Assemblies, LowerEndCapLength, LowerShieldLength, LowerReflectorLength, LowerGasPlenumLength,      
                    LowerInsulatorPelletLength, FuelLength, UpperInsulatorPelletLength, UpperGasPlenumLength, UpperReflectorLength,    
					UpperShieldLength, UpperEndCapLength):

	# Number of internal hexagonal sub-channels per assembly
	InteriorChannelsPerAssembly = 6 * FuelPinRows ** 2
	
	# Number of edge hexagonal sub-channels per assembly
	EdgeChannelsPerAssembly     = 6 * FuelPinRows
	
	# Number of corner hexagonal sub-channels per assembly (always 6)
	CornerChannelsPerAssembly   = 6

	ChannelsPerAssembly = InteriorChannelsPerAssembly + EdgeChannelsPerAssembly + CornerChannelsPerAssembly
	
	# Summed subchannels in the core
	CoreInteriorChannels        = InteriorChannelsPerAssembly * Assemblies
	CoreEdgeChannels            = EdgeChannelsPerAssembly * Assemblies
	CoreCornerChannels          = CornerChannelsPerAssembly * Assemblies
	CoreTotalChannels           = CoreInteriorChannels + CoreEdgeChannels + CoreCornerChannels 
	
	# Total length of the flow channel below the core
	BelowCoreChannelLength = LowerEndCapLength + LowerShieldLength + LowerReflectorLength + LowerGasPlenumLength + LowerInsulatorPelletLength
	
	# Total length of the flow channel below the core
	AboveCoreChannelLength = UpperInsulatorPelletLength + UpperGasPlenumLength + UpperReflectorLength + UpperShieldLength + UpperEndCapLength


	return(InteriorChannelsPerAssembly,EdgeChannelsPerAssembly,CornerChannelsPerAssembly,CoreInteriorChannels, \
		   CoreEdgeChannels,CoreCornerChannels,CoreTotalChannels,BelowCoreChannelLength, AboveCoreChannelLength, \
		   ChannelsPerAssembly)	