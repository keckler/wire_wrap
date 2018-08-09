import math

def colors():

	BondColor              = "195 240 247" # Light blue
	FuelColor              = "3 115 133"   # Dark blue
	InsulatorColor         = "232 223 223"
	ShieldColor            = "94 18 18"
	SteelColor             = "77 77 75"
	ReflectorColor         = SteelColor #"168 99 20" # Dark brown
	CladdingColor          = SteelColor	
	GridPlateColor         = SteelColor
	DuctColor              = SteelColor
	BarrelColor            = "94 89 90"
	EndCapColor            = SteelColor
	AxialReflectorColor    = SteelColor
	BottomPlateColor       = "64 58 59"
	AxialShieldColor       = ShieldColor
	BuControlAbsorberColor = ShieldColor
	ScramAbsorberColor     = ShieldColor
	InsulatorColor         = "245 245 98"
	HotCoolant             = "255 41 41"
	MediumCoolant          = "237 154 38"
	ColdCoolant            = "0 132 224"
	GasColor               = "245 245 213"
	PerturbedColor         = "255 247 0"

	CoolantGradient20 = ["0 132 224", "13 127 214", "26 122 204", "40 117 195", "53 112 185", "67 108 175", "80 103 166", "93 98 156", "107 93 146", "120 88 137",
						 "134 84 127", "147 79 118", "161 74 108", "174 69 98", "187 64 89", "201 60 79", "214 55 69", "228 50 60", "241 45 50", "255 41 41"]

	FuelGradient20 = ["255 71 68", "253 65 61", "251 59 56", "249 54 52", "247 48 47", "246 43 43", "244 37 38", "242 32 34", "240 26 29", "239 21 25",
					  "239 21 25", "240 26 29", "242 32 34", "244 37 38", "246 43 43", "247 48 47", "249 54 52", "251 59 56", "253 65 61", "255 71 68"]

	return(FuelColor, InsulatorColor, ShieldColor, SteelColor, HotCoolant,MediumCoolant, ColdCoolant, GasColor,
		   GridPlateColor, BarrelColor, InsulatorColor, EndCapColor, AxialReflectorColor, AxialShieldColor,
		   BottomPlateColor, CoolantGradient20, FuelGradient20, DuctColor, FuelColor, BondColor, CladdingColor, ReflectorColor,
		   BuControlAbsorberColor, ScramAbsorberColor, PerturbedColor)

def makegridplate(Name, CoolantInletTemperature, GridPlateCellDensity, GridPlateMassFractions, GridPlateColor,
				  LowerGridPlateSteelFraction, LowerGridPlateSteel, Coolant):

	# Start writing the materials file
	mi = open(Name + "_material_gridplate", 'w')

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

def makebottomplate(Name, CoolantInletTemperature, BottomPlateCellDensity, BottomPlateMassFractions, BottomPlateColor,
				  	BottomPlateSteel):

	# Start writing the materials file
	mi = open(Name + "_material_bottomplate", 'w')

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

def makebelowcorecoolant(Name, CoolantIsotopeMassFractions, CoolantInletDensity, CoolantInletTemperature, ColdCoolant,
						 Coolant):

	mi = open(Name + "_material_coldcoolant", 'w')	

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

	A = "mat belowcorecoolantmat -{0:02.5f}".format(CoolantInletDensity/1000) + " rgb " + ColdCoolant + " \n"

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

def makelowerplenumcoolant(Name, CoolantIsotopeMassFractions, CoolantInletDensity, CoolantInletTemperature, ColdCoolant,
						   Coolant):

	mi = open(Name + "_material_lowerplenumcoolant", 'w')	

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Lower plenum (reflector, shield, inlet plenum) coolant material definition     \n"
	C = "% ###   Consists of 100% " + Coolant + " by volume                                     \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantInletTemperature-273) + " deg. C   \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat lowerplenumcoolantmat -{0:02.5f}".format(CoolantInletDensity/1000) + " rgb " + ColdCoolant + " \n"

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

