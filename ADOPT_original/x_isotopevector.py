import math

def corecellnames(Batches, SerpentAxialZones):

	CellNames = []

	for batch in range(Batches):

		for z in range(SerpentAxialZones):

			AB = "Batch" + str(batch+1) + "Axial" + str(z+1)
			CellNames.append(AB)

	return(CellNames)

def serpentcoregeometry(Batches, TotalAssemblyArea, SerpentAxialZones, FuelLength, Assemblies, 
	                    AssemblyPitch, RadialReflectorRows, RadialShieldRows, SerpentOutsideDistance,
	                    InternalControlAssemblies):

	CoreVolume = TotalAssemblyArea * (Assemblies + InternalControlAssemblies) * FuelLength
	Cells      = Batches * SerpentAxialZones
	CellVolume = 1e6 * CoreVolume / Cells 

	EquivalentCoreArea     = TotalAssemblyArea * (Assemblies + InternalControlAssemblies)
	EquivalentCellArea     = EquivalentCoreArea / Batches
	EquivalentCoreRadius   = math.sqrt(math.pi * EquivalentCoreArea) / math.pi
	EquivalentCoreDiameter = EquivalentCoreRadius * 2

	SCR = math.sqrt(math.pi * EquivalentCellArea) / math.pi

	RX = 0
	SerpentCoreRadius = []

	for batch in range(Batches):
	
		CalculatedArea = 1e-30

		while CalculatedArea < EquivalentCellArea:

			RX += 1e-5
			MinusArea = (batch) * EquivalentCellArea
			CalculatedArea = math.pi * RX ** 2 - MinusArea

		SerpentCoreRadius.append(RX)

	CoreOuterRadius = RX
	ReflectorOuterRadius = RX + RadialReflectorRows * AssemblyPitch / 100
	ShieldOuterRadius    = ReflectorOuterRadius + RadialShieldRows * AssemblyPitch / 100
	SystemOuterRadius    = ShieldOuterRadius*100 + SerpentOutsideDistance
	ReflectorVolume = math.pi * (ReflectorOuterRadius ** 2) - math.pi * (RX ** 2)
	ShieldVolume    = math.pi * (ShieldOuterRadius ** 2) - math.pi * (ReflectorOuterRadius ** 2)

	return(SerpentCoreRadius, CellVolume, ReflectorOuterRadius, ReflectorVolume, CoreOuterRadius, 
		   ShieldOuterRadius, ShieldVolume, SystemOuterRadius)	

def coreisotopes(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
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
				 SerpentAxialBondTemperature, SerpentAxialFuelTemperature, serpfilepath, Name, Fissile, 
				 Fertile, Fuel, Cladding, Bond, Coolant, Duct, CellNames, FissileFraction, CellVolume,
				 SerpentTemperaturePoints, FuelLength, SerpentCoreRadius, SerpentDepletion, EDIS):

	mi = open(Name + "_mburn", 'w')
	i = 0

	for batch in range(Batches):

		for z in range(SerpentAxialZones):
	
			FuelMassDensityGCC          = FuelVolumeFraction          * SerpentAxialFuelDensity[z]
			BondMassDensityGCC          = GapVolumeFraction           * SerpentAxialBondDensity[z] 
			CladdingMassDensityGCC      = CladdingVolumeFraction      * SerpentAxialCladdingDensity[z]
			ActiveCoolantMassDensityGCC = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[z]
			DuctMassDensityGCC          = DuctVolumeFraction          * SerpentAxialDuctDensity[z]
			IAGapMassDensityGCC         = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[z]
			CoreMassDensityGCC          = FuelMassDensityGCC + BondMassDensityGCC + CladdingMassDensityGCC + ActiveCoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

			FuelMass          = FuelMassDensityGCC          * CellVolume / 1e3
			BondMass          = BondMassDensityGCC          * CellVolume / 1e3
			CladdingMass      = CladdingMassDensityGCC      * CellVolume / 1e3
			ActiveCoolantMass = ActiveCoolantMassDensityGCC * CellVolume / 1e3
			DuctMass          = DuctMassDensityGCC          * CellVolume / 1e3
			IAGapMass         = IAGapMassDensityGCC         * CellVolume / 1e3
			CoreMass          = CoreMassDensityGCC          * CellVolume / 1e3

			FuelMassFraction          = FuelMassDensityGCC          /  CoreMassDensityGCC
			BondMassFraction          = BondMassDensityGCC          /  CoreMassDensityGCC
			CladdingMassFraction      = CladdingMassDensityGCC      /  CoreMassDensityGCC
			ActiveCoolantMassFraction = ActiveCoolantMassDensityGCC /  CoreMassDensityGCC
			DuctMassFraction          = DuctMassDensityGCC          /  CoreMassDensityGCC
			IAGapMassFraction         = IAGapMassDensityGCC         /  CoreMassDensityGCC
 
			NonActinideBatch = NonActinideIsotopeMassFractions.get(batch)
			FissileBatch     = FissileIsotopeMassFractions.get(batch)
			FertileBatch     = FertileIsotopeMassFractions.get(batch)

			FuelTemperature = SerpentAxialFuelTemperature[z]

			LowFuel = FuelLength / 2
			FuelStep = FuelLength / SerpentAxialZones

			FissileMassF = 0
			for k,v in FissileBatch.items():

				FissileMassF += v

			FertileMassF = 0
			for k,v in FertileBatch.items():

				FertileMassF += v

			NonA = 1 - FissileMassF - FertileMassF

			mi.write("% ####################################################                      \n")
			mi.write("%                                                                           \n")			
			mi.write("%    Core zell " + CellNames[i] +                                          "\n")
			mi.write("%                                                                           \n")			
			mi.write("%    Materials                                                              \n")
			mi.write("%    -------------------------------------------------                      \n")	
			mi.write("%    Fuel-type:        " + Fuel                                          + "\n")	
			mi.write("%    Fissile material: " + str(Fissile[batch]) + " ({0:02.2%}".format(FissileFraction[batch]) + ") \n")					
			mi.write("%    Fertile material: " + str(Fertile[batch]) + " ({0:02.2%}".format(1 - FissileFraction[batch]) + ") \n")					
			mi.write("%    Bond/gap:         " + Bond                                          + "\n")	
			mi.write("%    Cladding:         " + Cladding                                      + "\n")	
			mi.write("%    Coolant:          " + Coolant                                       + "\n")	
			mi.write("%    Duct:             " + Duct                                          + "\n")	
			mi.write("%                                                                           \n")
			mi.write("%    Geometry                                                               \n")
			mi.write("%    -------------------------------------------------                      \n")
			mi.write("%    Cell volume: {0:02.3f}".format(CellVolume/1e6)                     + " m^3 \n")
			mi.write("%    Axially between  z = {0:02.3f}".format( z * FuelStep ) + " and {0:02.3f}".format((z+1) * FuelStep) + " m \n")
			
			if batch == 0:
				mi.write("%    Radially between r = 0.000 and {0:02.3f}".format(SerpentCoreRadius[batch]) + " m \n")
			else:
				mi.write("%    Radially between r = {0:02.3f}".format(SerpentCoreRadius[batch-1]) + " and {0:02.3f}".format(SerpentCoreRadius[batch]) + " m \n")

			mi.write("%                                                                            \n")
			mi.write("%    Mass fractions                                                          \n")			
			mi.write("%    -------------------------------------------------                       \n")	
			mi.write("%    Fuel            = {0:02.2%}".format(FuelMassFraction)                + "\n")
			mi.write("%    Bond/gap        = {0:02.2%}".format(BondMassFraction)                + "\n")
			mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)            + "\n")
			mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantMassFraction)       + "\n")						
			mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
			mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
			mi.write("%                                                                            \n")							
			mi.write("%    Volume fractions                                                        \n")			
			mi.write("%    -------------------------------------------------                       \n")	
			mi.write("%    Fuel            = {0:02.2%}".format(FuelVolumeFraction)              + "\n")
			mi.write("%    Bond/gap        = {0:02.2%}".format(GapVolumeFraction)               + "\n")
			mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)          + "\n")
			mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)     + "\n")						
			mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)              + "\n")
			mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)     + "\n")
			mi.write("%                                                                            \n")							
			mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
			mi.write("%    -------------------------------------------------                       \n")	
			mi.write("%    Fuel            = {0:02.3f}".format(FuelMassDensityGCC)              + "\n")
			mi.write("%    Bond/gap        = {0:02.3f}".format(BondMassDensityGCC)              + "\n")
			mi.write("%    Cladding        = {0:02.3f}".format(CladdingMassDensityGCC)          + "\n")
			mi.write("%    Active coolant  = {0:02.3f}".format(ActiveCoolantMassDensityGCC)     + "\n")						
			mi.write("%    Duct            = {0:02.3f}".format(DuctMassDensityGCC)              + "\n")
			mi.write("%    IA-gap coolant  = {0:02.3f}".format(IAGapMassDensityGCC)             + "\n")
			mi.write("%    Total cell      = {0:02.3f}".format(CoreMassDensityGCC)              + "\n")
			mi.write("%                                                                            \n")
			mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
			mi.write("%    -------------------------------------------------                       \n")	
			mi.write("%    Fuel            = {0:02.1f}".format(SerpentAxialFuelTemperature[z]-273.15) + "\n")
			mi.write("%    Bond/gap        = {0:02.1f}".format(SerpentAxialBondTemperature[z]-273.15) + "\n")
			mi.write("%    Cladding        = {0:02.1f}".format(SerpentAxialCladdingTemperature[z]-273.15) + "\n")			
			mi.write("%    Active coolant  = {0:02.1f}".format(SerpentAxialCoolantTemperature[z]-273.15) + "\n")
			mi.write("%    Duct            = {0:02.1f}".format(SerpentAxialDuctTemperature[z]-273.15) + "\n")
			mi.write("%    IA-gap coolant  = {0:02.1f}".format(SerpentAxialIAGapTemperature[z]-273.15) + "\n")
			mi.write("%                                                                            \n")
			mi.write("%    Component density (g/cc)                                                \n")			
			mi.write("%    -------------------------------------------------                       \n")	
			mi.write("%    Fuel            = {0:02.3f}".format(SerpentAxialFuelDensity[z])      + "\n")
			mi.write("%    Bond/gap        = {0:02.3f}".format(SerpentAxialBondDensity[z])      + "\n")
			mi.write("%    Cladding        = {0:02.3f}".format(SerpentAxialCladdingDensity[z])  + "\n")
			mi.write("%    Active coolant  = {0:02.3f}".format(SerpentAxialCoolantDensity[z])   + "\n")						
			mi.write("%    Duct            = {0:02.3f}".format(SerpentAxialDuctDensity[z])      + "\n")
			mi.write("%    IA-gap coolant  = {0:02.3f}".format(SerpentAxialIAGapDensity[z])     + "\n")			
			mi.write("%                                                                            \n")
			mi.write("%    Component mass (kg/cell)                                                \n")			
			mi.write("%    -------------------------------------------------                       \n")	
			mi.write("%    Fissile material  = {0:02.1f}".format(FuelMass * FissileMassF)       + "\n")			
			mi.write("%    Fertile material  = {0:02.1f}".format(FuelMass * FertileMassF)       + "\n")	
			mi.write("%    Non-actinide fuel = {0:02.1f}".format(FuelMass * NonA)               + "\n")	
			mi.write("%    Total fuel        = {0:02.1f}".format(FuelMass)                      + "\n")			
			mi.write("%    Bond/gap          = {0:02.1f}".format(BondMass)                      + "\n")
			mi.write("%    Cladding          = {0:02.1f}".format(CladdingMass)                  + "\n")
			mi.write("%    Active coolant    = {0:02.1f}".format(ActiveCoolantMass)             + "\n")						
			mi.write("%    Duct              = {0:02.1f}".format(DuctMass)                      + "\n")
			mi.write("%    IA-gap coolant    = {0:02.1f}".format(IAGapMass)                     + "\n")
			mi.write("%    Total cell        = {0:02.1f}".format(CoreMass)                      + "\n")						
			mi.write("%                                                                            \n")
			mi.write("% ######################################################                     \n")
			mi.write("\n")	

			if SerpentDepletion == "on" or EDIS == "on":

				X1 = "mat " + CellNames[i] + " -{0:02.5f}".format(CoreMassDensityGCC) + " vol {0:02.1f}".format(CellVolume) + " burn 1 \n"

			else:

				X1 = "mat " + CellNames[i] + " -{0:02.5f}".format(CoreMassDensityGCC) + " vol {0:02.1f}".format(CellVolume) + " \n"

			i += 1
			mi.write(X1)

			if FuelTemperature <= 450:

				FuelXSid = ".03c"

			elif FuelTemperature > 450 and FuelTemperature <= 750:

				FuelXSid = ".06c"

			elif FuelTemperature > 750 and FuelTemperature <= 1050:

				FuelXSid = ".12c"

			elif FuelTemperature > 1050 and FuelTemperature <= 1350:

				FuelXSid = ".12c"

			elif FuelTemperature > 1350 and FuelTemperature <= 1650:	
			
				FuelXSid = ".15c"	

			elif FuelTemperature > 1650:
			
				FuelXSid = ".18c"	

			FuelIsotopeMassDensityGCC = {}
			FuelIsotopeMassFraction   = {}

			if Fuel != "MetallicTh":

				X1 = "Non-actinide component of fuel (" + Fuel + ") \n"
	
				for k,v in NonActinideBatch.items():
	
					NonActinideIsotopeMassDensityGCC = v * FuelMassDensityGCC
					NonActinideIsotopeMassDensityGCC2 = {k : NonActinideIsotopeMassDensityGCC}
	
					NonActinideCoreMassFraction = v * FuelMassFraction
					NonActinideCoreMassFraction2 = {k : NonActinideCoreMassFraction}
	
					FuelIsotopeMassDensityGCC.update(NonActinideIsotopeMassDensityGCC2)
					FuelIsotopeMassFraction.update(NonActinideCoreMassFraction2)
	
					if len(k) == 4:
	
						AA = k + FuelXSid + "  -{0:02.5e}".format(NonActinideCoreMassFraction) + "     % " + X1
    	
					else:    
    	
						AA = k + FuelXSid + " -{0:02.5e}".format(NonActinideCoreMassFraction)  + "     % " + X1
	
					mi.write(AA)

			X1 = "Fissile component of fuel (" + Fissile[batch] + ") \n"

			for k,v in FissileBatch.items():

				FissileIsotopeMassDensityGCC = v * FuelMassDensityGCC
				FissileIsotopeMassDensityGCC2 = {k : FissileIsotopeMassDensityGCC}

				FissileCoreMassFraction = v * FuelMassFraction
				FissileCoreMassFraction2 = {k : FissileCoreMassFraction}

				FuelIsotopeMassDensityGCC.update(FissileIsotopeMassDensityGCC2)
				FuelIsotopeMassFraction.update(FissileCoreMassFraction2)

				AA = k + FuelXSid + " -{0:02.5e}".format(FissileCoreMassFraction) + "     % " + X1
				mi.write(AA)

			X1 = "Fertile component of fuel (" + Fertile[batch] + ") \n"

			for k,v in FertileBatch.items():

				FertileIsotopeMassDensityGCC = v * FuelMassDensityGCC
				FertileIsotopeMassDensityGCC2 = {k : FertileIsotopeMassDensityGCC}

				FertileCoreMassFraction = v * FuelMassFraction
				FertileCoreMassFraction2 = {k : FertileCoreMassFraction}

				FuelIsotopeMassDensityGCC.update(FertileIsotopeMassDensityGCC2)
				FuelIsotopeMassFraction.update(FertileCoreMassFraction2)

				AA = k + FuelXSid + " -{0:02.5e}".format(FertileCoreMassFraction) + "     % " + X1
				mi.write(AA)

			X1 = "Bond/gap isotope (" + Bond + ") \n"

			BondTemperature = SerpentAxialBondTemperature[z]

			if BondTemperature <= 450:

				BondXSid = ".03c"

			elif BondTemperature > 450 and BondTemperature <= 750:

				BondXSid = ".06c"

			elif BondTemperature > 750 and BondTemperature <= 1050:

				BondXSid = ".12c"

			elif BondTemperature > 1050 and BondTemperature <= 1350:

				BondXSid = ".12c"

			elif BondTemperature > 1350 and BondTemperature <= 1650:	
			
				BondXSid = ".15c"	

			elif BondTemperature > 1650:
			
				BondXSid = ".18c"				

			BondMassDensityGCC   = {}
			BondCoreMassFraction = {}

			for k,v in BondIsotopeMassFractions.items():

				BondIsotopeCoreMassFraction  = v * BondMassFraction

				if len(k) == 4:

					AA = k + BondXSid + "  -{0:02.5e}".format(BondIsotopeCoreMassFraction) + "     % " + X1
				
				else:

					AA = k + BondXSid + " -{0:02.5e}".format(BondIsotopeCoreMassFraction)  + "     % " + X1

				mi.write(AA)

			X1 = "Cladding isotope (" + Cladding + ") \n"

			CladdingTemperature = SerpentAxialCladdingTemperature[z]

			if CladdingTemperature <= 450:

				CladdingXSid = ".03c"

			elif CladdingTemperature > 450 and CladdingTemperature <= 750:

				CladdingXSid = ".06c"

			elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

				CladdingXSid = ".12c"

			elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

				CladdingXSid = ".12c"

			elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
			
				CladdingXSid = ".15c"	

			elif CladdingTemperature > 1650:
			
				CladdingXSid = ".18c"				

			CladdingMassDensityGCC   = {}
			CladdingCoreMassFraction = {}

			for k,v in CladdingIsotopeMassFractions.items():

				CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

				if len(k) == 4:

					AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
				
				else:

					AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

				mi.write(AA)

			X1 = "Coolant isotope (" + Coolant + ") \n"

			CoolantTemperature = SerpentAxialCoolantTemperature[z]

			if CoolantTemperature <= 450:

				CoolantXSid = ".03c"

			elif CoolantTemperature > 450 and CoolantTemperature <= 750:

				CoolantXSid = ".06c"

			elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

				CoolantXSid = ".12c"

			elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

				CoolantXSid = ".12c"

			elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
			
				CoolantXSid = ".15c"	

			elif CoolantTemperature > 1650:
			
				CoolantXSid = ".18c"				

			CoolantMassDensityGCC   = {}
			CoolantCoreMassFraction = {}

			for k,v in CoolantIsotopeMassFractions.items():

				CoolantIsotopeCoreMassFraction  = v * ActiveCoolantMassFraction

				if len(k) == 4:

					AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
				
				else:

					AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

				mi.write(AA)	

			X1 = "Duct isotope (" + Duct + ") \n"

			DuctTemperature = SerpentAxialDuctTemperature[z]

			if DuctTemperature <= 450:

				DuctXSid = ".03c"

			elif DuctTemperature > 450 and DuctTemperature <= 750:

				DuctXSid = ".06c"

			elif DuctTemperature > 750 and DuctTemperature <= 1050:

				DuctXSid = ".12c"

			elif DuctTemperature > 1050 and DuctTemperature <= 1350:

				DuctXSid = ".12c"

			elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
			
				DuctXSid = ".15c"	

			elif DuctTemperature > 1650:
			
				DuctXSid = ".18c"				

			DuctMassDensityGCC   = {}
			DuctCoreMassFraction = {}

			for k,v in DuctIsotopeMassFractions.items():

				DuctIsotopeCoreMassFraction  = v * DuctMassFraction

				if len(k) == 4:

					AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
				
				else:

					AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

				mi.write(AA)

			X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

			IAGapTemperature = SerpentAxialIAGapTemperature[z]

			if IAGapTemperature <= 450:

				IAGapXSid = ".03c"

			elif IAGapTemperature > 450 and IAGapTemperature <= 750:

				IAGapXSid = ".06c"

			elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

				IAGapXSid = ".12c"

			elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

				IAGapXSid = ".12c"

			elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
			
				IAGapXSid = ".15c"	

			elif IAGapTemperature > 1650:
			
				IAGapXSid = ".18c"				
  
			IAGapMassDensityGCC   = {}
			IAGapCoreMassFraction = {}

			for k,v in CoolantIsotopeMassFractions.items():

				IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

				if len(k) == 4:

					AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
				
				else:

					AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

				mi.write(AA)

			mi.write("\n")	

	mi.write("\n")
	mi.close()

