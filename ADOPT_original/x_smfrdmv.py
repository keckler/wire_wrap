import math

def makegridplate_voided(Name, CoolantInletTemperature, GridPlateCellDensity, GridPlateMassFractions, GridPlateColor,
				  		  LowerGridPlateSteelFraction, LowerGridPlateSteel, Coolant):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'w')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Lower grid plate material \n"
	C = "% ###   Consists of {0:02.1%}".format(LowerGridPlateSteelFraction) + " " + LowerGridPlateSteel + " and {0:02.1%}".format(1-LowerGridPlateSteelFraction) + " " + Coolant + " by volume  \n"   
	D = "% ###   The smeared material is at {0:02.1f}".format(CoolantInletTemperature-273) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat gridplatemat -{0:02.5f}".format(GridPlateCellDensity) + " rgb " + GridPlateColor + " \n"

	mi.write(A)

	if CoolantInletTemperature <= 450:

		PlateXSid = ".03c"

	elif CoolantInletTemperature > 450 and CoolantInletTemperature <= 750:

		PlateXSid = ".06c"

	elif CoolantInletTemperature > 750 and CoolantInletTemperature <= 1050:

		PlateXSid = ".12c"

	elif CoolantInletTemperature > 1050 and CoolantInletTemperature <= 1350:

		PlateXSid = ".12c"

	elif CoolantInletTemperature > 1350 and CoolantInletTemperature <= 1650:	
	
		PlateXSid = ".15c"	

	elif CoolantInletTemperature > 1650:
	
		PlateXSid = ".18c"	

	for k,v in GridPlateMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + PlateXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + PlateXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	


def makebottomplate_voided(Name, CoolantInletTemperature, BottomPlateCellDensity, BottomPlateMassFractions, BottomPlateColor,
				  	BottomPlateSteel):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Bottom plate material \n"
	C = "% ###   Consists of 100% " + BottomPlateSteel + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat bottomplatemat -{0:02.5f}".format(BottomPlateCellDensity) + " rgb " + BottomPlateColor + " \n"

	mi.write(A)

	if CoolantInletTemperature <= 450:

		PlateXSid = ".03c"

	elif CoolantInletTemperature > 450 and CoolantInletTemperature <= 750:

		PlateXSid = ".06c"

	elif CoolantInletTemperature > 750 and CoolantInletTemperature <= 1050:

		PlateXSid = ".12c"

	elif CoolantInletTemperature > 1050 and CoolantInletTemperature <= 1350:

		PlateXSid = ".12c"

	elif CoolantInletTemperature > 1350 and CoolantInletTemperature <= 1650:	
	
		PlateXSid = ".15c"	

	elif CoolantInletTemperature > 1650:
	
		PlateXSid = ".18c"	

	for k,v in BottomPlateMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + PlateXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + PlateXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makebelowcorecoolant_voided(Name, CoolantIsotopeMassFractions, CoolantInletDensity, CoolantInletTemperature, ColdCoolant,
						        Coolant):

	mi = open(Name + "_material_totvoid", 'a')	

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Cold (inlet) coolant material definition                                                                 \n"
	C = "% ###   Consists of 100% " + Coolant + " by volume                                                               \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273) + " deg. C                             \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat belowcorecoolantmat -1e-30 rgb " + ColdCoolant + " \n"

	mi.write(A)

	if CoolantInletTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantInletTemperature > 450 and CoolantInletTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantInletTemperature > 750 and CoolantInletTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantInletTemperature > 1050 and CoolantInletTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantInletTemperature > 1350 and CoolantInletTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantInletTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(v) + " \n" 
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(v)  + " \n" 

		mi.write(AA)						

	mi.write("\n")
	mi.close()	