def makeupperplenumcoolant(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, CoolantOutletTemperature, HotCoolant,
						   Coolant):

	mi = open(Name + "_material_upperplenumcoolant", 'w')	

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Upper plenum (reflector, shield, gas plenum) coolant material definition     \n"
	C = "% ###   Consists of 100% " + Coolant + " by volume                                     \n"   
	D = "% ###   The material is at {0:02.1f}".format(CoolantOutletTemperature-273) + " deg. C   \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")

	A = "mat upperplenumcoolantmat -{0:02.5f}".format(CoolantOutletDensity/1000) + " rgb " + HotCoolant + " \n"

	mi.write(A)

	if CoolantOutletTemperature <= 450:

		CoolantXSid = ".03c"

	elif CoolantOutletTemperature > 450 and CoolantOutletTemperature <= 750:

		CoolantXSid = ".06c"

	elif CoolantOutletTemperature > 750 and CoolantOutletTemperature <= 1050:

		CoolantXSid = ".12c"

	elif CoolantOutletTemperature > 1050 and CoolantOutletTemperature <= 1350:

		CoolantXSid = ".12c"

	elif CoolantOutletTemperature > 1350 and CoolantOutletTemperature <= 1650:	
	
		CoolantXSid = ".15c"	

	elif CoolantOutletTemperature > 1650:
	
		CoolantXSid = ".18c"				

	for k,v in CoolantIsotopeMassFractions.items():

		if len(k) == 4:

			AA = k + CoolantXSid + "  -{0:02.5e}".format(v) + " \n" 
		
		else:

			AA = k + CoolantXSid + " -{0:02.5e}".format(v)  + " \n" 

		mi.write(AA)						

	mi.write("\n")
	mi.close()	

def makecorecoolant(Name, CoolantIsotopeMassFractions, Coolant, SerpentAxialCoolantDensity, SerpentAxialCoolantTemperature,
					SerpentAxialZones, CoolantGradient20):

	mi = open(Name + "_material_activecoolant", 'w')

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

			A = "mat corecoolantmat" + str(zone+1) + " -{0:02.5f}".format(CoolantDensity) + " rgb " + CoolantGradient20[zone] + "\n"

		else:

			A = "mat corecoolantmat" + str(zone+1) + " -{0:02.5f}".format(CoolantDensity) + " \n"
	
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

def makeabovecorecoolant(Name, CoolantIsotopeMassFractions, CoolantOutletDensity, AverageCoolantOutletTemperature, HotCoolant,
						 Coolant):

	if Coolant == "Pb":

		CoolantDensity      = (11441-1.2795 * AverageCoolantOutletTemperature)/1000
	
	elif Coolant == "Na":

		CoolantDensity      = (1014 - 0.235 * AverageCoolantOutletTemperature)/1000
	
	elif Coolant == "LBE":
	
		CoolantDensity      = (10725 - 1.22 * AverageCoolantOutletTemperature)/1000

	mi = open(Name + "_material_hotcoolant", 'w')	

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

	A = "mat abovecorecoolantmat -{0:02.5f}".format(CoolantDensity) + " rgb " + HotCoolant + " \n"

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
	
def makecoreduct(Name, DuctIsotopeMassFractions, Duct, SerpentAxialDuctDensity, SerpentAxialDuctTemperature,
			     SerpentAxialZones, DuctColor):

	mi = open(Name + "_material_duct", 'w')

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

def makebelowcorecladding(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
			     		  SerpentAxialZones, CladdingColor):

	mi = open(Name + "_material_coldcladding", 'w')

	CladdingDensity     = SerpentAxialCladdingDensity[0]
	CladdingTemperature = SerpentAxialCladdingTemperature[0]

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Cladding material definition below the active core \n"
	C = "% ###   Consists of 100% " + Cladding + " by volume                                                               \n"   
	D = "% ###   The material is at {0:02.1f}".format(CladdingTemperature-273) + " deg. C                            \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")
	
	A = "mat belowcorecladdingmat -{0:02.5f}".format(CladdingDensity) + " rgb " + CladdingColor + "\n"
	
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