def reflectorserpent(ReflectorPinVolumeFraction, ReflectorPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
					 DuctIsotopeMassFractions, ReflectorIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
					 SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
					 SerpentAxialReflectorDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
					 SerpentAxialDuctTemperature, serpfilepath, Name, ReflectorVolume, CoreOuterRadius,
					 ReflectorOuterRadius, FuelLength, ReflectorPinOuterRadius, ReflectorPinPitch, outerreflrgb):

	mi = open(Name + "_nonfuel", 'a')

	ReflectorPinVolumeFraction1 = ReflectorPinVolumeFraction
	ReflectorPinVolumeFraction  = ReflectorPinVolumeFraction - DuctVolumeFraction - InterAssemblyVolumeFraction
	CoolantVolumeFraction       = - ReflectorPinVolumeFraction * (ReflectorPinVolumeFraction1-1) / ReflectorPinVolumeFraction1

	for z in range(SerpentAxialZones):

		ReflectorPinDensityGCC = ReflectorPinVolumeFraction  * SerpentAxialReflectorDensity[z]
		CoolantMassDensityGCC  = CoolantVolumeFraction       * SerpentAxialCoolantDensity[z]
		DuctMassDensityGCC     = DuctVolumeFraction          * SerpentAxialDuctDensity[z]
		IAGapMassDensityGCC    = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[z]

		ReflectorCellMassDensityGCC = ReflectorPinDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC

		ReflectorPinMassFraction = ReflectorPinDensityGCC / ReflectorCellMassDensityGCC
		CoolantMassFraction      = CoolantMassDensityGCC  / ReflectorCellMassDensityGCC
		DuctMassFraction         = DuctMassDensityGCC     / ReflectorCellMassDensityGCC
		IAGapMassFraction        = IAGapMassDensityGCC    / ReflectorCellMassDensityGCC      
		
		ReflectorTemperature = SerpentAxialDuctTemperature[z]
		CoolantTemperature   = SerpentAxialCoolantTemperature[z]
		IAGapTemperature     = SerpentAxialIAGapTemperature[z]
		DuctTemperature      = SerpentAxialDuctTemperature[z]

		mi.write("\n")
		mi.write("% ####################################################                      \n")
		mi.write("%                                                                           \n")			
		mi.write("%    Cell radialreflector" + str(z+1) + "                                   \n")
		mi.write("%                                                                           \n")			
		mi.write("%    Materials                                                              \n")
		mi.write("%    -------------------------------------------------                      \n")	
		mi.write("%    Reflector-pin: " + ReflectorPinMaterial                             + "\n")							
		mi.write("%    Coolant:       " + Coolant                                          + "\n")	
		mi.write("%    Duct:          " + Duct                                             + "\n")	
		mi.write("%                                                                           \n")
		mi.write("%    General geometry                                                       \n")
		mi.write("%    -------------------------------------------------                      \n")
		mi.write("%    Cell volume: {0:02.3f}".format(ReflectorVolume)                + " m^3 \n")
		mi.write("%    Axially between  z = 0 and " + str(FuelLength)                   + " m \n")
		mi.write("%    Radially between r = {0:02.3f}".format(CoreOuterRadius) + " and {0:02.3f}".format(ReflectorOuterRadius) + " m \n")
		mi.write("%                                                                            \n")
		mi.write("%    Calculated geometry                                                     \n")
		mi.write("%    -------------------------------------------------                       \n")
		mi.write("%    Reflector pin diameter: {0:02.3f}".format(ReflectorPinOuterRadius*2)   + " cm \n")		
		mi.write("%    Reflector pin pitch:    {0:02.3f}".format(ReflectorPinPitch)        + " cm \n")	
		mi.write("%    Reflector pin P/D:      {0:02.3f}".format(ReflectorPinPitch/(ReflectorPinOuterRadius*2))   + " \n")					
		mi.write("%                                                                            \n")		
		mi.write("%    Mass fractions                                                          \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Reflector-pin   = {0:02.2%}".format(ReflectorPinMassFraction)        + "\n")
		mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)             + "\n")						
		mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
		mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
		mi.write("%                                                                            \n")							
		mi.write("%    Volume fractions                                                        \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Reflector-pin   = {0:02.2%}".format(ReflectorPinVolumeFraction) + " ({0:02.2%}".format(ReflectorPinVolumeFraction1)   + " in-assembly) \n")
		mi.write("%    Active coolant  = {0:02.2%}".format(CoolantVolumeFraction)      + " ({0:02.2%}".format(1-ReflectorPinVolumeFraction1) + " in-assembly) \n")				
		mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)         + "\n")
		mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)               + "\n")
		mi.write("%                                                                            \n")						
		mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Reflector-pin   = {0:02.2f}".format(ReflectorPinDensityGCC)          + "\n")
		mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)           + "\n")						
		mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)              + "\n")
		mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)             + "\n")
		mi.write("%    Cell total      = {0:02.2f}".format(ReflectorCellMassDensityGCC)     + "\n")
		mi.write("%                                                                            \n")
		mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Reflector-pin   = {0:02.1f}".format(ReflectorTemperature-273.15)     + "\n")
		mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)       + "\n")						
		mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)          + "\n")
		mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)         + "\n")
		mi.write("%                                                                            \n")
		mi.write("%    Component density (g/cc)                                                \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Reflector-pin  = {0:02.3f}".format(SerpentAxialReflectorDensity[z])  + "\n")
		mi.write("%    Active coolant = {0:02.3f}".format(SerpentAxialCoolantDensity[z])    + "\n")
		mi.write("%    Duct           = {0:02.3f}".format(SerpentAxialDuctDensity[z])       + "\n")
		mi.write("%    IA-gap coolant = {0:02.3f}".format(SerpentAxialIAGapDensity[z])      + "\n")									
		mi.write("%                                                                            \n")
		mi.write("%    Component mass (kg/cell)                                                \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Reflector-pin  = {0:02.1f}".format(1e3 * ReflectorPinDensityGCC * ReflectorVolume) + "\n")			
		mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * ReflectorVolume)  + "\n")	
		mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC * ReflectorVolume)     + "\n")	
		mi.write("%    IA-gap coolant = {0:02.1f}".format(1e3 * IAGapMassDensityGCC * ReflectorVolume)    + "\n")									
		mi.write("%                                                                            \n")
		mi.write("% ######################################################                     \n")
		mi.write("\n")	

		X1 = "mat radialreflectormat" + str(z) + " -{0:02.5f}".format(ReflectorCellMassDensityGCC) + " rgb " + outerreflrgb + " \n"

		mi.write(X1)

		if ReflectorTemperature <= 450:

			ReflectorXSid = ".03c"

		elif ReflectorTemperature > 450 and ReflectorTemperature <= 750:

			ReflectorXSid = ".06c"

		elif ReflectorTemperature > 750 and ReflectorTemperature <= 1050:

			ReflectorXSid = ".12c"

		elif ReflectorTemperature > 1050 and ReflectorTemperature <= 1350:

			ReflectorXSid = ".12c"

		elif ReflectorTemperature > 1350 and ReflectorTemperature <= 1650:	
		
			ReflectorXSid = ".15c"	

		elif ReflectorTemperature > 1650:
		
			ReflectorXSid = ".18c"	

		X1 = "Reflector-pin isotope (" + ReflectorPinMaterial + ") \n"

		for k,v in ReflectorIsotopeMassFractions.items():

			ReflectorIsotopeCoreMassFraction  = v * ReflectorPinMassFraction

			if len(k) == 4:

				AA = k + ReflectorXSid + "  -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + ReflectorXSid + " -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)

		X1 = "Coolant isotope (" + Coolant + ") \n"

		if CoolantTemperature <= 450:

			CoolantXSid = ".03c"

		elif CoolantTemperature > 450 and CoolantTemperature <= 750:

			CoolantXSid = ".06c"

		elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

			CoolantXSid = ".12c"

		elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

			CoolantXSid = ".12c"

		elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
		
			CoolantXSid = ".15c"	

		elif CoolantTemperature > 1650:
		
			CoolantXSid = ".18c"				

		for k,v in CoolantIsotopeMassFractions.items():

			CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

			if len(k) == 4:

				AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)				

		X1 = "Duct isotope (" + Duct + ") \n"

		if DuctTemperature <= 450:

			DuctXSid = ".03c"

		elif DuctTemperature > 450 and DuctTemperature <= 750:

			DuctXSid = ".06c"

		elif DuctTemperature > 750 and DuctTemperature <= 1050:

			DuctXSid = ".12c"

		elif DuctTemperature > 1050 and DuctTemperature <= 1350:

			DuctXSid = ".12c"

		elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
		
			DuctXSid = ".15c"	

		elif DuctTemperature > 1650:
		
			DuctXSid = ".18c"				

		for k,v in DuctIsotopeMassFractions.items():

			DuctIsotopeCoreMassFraction  = v * DuctMassFraction

			if len(k) == 4:

				AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)

		X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

		if IAGapTemperature <= 450:

			IAGapXSid = ".03c"

		elif IAGapTemperature > 450 and IAGapTemperature <= 750:

			IAGapXSid = ".06c"

		elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

			IAGapXSid = ".12c"

		elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

			IAGapXSid = ".12c"

		elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
		
			IAGapXSid = ".15c"	

		elif IAGapTemperature > 1650:
		
			IAGapXSid = ".18c"				

		for k,v in CoolantIsotopeMassFractions.items():

			IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

			if len(k) == 4:

				AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)	

	mi.write("\n")
	mi.close()