def makecorecoolant_voided(Name, CoolantIsotopeMassFractions, Coolant, SerpentAxialCoolantDensity, SerpentAxialCoolantTemperature,
					       SerpentAxialZones, CoolantGradient20):

	mi = open(Name + "_material_totvoid", 'a')

	for zone in range(SerpentAxialZones):

		CoolantDensity     = SerpentAxialCoolantDensity[zone]
		CoolantTemperature = SerpentAxialCoolantTemperature[zone]

		A = "% ######################################################### //// ######## //// ####### \n"
		B = "% ###   Coolant material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
		C = "% ###   Consists of 100% " + Coolant + " by volume                                                               \n"   
		D = "% ###   The material is at {0:02.1f}".format(CoolantTemperature-273) + " deg. C                            \n"
		E = "% ######################################################### //// ######## //// ####### \n" 
  	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write(D)
		mi.write(E)
		mi.write("\n")
	
		if SerpentAxialZones == 20:

			A = "mat corecoolantmat" + str(zone+1) + " -1e-30 rgb " + CoolantGradient20[zone] + "\n"

		else:

			A = "mat corecoolantmat" + str(zone+1) + " -1e-30 \n"
	
		mi.write(A)
	
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
	
			if len(k) == 4:
	
				AA = k + CoolantXSid + "  -{0:02.5e}".format(v) + " \n" 
			
			else:
	
				AA = k + CoolantXSid + " -{0:02.5e}".format(v)  + " \n" 
	
			mi.write(AA)						
	
		mi.write("\n")
	
	mi.close()	

def makeabovecorecoolant_voided(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, AverageCoolantOutletTemperature, HotCoolant,
						        Coolant):

	if Coolant == "Pb":

		CoolantDensity      = (11441-1.2795 * AverageCoolantOutletTemperature)/1000
	
	elif Coolant == "Na":

		CoolantDensity      = (1014 - 0.235 * AverageCoolantOutletTemperature)/1000
	
	elif Coolant == "LBE":
	
		CoolantDensity      = (10725 - 1.22 * AverageCoolantOutletTemperature)/1000

	mi = open(Name + "_material_totvoid", 'a')	

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Hot (outlet) coolant material definition                                                                 \n"
	C = "% ###   Consists of 100% " + Coolant + " by volume                                                               \n"   
	D = "% ###   The material is at {0:02.1f}".format(AverageCoolantOutletTemperature-273) + " deg. C                            \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat abovecorecoolantmat -1e-30 rgb " + HotCoolant + " \n"

	mi.write(A)

	if AverageCoolantOutletTemperature <= 450:

		CoolantXSid = ".03c"

	elif AverageCoolantOutletTemperature > 450 and AverageCoolantOutletTemperature <= 750:

		CoolantXSid = ".06c"

	elif AverageCoolantOutletTemperature > 750 and AverageCoolantOutletTemperature <= 1050:

		CoolantXSid = ".12c"

	elif AverageCoolantOutletTemperature > 1050 and AverageCoolantOutletTemperature <= 1350:

		CoolantXSid = ".12c"

	elif AverageCoolantOutletTemperature > 1350 and AverageCoolantOutletTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif AverageCoolantOutletTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(v) + " \n" 
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(v)  + " \n" 

		mi.write(AA)						

	mi.write("\n")
	mi.close()	
	
def makecoreduct_voided(Name, DuctIsotopeMassFractions, Duct, SerpentAxialDuctDensity, SerpentAxialDuctTemperature,
			            SerpentAxialZones, DuctColor):

	mi = open(Name + "_material_totvoid", 'a')

	for zone in range(SerpentAxialZones):

		DuctDensity     = SerpentAxialDuctDensity[zone]
		DuctTemperature = SerpentAxialDuctTemperature[zone]

		A = "% ######################################################### //// ######## //// ####### \n"
		B = "% ###   Duct material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
		C = "% ###   Consists of 100% " + Duct + " by volume                                                               \n"   
		D = "% ###   The material is at {0:02.1f}".format(DuctTemperature-273) + " deg. C                            \n"
		E = "% ######################################################### //// ######## //// ####### \n" 
  	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write(D)
		mi.write(E)
		mi.write("\n")
	
		A = "mat coreductmat" + str(zone+1) + " -{0:02.5f}".format(DuctDensity) + " rgb " + DuctColor + " \n"
	
		mi.write(A)
	
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
	
			if len(k) == 4:
	
				AA = k + DuctXSid + "  -{0:02.5e}".format(v) + " \n" 
			
			else:
	
				AA = k + DuctXSid + " -{0:02.5e}".format(v)  + " \n" 
	
			mi.write(AA)						
	
		mi.write("\n")
	
	mi.close()	