def makeabovecorecladding(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
			     		  SerpentAxialZones, CladdingColor):

	mi = open(Name + "_material_hotcladding", 'w')

	CladdingDensity     = SerpentAxialCladdingDensity[SerpentAxialZones-1]
	CladdingTemperature = SerpentAxialCladdingTemperature[SerpentAxialZones-1]

	A = "% ######################################################### //// ######## //// ####### \n"
	B = "% ###   Cladding material definition above the active core \n"
	C = "% ###   Consists of 100% " + Cladding + " by volume                                    \n"   
	D = "% ###   The material is at {0:02.1f}".format(CladdingTemperature-273) + " deg. C       \n"
	E = "% ######################################################### //// ######## //// ####### \n" 
  	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")
	
	A = "mat abovecorecladdingmat -{0:02.5f}".format(CladdingDensity) + " rgb " + CladdingColor + "\n"
	
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

def makecorebond(Name, BondIsotopeMassFractions, Bond, SerpentAxialBondDensity, SerpentAxialBondTemperature,
			     SerpentAxialZones, BondColor):

	mi = open(Name + "_material_bond", 'w')

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

def makecorecladding(Name, CladdingIsotopeMassFractions, Cladding, SerpentAxialCladdingDensity, SerpentAxialCladdingTemperature,
			     SerpentAxialZones, CladdingColor, Batches):

	mi = open(Name + "_material_cladding", 'w')

	for batch in range(Batches):

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
		
			A = "mat corecladdingmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(CladdingDensity) + " rgb " + CladdingColor + "\n"
		
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

