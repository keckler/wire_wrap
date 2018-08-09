import math

def volumefraction(FTF, Pitch, Diameter, PinsPerAssembly, FreshFuelRadius, CladdingThickness, GapOuterRadius, TotalAssemblyArea,
	               AssemblyFlowArea, GapInnerRadius, InnerAssemblyArea, DuctedAssemblyArea, InternalControlAssemblies, Assemblies):

	FuelArea           = math.pi * PinsPerAssembly * (FreshFuelRadius ** 2) 
	GapArea            = math.pi * PinsPerAssembly * (GapOuterRadius ** 2)  - math.pi * PinsPerAssembly * GapInnerRadius ** 2 
	CladdingArea       = math.pi * PinsPerAssembly * ((Diameter/2) ** 2)    - math.pi * PinsPerAssembly * GapOuterRadius ** 2 
	ActiveCoolantArea  = AssemblyFlowArea
	DuctArea           = DuctedAssemblyArea - InnerAssemblyArea
	InterAssemblyArea  = TotalAssemblyArea  - DuctedAssemblyArea

	RodArea = math.pi * PinsPerAssembly * ((Diameter/2) ** 2) 

	FAFuelVolumeFraction          = FuelArea          / TotalAssemblyArea
	FAGapVolumeFraction           = GapArea           / TotalAssemblyArea
	FACladdingVolumeFraction      = CladdingArea      / TotalAssemblyArea
	FAActiveCoolantVolumeFraction = ActiveCoolantArea / TotalAssemblyArea
	FADuctVolumeFraction          = DuctArea          / TotalAssemblyArea
	FAInterAssemblyVolumeFraction = InterAssemblyArea / TotalAssemblyArea
	FATotCheck                    = FAFuelVolumeFraction + FACladdingVolumeFraction + FAGapVolumeFraction + FAActiveCoolantVolumeFraction + FADuctVolumeFraction + FAInterAssemblyVolumeFraction
	FAWireVolumeFraction          = 1-FATotCheck
	FACladdingAndWireVolumeFraction = FACladdingVolumeFraction + FAWireVolumeFraction

	ControlFraction = InternalControlAssemblies / (Assemblies + InternalControlAssemblies)
	TotalAssemblyAreaX = TotalAssemblyArea * (1+ ControlFraction)
	ExtraArea = TotalAssemblyAreaX - TotalAssemblyArea

	FuelVolumeFraction          = FuelArea          / TotalAssemblyAreaX
	GapVolumeFraction           = GapArea           / TotalAssemblyAreaX
	CladdingVolumeFraction      = CladdingArea      / TotalAssemblyAreaX

	DuctAreaX          = DuctArea          + ExtraArea * (DuctArea          / (DuctArea + InterAssemblyArea + ActiveCoolantArea))
	InterAssemblyAreaX = InterAssemblyArea + ExtraArea * (InterAssemblyArea / (DuctArea + InterAssemblyArea + ActiveCoolantArea))
	ActiveCoolantAreaX = ActiveCoolantArea + ExtraArea * (ActiveCoolantArea / (DuctArea + InterAssemblyArea + ActiveCoolantArea))

	InterAssemblyVolumeFraction = InterAssemblyAreaX / TotalAssemblyAreaX
	ActiveCoolantVolumeFraction = ActiveCoolantAreaX / TotalAssemblyAreaX
	DuctVolumeFraction          = DuctAreaX          / TotalAssemblyAreaX

	TotCheck                      = FuelVolumeFraction + CladdingVolumeFraction + GapVolumeFraction + ActiveCoolantVolumeFraction + DuctVolumeFraction + InterAssemblyVolumeFraction
	WireVolumeFraction            = 1-TotCheck
	CladdingAndWireVolumeFraction = CladdingVolumeFraction + WireVolumeFraction	

	# Initial value of the combined volume fraction of cladding and wire
	EquivalentCladdingVolumeFraction = CladdingVolumeFraction
	EquivalentCladdingRadius         = (Diameter/2)

	while EquivalentCladdingVolumeFraction < CladdingAndWireVolumeFraction:

		EquivalentCladdingRadius        += 1e-5
		EquivalentCladdingArea           = math.pi * PinsPerAssembly * ((EquivalentCladdingRadius) ** 2)    - math.pi * PinsPerAssembly * GapOuterRadius ** 2 
		EquivalentCladdingVolumeFraction = EquivalentCladdingArea / TotalAssemblyArea

	return(FuelVolumeFraction,GapVolumeFraction,CladdingVolumeFraction,ActiveCoolantVolumeFraction, DuctVolumeFraction, \
		   InterAssemblyVolumeFraction,WireVolumeFraction, EquivalentCladdingRadius)