def makecorecladding_voided(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
			                SerpentAxialZones, CladdingColor):

	mi = open(Name + "_material_totvoid", 'a')

	for zone in range(SerpentAxialZones):

		CladdingDensity     = SerpentAxialCladdingDensity[zone]
		CladdingTemperature = SerpentAxialCladdingTemperature[zone]

		A = "% ######################################################### //// ######## //// ####### \n"
		B = "% ###   Cladding material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
		C = "% ###   Consists of 100% " + Cladding + " by volume                                                               \n"   
		D = "% ###   The material is at {0:02.1f}".format(CladdingTemperature-273) + " deg. C                            \n"
		E = "% ######################################################### //// ######## //// ####### \n" 
  	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write(D)
		mi.write(E)
		mi.write("\n")
	
		A = "mat corecladdingmat" + str(zone+1) + " -{0:02.5f}".format(CladdingDensity) + " rgb " + CladdingColor + "\n"
	
		mi.write(A)
	
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
	
		for k,v in CladdingIsotopeMassFractions.items():
	
			if len(k) == 4:
	
				AA = k + CladdingXSid + "  -{0:02.5e}".format(v) + " \n" 
			
			else:
	
				AA = k + CladdingXSid + " -{0:02.5e}".format(v)  + " \n" 
	
			mi.write(AA)						
	
		mi.write("\n")
	
	mi.close()	

def makecorebond_voided(Name, BondIsotopeMassFractions, Bond, SerpentAxialBondDensity, SerpentAxialBondTemperature,
			            SerpentAxialZones, BondColor):

	mi = open(Name + "_material_totvoid", 'a')

	for zone in range(SerpentAxialZones):

		BondDensity     = SerpentAxialBondDensity[zone]
		BondTemperature = SerpentAxialBondTemperature[zone]

		A = "% ######################################################### //// ######## //// ####### \n"
		B = "% ###   Bond material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
		C = "% ###   Consists of 100% " + Bond + " by volume                                                               \n"   
		D = "% ###   The material is at {0:02.1f}".format(BondTemperature-273) + " deg. C                            \n"
		E = "% ######################################################### //// ######## //// ####### \n" 
  	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write(D)
		mi.write(E)
		mi.write("\n")
	
		A = "mat corebondmat" + str(zone+1) + " -{0:02.5f}".format(BondDensity) + " rgb " + BondColor + " \n"
	
		mi.write(A)
	
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
	
		for k,v in BondIsotopeMassFractions.items():
	
			if len(k) == 4:
	
				AA = k + BondXSid + "  -{0:02.5e}".format(v) + " \n" 
			
			else:
	
				AA = k + BondXSid + " -{0:02.5e}".format(v)  + " \n" 
	
			mi.write(AA)						
	
		mi.write("\n")
	
	mi.close()