def makefuelnb(Name, Fuel, SerpentAxialFuelDensity, SerpentAxialFuelTemperature,
			   SerpentAxialZones, NonActinideIsotopeMassFractions, FissileIsotopeMassFractions,
			   FertileIsotopeMassFractions, Batches, Porosity, FissileFraction, Fissile, Fertile, FuelGradient20,
			   SerpentDepletion, FuelColor, FuelAverageDensity, AxialEnrichmentZoning, TotalFuelMaterials):

	mix = open(Name + "_material_fuel", 'w')
	mi  = open(Name + "_material_fuelnb", 'w')
	mid = open(Name + "_material_fuel_doppler", 'w')

	y = 0

	for batch in range(Batches):

		for zone in range(SerpentAxialZones):

			if batch == 0:

				y = zone

			else:
				
				y = zone + SerpentAxialZones * batch

			#print("batch:   " + str(batch) + ", axial: " + str(zone))
			#print("value:   " + str(y))
			#print("fissile: " + str(FissileFraction[y]))

			FuelDensity     = FuelAverageDensity
			FuelTemperature = SerpentAxialFuelTemperature[zone]
	
			A = "% ######################################################### //// ######## //// ####### \n"
			B = "% ###   Fuel material definition, batch " + str(batch+1) + ", axial level " + str(zone+1) + " of  " + str(SerpentAxialZones) + " \n"
			C = "% ###   " + Fuel + ", {0:02.2%}".format(FissileFraction[y]) + " fissile (" + Fissile[y] + ") and {0:02.2%}".format(1-FissileFraction[y]) + " fertile (" + Fertile[y] + "), {0:02.1%}".format(Porosity) + " porosity \n"   
			D = "% ###   The material is at {0:02.1f}".format(FuelTemperature-273) + " deg. C                            \n"
			E = "% ######################################################### //// ######## //// ####### \n" 
  	
			mi.write(A)
			mi.write(B)
			mi.write(C)
			mi.write(D)
			mi.write(E)
			mi.write("\n")

			mid.write(A)
			mid.write(B)
			mid.write(C)
			mid.write(D)
			mid.write(E)
			mid.write("\n")			
		
			mix.write(A)
			mix.write(B)
			mix.write(C)
			mix.write(D)
			mix.write(E)
			mix.write("\n")		

			#A = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " rgb " + FuelColor + " \n"
			#B = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " burn 1 rgb " + FuelColor + " \n"

			if batch == 0:

				A = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " rgb 182 43 44 \n"
				B = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " burn 1 rgb 182 43 44 \n"

			elif batch == 1:

				A = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " rgb 96 50 50 \n"
				B = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " burn 1 rgb 96 50 50 \n"

			elif batch == 2:

				A = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " rgb 75 93 95 \n"
				B = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " burn 1 rgb 75 93 95 \n"

			else:

				A = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " \n"
				B = "mat fuelmat_ax" + str(zone+1) + "_batch" + str(batch+1) + " -{0:02.5f}".format(FuelDensity) + " burn 1 \n"


			#if SerpentAxialZones == 20:

			#	A = A + " rgb " + FuelGradient20[zone] + "\n"

			mi.write(A)
			mid.write(A)
			mix.write(B)
		
			if FuelTemperature <= 450:
		
				FuelXSid = ".03c" # ORG
				FuelXSid_Doppler = ".12c" # 900K DOPPLER
		
			elif FuelTemperature > 450 and FuelTemperature <= 750:
		
				FuelXSid = ".06c" # ORG
				FuelXSid_Doppler = ".15c" # 900K DOPPLER
		
			elif FuelTemperature > 750 and FuelTemperature <= 1050:
		
				FuelXSid = ".09c" # ORG
				FuelXSid_Doppler = ".18c" # 900K DOPPLER				
		
			elif FuelTemperature > 1050 and FuelTemperature <= 1350:
		
				FuelXSid = ".12c" # ORG
				FuelXSid_Doppler = ".03c" # 900K DOPPLER
		
			elif FuelTemperature > 1350 and FuelTemperature <= 1650:	
			
				FuelXSid = ".15c" # ORG	
				FuelXSid_Doppler = ".06c" # 900K DOPPLER	
		
			elif FuelTemperature > 1650:
			
				FuelXSid = ".18c" # ORG			
				FuelXSid_Doppler = ".09c" # 900K DOPPLER									

			if Fuel != "MetallicU" and Fuel != "MetallicTh":
		
				NONA = NonActinideIsotopeMassFractions[y]
	
				for k,v in NONA.items():
			
					if len(k) == 4:
			
						AA = k + FuelXSid + "  -{0:02.5e}".format(v) + " \n" 
						BB = k + FuelXSid_Doppler  + "  -{0:02.5e}".format(v) + " \n" 
					
					else:
			
						AA = k + FuelXSid + " -{0:02.5e}".format(v)  + " \n" 
						BB = k + FuelXSid_Doppler + " -{0:02.5e}".format(v)  + " \n" 
			
					mi.write(AA)
					mid.write(BB)	
					mix.write(AA)				

			FERA = FertileIsotopeMassFractions[y]

			for k,v in FERA.items():
		
				if len(k) == 4:
		
					AA = k + FuelXSid + "  -{0:02.5e}".format(v) + " \n"
					BB = k + FuelXSid_Doppler + "  -{0:02.5e}".format(v) + " \n" 
				
				else:
		
					AA = k + FuelXSid + " -{0:02.5e}".format(v)  + " \n" 
					BB = k + FuelXSid_Doppler + " -{0:02.5e}".format(v)  + " \n" 
		
				mi.write(AA)
				mid.write(BB)
				mix.write(AA)
		
			FISA = FissileIsotopeMassFractions[y]

			for k,v in FISA.items():
		
				if len(k) == 4:
		
					AA = k + FuelXSid + "  -{0:02.5e}".format(v) + " \n" 
					BB = k + FuelXSid_Doppler + "  -{0:02.5e}".format(v) + " \n" 
				
				else:
		
					AA = k + FuelXSid + " -{0:02.5e}".format(v)  + " \n" 
					BB = k + FuelXSid_Doppler + " -{0:02.5e}".format(v)  + " \n" 
		
				mi.write(AA)
				mid.write(BB)	
				mix.write(AA)

			mi.write("\n")
			mid.write("\n")
			mix.write("\n")

	mi.close()
	mid.close()
	mix.close()