def lowergasplenum(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
				   ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
				   CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
				   CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
				   SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
				   SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
				   SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
				   SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
				   serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, LowerGasPlenumLength,
				   CoreOuterRadius, Cladding, Coolant, Duct, gasrgb):

	mi = open(Name + "_nonfuel", 'a')

	LGPCellVolume = LowerGasPlenumLength * (CoreOuterRadius ** 2) * math.pi

	GasTemperature       = SerpentAxialCladdingTemperature[0] + 7.25
	CladdingTemperature  = SerpentAxialCladdingTemperature[0]
	CoolantTemperature   = SerpentAxialCoolantTemperature[0]
	IAGapTemperature     = SerpentAxialIAGapTemperature[0]
	DuctTemperature      = SerpentAxialDuctTemperature[0]

	R   = 8.3144621
	AHe = 4.0026032
	GasPressure = 2e6
	GasDensity = (GasPressure * GasTemperature / 273.15) / R / GasTemperature * AHe / 1e6

	GasMassDensityGCC           = (FuelVolumeFraction + GapVolumeFraction) * GasDensity
	CladdingMassDensityGCC      = CladdingVolumeFraction      * SerpentAxialCladdingDensity[0]
	CoolantMassDensityGCC       = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[0]
	DuctMassDensityGCC          = DuctVolumeFraction          * SerpentAxialDuctDensity[0]
	IAGapMassDensityGCC         = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[0]
	CoreMassDensityGCC          = GasMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

	GasMass           = GasMassDensityGCC           * LGPCellVolume / 1e3
	CladdingMass      = CladdingMassDensityGCC      * LGPCellVolume / 1e3
	ActiveCoolantMass = CoolantMassDensityGCC       * LGPCellVolume / 1e3
	DuctMass          = DuctMassDensityGCC          * LGPCellVolume / 1e3
	IAGapMass         = IAGapMassDensityGCC         * LGPCellVolume / 1e3
	CoreMass          = CoreMassDensityGCC          * LGPCellVolume / 1e3

	GasMassFraction           = GasMassDensityGCC           /  CoreMassDensityGCC
	CladdingMassFraction      = CladdingMassDensityGCC      /  CoreMassDensityGCC
	CoolantMassFraction       = CoolantMassDensityGCC       /  CoreMassDensityGCC
	DuctMassFraction          = DuctMassDensityGCC          /  CoreMassDensityGCC
	IAGapMassFraction         = IAGapMassDensityGCC         /  CoreMassDensityGCC

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell lowergasplenum                                                       \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Cladding: " + Cladding                                                 + "\n")							
	mi.write("%    Coolant:  " + Coolant                                                  + "\n")	
	mi.write("%    Duct:     " + Duct                                                     + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(LGPCellVolume)                    + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(LowerGasPlenumLength)               + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(CoreOuterRadius*2)                  + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2%}".format(GasMassFraction)                   + "\n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)              + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)               + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                  + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)                 + "\n")
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2%}".format(FuelVolumeFraction + GapVolumeFraction) + " \n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)            + "\n")				
	mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)       + "\n")
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)       + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2f}".format(GasMassDensityGCC)                 + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(CladdingMassDensityGCC)            + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)             + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)               + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(CoreMassDensityGCC)                + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.1f}".format(GasTemperature-273.15)             + "\n")
	mi.write("%    Cladding        = {0:02.1f}".format(CladdingTemperature-273.15)        + "\n")						
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)         + "\n")
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)            + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)           + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2f}".format(GasDensity)                        + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(SerpentAxialCladdingDensity[0])    + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(SerpentAxialCoolantDensity[0])     + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(SerpentAxialDuctDensity[0])        + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(SerpentAxialIAGapDensity[0])       + "\n")							
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Fission gas    = {0:02.1f}".format(1e3 * GasMassDensityGCC      * LGPCellVolume) + "\n")			
	mi.write("%    Cladding       = {0:02.1f}".format(1e3 * CladdingMassDensityGCC * LGPCellVolume) + "\n")	
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC  * LGPCellVolume) + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC     * LGPCellVolume) + "\n")
	mi.write("%    IA-gap         = {0:02.1f}".format(1e3 * IAGapMassDensityGCC    * LGPCellVolume) + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")		

	X1 = "mat lowergasplenummat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + gasrgb + "\n"

	mi.write(X1)
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * (CoolantMassFraction + GasMassFraction)

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Cladding isotope (" + Cladding + ") \n"

	if CladdingTemperature <= 450:

		CladdingXSid = ".03c"

	elif CladdingTemperature > 450 and CladdingTemperature <= 750:

		CladdingXSid = ".06c"

	elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
	
		CladdingXSid = ".15c"	

	elif CladdingTemperature > 1650:
	
		CladdingXSid = ".18c"				

	CladdingMassDensityGCC   = {}
	CladdingCoreMassFraction = {}

	for k,v in CladdingIsotopeMassFractions.items():

		CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

		if len(k) == 4:

			AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)


	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	mi.write("\n")
	mi.close()

def lowerreflector(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
				   ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
				   CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
				   CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
				   SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
				   SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
				   SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
				   SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
				   serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, LowerReflectorLength,
				   CoreOuterRadius, Cladding, Coolant, Duct, ReflectorPinMaterial, SerpentAxialReflectorDensity,
				   ReflectorIsotopeMassFractions, innerreflrgb):

	mi = open(Name + "_nonfuel", 'a')

	LowerReflectorCellVolume = LowerReflectorLength * (CoreOuterRadius ** 2) * math.pi

	ReflectorTemperature = SerpentAxialCladdingTemperature[0]
	CladdingTemperature  = SerpentAxialCladdingTemperature[0]
	CoolantTemperature   = SerpentAxialCoolantTemperature[0]
	IAGapTemperature     = SerpentAxialIAGapTemperature[0]
	DuctTemperature      = SerpentAxialDuctTemperature[0]

	ReflectorMassDensityGCC     = (FuelVolumeFraction + GapVolumeFraction) * SerpentAxialReflectorDensity[0]
	CladdingMassDensityGCC      = CladdingVolumeFraction      * SerpentAxialCladdingDensity[0]
	CoolantMassDensityGCC       = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[0]
	DuctMassDensityGCC          = DuctVolumeFraction          * SerpentAxialDuctDensity[0]
	IAGapMassDensityGCC         = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[0]
	CoreMassDensityGCC          = ReflectorMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

	ReflectorMass     = ReflectorMassDensityGCC     * LowerReflectorCellVolume / 1e3
	CladdingMass      = CladdingMassDensityGCC      * LowerReflectorCellVolume / 1e3
	ActiveCoolantMass = CoolantMassDensityGCC       * LowerReflectorCellVolume / 1e3
	DuctMass          = DuctMassDensityGCC          * LowerReflectorCellVolume / 1e3
	IAGapMass         = IAGapMassDensityGCC         * LowerReflectorCellVolume / 1e3
	CoreMass          = CoreMassDensityGCC          * LowerReflectorCellVolume / 1e3

	ReflectorMassFraction     = ReflectorMassDensityGCC     /  CoreMassDensityGCC
	CladdingMassFraction      = CladdingMassDensityGCC      /  CoreMassDensityGCC
	CoolantMassFraction       = CoolantMassDensityGCC       /  CoreMassDensityGCC
	DuctMassFraction          = DuctMassDensityGCC          /  CoreMassDensityGCC
	IAGapMassFraction         = IAGapMassDensityGCC         /  CoreMassDensityGCC

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell lowerreflector                                                       \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector: " + ReflectorPinMaterial                                    + "\n")
	mi.write("%    Cladding:  " + Cladding                                                + "\n")							
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%    Duct:      " + Duct                                                    + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(LowerReflectorCellVolume)         + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(LowerReflectorLength)               + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(CoreOuterRadius*2)                  + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2%}".format(ReflectorMassFraction)             + "\n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)              + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)               + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                  + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)                 + "\n")
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2%}".format(FuelVolumeFraction + GapVolumeFraction) + " \n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)            + "\n")				
	mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)       + "\n")
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)       + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2f}".format(ReflectorMassDensityGCC)           + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(CladdingMassDensityGCC)            + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)             + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)               + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(CoreMassDensityGCC)                + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.1f}".format(ReflectorTemperature-273.15)       + "\n")
	mi.write("%    Cladding        = {0:02.1f}".format(CladdingTemperature-273.15)        + "\n")						
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)         + "\n")
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)            + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)           + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2f}".format(SerpentAxialReflectorDensity[0])   + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(SerpentAxialCladdingDensity[0])    + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(SerpentAxialCoolantDensity[0])     + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(SerpentAxialDuctDensity[0])        + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(SerpentAxialIAGapDensity[0])       + "\n")							
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector      = {0:02.1f}".format(1e3 * ReflectorMassDensityGCC * LowerReflectorCellVolume) + "\n")			
	mi.write("%    Cladding       = {0:02.1f}".format(1e3 * CladdingMassDensityGCC  * LowerReflectorCellVolume) + "\n")	
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC   * LowerReflectorCellVolume) + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC      * LowerReflectorCellVolume) + "\n")
	mi.write("%    IA-gap         = {0:02.1f}".format(1e3 * IAGapMassDensityGCC     * LowerReflectorCellVolume) + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")		

	X1 = "mat lowerreflectormat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + innerreflrgb + "\n"

	mi.write(X1)

	X1 = "Reflector isotope (" + ReflectorPinMaterial + ") \n"

	if ReflectorTemperature <= 450:

		ReflectorXSid = ".03c"

	elif ReflectorTemperature > 450 and ReflectorTemperature <= 750:

		ReflectorXSid = ".06c"

	elif ReflectorTemperature > 750 and ReflectorTemperature <= 1050:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1050 and ReflectorTemperature <= 1350:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1350 and ReflectorTemperature <= 1650:	
	
		ReflectorXSid = ".15c"	

	elif ReflectorTemperature > 1650:
	
		ReflectorXSid = ".18c"				

	for k,v in ReflectorIsotopeMassFractions.items():

		ReflectorIsotopeCoreMassFraction  = v * ReflectorMassFraction

		if len(k) == 4:

			AA = k + ReflectorXSid + "  -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ReflectorXSid + " -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Cladding isotope (" + Cladding + ") \n"

	if CladdingTemperature <= 450:

		CladdingXSid = ".03c"

	elif CladdingTemperature > 450 and CladdingTemperature <= 750:

		CladdingXSid = ".06c"

	elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
	
		CladdingXSid = ".15c"	

	elif CladdingTemperature > 1650:
	
		CladdingXSid = ".18c"				

	CladdingMassDensityGCC   = {}
	CladdingCoreMassFraction = {}

	for k,v in CladdingIsotopeMassFractions.items():

		CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

		if len(k) == 4:

			AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)


	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)			

	mi.write("\n")
	mi.close()	