def makefuel_voided(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
			        SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
			        FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
			        SerpentDepletion, FuelColor):

	mi = open(Name + "_material_totvoid", 'a')

	for batch in range(Batches):

		for zone in range(SerpentAxialZones):

			FuelDensity     = SerpentAxialFuelDensity[zone]
			FuelTemperature = SerpentAxialFuelTemperature[zone]
	
			A = "% ######################################################### //// ######## //// ####### \n"
			B = "% ###   Fuel material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
			C = "% ###   " + Fuel + ", {0:02.2%}".format(FissileFraction[batch]) + " fissile (" + Fissile[batch] + ") and {0:02.2%}".format(1-FissileFraction[batch]) + " fertile (" + Fertile[batch] + "), {0:02.1%}".format(Porosity) + " porosity \n"   
			D = "% ###   The material is at {0:02.1f}".format(FuelTemperature-273) + " deg. C                            \n"
			E = "% ######################################################### //// ######## //// ####### \n" 
  	
			mi.write(A)
			mi.write(B)
			mi.write(C)
			mi.write(D)
			mi.write(E)
			mi.write("\n")
		
			A = "mat fuelmat" + str(zone+1) + " -{0:02.5f}".format(FuelDensity) + " rgb " + FuelColor

			if SerpentDepletion == "on":

				A = A + " burn 1"

			A = A + "\n"

			mi.write(A)
		
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
		
			NONA = NonActinideIsotopeMassFractions[batch]

			for k,v in NONA.items():
		
				if len(k) == 4:
		
					AA = k + FuelXSid + "  -{0:02.5e}".format(v) + " \n" 
				
				else:
		
					AA = k + FuelXSid + " -{0:02.5e}".format(v)  + " \n" 
		
				mi.write(AA)						

			FERA = FertileIsotopeMassFractions[batch]

			for k,v in FERA.items():
		
				if len(k) == 4:
		
					AA = k + FuelXSid + "  -{0:02.5e}".format(v) + " \n" 
				
				else:
		
					AA = k + FuelXSid + " -{0:02.5e}".format(v)  + " \n" 
		
				mi.write(AA)	
		
			FISA = FissileIsotopeMassFractions[batch]

			for k,v in FISA.items():
		
				if len(k) == 4:
		
					AA = k + FuelXSid + "  -{0:02.5e}".format(v) + " \n" 
				
				else:
		
					AA = k + FuelXSid + " -{0:02.5e}".format(v)  + " \n" 
		
				mi.write(AA)	

			mi.write("\n")
		
	mi.close()

def makecorebarrel_voided(Name, CoreBarrelSteel, CoolantAverageTemperature, D9, HT9, T91, BarrelMassFractions, BarrelDensity, BarrelColor):	

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Core barrel material \n"
	C = "% ###   Consists of 100% " + CoreBarrelSteel + " by volume  \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantAverageTemperature-273) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat barrelmat -{0:02.5f}".format(BarrelDensity) + " rgb " + BarrelColor + " \n"

	mi.write(A)

	if CoolantAverageTemperature <= 450:

		BarrelXSid = ".03c"

	elif CoolantAverageTemperature > 450 and CoolantAverageTemperature <= 750:

		BarrelXSid = ".06c"

	elif CoolantAverageTemperature > 750 and CoolantAverageTemperature <= 1050:

		BarrelXSid = ".12c"

	elif CoolantAverageTemperature > 1050 and CoolantAverageTemperature <= 1350:

		BarrelXSid = ".12c"

	elif CoolantAverageTemperature > 1350 and CoolantAverageTemperature <= 1650:	
	
		BarrelXSid = ".15c"	

	elif CoolantAverageTemperature > 1650:
	
		BarrelXSid = ".18c"	

	for k,v in BarrelMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + BarrelXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + BarrelXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()

def makeradialreflector_voided(Name, ReflectorIsotopeMassFractions, ReflectorPinMaterial, SerpentAxialReflectorDensity, 
						       SerpentAxialDuctTemperature, SerpentAxialZones, ReflectorColor):

	mi = open(Name + "_material_totvoid", 'a')

	for zone in range(SerpentAxialZones):

		ReflectorDensity     = SerpentAxialReflectorDensity[zone]
		ReflectorTemperature = SerpentAxialDuctTemperature[zone]

		A = "% ######################################################### //// ######## //// ####### \n"
		B = "% ###   Reflector material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
		C = "% ###   Consists of 100% " + ReflectorPinMaterial + " by volume                                                               \n"   
		D = "% ###   The material is at {0:02.1f}".format(ReflectorTemperature-273) + " deg. C                            \n"
		E = "% ######################################################### //// ######## //// ####### \n" 
  	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write(D)
		mi.write(E)
		mi.write("\n")
	
		A = "mat radialreflectorpin" + str(zone+1) + " -{0:02.5f}".format(ReflectorDensity) + " rgb " + ReflectorColor + "\n"
	
		mi.write(A)
	
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
	
			if len(k) == 4:
	
				AA = k + ReflectorXSid + "  -{0:02.5e}".format(v) + " \n" 
			
			else:
	
				AA = k + ReflectorXSid + " -{0:02.5e}".format(v)  + " \n" 
	
			mi.write(AA)						
	
		mi.write("\n")
	
	mi.close()		