def makecorebarrel(Name, CoreBarrelSteel, CoolantAverageTemperature, D9, HT9, T91, BarrelMassFractions, BarrelDensity, BarrelColor):	

	# Start writing the materials file
	mi = open(Name + "_material_barrel", 'w')

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

def makeradialreflector(Name, ReflectorIsotopeMassFractions, ReflectorPinMaterial, SerpentAxialReflectorDensity, 
						SerpentAxialDuctTemperature, SerpentAxialZones, ReflectorColor):

	mi = open(Name + "_material_radialreflector", 'w')

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

def makeradialshield(Name, ShieldIsotopeMassFractions, ShieldPinMaterial, SerpentAxialShieldDensity, 
					 SerpentAxialDuctTemperature, SerpentAxialZones, ShieldColor):

	mi = open(Name + "_material_radialshield", 'w')

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

def makelowerinsulator(Name, CoolantInletTemperature, LowerInsulatorDensity, InsulatorColor, InsulatorMaterial,
				       InsulatorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_lowerinsulator", 'w')

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

def makeupperinsulator(Name, CoolantOutletTemperature, UpperInsulatorDensity, InsulatorColor, InsulatorMaterial,
				       InsulatorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_upperinsulator", 'w')

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

def makelowerendcap(Name, CoolantInletTemperature, LowerEndCapDensity, EndCapColor, EndCapMaterial,
				       EndCapMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_lowerendcap", 'w')

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

def makeupperendcap(Name, CoolantOutletTemperature, UpperEndCapDensity, EndCapColor, EndCapMaterial,
				       EndCapMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_upperendcap", 'w')

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

def makelowerinnerreflector(Name, CoolantInletTemperature, LowerInnerAxialReflectorDensity, AxialReflectorColor, AxialReflectorPinMaterial,
				       	    InnerReflectorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_lowerinnerreflector", 'w')

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

def makeupperinnerreflector(Name, CoolantOutletTemperature, UpperInnerAxialReflectorDensity, AxialReflectorColor, AxialReflectorPinMaterial,
				       	    InnerReflectorMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_upperinnerreflector", 'w')

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

def makelowerinnershield(Name, CoolantInletTemperature, LowerInnerAxialShieldDensity, AxialShieldColor, AxialShieldPinMaterial,
				       	 InnerShieldMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_lowerinnershield", 'w')

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

def makeupperinnershield(Name, CoolantOutletTemperature, UpperInnerAxialShieldDensity, AxialShieldColor, AxialShieldPinMaterial,
				       	    InnerShieldMassFractions):

	# Start writing the materials file
	mi = open(Name + "_material_upperinnershield", 'w')

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

def makebucontrolabsorber(Name, CoolantAverageTemperature, BUControlMassFractions, BUControlDensity, BUControlAbsorber,
						  BuControlAbsorberColor, BUControlB10Fraction):

	# Start writing the materials file
	mi = open(Name + "_material_bucontrolabsorber", 'w')

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

def makescramabsorber(Name, CoolantAverageTemperature, ScramMassFractions, ScramDensity, ScramAbsorber,
						  ScramAbsorberColor, ScramB10Fraction):

	# Start writing the materials file
	mi = open(Name + "_material_scramabsorber", 'w')

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

def systemgas(Name):

	# Start writing the materials file
	mi = open(Name + "_material_gas", 'w')

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