def lowershield(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
				ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
				CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
				CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
				SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
				SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
				SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
				SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
				serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, LowerShieldLength,
				CoreOuterRadius, Cladding, Coolant, Duct, ShieldPinMaterial, SerpentAxialShieldDensity,
				ShieldIsotopeMassFractions, innershieldrgb):

	mi = open(Name + "_nonfuel", 'a')

	LowerShieldCellVolume = LowerShieldLength * (CoreOuterRadius ** 2) * math.pi

	ShieldTemperature    = SerpentAxialCladdingTemperature[0]
	CladdingTemperature  = SerpentAxialCladdingTemperature[0]
	CoolantTemperature   = SerpentAxialCoolantTemperature[0]
	IAGapTemperature     = SerpentAxialIAGapTemperature[0]
	DuctTemperature      = SerpentAxialDuctTemperature[0]

	ShieldMassDensityGCC     = (FuelVolumeFraction + GapVolumeFraction) * SerpentAxialShieldDensity[0]
	CladdingMassDensityGCC   = CladdingVolumeFraction      * SerpentAxialCladdingDensity[0]
	CoolantMassDensityGCC    = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[0]
	DuctMassDensityGCC       = DuctVolumeFraction          * SerpentAxialDuctDensity[0]
	IAGapMassDensityGCC      = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[0]
	CoreMassDensityGCC       = ShieldMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

	ShieldMass        = ShieldMassDensityGCC   * LowerShieldCellVolume / 1e3
	CladdingMass      = CladdingMassDensityGCC * LowerShieldCellVolume / 1e3
	ActiveCoolantMass = CoolantMassDensityGCC  * LowerShieldCellVolume / 1e3
	DuctMass          = DuctMassDensityGCC     * LowerShieldCellVolume / 1e3
	IAGapMass         = IAGapMassDensityGCC    * LowerShieldCellVolume / 1e3
	CoreMass          = CoreMassDensityGCC     * LowerShieldCellVolume / 1e3

	ShieldMassFraction     = ShieldMassDensityGCC     /  CoreMassDensityGCC
	CladdingMassFraction   = CladdingMassDensityGCC   /  CoreMassDensityGCC
	CoolantMassFraction    = CoolantMassDensityGCC    /  CoreMassDensityGCC
	DuctMassFraction       = DuctMassDensityGCC       /  CoreMassDensityGCC
	IAGapMassFraction      = IAGapMassDensityGCC      /  CoreMassDensityGCC

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell lowershield                                                          \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield:    " + ShieldPinMaterial                                       + "\n")
	mi.write("%    Cladding:  " + Cladding                                                + "\n")							
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%    Duct:      " + Duct                                                    + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(LowerShieldCellVolume)            + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(LowerShieldLength)                  + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(CoreOuterRadius*2)                  + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2%}".format(ShieldMassFraction)                + "\n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)              + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)               + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                  + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)                 + "\n")
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2%}".format(FuelVolumeFraction + GapVolumeFraction) + " \n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)            + "\n")				
	mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)       + "\n")
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)       + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2f}".format(ShieldMassDensityGCC)              + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(CladdingMassDensityGCC)            + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)             + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)               + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(CoreMassDensityGCC)                + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.1f}".format(ShieldTemperature-273.15)          + "\n")
	mi.write("%    Cladding        = {0:02.1f}".format(CladdingTemperature-273.15)        + "\n")						
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)         + "\n")
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)            + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)           + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2f}".format(SerpentAxialShieldDensity[0])      + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(SerpentAxialCladdingDensity[0])    + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(SerpentAxialCoolantDensity[0])     + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(SerpentAxialDuctDensity[0])        + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(SerpentAxialIAGapDensity[0])       + "\n")							
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield         = {0:02.1f}".format(1e3 * ShieldMassDensityGCC    * LowerShieldCellVolume) + "\n")			
	mi.write("%    Cladding       = {0:02.1f}".format(1e3 * CladdingMassDensityGCC  * LowerShieldCellVolume) + "\n")	
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC   * LowerShieldCellVolume) + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC      * LowerShieldCellVolume) + "\n")
	mi.write("%    IA-gap         = {0:02.1f}".format(1e3 * IAGapMassDensityGCC     * LowerShieldCellVolume) + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")		

	X1 = "mat lowershieldmat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + innershieldrgb + " \n"

	mi.write(X1)

	X1 = "Shield isotope (" + ShieldPinMaterial + ") \n"

	if ShieldTemperature <= 450:

		ShieldXSid = ".03c"

	elif ShieldTemperature > 450 and ShieldTemperature <= 750:

		ShieldXSid = ".06c"

	elif ShieldTemperature > 750 and ShieldTemperature <= 1050:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1050 and ShieldTemperature <= 1350:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1350 and ShieldTemperature <= 1650:	
	
		ShieldXSid = ".15c"	

	elif ShieldTemperature > 1650:
	
		ShieldXSid = ".18c"				

	for k,v in ShieldIsotopeMassFractions.items():

		ShieldIsotopeCoreMassFraction  = v * ShieldMassFraction

		if len(k) == 4:

			AA = k + ShieldXSid + "  -{0:02.5e}".format(ShieldIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ShieldXSid + " -{0:02.5e}".format(ShieldIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Cladding isotope (" + Cladding + ") \n"

	if CladdingTemperature <= 450:

		CladdingXSid = ".03c"

	elif CladdingTemperature > 450 and CladdingTemperature <= 750:

		CladdingXSid = ".06c"

	elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
	
		CladdingXSid = ".15c"	

	elif CladdingTemperature > 1650:
	
		CladdingXSid = ".18c"				

	CladdingMassDensityGCC   = {}
	CladdingCoreMassFraction = {}

	for k,v in CladdingIsotopeMassFractions.items():

		CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

		if len(k) == 4:

			AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)


	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)			

	mi.write("\n")
	mi.close()	

def belowcorecoolant(CoolantIsotopeMassFractions, SerpentAxialCoolantDensity, Coolant, 
	                 Name, ShieldOuterRadius, serpfilepath, SerpentAxialCoolantTemperature, outsidergb):

	mi = open(Name + "_nonfuel", 'a')

	LowerCoolantCellVolume = 2 * (ShieldOuterRadius ** 2) * math.pi

	#print(SerpentAxialCoolantTemperature)

	CoolantTemperature     = SerpentAxialCoolantTemperature[0]
	CoolantMassDensityGCC  = SerpentAxialCoolantDensity[0]
	CoreMassDensityGCC     = CoolantMassDensityGCC  
	CoolantMassFraction    = 1

	CoolantMass  = CoolantMassDensityGCC * LowerCoolantCellVolume / 1e3

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell belowcorecoolant                                                     \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")								
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(LowerCoolantCellVolume)           + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(2)                                  + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(ShieldOuterRadius*2)                + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Coolant    = {0:02.2%}".format(1)                                      + "\n")						
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")			
	mi.write("%    Coolant    = {0:02.2%}".format(1)                                      + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Cell total = {0:02.2f}".format(CoreMassDensityGCC)                     + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")							
	mi.write("%    Coolant    = {0:02.1f}".format(CoolantTemperature-273.15)              + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Coolant    = {0:02.2f}".format(SerpentAxialCoolantDensity[0])          + "\n")													
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")		
	mi.write("%    Coolant    = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * LowerCoolantCellVolume) + "\n")									
	mi.write("%                                                                              \n")
	mi.write("% ######################################################                       \n")
	mi.write("\n")		

	X1 = "mat belowcorecoolantmat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + outsidergb + "\n"

	mi.write(X1)
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)						

	mi.write("\n")
	mi.close()	


def shieldserpent(ShieldPinVolumeFraction, ShieldPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
				  DuctIsotopeMassFractions, ShieldIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
				  SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
				  SerpentAxialShieldDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
				  SerpentAxialDuctTemperature, serpfilepath, Name, CoreOuterRadius,
				  ShieldOuterRadius, FuelLength, ShieldPinOuterRadius, ShieldPinPitch, ShieldVolume, ReflectorOuterRadius,
				  outershieldrgb):

	mi = open(Name + "_nonfuel", 'a')

	ShieldPinVolumeFraction1 = ShieldPinVolumeFraction
	ShieldPinVolumeFraction  = ShieldPinVolumeFraction - DuctVolumeFraction - InterAssemblyVolumeFraction
	CoolantVolumeFraction    = - ShieldPinVolumeFraction * (ShieldPinVolumeFraction1-1) / ShieldPinVolumeFraction1

	for z in range(SerpentAxialZones):

		ShieldPinDensityGCC    = ShieldPinVolumeFraction  * SerpentAxialShieldDensity[z]
		CoolantMassDensityGCC  = CoolantVolumeFraction       * SerpentAxialCoolantDensity[z]
		DuctMassDensityGCC     = DuctVolumeFraction          * SerpentAxialDuctDensity[z]
		IAGapMassDensityGCC    = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[z]

		ShieldCellMassDensityGCC = ShieldPinDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC

		ShieldPinMassFraction    = ShieldPinDensityGCC / ShieldCellMassDensityGCC
		CoolantMassFraction      = CoolantMassDensityGCC  / ShieldCellMassDensityGCC
		DuctMassFraction         = DuctMassDensityGCC     / ShieldCellMassDensityGCC
		IAGapMassFraction        = IAGapMassDensityGCC    / ShieldCellMassDensityGCC      
		
		ShieldTemperature    = SerpentAxialDuctTemperature[z]
		CoolantTemperature   = SerpentAxialCoolantTemperature[z]
		IAGapTemperature     = SerpentAxialIAGapTemperature[z]
		DuctTemperature      = SerpentAxialDuctTemperature[z]

		mi.write("\n")
		mi.write("% ####################################################                      \n")
		mi.write("%                                                                           \n")			
		mi.write("%    Cell radialshield" + str(z+1) + "                                      \n")
		mi.write("%                                                                           \n")			
		mi.write("%    Materials                                                              \n")
		mi.write("%    -------------------------------------------------                      \n")	
		mi.write("%    Shield-pin: " + ShieldPinMaterial                                   + "\n")							
		mi.write("%    Coolant:    " + Coolant                                             + "\n")	
		mi.write("%    Duct:       " + Duct                                                + "\n")	
		mi.write("%                                                                           \n")
		mi.write("%    General geometry                                                       \n")
		mi.write("%    -------------------------------------------------                      \n")
		mi.write("%    Cell volume: {0:02.3f}".format(ShieldVolume)                   + " m^3 \n")
		mi.write("%    Axially between  z = 0 and " + str(FuelLength)                   + " m \n")
		mi.write("%    Radially between r = {0:02.3f}".format(ReflectorOuterRadius) + " and {0:02.3f}".format(ShieldOuterRadius) + " m \n")
		mi.write("%                                                                            \n")
		mi.write("%    Calculated geometry                                                     \n")
		mi.write("%    -------------------------------------------------                       \n")
		mi.write("%    Shield pin diameter: {0:02.3f}".format(ShieldPinOuterRadius*2) + " cm \n")		
		mi.write("%    Shield pin pitch:    {0:02.3f}".format(ShieldPinPitch)         + " cm \n")	
		mi.write("%    Shield pin P/D:      {0:02.3f}".format(ShieldPinPitch/(ShieldPinOuterRadius*2))   + " \n")					
		mi.write("%                                                                            \n")		
		mi.write("%    Mass fractions                                                          \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Shield-pin      = {0:02.2%}".format(ShieldPinMassFraction)           + "\n")
		mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)             + "\n")						
		mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
		mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
		mi.write("%                                                                            \n")							
		mi.write("%    Volume fractions                                                        \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Shield-pin      = {0:02.2%}".format(ShieldPinVolumeFraction) + " ({0:02.2%}".format(ShieldPinVolumeFraction1)   + " in-assembly) \n")
		mi.write("%    Active coolant  = {0:02.2%}".format(CoolantVolumeFraction)   + " ({0:02.2%}".format(1-ShieldPinVolumeFraction1) + " in-assembly) \n")				
		mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)              + "\n")
		mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)     + "\n")
		mi.write("%                                                                            \n")						
		mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Shield-pin   = {0:02.2f}".format(ShieldPinDensityGCC)                + "\n")
		mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)           + "\n")						
		mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)              + "\n")
		mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)             + "\n")
		mi.write("%    Cell total      = {0:02.2f}".format(ShieldCellMassDensityGCC)        + "\n")
		mi.write("%                                                                            \n")
		mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Shield-pin   = {0:02.1f}".format(ShieldTemperature-273.15)     + "\n")
		mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)       + "\n")						
		mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)          + "\n")
		mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)         + "\n")
		mi.write("%                                                                            \n")
		mi.write("%    Component density (g/cc)                                                \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Shield-pin  = {0:02.3f}".format(SerpentAxialShieldDensity[z])  + "\n")
		mi.write("%    Active coolant = {0:02.3f}".format(SerpentAxialCoolantDensity[z])    + "\n")
		mi.write("%    Duct           = {0:02.3f}".format(SerpentAxialDuctDensity[z])       + "\n")
		mi.write("%    IA-gap coolant = {0:02.3f}".format(SerpentAxialIAGapDensity[z])      + "\n")									
		mi.write("%                                                                            \n")
		mi.write("%    Component mass (kg/cell)                                                \n")			
		mi.write("%    -------------------------------------------------                       \n")	
		mi.write("%    Shield-pin     = {0:02.1f}".format(1e3 * ShieldPinDensityGCC   * ShieldVolume) + "\n")			
		mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * ShieldVolume)  + "\n")	
		mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC    * ShieldVolume)     + "\n")	
		mi.write("%    IA-gap coolant = {0:02.1f}".format(1e3 * IAGapMassDensityGCC   * ShieldVolume)    + "\n")									
		mi.write("%                                                                            \n")
		mi.write("% ######################################################                     \n")
		mi.write("\n")	

		X1 = "mat radialshieldmat" + str(z) + " -{0:02.5f}".format(ShieldCellMassDensityGCC) + " rgb " + outershieldrgb + "\n"

		mi.write(X1)

		if ShieldTemperature <= 450:

			ShieldXSid = ".03c"

		elif ShieldTemperature > 450 and ShieldTemperature <= 750:

			ShieldXSid = ".06c"

		elif ShieldTemperature > 750 and ShieldTemperature <= 1050:

			ShieldXSid = ".12c"

		elif ShieldTemperature > 1050 and ShieldTemperature <= 1350:

			ShieldXSid = ".12c"

		elif ShieldTemperature > 1350 and ShieldTemperature <= 1650:	
		
			ShieldXSid = ".15c"	

		elif ShieldTemperature > 1650:
		
			ShieldXSid = ".18c"	

		X1 = "Shield-pin isotope (" + ShieldPinMaterial + ") \n"

		for k,v in ShieldIsotopeMassFractions.items():

			ShieldIsotopeCoreMassFraction  = v * ShieldPinMassFraction

			if len(k) == 4:

				AA = k + ShieldXSid + "  -{0:02.5e}".format(ShieldIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + ShieldXSid + " -{0:02.5e}".format(ShieldIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)

		X1 = "Coolant isotope (" + Coolant + ") \n"

		if CoolantTemperature <= 450:

			CoolantXSid = ".03c"

		elif CoolantTemperature > 450 and CoolantTemperature <= 750:

			CoolantXSid = ".06c"

		elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

			CoolantXSid = ".12c"

		elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

			CoolantXSid = ".12c"

		elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
		
			CoolantXSid = ".15c"	

		elif CoolantTemperature > 1650:
		
			CoolantXSid = ".18c"				

		for k,v in CoolantIsotopeMassFractions.items():

			CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

			if len(k) == 4:

				AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)				

		X1 = "Duct isotope (" + Duct + ") \n"

		if DuctTemperature <= 450:

			DuctXSid = ".03c"

		elif DuctTemperature > 450 and DuctTemperature <= 750:

			DuctXSid = ".06c"

		elif DuctTemperature > 750 and DuctTemperature <= 1050:

			DuctXSid = ".12c"

		elif DuctTemperature > 1050 and DuctTemperature <= 1350:

			DuctXSid = ".12c"

		elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
		
			DuctXSid = ".15c"	

		elif DuctTemperature > 1650:
		
			DuctXSid = ".18c"				

		for k,v in DuctIsotopeMassFractions.items():

			DuctIsotopeCoreMassFraction  = v * DuctMassFraction

			if len(k) == 4:

				AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)

		X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

		if IAGapTemperature <= 450:

			IAGapXSid = ".03c"

		elif IAGapTemperature > 450 and IAGapTemperature <= 750:

			IAGapXSid = ".06c"

		elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

			IAGapXSid = ".12c"

		elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

			IAGapXSid = ".12c"

		elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
		
			IAGapXSid = ".15c"	

		elif IAGapTemperature > 1650:
		
			IAGapXSid = ".18c"				

		for k,v in CoolantIsotopeMassFractions.items():

			IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

			if len(k) == 4:

				AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
			
			else:

				AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

			mi.write(AA)

	mi.write("\n")
	mi.close()			