def makeradialshield_voided(Name, ShieldIsotopeMassFractions, ShieldPinMaterial, SerpentAxialShieldDensity, 
					        SerpentAxialDuctTemperature, SerpentAxialZones, ShieldColor):

	mi = open(Name + "_material_totvoid", 'a')

	for zone in range(SerpentAxialZones):

		ShieldDensity     = SerpentAxialShieldDensity[zone]
		ShieldTemperature = SerpentAxialDuctTemperature[zone]

		A = "% ######################################################### //// ######## //// ####### \n"
		B = "% ###   Shield material definition at axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
		C = "% ###   Consists of 100% " + ShieldPinMaterial + " by volume                                                               \n"   
		D = "% ###   The material is at {0:02.1f}".format(ShieldTemperature-273) + " deg. C                            \n"
		E = "% ######################################################### //// ######## //// ####### \n" 
  	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write(D)
		mi.write(E)
		mi.write("\n")
	
		A = "mat radialshieldpin" + str(zone+1) + " -{0:02.5f}".format(ShieldDensity) + " rgb " + ShieldColor + "\n"
	
		mi.write(A)
	
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
	
			if len(k) == 4:
	
				AA = k + ShieldXSid + "  -{0:02.5e}".format(v) + " \n" 
			
			else:
	
				AA = k + ShieldXSid + " -{0:02.5e}".format(v)  + " \n" 
	
			mi.write(AA)						
	
		mi.write("\n")
	
	mi.close()	