def SMFRmasses(SerpentPerturbedAxialFuelDensity, FuelStep0, CoreBarrelRadius0, FuelVolumeFraction, GapVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction,
			   ActiveCoolantVolumeFraction, CladdingVolumeFraction, WireVolumeFraction, RelColDensDiff, SerpentAxialZones, FuelLength,
			   RelFuelDensDiff, Name, SerpentAxialCoolantDensity, SerpentPerturbedAxialCoolantDensity, SerpentAxialFuelDensity, RelCladDensDiff,
			   SerpentAxialCladdingDensity, SerpentPerturbedAxialCladdingDensity, FueledRadius, SequentialAxialFuelReactivity, SequentialAxialCladReactivity, SequentialAxialInCoreCoolantReactivity,
			   AssemblyHexagonSideLength, Assemblies, GridPlateVolume, InletPlenumVolume, LowerGridPlateSteelFraction, LowerEndCapLength, LowerShieldLength,
			   LowerReflectorLength, LowerGasPlenumLength, LowerInsulatorPelletLength, UpperEndCapLength, UpperShieldLength, UpperReflectorLength, UpperGasPlenumLength, UpperInsulatorPelletLength,
			   GridPlateCellDensity, GridPlateCellDensity_perturbed, LowerPlenumCoolantDensityDifference, UpperPlenumCoolantDensityDifference):

	solq = open("results/" + Name + "/SAS_Neutronics.txt", 'a')

	FuelStep0             = 100 * FuelLength / SerpentAxialZones
	ActiveZoneArea        = Assemblies * (3 * math.sqrt(3) / 2) * ((AssemblyHexagonSideLength/100) ** 2) # m^2
	TotalActiveZoneVolume = ActiveZoneArea * FuelLength
	ActiveZoneVolume      = ActiveZoneArea * FuelLength / SerpentAxialZones

	TotalCoolantSectionVolume = (ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction) * TotalActiveZoneVolume
	TotalFuelSectionVolume    = FuelVolumeFraction     * TotalActiveZoneVolume 
	TotalCladSectionVolume    = CladdingVolumeFraction * TotalActiveZoneVolume
	TotalDuctSectionVolume    = DuctVolumeFraction     * TotalActiveZoneVolume

	CoolantSectionVolume = (ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction) * ActiveZoneVolume
	FuelSectionVolume    = FuelVolumeFraction     * ActiveZoneVolume 
	CladSectionVolume    = CladdingVolumeFraction * ActiveZoneVolume
	DuctSectionVolume    = DuctVolumeFraction     * ActiveZoneVolume

	A0 = "The total active core volume is:          {0:02.2f}".format(TotalActiveZoneVolume)     + " m^3 \n"
	A1 = "The total active core coolant volume is:  {0:02.2f}".format(TotalCoolantSectionVolume) + " m^3 \n"
	A2 = "The total active core fuel volume is:     {0:02.2f}".format(TotalFuelSectionVolume)    + " m^3 \n"
	A3 = "The total active core cladding volume is: {0:02.2f}".format(TotalCladSectionVolume)    + " m^3 \n"
	A4 = "The total active core duct volume is:     {0:02.2f}".format(TotalDuctSectionVolume)    + " m^3 \n"

	A = "The axially sequential total active core zone volume is: {0:02.2f}".format(ActiveZoneVolume)     + " m^3 \n"
	B = "The volume of coolant per sequential axial zone is:      {0:02.2f}".format(CoolantSectionVolume) + " m^3 \n"
	C = "The volume of fuel per sequential axial zone is:         {0:02.2f}".format(FuelSectionVolume)    + " m^3 \n"
	D = "The volume of cladding per sequential axial zone is:     {0:02.2f}".format(CladSectionVolume)    + " m^3 \n"
	E = "The volume of duct per sequential axial zone is:         {0:02.2f}".format(DuctSectionVolume)    + " m^3 \n"

	solq.write(A0)
	solq.write(A1)
	solq.write(A2)
	solq.write(A3)
	solq.write(A4)	
	solq.write("\n")			
	solq.write(A)
	solq.write(B)
	solq.write(C)
	solq.write(D)
	solq.write(E)	
	solq.write("\n")

	BelowCoreChannelLength           = (LowerEndCapLength + LowerShieldLength + LowerReflectorLength + LowerGasPlenumLength + LowerInsulatorPelletLength)
	BelowCoreInAssemblyCoolantVolume = (ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction) * ActiveZoneArea * BelowCoreChannelLength

	GridPlateCoolantVolume   = (1-LowerGridPlateSteelFraction) * GridPlateVolume/(100**3)
	InletPlenumCoolantVolume = InletPlenumVolume/(100**3)

	TotalBelowCoreVolume = BelowCoreInAssemblyCoolantVolume + GridPlateCoolantVolume + InletPlenumCoolantVolume

	GridPlateMassDifference           = ((GridPlateVolume) * (GridPlateCellDensity - GridPlateCellDensity_perturbed))/1000 # kg
	BelowCoreInAssemblyMassDifference = ((BelowCoreInAssemblyCoolantVolume * 100**3) * LowerPlenumCoolantDensityDifference)/1000 # m^3 * g/cm^3
	InletPlenumMassDifference         = ((InletPlenumCoolantVolume * 100**3) * LowerPlenumCoolantDensityDifference)/1000

	BelowCoreCoolantMassDifference = GridPlateMassDifference + BelowCoreInAssemblyMassDifference + InletPlenumMassDifference

	E1 = "The coolant volume in the fuel assembly below the core is:      {0:02.2f}".format(BelowCoreInAssemblyCoolantVolume) + " m^3 \n"
	E2 = "The coolant volume in the grid plate is:                        {0:02.2f}".format(GridPlateCoolantVolume)           + " m^3 \n"
	E3 = "The coolant volume in the inlet plenum is:                      {0:02.2f}".format(InletPlenumCoolantVolume)         + " m^3 \n"
	E4 = "The total volume of coolant in the below-core zones is:         {0:02.2f}".format(TotalBelowCoreVolume)             + " m^3 \n"
	E5 = "The total mass of removed coolant from the below-core zones is: {0:02.0f}".format(BelowCoreCoolantMassDifference)   + " kg \n"

	AboveCoreChannelLength           = (UpperEndCapLength + UpperShieldLength + UpperReflectorLength + UpperGasPlenumLength + UpperInsulatorPelletLength)
	AboveCoreInAssemblyCoolantVolume = (ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction) * ActiveZoneArea * AboveCoreChannelLength
	AboveCoreCoolantMassDifference   = ((AboveCoreInAssemblyCoolantVolume * 100**3) * UpperPlenumCoolantDensityDifference)/1000 # m^3 * g/cm^3

	F1 = "The coolant volume in the fuel assembly above the core is:      {0:02.2f}".format(AboveCoreInAssemblyCoolantVolume) + " m^3 \n"
	F2 = "The total mass of removed coolant from the above-core zones is: {0:02.0f}".format(AboveCoreCoolantMassDifference)   + " kg \n"	

	if SequentialAxialInCoreCoolantReactivity == "on":

		solq.write(E1)
		solq.write(E2)
		solq.write(E3)
		solq.write(E4)
		solq.write(E5)	
		solq.write("\n")
	
		solq.write(F1)
		solq.write(F2)
		solq.write("\n")

	ColMassDiff  = []
	FuelMassDiff = []
	CladMassDiff = []

	if SequentialAxialInCoreCoolantReactivity == "on":

		solq.write("In-core coolant perturbation information: \n")
		solq.write("\n")
	
		for z in range(SerpentAxialZones):

			CoolantMassDifference = RelColDensDiff[z] * 1000 * CoolantSectionVolume
			ColMassDiff.append(CoolantMassDifference)
	
			A = "Axial zone " + str(z+1) + "/" + str(SerpentAxialZones) + " \n"
			B = "Operating condition coolant density:  {0:02.2f}".format(SerpentAxialCoolantDensity[z])          + " g/cm^3 \n" 
			C = "Perturbed coolant density:            {0:02.2f}".format(SerpentPerturbedAxialCoolantDensity[z]) + " g/cm^3 \n" 
			D = "Total cell coolant mass perturbation: {0:02.0f}".format(CoolantMassDifference)                  + " kg     \n"
	
			solq.write(A)		
			solq.write(B)	
			solq.write(C)	
			solq.write(D)
			solq.write("\n")							
	
		solq.write("\n")

	if SequentialAxialFuelReactivity == "on":

		solq.write("Fuel perturbation information: \n")

		for z in range(SerpentAxialZones):
	
			FuelMassDifference = RelFuelDensDiff[z] * 1000 * FuelSectionVolume
			FuelMassDiff.append(FuelMassDifference)
	
			A = "Axial zone " + str(z+1) + "/" + str(SerpentAxialZones) + " \n"
			B = "Operating condition fuel density:  {0:02.2f}".format(SerpentAxialFuelDensity[z])          + " g/cm^3 \n" 
			C = "Perturbed fuel density:            {0:02.2f}".format(SerpentPerturbedAxialFuelDensity[z]) + " g/cm^3 \n" 
			D = "Total cell fuel mass perturbation: {0:02.0f}".format(FuelMassDifference)                  + " kg     \n"
	
			solq.write(A)		
			solq.write(B)	
			solq.write(C)	
			solq.write(D)
			solq.write("\n")							
	
		solq.write("\n")

	if SequentialAxialCladReactivity == "on":

		solq.write("Cladding perturbation information: \n")
	
		for z in range(SerpentAxialZones):
	
			CladMassDifference = RelCladDensDiff[z] * 1000 * CladSectionVolume
			CladMassDiff.append(CladMassDifference)
	
			A = "Axial zone " + str(z+1) + "/" + str(SerpentAxialZones) + " \n"
			B = "Operating condition cladding density:  {0:02.2f}".format(SerpentAxialCladdingDensity[z])          + " g/cm^3 \n" 
			C = "Perturbed cladding density:            {0:02.2f}".format(SerpentPerturbedAxialCladdingDensity[z]) + " g/cm^3 \n" 
			D = "Total cell cladding mass perturbation: {0:02.0f}".format(CladMassDifference)                  + " kg     \n"
	
			solq.write(A)		
			solq.write(B)	
			solq.write(C)	
			solq.write(D)
			solq.write("\n")							
	
		solq.write("\n")

	BelowMassDiff = BelowCoreCoolantMassDifference
	AboveMassDiff = AboveCoreCoolantMassDifference	

	return(ColMassDiff, FuelMassDiff, CladMassDiff, BelowMassDiff, AboveMassDiff)