def abovecorecoolant(CoolantIsotopeMassFractions, SerpentAxialCoolantDensity, Coolant, 
	                 Name, ShieldOuterRadius, serpfilepath, SerpentAxialCoolantTemperature,
	                 SerpentTemperaturePoints, outsidergb):

	mi = open(Name + "_nonfuel", 'a')

	UpperCoolantCellVolume = 2 * (ShieldOuterRadius ** 2) * math.pi

	x = len(SerpentTemperaturePoints)

	CoolantTemperature     = SerpentAxialCoolantTemperature[x-1]
	CoolantMassDensityGCC  = SerpentAxialCoolantDensity[x-1]
	CoreMassDensityGCC     = CoolantMassDensityGCC  
	CoolantMassFraction    = 1

	CoolantMass  = CoolantMassDensityGCC * UpperCoolantCellVolume / 1e3

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell abovecorecoolant                                                     \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")								
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(UpperCoolantCellVolume)           + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(2)                                  + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(ShieldOuterRadius*2)                + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Coolant    = {0:02.2%}".format(1)                                      + "\n")						
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")			
	mi.write("%    Coolant    = {0:02.2%}".format(1)                                      + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Cell total = {0:02.2f}".format(CoreMassDensityGCC)                     + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")							
	mi.write("%    Coolant    = {0:02.1f}".format(CoolantTemperature-273.15)              + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Coolant    = {0:02.2f}".format(SerpentAxialCoolantDensity[x-1])        + "\n")													
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")		
	mi.write("%    Coolant    = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * UpperCoolantCellVolume) + "\n")									
	mi.write("%                                                                              \n")
	mi.write("% ######################################################                       \n")
	mi.write("\n")		

	X1 = "mat abovecorecoolantmat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + outsidergb + " \n"

	mi.write(X1)
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)						

	mi.write("\n")
	mi.close()	

def outsidecorecoolant(CoolantIsotopeMassFractions, SerpentAxialCoolantDensity, Coolant, 
	                   Name, ShieldOuterRadius, serpfilepath, SerpentAxialCoolantTemperature,
	                   SerpentTemperaturePoints, SystemOuterRadius, CoolantAverageTemperature, outsidergb):

	mi = open(Name + "_nonfuel", 'a')

	OutsideCoolantCellVolume = 2 * (SystemOuterRadius ** 2) * math.pi

	x = len(SerpentTemperaturePoints)

	AveDens = (SerpentAxialCoolantDensity[0] + SerpentAxialCoolantDensity[x-1]) / 2

	CoolantTemperature     = CoolantAverageTemperature
	CoolantMassDensityGCC  = AveDens
	CoreMassDensityGCC     = CoolantMassDensityGCC  
	CoolantMassFraction    = 1

	CoolantMass  = CoolantMassDensityGCC * OutsideCoolantCellVolume / 1e3

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell abovecorecoolant                                                     \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")								
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(OutsideCoolantCellVolume)           + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(2)                                  + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(ShieldOuterRadius*2)                + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Coolant    = {0:02.2%}".format(1)                                      + "\n")						
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")			
	mi.write("%    Coolant    = {0:02.2%}".format(1)                                      + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Cell total = {0:02.2f}".format(CoreMassDensityGCC)                     + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")							
	mi.write("%    Coolant    = {0:02.1f}".format(CoolantTemperature-273.15)              + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Coolant    = {0:02.2f}".format(AveDens)                                + "\n")													
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")		
	mi.write("%    Coolant    = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * OutsideCoolantCellVolume) + "\n")									
	mi.write("%                                                                              \n")
	mi.write("% ######################################################                       \n")
	mi.write("\n")		

	X1 = "mat outsidecoolantmat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + outsidergb + " \n"

	mi.write(X1)
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)						

	mi.write("\n")
	mi.close()	



def belowcorerefl(ReflectorPinVolumeFraction, ReflectorPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
				  DuctIsotopeMassFractions, ReflectorIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
				  SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
				  SerpentAxialReflectorDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
				  SerpentAxialDuctTemperature, serpfilepath, Name, ReflectorVolume, CoreOuterRadius,
				  ReflectorOuterRadius, FuelLength, ReflectorPinOuterRadius, ReflectorPinPitch, BelowCoreSerpentLength,
				  outerreflrgb):

	mi = open(Name + "_nonfuel", 'a')

	ReflectorPinVolumeFraction1 = ReflectorPinVolumeFraction
	ReflectorPinVolumeFraction  = ReflectorPinVolumeFraction - DuctVolumeFraction - InterAssemblyVolumeFraction
	CoolantVolumeFraction       = - ReflectorPinVolumeFraction * (ReflectorPinVolumeFraction1-1) / ReflectorPinVolumeFraction1

	ReflectorPinDensityGCC = ReflectorPinVolumeFraction  * SerpentAxialReflectorDensity[0]
	CoolantMassDensityGCC  = CoolantVolumeFraction       * SerpentAxialCoolantDensity[0]
	DuctMassDensityGCC     = DuctVolumeFraction          * SerpentAxialDuctDensity[0]
	IAGapMassDensityGCC    = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[0]

	ReflectorCellMassDensityGCC = ReflectorPinDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC

	ReflectorPinMassFraction = ReflectorPinDensityGCC / ReflectorCellMassDensityGCC
	CoolantMassFraction      = CoolantMassDensityGCC  / ReflectorCellMassDensityGCC
	DuctMassFraction         = DuctMassDensityGCC     / ReflectorCellMassDensityGCC
	IAGapMassFraction        = IAGapMassDensityGCC    / ReflectorCellMassDensityGCC      
	
	ReflectorTemperature = SerpentAxialDuctTemperature[0]
	CoolantTemperature   = SerpentAxialCoolantTemperature[0]
	IAGapTemperature     = SerpentAxialIAGapTemperature[0]
	DuctTemperature      = SerpentAxialDuctTemperature[0]

	BelowCoreReflectorVolume = BelowCoreSerpentLength * (  math.pi * ReflectorOuterRadius ** 2 - math.pi * CoreOuterRadius ** 2  )


	mi.write("\n")
	mi.write("% ####################################################                      \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Cell belowcoreradialreflector                                          \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Materials                                                              \n")
	mi.write("%    -------------------------------------------------                      \n")	
	mi.write("%    Reflector-pin: " + ReflectorPinMaterial                             + "\n")							
	mi.write("%    Coolant:       " + Coolant                                          + "\n")	
	mi.write("%    Duct:          " + Duct                                             + "\n")	
	mi.write("%                                                                           \n")
	mi.write("%    General geometry                                                       \n")
	mi.write("%    -------------------------------------------------                      \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(BelowCoreReflectorVolume)      + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(BelowCoreSerpentLength)        + " m   \n")	
	mi.write("%    Radially between r = {0:02.3f}".format(CoreOuterRadius) + " and {0:02.3f}".format(ReflectorOuterRadius) + " m \n")
	mi.write("%                                                                            \n")
	mi.write("%    Calculated geometry                                                     \n")
	mi.write("%    -------------------------------------------------                       \n")
	mi.write("%    Reflector pin diameter: {0:02.3f}".format(ReflectorPinOuterRadius*2)   + " cm \n")		
	mi.write("%    Reflector pin pitch:    {0:02.3f}".format(ReflectorPinPitch)        + " cm \n")	
	mi.write("%    Reflector pin P/D:      {0:02.3f}".format(ReflectorPinPitch/(ReflectorPinOuterRadius*2))   + " \n")					
	mi.write("%                                                                            \n")		
	mi.write("%    Mass fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.2%}".format(ReflectorPinMassFraction)        + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)             + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
	mi.write("%                                                                            \n")							
	mi.write("%    Volume fractions                                                        \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.2%}".format(ReflectorPinVolumeFraction) + " ({0:02.2%}".format(ReflectorPinVolumeFraction1)   + " in-assembly) \n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantVolumeFraction)      + " ({0:02.2%}".format(1-ReflectorPinVolumeFraction1) + " in-assembly) \n")				
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)         + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)               + "\n")
	mi.write("%                                                                            \n")						
	mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.2f}".format(ReflectorPinDensityGCC)          + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)           + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)              + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)             + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(ReflectorCellMassDensityGCC)     + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.1f}".format(ReflectorTemperature-273.15)     + "\n")
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)       + "\n")						
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)          + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)         + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Component density (g/cc)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin  = {0:02.3f}".format(SerpentAxialReflectorDensity[0])  + "\n")
	mi.write("%    Active coolant = {0:02.3f}".format(SerpentAxialCoolantDensity[0])    + "\n")
	mi.write("%    Duct           = {0:02.3f}".format(SerpentAxialDuctDensity[0])       + "\n")
	mi.write("%    IA-gap coolant = {0:02.3f}".format(SerpentAxialIAGapDensity[0])      + "\n")									
	mi.write("%                                                                            \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin  = {0:02.1f}".format(1e3 * ReflectorPinDensityGCC * ReflectorVolume) + "\n")			
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * ReflectorVolume)  + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC * ReflectorVolume)     + "\n")	
	mi.write("%    IA-gap coolant = {0:02.1f}".format(1e3 * IAGapMassDensityGCC * ReflectorVolume)    + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")	

	X1 = "mat belowcoreradialreflectormat -{0:02.5f}".format(ReflectorCellMassDensityGCC) + " rgb " + outerreflrgb + "\n"

	mi.write(X1)

	if ReflectorTemperature <= 450:

		ReflectorXSid = ".03c"

	elif ReflectorTemperature > 450 and ReflectorTemperature <= 750:

		ReflectorXSid = ".06c"

	elif ReflectorTemperature > 750 and ReflectorTemperature <= 1050:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1050 and ReflectorTemperature <= 1350:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1350 and ReflectorTemperature <= 1650:	
	
		ReflectorXSid = ".15c"	

	elif ReflectorTemperature > 1650:
	
		ReflectorXSid = ".18c"	

	X1 = "Reflector-pin isotope (" + ReflectorPinMaterial + ") \n"

	for k,v in ReflectorIsotopeMassFractions.items():

		ReflectorIsotopeCoreMassFraction  = v * ReflectorPinMassFraction

		if len(k) == 4:

			AA = k + ReflectorXSid + "  -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ReflectorXSid + " -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	

	mi.write("\n")
	mi.close()

def belowcoreradialshield(ShieldPinVolumeFraction, ShieldPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
				  		  DuctIsotopeMassFractions, ShieldIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
				  		  SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
				  		  SerpentAxialShieldDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
				  		  SerpentAxialDuctTemperature, serpfilepath, Name, CoreOuterRadius, ShieldOuterRadius, FuelLength, 
				  		  ShieldPinOuterRadius, ShieldPinPitch, ShieldVolume, ReflectorOuterRadius, BelowCoreSerpentLength,
				  		  outershieldrgb):

	mi = open(Name + "_nonfuel", 'a')

	ShieldPinVolumeFraction1 = ShieldPinVolumeFraction
	ShieldPinVolumeFraction  = ShieldPinVolumeFraction - DuctVolumeFraction - InterAssemblyVolumeFraction
	CoolantVolumeFraction    = - ShieldPinVolumeFraction * (ShieldPinVolumeFraction1-1) / ShieldPinVolumeFraction1

	ShieldPinDensityGCC    = ShieldPinVolumeFraction  * SerpentAxialShieldDensity[0]
	CoolantMassDensityGCC  = CoolantVolumeFraction       * SerpentAxialCoolantDensity[0]
	DuctMassDensityGCC     = DuctVolumeFraction          * SerpentAxialDuctDensity[0]
	IAGapMassDensityGCC    = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[0]

	ShieldCellMassDensityGCC = ShieldPinDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC

	ShieldPinMassFraction    = ShieldPinDensityGCC / ShieldCellMassDensityGCC
	CoolantMassFraction      = CoolantMassDensityGCC  / ShieldCellMassDensityGCC
	DuctMassFraction         = DuctMassDensityGCC     / ShieldCellMassDensityGCC
	IAGapMassFraction        = IAGapMassDensityGCC    / ShieldCellMassDensityGCC      
	
	ShieldTemperature    = SerpentAxialDuctTemperature[0]
	CoolantTemperature   = SerpentAxialCoolantTemperature[0]
	IAGapTemperature     = SerpentAxialIAGapTemperature[0]
	DuctTemperature      = SerpentAxialDuctTemperature[0]

	BelowCoreShieldVolume = BelowCoreSerpentLength * (  math.pi * ShieldOuterRadius ** 2  - math.pi * ReflectorOuterRadius ** 2  )

	mi.write("\n")
	mi.write("% ####################################################                      \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Cell belowcoreradialshield                                             \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Materials                                                              \n")
	mi.write("%    -------------------------------------------------                      \n")	
	mi.write("%    Shield-pin: " + ShieldPinMaterial                                   + "\n")							
	mi.write("%    Coolant:    " + Coolant                                             + "\n")	
	mi.write("%    Duct:       " + Duct                                                + "\n")	
	mi.write("%                                                                           \n")
	mi.write("%    General geometry                                                       \n")
	mi.write("%    -------------------------------------------------                      \n")
	mi.write("%    Cell volume: {0:02.3f}".format(ShieldVolume)                   + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(BelowCoreSerpentLength)        + " m   \n")	
	mi.write("%    Radially between r = {0:02.3f}".format(ReflectorOuterRadius) + " and {0:02.3f}".format(ShieldOuterRadius) + " m \n")
	mi.write("%                                                                            \n")
	mi.write("%    Calculated geometry                                                     \n")
	mi.write("%    -------------------------------------------------                       \n")
	mi.write("%    Shield pin diameter: {0:02.3f}".format(ShieldPinOuterRadius*2) + " cm \n")		
	mi.write("%    Shield pin pitch:    {0:02.3f}".format(ShieldPinPitch)         + " cm \n")	
	mi.write("%    Shield pin P/D:      {0:02.3f}".format(ShieldPinPitch/(ShieldPinOuterRadius*2))   + " \n")					
	mi.write("%                                                                            \n")		
	mi.write("%    Mass fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.2%}".format(ShieldPinMassFraction)           + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)             + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
	mi.write("%                                                                            \n")							
	mi.write("%    Volume fractions                                                        \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.2%}".format(ShieldPinVolumeFraction) + " ({0:02.2%}".format(ShieldPinVolumeFraction1)   + " in-assembly) \n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantVolumeFraction)   + " ({0:02.2%}".format(1-ShieldPinVolumeFraction1) + " in-assembly) \n")				
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)              + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)     + "\n")
	mi.write("%                                                                            \n")						
	mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.2f}".format(ShieldPinDensityGCC)                + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)           + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)              + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)             + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(ShieldCellMassDensityGCC)        + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.1f}".format(ShieldTemperature-273.15)     + "\n")
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)       + "\n")						
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)          + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)         + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Component density (g/cc)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin     = {0:02.3f}".format(SerpentAxialShieldDensity[0])  + "\n")
	mi.write("%    Active coolant = {0:02.3f}".format(SerpentAxialCoolantDensity[0])    + "\n")
	mi.write("%    Duct           = {0:02.3f}".format(SerpentAxialDuctDensity[0])       + "\n")
	mi.write("%    IA-gap coolant = {0:02.3f}".format(SerpentAxialIAGapDensity[0])      + "\n")									
	mi.write("%                                                                            \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin     = {0:02.1f}".format(1e3 * ShieldPinDensityGCC   * ShieldVolume) + "\n")			
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * ShieldVolume)  + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC    * ShieldVolume)     + "\n")	
	mi.write("%    IA-gap coolant = {0:02.1f}".format(1e3 * IAGapMassDensityGCC   * ShieldVolume)    + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")	

	X1 = "mat belowcoreradialshieldmat -{0:02.5f}".format(ShieldCellMassDensityGCC) + " rgb " + outershieldrgb + "\n"

	mi.write(X1)

	if ShieldTemperature <= 450:

		ShieldXSid = ".03c"

	elif ShieldTemperature > 450 and ShieldTemperature <= 750:

		ShieldXSid = ".06c"

	elif ShieldTemperature > 750 and ShieldTemperature <= 1050:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1050 and ShieldTemperature <= 1350:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1350 and ShieldTemperature <= 1650:	
	
		ShieldXSid = ".15c"	

	elif ShieldTemperature > 1650:
	
		ShieldXSid = ".18c"	

	X1 = "Shield-pin isotope (" + ShieldPinMaterial + ") \n"

	for k,v in ShieldIsotopeMassFractions.items():

		ShieldIsotopeCoreMassFraction  = v * ShieldPinMassFraction

		if len(k) == 4:

			AA = k + ShieldXSid + "  -{0:02.5e}".format(ShieldIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ShieldXSid + " -{0:02.5e}".format(ShieldIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	mi.write("\n")
	mi.close()				

def upperreflector(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
				   ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
				   CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
				   CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
				   SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
				   SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
				   SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
				   SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
				   serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, UpperReflectorLength,
				   CoreOuterRadius, Cladding, Coolant, Duct, ReflectorPinMaterial, SerpentAxialReflectorDensity,
				   ReflectorIsotopeMassFractions, SerpentTemperaturePoints, innerreflrgb):

	mi = open(Name + "_nonfuel", 'a')

	UpperReflectorCellVolume = UpperReflectorLength * (CoreOuterRadius ** 2) * math.pi

	x = len(SerpentTemperaturePoints)

	ReflectorTemperature = SerpentAxialCladdingTemperature[x-1]
	CladdingTemperature  = SerpentAxialCladdingTemperature[x-1]
	CoolantTemperature   = SerpentAxialCoolantTemperature[x-1]
	IAGapTemperature     = SerpentAxialIAGapTemperature[x-1]
	DuctTemperature      = SerpentAxialDuctTemperature[x-1]

	ReflectorMassDensityGCC     = (FuelVolumeFraction + GapVolumeFraction) * SerpentAxialReflectorDensity[x-1]
	CladdingMassDensityGCC      = CladdingVolumeFraction      * SerpentAxialCladdingDensity[x-1]
	CoolantMassDensityGCC       = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[x-1]
	DuctMassDensityGCC          = DuctVolumeFraction          * SerpentAxialDuctDensity[x-1]
	IAGapMassDensityGCC         = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[x-1]
	CoreMassDensityGCC          = ReflectorMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

	ReflectorMass     = ReflectorMassDensityGCC     * UpperReflectorCellVolume / 1e3
	CladdingMass      = CladdingMassDensityGCC      * UpperReflectorCellVolume / 1e3
	ActiveCoolantMass = CoolantMassDensityGCC       * UpperReflectorCellVolume / 1e3
	DuctMass          = DuctMassDensityGCC          * UpperReflectorCellVolume / 1e3
	IAGapMass         = IAGapMassDensityGCC         * UpperReflectorCellVolume / 1e3
	CoreMass          = CoreMassDensityGCC          * UpperReflectorCellVolume / 1e3

	ReflectorMassFraction     = ReflectorMassDensityGCC     /  CoreMassDensityGCC
	CladdingMassFraction      = CladdingMassDensityGCC      /  CoreMassDensityGCC
	CoolantMassFraction       = CoolantMassDensityGCC       /  CoreMassDensityGCC
	DuctMassFraction          = DuctMassDensityGCC          /  CoreMassDensityGCC
	IAGapMassFraction         = IAGapMassDensityGCC         /  CoreMassDensityGCC

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell upperreflector                                                       \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector: " + ReflectorPinMaterial                                    + "\n")
	mi.write("%    Cladding:  " + Cladding                                                + "\n")							
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%    Duct:      " + Duct                                                    + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(UpperReflectorCellVolume)         + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(UpperReflectorLength)               + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(CoreOuterRadius*2)                  + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2%}".format(ReflectorMassFraction)             + "\n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)              + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)               + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                  + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)                 + "\n")
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2%}".format(FuelVolumeFraction + GapVolumeFraction) + " \n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)            + "\n")				
	mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)       + "\n")
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)       + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2f}".format(ReflectorMassDensityGCC)           + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(CladdingMassDensityGCC)            + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)             + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)               + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(CoreMassDensityGCC)                + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.1f}".format(ReflectorTemperature-273.15)       + "\n")
	mi.write("%    Cladding        = {0:02.1f}".format(CladdingTemperature-273.15)        + "\n")						
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)         + "\n")
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)            + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)           + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Reflector       = {0:02.2f}".format(SerpentAxialReflectorDensity[x-1])   + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(SerpentAxialCladdingDensity[x-1])    + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(SerpentAxialCoolantDensity[x-1])     + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(SerpentAxialDuctDensity[x-1])        + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(SerpentAxialIAGapDensity[x-1])       + "\n")							
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector      = {0:02.1f}".format(1e3 * ReflectorMassDensityGCC * UpperReflectorCellVolume) + "\n")			
	mi.write("%    Cladding       = {0:02.1f}".format(1e3 * CladdingMassDensityGCC  * UpperReflectorCellVolume) + "\n")	
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC   * UpperReflectorCellVolume) + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC      * UpperReflectorCellVolume) + "\n")
	mi.write("%    IA-gap         = {0:02.1f}".format(1e3 * IAGapMassDensityGCC     * UpperReflectorCellVolume) + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")		

	X1 = "mat upperreflectormat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + innerreflrgb + "\n"

	mi.write(X1)

	X1 = "Reflector isotope (" + ReflectorPinMaterial + ") \n"

	if ReflectorTemperature <= 450:

		ReflectorXSid = ".03c"

	elif ReflectorTemperature > 450 and ReflectorTemperature <= 750:

		ReflectorXSid = ".06c"

	elif ReflectorTemperature > 750 and ReflectorTemperature <= 1050:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1050 and ReflectorTemperature <= 1350:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1350 and ReflectorTemperature <= 1650:	
	
		ReflectorXSid = ".15c"	

	elif ReflectorTemperature > 1650:
	
		ReflectorXSid = ".18c"				

	for k,v in ReflectorIsotopeMassFractions.items():

		ReflectorIsotopeCoreMassFraction  = v * ReflectorMassFraction

		if len(k) == 4:

			AA = k + ReflectorXSid + "  -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ReflectorXSid + " -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Cladding isotope (" + Cladding + ") \n"

	if CladdingTemperature <= 450:

		CladdingXSid = ".03c"

	elif CladdingTemperature > 450 and CladdingTemperature <= 750:

		CladdingXSid = ".06c"

	elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
	
		CladdingXSid = ".15c"	

	elif CladdingTemperature > 1650:
	
		CladdingXSid = ".18c"				

	CladdingMassDensityGCC   = {}
	CladdingCoreMassFraction = {}

	for k,v in CladdingIsotopeMassFractions.items():

		CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

		if len(k) == 4:

			AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)


	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)			

	mi.write("\n")
	mi.close()		