def makelowerinsulator_voided(Name, CoolantInletTemperature, LowerInsulatorDensity, InsulatorColor, InsulatorMaterial,
				              InsulatorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Insulator material \n"
	C = "% ###   Consists of 100% " + InsulatorMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273+10) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat lowerinsulatorpellet -{0:02.5f}".format(LowerInsulatorDensity) + " rgb " + InsulatorColor + " \n"

	mi.write(A)

	if (CoolantInletTemperature + 15) <= 450:

		InsulatorXSid = ".03c"

	elif (CoolantInletTemperature + 15) > 450 and (CoolantInletTemperature + 15) <= 750:

		InsulatorXSid = ".06c"

	elif (CoolantInletTemperature + 15) > 750 and (CoolantInletTemperature + 15) <= 1050:

		InsulatorXSid = ".12c"

	elif (CoolantInletTemperature + 15) > 1050 and (CoolantInletTemperature + 15) <= 1350:

		InsulatorXSid = ".12c"

	elif (CoolantInletTemperature + 15) > 1350 and (CoolantInletTemperature + 15) <= 1650:	
	
		InsulatorXSid = ".15c"	

	elif (CoolantInletTemperature + 15) > 1650:
	
		InsulatorXSid = ".18c"	

	for k,v in InsulatorMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + InsulatorXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + InsulatorXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makeupperinsulator_voided(Name, CoolantOutletTemperature, UpperInsulatorDensity, InsulatorColor, InsulatorMaterial,
				              InsulatorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Insulator material \n"
	C = "% ###   Consists of 100% " + InsulatorMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantOutletTemperature-273+15) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat upperinsulatorpellet -{0:02.5f}".format(UpperInsulatorDensity) + " rgb " + InsulatorColor + " \n"

	mi.write(A)

	if (CoolantOutletTemperature + 15) <= 450:

		InsulatorXSid = ".03c"

	elif (CoolantOutletTemperature + 15) > 450 and (CoolantOutletTemperature + 15) <= 750:

		InsulatorXSid = ".06c"

	elif (CoolantOutletTemperature + 15) > 750 and (CoolantOutletTemperature + 15) <= 1050:

		InsulatorXSid = ".12c"

	elif (CoolantOutletTemperature + 15) > 1050 and (CoolantOutletTemperature + 15) <= 1350:

		InsulatorXSid = ".12c"

	elif (CoolantOutletTemperature + 15) > 1350 and (CoolantOutletTemperature + 15) <= 1650:	
	
		InsulatorXSid = ".15c"	

	elif (CoolantOutletTemperature + 15) > 1650:
	
		InsulatorXSid = ".18c"	

	for k,v in InsulatorMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + InsulatorXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + InsulatorXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makelowerendcap_voided(Name, CoolantInletTemperature, LowerEndCapDensity, EndCapColor, EndCapMaterial,
				           EndCapMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Lower end cap material \n"
	C = "% ###   Consists of 100% " + EndCapMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273+15) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat lowerendcapmat -{0:02.5f}".format(LowerEndCapDensity) + " rgb " + EndCapColor + " \n"

	mi.write(A)

	if (CoolantInletTemperature + 15) <= 450:

		EndCapXSid = ".03c"

	elif (CoolantInletTemperature + 15) > 450 and (CoolantInletTemperature + 15) <= 750:

		EndCapXSid = ".06c"

	elif (CoolantInletTemperature + 15) > 750 and (CoolantInletTemperature + 15) <= 1050:

		EndCapXSid = ".12c"

	elif (CoolantInletTemperature + 15) > 1050 and (CoolantInletTemperature + 15) <= 1350:

		EndCapXSid = ".12c"

	elif (CoolantInletTemperature + 15) > 1350 and (CoolantInletTemperature + 15) <= 1650:	
	
		EndCapXSid = ".15c"	

	elif (CoolantInletTemperature + 15) > 1650:
	
		EndCapXSid = ".18c"	

	for k,v in EndCapMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + EndCapXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + EndCapXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makeupperendcap_voided(Name, CoolantOutletTemperature, UpperEndCapDensity, EndCapColor, EndCapMaterial,
				           EndCapMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Upper end cap material \n"
	C = "% ###   Consists of 100% " + EndCapMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantOutletTemperature-273+15) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat upperendcapmat -{0:02.5f}".format(UpperEndCapDensity) + " rgb " + EndCapColor + " \n"

	mi.write(A)

	if (CoolantOutletTemperature + 15) <= 450:

		EndCapXSid = ".03c"

	elif (CoolantOutletTemperature + 15) > 450 and (CoolantOutletTemperature + 15) <= 750:

		EndCapXSid = ".06c"

	elif (CoolantOutletTemperature + 15) > 750 and (CoolantOutletTemperature + 15) <= 1050:

		EndCapXSid = ".12c"

	elif (CoolantOutletTemperature + 15) > 1050 and (CoolantOutletTemperature + 15) <= 1350:

		EndCapXSid = ".12c"

	elif (CoolantOutletTemperature + 15) > 1350 and (CoolantOutletTemperature + 15) <= 1650:	
	
		EndCapXSid = ".15c"	

	elif (CoolantOutletTemperature + 15) > 1650:
	
		EndCapXSid = ".18c"	

	for k,v in EndCapMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + EndCapXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + EndCapXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makelowerinnerreflector_voided(Name, CoolantInletTemperature, LowerInnerAxialReflectorDensity, AxialReflectorColor, AxialReflectorPinMaterial,
				       	           InnerReflectorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Lower innner reflector material \n"
	C = "% ###   Consists of 100% " + AxialReflectorPinMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273+25) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat loweraxialreflectormat -{0:02.5f}".format(LowerInnerAxialReflectorDensity) + " rgb " + AxialReflectorColor + " \n"

	mi.write(A)

	if (CoolantInletTemperature + 25) <= 450:

		LowerAxialReflectorXSid = ".03c"

	elif (CoolantInletTemperature + 25) > 450 and (CoolantInletTemperature + 25) <= 750:

		LowerAxialReflectorXSid = ".06c"

	elif (CoolantInletTemperature + 25) > 750 and (CoolantInletTemperature + 25) <= 1050:

		LowerAxialReflectorXSid = ".12c"

	elif (CoolantInletTemperature + 25) > 1050 and (CoolantInletTemperature + 25) <= 1350:

		LowerAxialReflectorXSid = ".12c"

	elif (CoolantInletTemperature + 25) > 1350 and (CoolantInletTemperature + 25) <= 1650:	
	
		LowerAxialReflectorXSid = ".15c"	

	elif (CoolantInletTemperature + 25) > 1650:
	
		LowerAxialReflectorXSid = ".18c"	

	for k,v in InnerReflectorMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + LowerAxialReflectorXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + LowerAxialReflectorXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makeupperinnerreflector_voided(Name, CoolantOutletTemperature, UpperInnerAxialReflectorDensity, AxialReflectorColor, AxialReflectorPinMaterial,
				       	           InnerReflectorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Upper innner reflector material \n"
	C = "% ###   Consists of 100% " + AxialReflectorPinMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantOutletTemperature-273+25) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat upperaxialreflectormat -{0:02.5f}".format(UpperInnerAxialReflectorDensity) + " rgb " + AxialReflectorColor + " \n"

	mi.write(A)

	if (CoolantOutletTemperature + 25) <= 450:

		UpperAxialReflectorXSid = ".03c"

	elif (CoolantOutletTemperature + 25) > 450 and (CoolantOutletTemperature + 25) <= 750:

		UpperAxialReflectorXSid = ".06c"

	elif (CoolantOutletTemperature + 25) > 750 and (CoolantOutletTemperature + 25) <= 1050:

		UpperAxialReflectorXSid = ".12c"

	elif (CoolantOutletTemperature + 25) > 1050 and (CoolantOutletTemperature + 25) <= 1350:

		UpperAxialReflectorXSid = ".12c"

	elif (CoolantOutletTemperature + 25) > 1350 and (CoolantOutletTemperature + 25) <= 1650:	
	
		UpperAxialReflectorXSid = ".15c"	

	elif (CoolantOutletTemperature + 25) > 1650:
	
		UpperAxialReflectorXSid = ".18c"	

	for k,v in InnerReflectorMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + UpperAxialReflectorXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + UpperAxialReflectorXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makelowerinnershield_voided(Name, CoolantInletTemperature, LowerInnerAxialShieldDensity, AxialShieldColor, AxialShieldPinMaterial,
				       	        InnerShieldMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Lower innner shield material \n"
	C = "% ###   Consists of 100% " + AxialShieldPinMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273+25) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat loweraxialshieldmat -{0:02.5f}".format(LowerInnerAxialShieldDensity) + " rgb " + AxialShieldColor + " \n"

	mi.write(A)

	if (CoolantInletTemperature + 25) <= 450:

		LowerAxialShieldXSid = ".03c"

	elif (CoolantInletTemperature + 25) > 450 and (CoolantInletTemperature + 25) <= 750:

		LowerAxialShieldXSid = ".06c"

	elif (CoolantInletTemperature + 25) > 750 and (CoolantInletTemperature + 25) <= 1050:

		LowerAxialShieldXSid = ".12c"

	elif (CoolantInletTemperature + 25) > 1050 and (CoolantInletTemperature + 25) <= 1350:

		LowerAxialShieldXSid = ".12c"

	elif (CoolantInletTemperature + 25) > 1350 and (CoolantInletTemperature + 25) <= 1650:	
	
		LowerAxialShieldXSid = ".15c"	

	elif (CoolantInletTemperature + 25) > 1650:
	
		LowerAxialShieldXSid = ".18c"	

	for k,v in InnerShieldMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + LowerAxialShieldXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + LowerAxialShieldXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makeupperinnershield_voided(Name, CoolantOutletTemperature, UpperInnerAxialShieldDensity, AxialShieldColor, AxialShieldPinMaterial,
				       	        InnerShieldMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Upper innner shield material \n"
	C = "% ###   Consists of 100% " + AxialShieldPinMaterial + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantOutletTemperature-273+25) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat upperaxialshieldmat -{0:02.5f}".format(UpperInnerAxialShieldDensity) + " rgb " + AxialShieldColor + " \n"

	mi.write(A)

	if (CoolantOutletTemperature + 25) <= 450:

		UpperAxialShieldXSid = ".03c"

	elif (CoolantOutletTemperature + 25) > 450 and (CoolantOutletTemperature + 25) <= 750:

		UpperAxialShieldXSid = ".06c"

	elif (CoolantOutletTemperature + 25) > 750 and (CoolantOutletTemperature + 25) <= 1050:

		UpperAxialShieldXSid = ".12c"

	elif (CoolantOutletTemperature + 25) > 1050 and (CoolantOutletTemperature + 25) <= 1350:

		UpperAxialShieldXSid = ".12c"

	elif (CoolantOutletTemperature + 25) > 1350 and (CoolantOutletTemperature + 25) <= 1650:	
	
		UpperAxialShieldXSid = ".15c"	

	elif (CoolantOutletTemperature + 25) > 1650:
	
		UpperAxialShieldXSid = ".18c"	

	for k,v in InnerShieldMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + UpperAxialShieldXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + UpperAxialShieldXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()	

def makebucontrolabsorber_voided(Name, CoolantAverageTemperature, BUControlMassFractions, BUControlDensity, BUControlAbsorber,
						         BuControlAbsorberColor, BUControlB10Fraction):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   BU-control assembly absorber material \n"
	if BUControlAbsorber == "B4C":
		C = "% ###   Consists of " + BUControlAbsorber + ", enriched to {0:02.1%}".format(BUControlB10Fraction) + " in B-10 \n"   
	else:
		C = "% ###   Consists of 100% of " + BUControlAbsorber + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantAverageTemperature-273) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat bucontrolabsorber -{0:02.5f}".format(BUControlDensity) + " rgb " + BuControlAbsorberColor + " \n"

	mi.write(A)

	if (CoolantAverageTemperature) <= 450:

		BuControlXSid = ".03c"

	elif (CoolantAverageTemperature) > 450 and (CoolantAverageTemperature) <= 750:

		BuControlXSid = ".06c"

	elif (CoolantAverageTemperature) > 750 and (CoolantAverageTemperature) <= 1050:

		BuControlXSid = ".12c"

	elif (CoolantAverageTemperature) > 1050 and (CoolantAverageTemperature) <= 1350:

		BuControlXSid = ".12c"

	elif (CoolantAverageTemperature) > 1350 and (CoolantAverageTemperature) <= 1650:	
	
		BuControlXSid = ".15c"	

	elif (CoolantAverageTemperature) > 1650:
	
		BuControlXSid = ".18c"	

	for k,v in BUControlMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + BuControlXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + BuControlXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()