def uppergasplenum(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
				   ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
				   CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
				   CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
				   SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
				   SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
				   SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
				   SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
				   serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, UpperGasPlenumLength,
				   CoreOuterRadius, Cladding, Coolant, Duct, SerpentTemperaturePoints, gasrgb):

	mi = open(Name + "_nonfuel", 'a')

	UGPCellVolume = UpperGasPlenumLength * (CoreOuterRadius ** 2) * math.pi

	x = len(SerpentTemperaturePoints)

	GasTemperature       = SerpentAxialCladdingTemperature[x-1] + 7.25
	CladdingTemperature  = SerpentAxialCladdingTemperature[x-1]
	CoolantTemperature   = SerpentAxialCoolantTemperature[x-1]
	IAGapTemperature     = SerpentAxialIAGapTemperature[x-1]
	DuctTemperature      = SerpentAxialDuctTemperature[x-1]

	R   = 8.3144621
	AHe = 4.0026032
	GasPressure = 2e6
	GasDensity = (GasPressure * GasTemperature / 273.15) / R / GasTemperature * AHe / 1e6

	GasMassDensityGCC           = (FuelVolumeFraction + GapVolumeFraction) * GasDensity
	CladdingMassDensityGCC      = CladdingVolumeFraction      * SerpentAxialCladdingDensity[x-1]
	CoolantMassDensityGCC       = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[x-1]
	DuctMassDensityGCC          = DuctVolumeFraction          * SerpentAxialDuctDensity[x-1]
	IAGapMassDensityGCC         = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[x-1]
	CoreMassDensityGCC          = GasMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

	GasMass           = GasMassDensityGCC           * UGPCellVolume / 1e3
	CladdingMass      = CladdingMassDensityGCC      * UGPCellVolume / 1e3
	ActiveCoolantMass = CoolantMassDensityGCC       * UGPCellVolume / 1e3
	DuctMass          = DuctMassDensityGCC          * UGPCellVolume / 1e3
	IAGapMass         = IAGapMassDensityGCC         * UGPCellVolume / 1e3
	CoreMass          = CoreMassDensityGCC          * UGPCellVolume / 1e3

	GasMassFraction           = GasMassDensityGCC           /  CoreMassDensityGCC
	CladdingMassFraction      = CladdingMassDensityGCC      /  CoreMassDensityGCC
	CoolantMassFraction       = CoolantMassDensityGCC       /  CoreMassDensityGCC
	DuctMassFraction          = DuctMassDensityGCC          /  CoreMassDensityGCC
	IAGapMassFraction         = IAGapMassDensityGCC         /  CoreMassDensityGCC

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell uppergasplenum                                                       \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Cladding: " + Cladding                                                 + "\n")							
	mi.write("%    Coolant:  " + Coolant                                                  + "\n")	
	mi.write("%    Duct:     " + Duct                                                     + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(UGPCellVolume)                    + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(UpperGasPlenumLength)               + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(CoreOuterRadius*2)                  + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2%}".format(GasMassFraction)                   + "\n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)              + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)               + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                  + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)                 + "\n")
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2%}".format(FuelVolumeFraction + GapVolumeFraction) + " \n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)            + "\n")				
	mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)       + "\n")
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)       + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2f}".format(GasMassDensityGCC)                 + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(CladdingMassDensityGCC)            + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)             + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)               + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(CoreMassDensityGCC)                + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.1f}".format(GasTemperature-273.15)             + "\n")
	mi.write("%    Cladding        = {0:02.1f}".format(CladdingTemperature-273.15)        + "\n")						
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)         + "\n")
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)            + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)           + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Fission gas     = {0:02.2f}".format(GasDensity)                        + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(SerpentAxialCladdingDensity[x-1])    + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(SerpentAxialCoolantDensity[x-1])     + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(SerpentAxialDuctDensity[x-1])        + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(SerpentAxialIAGapDensity[x-1])       + "\n")							
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Fission gas    = {0:02.1f}".format(1e3 * GasMassDensityGCC      * UGPCellVolume) + "\n")			
	mi.write("%    Cladding       = {0:02.1f}".format(1e3 * CladdingMassDensityGCC * UGPCellVolume) + "\n")	
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC  * UGPCellVolume) + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC     * UGPCellVolume) + "\n")
	mi.write("%    IA-gap         = {0:02.1f}".format(1e3 * IAGapMassDensityGCC    * UGPCellVolume) + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")		

	X1 = "mat uppergasplenummat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + gasrgb + " \n"

	mi.write(X1)
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * (CoolantMassFraction + GasMassFraction)

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Cladding isotope (" + Cladding + ") \n"

	if CladdingTemperature <= 450:

		CladdingXSid = ".03c"

	elif CladdingTemperature > 450 and CladdingTemperature <= 750:

		CladdingXSid = ".06c"

	elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
	
		CladdingXSid = ".15c"	

	elif CladdingTemperature > 1650:
	
		CladdingXSid = ".18c"				

	CladdingMassDensityGCC   = {}
	CladdingCoreMassFraction = {}

	for k,v in CladdingIsotopeMassFractions.items():

		CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

		if len(k) == 4:

			AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)


	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	

	mi.write("\n")
	mi.close()