def makescramabsorber_voided(Name, CoolantAverageTemperature, ScramMassFractions, ScramDensity, ScramAbsorber,
						     ScramAbsorberColor, ScramB10Fraction):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   BU-control assembly absorber material \n"
	if ScramAbsorber == "B4C":
		C = "% ###   Consists of " + ScramAbsorber + ", enriched to {0:02.1%}".format(ScramB10Fraction) + " in B-10 \n"   
	else:
		C = "% ###   Consists of 100% of " + ScramAbsorber + " \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantAverageTemperature-273) + " deg. C \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat scramabsorber -{0:02.5f}".format(ScramDensity) + " rgb " + ScramAbsorberColor + " \n"

	mi.write(A)

	if (CoolantAverageTemperature) <= 450:

		BuControlXSid = ".03c"

	elif (CoolantAverageTemperature) > 450 and (CoolantAverageTemperature) <= 750:

		BuControlXSid = ".06c"

	elif (CoolantAverageTemperature) > 750 and (CoolantAverageTemperature) <= 1050:

		BuControlXSid = ".12c"

	elif (CoolantAverageTemperature) > 1050 and (CoolantAverageTemperature) <= 1350:

		BuControlXSid = ".12c"

	elif (CoolantAverageTemperature) > 1350 and (CoolantAverageTemperature) <= 1650:	
	
		BuControlXSid = ".15c"	

	elif (CoolantAverageTemperature) > 1650:
	
		BuControlXSid = ".18c"	

	for k,v in ScramMassFractions.items():
		
		if len(k) == 4:
		
			AA = k + BuControlXSid + "  -{0:02.5e}".format(v) + "  \n"

		else:    
    	
			AA = k + BuControlXSid + " -{0:02.5e}".format(v)  + "  \n"
	
		mi.write(AA)

	mi.write("\n")
	mi.close()

def systemgas_voided(Name):

	# Start writing the materials file
	mi = open(Name + "_material_totvoid", 'a')

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Gas in the system     \n"
	C = "% ###   Modeled as Krypton-84 \n"   
	D = "% ######################################################### //// ######## //// ####### \n" 
 	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write("\n")

	mi.write("mat gas -0.01    \n")
	mi.write("36084.12c 1.00 \n")