def uppershield(FuelVolumeFraction, GapVolumeFraction, CladdingVolumeFraction, WireVolumeFraction,
				ActiveCoolantVolumeFraction, DuctVolumeFraction, InterAssemblyVolumeFraction, 
				CladdingIsotopeMassFractions, CladdingAverageAtomicMass, DuctIsotopeMassFractions, 
				CoolantIsotopeMassFractions, BondIsotopeMassFractions, SerpentAxialCoolantDensity, 
				SerpentAxialIAGapDensity, SerpentAxialCladdingDensity, SerpentAxialDuctDensity, 
				SerpentAxialBondDensity, SerpentAxialFuelDensity, SerpentAxialZones, Batches, 
				SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature, 
				SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature, 
				serpfilepath, Name, ColdFillGasPressure, CoolantInletTemperature, UpperShieldLength,
				CoreOuterRadius, Cladding, Coolant, Duct, ShieldPinMaterial, SerpentAxialShieldDensity,
				ShieldIsotopeMassFractions, SerpentTemperaturePoints, innershieldrgb):

	mi = open(Name + "_nonfuel", 'a')

	UpperShieldCellVolume = UpperShieldLength * (CoreOuterRadius ** 2) * math.pi

	x = len(SerpentTemperaturePoints)

	ShieldTemperature    = SerpentAxialCladdingTemperature[x-1]
	CladdingTemperature  = SerpentAxialCladdingTemperature[x-1]
	CoolantTemperature   = SerpentAxialCoolantTemperature[x-1]
	IAGapTemperature     = SerpentAxialIAGapTemperature[x-1]
	DuctTemperature      = SerpentAxialDuctTemperature[x-1]

	ShieldMassDensityGCC     = (FuelVolumeFraction + GapVolumeFraction) * SerpentAxialShieldDensity[x-1]
	CladdingMassDensityGCC   = CladdingVolumeFraction      * SerpentAxialCladdingDensity[x-1]
	CoolantMassDensityGCC    = ActiveCoolantVolumeFraction * SerpentAxialCoolantDensity[x-1]
	DuctMassDensityGCC       = DuctVolumeFraction          * SerpentAxialDuctDensity[x-1]
	IAGapMassDensityGCC      = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[x-1]
	CoreMassDensityGCC       = ShieldMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC        

	ShieldMass        = ShieldMassDensityGCC   * UpperShieldCellVolume / 1e3
	CladdingMass      = CladdingMassDensityGCC * UpperShieldCellVolume / 1e3
	ActiveCoolantMass = CoolantMassDensityGCC  * UpperShieldCellVolume / 1e3
	DuctMass          = DuctMassDensityGCC     * UpperShieldCellVolume / 1e3
	IAGapMass         = IAGapMassDensityGCC    * UpperShieldCellVolume / 1e3
	CoreMass          = CoreMassDensityGCC     * UpperShieldCellVolume / 1e3

	ShieldMassFraction     = ShieldMassDensityGCC     /  CoreMassDensityGCC
	CladdingMassFraction   = CladdingMassDensityGCC   /  CoreMassDensityGCC
	CoolantMassFraction    = CoolantMassDensityGCC    /  CoreMassDensityGCC
	DuctMassFraction       = DuctMassDensityGCC       /  CoreMassDensityGCC
	IAGapMassFraction      = IAGapMassDensityGCC      /  CoreMassDensityGCC

	mi.write("% ####################################################                         \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Cell uppershield                                                          \n")
	mi.write("%                                                                              \n")			
	mi.write("%    Materials                                                                 \n")
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield:    " + ShieldPinMaterial                                       + "\n")
	mi.write("%    Cladding:  " + Cladding                                                + "\n")							
	mi.write("%    Coolant:   " + Coolant                                                 + "\n")	
	mi.write("%    Duct:      " + Duct                                                    + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    General geometry                                                          \n")
	mi.write("%    -------------------------------------------------                         \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(UpperShieldCellVolume)            + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(UpperShieldLength)                  + " m \n")
	mi.write("%    Diameter:     {0:02.3f}".format(CoreOuterRadius*2)                  + " m \n")
	mi.write("%                                                                              \n")	
	mi.write("%    Mass fractions                                                            \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2%}".format(ShieldMassFraction)                + "\n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingMassFraction)              + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)               + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                  + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)                 + "\n")
	mi.write("%                                                                              \n")							
	mi.write("%    Volume fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2%}".format(FuelVolumeFraction + GapVolumeFraction) + " \n")
	mi.write("%    Cladding        = {0:02.2%}".format(CladdingVolumeFraction)            + "\n")				
	mi.write("%    Active coolant  = {0:02.2%}".format(ActiveCoolantVolumeFraction)       + "\n")
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)       + "\n")				
	mi.write("%                                                                              \n")	
	mi.write("%    Cell-averaged mass density (g/cc)                                         \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2f}".format(ShieldMassDensityGCC)              + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(CladdingMassDensityGCC)            + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)             + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)               + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(CoreMassDensityGCC)                + "\n")
	mi.write("%                                                                              \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                       \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.1f}".format(ShieldTemperature-273.15)          + "\n")
	mi.write("%    Cladding        = {0:02.1f}".format(CladdingTemperature-273.15)        + "\n")						
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)         + "\n")
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)            + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)           + "\n")	
	mi.write("%                                                                              \n")
	mi.write("%    Component density (g/cc)                                                  \n")			
	mi.write("%    -------------------------------------------------                         \n")	
	mi.write("%    Shield          = {0:02.2f}".format(SerpentAxialShieldDensity[x-1])      + "\n")
	mi.write("%    Cladding        = {0:02.2f}".format(SerpentAxialCladdingDensity[x-1])    + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(SerpentAxialCoolantDensity[x-1])     + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(SerpentAxialDuctDensity[x-1])        + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(SerpentAxialIAGapDensity[x-1])       + "\n")							
	mi.write("%                                                                              \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield         = {0:02.1f}".format(1e3 * ShieldMassDensityGCC    * UpperShieldCellVolume) + "\n")			
	mi.write("%    Cladding       = {0:02.1f}".format(1e3 * CladdingMassDensityGCC  * UpperShieldCellVolume) + "\n")	
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC   * UpperShieldCellVolume) + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC      * UpperShieldCellVolume) + "\n")
	mi.write("%    IA-gap         = {0:02.1f}".format(1e3 * IAGapMassDensityGCC     * UpperShieldCellVolume) + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")		

	X1 = "mat uppershieldmat -{0:02.5f}".format(CoreMassDensityGCC) + " rgb " + innershieldrgb + " \n"

	mi.write(X1)

	X1 = "Shield isotope (" + ShieldPinMaterial + ") \n"

	if ShieldTemperature <= 450:

		ShieldXSid = ".03c"

	elif ShieldTemperature > 450 and ShieldTemperature <= 750:

		ShieldXSid = ".06c"

	elif ShieldTemperature > 750 and ShieldTemperature <= 1050:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1050 and ShieldTemperature <= 1350:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1350 and ShieldTemperature <= 1650:	
	
		ShieldXSid = ".15c"	

	elif ShieldTemperature > 1650:
	
		ShieldXSid = ".18c"				

	for k,v in ShieldIsotopeMassFractions.items():

		ShieldIsotopeCoreMassFraction  = v * ShieldMassFraction

		if len(k) == 4:

			AA = k + ShieldXSid + "  -{0:02.5e}".format(ShieldIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ShieldXSid + " -{0:02.5e}".format(ShieldIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	
	
	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Cladding isotope (" + Cladding + ") \n"

	if CladdingTemperature <= 450:

		CladdingXSid = ".03c"

	elif CladdingTemperature > 450 and CladdingTemperature <= 750:

		CladdingXSid = ".06c"

	elif CladdingTemperature > 750 and CladdingTemperature <= 1050:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1050 and CladdingTemperature <= 1350:

		CladdingXSid = ".12c"

	elif CladdingTemperature > 1350 and CladdingTemperature <= 1650:	
	
		CladdingXSid = ".15c"	

	elif CladdingTemperature > 1650:
	
		CladdingXSid = ".18c"				

	CladdingMassDensityGCC   = {}
	CladdingCoreMassFraction = {}

	for k,v in CladdingIsotopeMassFractions.items():

		CladdingIsotopeCoreMassFraction  = v * CladdingMassFraction

		if len(k) == 4:

			AA = k + CladdingXSid + "  -{0:02.5e}".format(CladdingIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CladdingXSid + " -{0:02.5e}".format(CladdingIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)


	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)			

	mi.write("\n")
	mi.close()	

def abovecoreradialshield(ShieldPinVolumeFraction, ShieldPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
				  		  DuctIsotopeMassFractions, ShieldIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
				  		  SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
				  		  SerpentAxialShieldDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
				  		  SerpentAxialDuctTemperature, serpfilepath, Name, CoreOuterRadius, ShieldOuterRadius, FuelLength, 
				  		  ShieldPinOuterRadius, ShieldPinPitch, ShieldVolume, ReflectorOuterRadius, AboveCoreSerpentLength,
				  		  SerpentTemperaturePoints, outershieldrgb):

	mi = open(Name + "_nonfuel", 'a')

	x = len(SerpentTemperaturePoints)

	ShieldPinVolumeFraction1 = ShieldPinVolumeFraction
	ShieldPinVolumeFraction  = ShieldPinVolumeFraction - DuctVolumeFraction - InterAssemblyVolumeFraction
	CoolantVolumeFraction    = - ShieldPinVolumeFraction * (ShieldPinVolumeFraction1-1) / ShieldPinVolumeFraction1

	ShieldPinDensityGCC    = ShieldPinVolumeFraction  * SerpentAxialShieldDensity[x-1]
	CoolantMassDensityGCC  = CoolantVolumeFraction       * SerpentAxialCoolantDensity[x-1]
	DuctMassDensityGCC     = DuctVolumeFraction          * SerpentAxialDuctDensity[x-1]
	IAGapMassDensityGCC    = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[x-1]

	ShieldCellMassDensityGCC = ShieldPinDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC

	ShieldPinMassFraction    = ShieldPinDensityGCC / ShieldCellMassDensityGCC
	CoolantMassFraction      = CoolantMassDensityGCC  / ShieldCellMassDensityGCC
	DuctMassFraction         = DuctMassDensityGCC     / ShieldCellMassDensityGCC
	IAGapMassFraction        = IAGapMassDensityGCC    / ShieldCellMassDensityGCC      
	
	ShieldTemperature    = SerpentAxialDuctTemperature[x-1]
	CoolantTemperature   = SerpentAxialCoolantTemperature[x-1]
	IAGapTemperature     = SerpentAxialIAGapTemperature[x-1]
	DuctTemperature      = SerpentAxialDuctTemperature[x-1]

	AboveCoreShieldVolume = AboveCoreSerpentLength * (  math.pi * ShieldOuterRadius ** 2  - math.pi * ReflectorOuterRadius ** 2  )

	mi.write("\n")
	mi.write("% ####################################################                      \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Cell abovecoreradialshield                                             \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Materials                                                              \n")
	mi.write("%    -------------------------------------------------                      \n")	
	mi.write("%    Shield-pin: " + ShieldPinMaterial                                   + "\n")							
	mi.write("%    Coolant:    " + Coolant                                             + "\n")	
	mi.write("%    Duct:       " + Duct                                                + "\n")	
	mi.write("%                                                                           \n")
	mi.write("%    General geometry                                                       \n")
	mi.write("%    -------------------------------------------------                      \n")
	mi.write("%    Cell volume: {0:02.3f}".format(ShieldVolume)                   + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(AboveCoreSerpentLength)        + " m   \n")	
	mi.write("%    Radially between r = {0:02.3f}".format(ReflectorOuterRadius) + " and {0:02.3f}".format(ShieldOuterRadius) + " m \n")
	mi.write("%                                                                            \n")
	mi.write("%    Calculated geometry                                                     \n")
	mi.write("%    -------------------------------------------------                       \n")
	mi.write("%    Shield pin diameter: {0:02.3f}".format(ShieldPinOuterRadius*2) + " cm \n")		
	mi.write("%    Shield pin pitch:    {0:02.3f}".format(ShieldPinPitch)         + " cm \n")	
	mi.write("%    Shield pin P/D:      {0:02.3f}".format(ShieldPinPitch/(ShieldPinOuterRadius*2))   + " \n")					
	mi.write("%                                                                            \n")		
	mi.write("%    Mass fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.2%}".format(ShieldPinMassFraction)           + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)             + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
	mi.write("%                                                                            \n")							
	mi.write("%    Volume fractions                                                        \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.2%}".format(ShieldPinVolumeFraction) + " ({0:02.2%}".format(ShieldPinVolumeFraction1)   + " in-assembly) \n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantVolumeFraction)   + " ({0:02.2%}".format(1-ShieldPinVolumeFraction1) + " in-assembly) \n")				
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)              + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)     + "\n")
	mi.write("%                                                                            \n")						
	mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.2f}".format(ShieldPinDensityGCC)                + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)           + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)              + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)             + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(ShieldCellMassDensityGCC)        + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin      = {0:02.1f}".format(ShieldTemperature-273.15)     + "\n")
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)       + "\n")						
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)          + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)         + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Component density (g/cc)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin     = {0:02.3f}".format(SerpentAxialShieldDensity[x-1])  + "\n")
	mi.write("%    Active coolant = {0:02.3f}".format(SerpentAxialCoolantDensity[x-1])    + "\n")
	mi.write("%    Duct           = {0:02.3f}".format(SerpentAxialDuctDensity[x-1])       + "\n")
	mi.write("%    IA-gap coolant = {0:02.3f}".format(SerpentAxialIAGapDensity[x-1])      + "\n")									
	mi.write("%                                                                            \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Shield-pin     = {0:02.1f}".format(1e3 * ShieldPinDensityGCC   * ShieldVolume) + "\n")			
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * ShieldVolume)  + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC    * ShieldVolume)     + "\n")	
	mi.write("%    IA-gap coolant = {0:02.1f}".format(1e3 * IAGapMassDensityGCC   * ShieldVolume)    + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")	

	X1 = "mat abovecoreradialshieldmat -{0:02.5f}".format(ShieldCellMassDensityGCC) + " rgb " + outershieldrgb + "\n"

	mi.write(X1)

	if ShieldTemperature <= 450:

		ShieldXSid = ".03c"

	elif ShieldTemperature > 450 and ShieldTemperature <= 750:

		ShieldXSid = ".06c"

	elif ShieldTemperature > 750 and ShieldTemperature <= 1050:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1050 and ShieldTemperature <= 1350:

		ShieldXSid = ".12c"

	elif ShieldTemperature > 1350 and ShieldTemperature <= 1650:	
	
		ShieldXSid = ".15c"	

	elif ShieldTemperature > 1650:
	
		ShieldXSid = ".18c"	

	X1 = "Shield-pin isotope (" + ShieldPinMaterial + ") \n"

	for k,v in ShieldIsotopeMassFractions.items():

		ShieldIsotopeCoreMassFraction  = v * ShieldPinMassFraction

		if len(k) == 4:

			AA = k + ShieldXSid + "  -{0:02.5e}".format(ShieldIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ShieldXSid + " -{0:02.5e}".format(ShieldIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	mi.write("\n")
	mi.close()	


def abovecorerefl(ReflectorPinVolumeFraction, ReflectorPinMaterial, Duct, Coolant, CoolantIsotopeMassFractions,
				  DuctIsotopeMassFractions, ReflectorIsotopeMassFractions, DuctVolumeFraction, InterAssemblyVolumeFraction,
				  SerpentAxialCoolantDensity, SerpentAxialDuctDensity, SerpentAxialIAGapDensity, SerpentAxialZones, 
				  SerpentAxialReflectorDensity, SerpentAxialIAGapTemperature, SerpentAxialCoolantTemperature, 
				  SerpentAxialDuctTemperature, serpfilepath, Name, ReflectorVolume, CoreOuterRadius,
				  ReflectorOuterRadius, FuelLength, ReflectorPinOuterRadius, ReflectorPinPitch, AboveCoreSerpentLength,
				  SerpentTemperaturePoints, outerreflrgb):

	mi = open(Name + "_nonfuel", 'a')

	x = len(SerpentTemperaturePoints)

	#print(x)
	#print(SerpentTemperaturePoints)
	#print(SerpentTemperaturePoints[x-1])
	print(SerpentAxialReflectorDensity)

	ReflectorPinVolumeFraction1 = ReflectorPinVolumeFraction
	ReflectorPinVolumeFraction  = ReflectorPinVolumeFraction - DuctVolumeFraction - InterAssemblyVolumeFraction
	CoolantVolumeFraction       = - ReflectorPinVolumeFraction * (ReflectorPinVolumeFraction1-1) / ReflectorPinVolumeFraction1

	ReflectorPinDensityGCC = ReflectorPinVolumeFraction  * SerpentAxialReflectorDensity[x-1]
	CoolantMassDensityGCC  = CoolantVolumeFraction       * SerpentAxialCoolantDensity[x-1]
	DuctMassDensityGCC     = DuctVolumeFraction          * SerpentAxialDuctDensity[x-1]
	IAGapMassDensityGCC    = InterAssemblyVolumeFraction * SerpentAxialIAGapDensity[x-1]

	ReflectorCellMassDensityGCC = ReflectorPinDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC + IAGapMassDensityGCC

	ReflectorPinMassFraction = ReflectorPinDensityGCC / ReflectorCellMassDensityGCC
	CoolantMassFraction      = CoolantMassDensityGCC  / ReflectorCellMassDensityGCC
	DuctMassFraction         = DuctMassDensityGCC     / ReflectorCellMassDensityGCC
	IAGapMassFraction        = IAGapMassDensityGCC    / ReflectorCellMassDensityGCC      
	
	ReflectorTemperature = SerpentAxialDuctTemperature[x-1]
	CoolantTemperature   = SerpentAxialCoolantTemperature[x-1]
	IAGapTemperature     = SerpentAxialIAGapTemperature[x-1]
	DuctTemperature      = SerpentAxialDuctTemperature[x-1]

	AboveCoreReflectorVolume = AboveCoreSerpentLength * (  math.pi * ReflectorOuterRadius ** 2 - math.pi * CoreOuterRadius ** 2  )

	mi.write("\n")
	mi.write("% ####################################################                      \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Cell abovecoreradialreflector                                          \n")
	mi.write("%                                                                           \n")			
	mi.write("%    Materials                                                              \n")
	mi.write("%    -------------------------------------------------                      \n")	
	mi.write("%    Reflector-pin: " + ReflectorPinMaterial                             + "\n")							
	mi.write("%    Coolant:       " + Coolant                                          + "\n")	
	mi.write("%    Duct:          " + Duct                                             + "\n")	
	mi.write("%                                                                           \n")
	mi.write("%    General geometry                                                       \n")
	mi.write("%    -------------------------------------------------                      \n")
	mi.write("%    Cell volume:  {0:02.3f}".format(AboveCoreReflectorVolume)      + " m^3 \n")
	mi.write("%    Axial length: {0:02.3f}".format(AboveCoreSerpentLength)        + " m   \n")	
	mi.write("%    Radially between r = {0:02.3f}".format(CoreOuterRadius) + " and {0:02.3f}".format(ReflectorOuterRadius) + " m \n")
	mi.write("%                                                                            \n")
	mi.write("%    Calculated geometry                                                     \n")
	mi.write("%    -------------------------------------------------                       \n")
	mi.write("%    Reflector pin diameter: {0:02.3f}".format(ReflectorPinOuterRadius*2)   + " cm \n")		
	mi.write("%    Reflector pin pitch:    {0:02.3f}".format(ReflectorPinPitch)        + " cm \n")	
	mi.write("%    Reflector pin P/D:      {0:02.3f}".format(ReflectorPinPitch/(ReflectorPinOuterRadius*2))   + " \n")					
	mi.write("%                                                                            \n")		
	mi.write("%    Mass fractions                                                          \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.2%}".format(ReflectorPinMassFraction)        + "\n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantMassFraction)             + "\n")						
	mi.write("%    Duct            = {0:02.2%}".format(DuctMassFraction)                + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(IAGapMassFraction)               + "\n")
	mi.write("%                                                                            \n")							
	mi.write("%    Volume fractions                                                        \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.2%}".format(ReflectorPinVolumeFraction) + " ({0:02.2%}".format(ReflectorPinVolumeFraction1)   + " in-assembly) \n")
	mi.write("%    Active coolant  = {0:02.2%}".format(CoolantVolumeFraction)      + " ({0:02.2%}".format(1-ReflectorPinVolumeFraction1) + " in-assembly) \n")				
	mi.write("%    Duct            = {0:02.2%}".format(DuctVolumeFraction)         + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2%}".format(InterAssemblyVolumeFraction)               + "\n")
	mi.write("%                                                                            \n")						
	mi.write("%    Cell-averaged mass density (g/cc)                                       \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.2f}".format(ReflectorPinDensityGCC)          + "\n")
	mi.write("%    Active coolant  = {0:02.2f}".format(CoolantMassDensityGCC)           + "\n")						
	mi.write("%    Duct            = {0:02.2f}".format(DuctMassDensityGCC)              + "\n")
	mi.write("%    IA-gap coolant  = {0:02.2f}".format(IAGapMassDensityGCC)             + "\n")
	mi.write("%    Cell total      = {0:02.2f}".format(ReflectorCellMassDensityGCC)     + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Cell-averaged temperatures (deg. C)                                     \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin   = {0:02.1f}".format(ReflectorTemperature-273.15)     + "\n")
	mi.write("%    Active coolant  = {0:02.1f}".format(CoolantTemperature-273.15)       + "\n")						
	mi.write("%    Duct            = {0:02.1f}".format(DuctTemperature-273.15)          + "\n")
	mi.write("%    IA-gap coolant  = {0:02.1f}".format(IAGapTemperature-273.15)         + "\n")
	mi.write("%                                                                            \n")
	mi.write("%    Component density (g/cc)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin  = {0:02.3f}".format(SerpentAxialReflectorDensity[x-1])  + "\n")
	mi.write("%    Active coolant = {0:02.3f}".format(SerpentAxialCoolantDensity[x-1])    + "\n")
	mi.write("%    Duct           = {0:02.3f}".format(SerpentAxialDuctDensity[x-1])       + "\n")
	mi.write("%    IA-gap coolant = {0:02.3f}".format(SerpentAxialIAGapDensity[x-1])      + "\n")									
	mi.write("%                                                                            \n")
	mi.write("%    Component mass (kg/cell)                                                \n")			
	mi.write("%    -------------------------------------------------                       \n")	
	mi.write("%    Reflector-pin  = {0:02.1f}".format(1e3 * ReflectorPinDensityGCC * ReflectorVolume) + "\n")			
	mi.write("%    Active coolant = {0:02.1f}".format(1e3 * CoolantMassDensityGCC * ReflectorVolume)  + "\n")	
	mi.write("%    Duct           = {0:02.1f}".format(1e3 * DuctMassDensityGCC * ReflectorVolume)     + "\n")	
	mi.write("%    IA-gap coolant = {0:02.1f}".format(1e3 * IAGapMassDensityGCC * ReflectorVolume)    + "\n")									
	mi.write("%                                                                            \n")
	mi.write("% ######################################################                     \n")
	mi.write("\n")	

	X1 = "mat abovecoreradialreflectormat -{0:02.5f}".format(ReflectorCellMassDensityGCC) + " rgb " + outerreflrgb + "\n"

	mi.write(X1)

	if ReflectorTemperature <= 450:

		ReflectorXSid = ".03c"

	elif ReflectorTemperature > 450 and ReflectorTemperature <= 750:

		ReflectorXSid = ".06c"

	elif ReflectorTemperature > 750 and ReflectorTemperature <= 1050:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1050 and ReflectorTemperature <= 1350:

		ReflectorXSid = ".12c"

	elif ReflectorTemperature > 1350 and ReflectorTemperature <= 1650:	
	
		ReflectorXSid = ".15c"	

	elif ReflectorTemperature > 1650:
	
		ReflectorXSid = ".18c"	

	X1 = "Reflector-pin isotope (" + ReflectorPinMaterial + ") \n"

	for k,v in ReflectorIsotopeMassFractions.items():

		ReflectorIsotopeCoreMassFraction  = v * ReflectorPinMassFraction

		if len(k) == 4:

			AA = k + ReflectorXSid + "  -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + ReflectorXSid + " -{0:02.5e}".format(ReflectorIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "Coolant isotope (" + Coolant + ") \n"

	if CoolantTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantTemperature > 450 and CoolantTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantTemperature > 750 and CoolantTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1050 and CoolantTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantTemperature > 1350 and CoolantTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		CoolantIsotopeCoreMassFraction  = v * CoolantMassFraction

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(CoolantIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(CoolantIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)				

	X1 = "Duct isotope (" + Duct + ") \n"

	if DuctTemperature <= 450:

		DuctXSid = ".03c"

	elif DuctTemperature > 450 and DuctTemperature <= 750:

		DuctXSid = ".06c"

	elif DuctTemperature > 750 and DuctTemperature <= 1050:

		DuctXSid = ".12c"

	elif DuctTemperature > 1050 and DuctTemperature <= 1350:

		DuctXSid = ".12c"

	elif DuctTemperature > 1350 and DuctTemperature <= 1650:	
	
		DuctXSid = ".15c"	

	elif DuctTemperature > 1650:
	
		DuctXSid = ".18c"				

	for k,v in DuctIsotopeMassFractions.items():

		DuctIsotopeCoreMassFraction  = v * DuctMassFraction

		if len(k) == 4:

			AA = k + DuctXSid + "  -{0:02.5e}".format(DuctIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + DuctXSid + " -{0:02.5e}".format(DuctIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)

	X1 = "IA-gap coolant isotope (" + Coolant + ") \n"

	if IAGapTemperature <= 450:

		IAGapXSid = ".03c"

	elif IAGapTemperature > 450 and IAGapTemperature <= 750:

		IAGapXSid = ".06c"

	elif IAGapTemperature > 750 and IAGapTemperature <= 1050:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1050 and IAGapTemperature <= 1350:

		IAGapXSid = ".12c"

	elif IAGapTemperature > 1350 and IAGapTemperature <= 1650:	
	
		IAGapXSid = ".15c"	

	elif IAGapTemperature > 1650:
	
		IAGapXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		IAGapIsotopeCoreMassFraction  = v * IAGapMassFraction

		if len(k) == 4:

			AA = k + IAGapXSid + "  -{0:02.5e}".format(IAGapIsotopeCoreMassFraction) + "     % " + X1
		
		else:

			AA = k + IAGapXSid + " -{0:02.5e}".format(IAGapIsotopeCoreMassFraction)  + "     % " + X1

		mi.write(AA)	

	mi.write("\n")
	mi.close()

