def serpentinput(SerpentCoreRadius, Batches, SerpentAxialZones, CellNames, serpfilepath, Name, 
				 LowerEndCapLength, LowerShieldLength, LowerReflectorLength, LowerGasPlenumLength, 
				 LowerInsulatorPelletLength, FuelLength,  UpperInsulatorPelletLength, UpperGasPlenumLength,  
				 UpperReflectorLength, UpperShieldLength, UpperEndCapLength, ReflectorOuterRadius, ShieldOuterRadius,
				 SerpentOutsideDistance, SystemOuterRadius, RadialShieldRows, RadialReflectorRows, BelowCoreSerpentLength,
				 AboveCoreSerpentLength, SerpentCylNeutrons, SerpentCylActiveCycles, SerpentCylInactiveCycles, SerpentCylPlotting, 
				 SerpentDepletion, SerpentDepletionSteps, SerpentDepletionType, SerpentDepletionEnd, SerpentInventory, Power,
				 SerpentDepletionPCC, SerpentDPA, SerpentACElibpath, SerpentDEClibpath, SerpentNFYlibpath, EDIS):

	mi = open(Name, 'w')

	AxialLevelSystemBottom    = -SerpentOutsideDistance        
	AxialLevelLowerShield     = 0.0
	AxialLevelLowerReflector  = AxialLevelLowerShield    + LowerShieldLength    * 100
	AxialLevelLowerGasPlenum  = AxialLevelLowerReflector + LowerReflectorLength * 100
	AxialLevelFuelBottom      = AxialLevelLowerGasPlenum + LowerGasPlenumLength * 100           

	FuelStep = 100 * FuelLength / SerpentAxialZones

	## SURFACES

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Axial surfaces ############################################## //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")		

	S1 = "surf systembottom      pz {0:02.2f}".format(AxialLevelSystemBottom)   + "      % Bottom level of the modeled system                   \n"
	mi.write(S1)

	S2 = "surf lowershield       pz {0:02.5f}".format(AxialLevelLowerShield)    + "      % Bottom of lower shield                               \n"
	S3 = "surf lowerreflector    pz {0:02.4f}".format(AxialLevelLowerReflector) + "      % Bottom of lower reflector  - top of lower shield     \n"
	S4 = "surf lowergasplenum    pz {0:02.4f}".format(AxialLevelLowerGasPlenum) + "      % Bottom of lower gas plenum - top of lower reflector  \n"

	if LowerShieldLength > 0:
		mi.write(S2)

	if LowerReflectorLength > 0:		
		mi.write(S3)

	if LowerGasPlenumLength > 0:		
		mi.write(S4)

	S5 = "surf fuelaxial1        pz {0:02.4f}".format(AxialLevelFuelBottom)     + "      % Bottom of fueled region    - top of lower gas plenum     \n"
	mi.write(S5)

	for fuelax in range(SerpentAxialZones):

		AxialLevelFuel = AxialLevelFuelBottom + (fuelax + 1) * FuelStep

		if fuelax < 9:
			S8 = "surf fuelaxial" + str(fuelax+2) + "        pz {0:02.3f}".format(AxialLevelFuel) + "      % Top of fuel axial level " + str(fuelax+1) + "/" + str(SerpentAxialZones) + "\n"
		elif fuelax >= 9 and fuelax < 100:
			S8 = "surf fuelaxial" + str(fuelax+2) + "       pz {0:02.3f}".format(AxialLevelFuel)  + "      % Top of fuel axial level " + str(fuelax+1) + "/" + str(SerpentAxialZones) + "\n"
		elif fuelax >= 100 and fuelax < 1000:
			S8 = "surf fuelaxial" + str(fuelax+2) + "      pz {0:02.3f}".format(AxialLevelFuel)   + "      % Top of fuel axial level " + str(fuelax+1) + "/" + str(SerpentAxialZones) + "\n"
		elif fuelax >= 1000 and fuelax < 10000:
			S8 = "surf fuelaxial" + str(fuelax+2) + "     pz {0:02.3f}".format(AxialLevelFuel)    + "      % Top of fuel axial level " + str(fuelax+1) + "/" + str(SerpentAxialZones) + "\n"

		mi.write(S8)

	AxialLevelUpperReflector = AxialLevelFuel           + UpperGasPlenumLength * 100         
	AxialLevelUpperShield    = AxialLevelUpperReflector + UpperReflectorLength * 100   
	AxialLevelCoreTop        = AxialLevelUpperShield    + UpperShieldLength    * 100
	AxialLevelSystemTop      = AxialLevelCoreTop        + SerpentOutsideDistance

	if UpperGasPlenumLength > 0:
		S1 = "surf upperreflector    pz {0:02.3f}".format(AxialLevelUpperReflector) + "      % Bottom of upper reflector - top of the upper gas plenum \n"
		mi.write(S1)

	if UpperReflectorLength > 0:	
		S2 = "surf uppershield       pz {0:02.3f}".format(AxialLevelUpperShield)    + "      % Bottom of upper shield    - top of upper reflector \n"
		mi.write(S2)

	if UpperShieldLength > 0:	
		S3 = "surf coretop           pz {0:02.3f}".format(AxialLevelCoreTop)        + "      % Top of the upper shield   - bottom of above-core coolant         \n"
		mi.write(S3)
	
	S4 = "surf systemtop         pz {0:02.3f}".format(AxialLevelSystemTop)          + "      % Top of the modeled system  \n"
	mi.write(S4)

	mi.write("\n")

	# OUTER ZONE LOWER SURFACE
	x = 3

	if LowerGasPlenumLength > 0:		
		lowsurf = "lowergasplenum"
		x -= 1

	if LowerReflectorLength > 0:		
		lowsurf = "lowerreflector"
		x -= 1
		
	if LowerShieldLength > 0:
		lowsurf = "lowershield"
		x -= 1

	if x == 3:

		lowsurf = "fuelaxial1"

	# OUTER ZONE UPPER SURFACE

	if UpperGasPlenumLength > 0:		
		upsurf = "upperreflector"

	if UpperReflectorLength > 0:		
		upsurf = "uppershield"

	if UpperShieldLength > 0:		
		upsurf = "coretop"		

	if UpperReflectorLength < 1e-3 and UpperGasPlenumLength < 1e-3 and UpperShieldLength < 1e-3:		
		upsurf = "fuelaxial" + str(SerpentAxialZones+1)

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Radial surfaces ############################################# //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")		

	i = 0
	for Radius in SerpentCoreRadius:

		i += 1
		S1 = "surf fuelradial" + str(i) + "       cyl 0.0 0.0 {0:02.3f}".format(Radius*100) + "       % Radial fuel zone (batch) " + str(i) + "/" + str(Batches) + "\n"
		mi.write(S1)

	if RadialReflectorRows > 0:

		S2 = "surf radialreflector   cyl 0.0 0.0 {0:02.3f}".format(ReflectorOuterRadius*100)    + "       % Radial reflector \n"
		mi.write(S2)

	if RadialShieldRows > 0:

		S3 = "surf radialshield      cyl 0.0 0.0 {0:02.3f}".format(ShieldOuterRadius*100)       + "       % Radial shield \n"
		mi.write(S3)

	S4 = "surf radialsystem      cyl 0.0 0.0 {0:02.3f}".format(SystemOuterRadius)       + "       % Radial total system \n"
	mi.write(S4)

	mi.write("\n")	

	## CELLS

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Lower axial cells ########################################### //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n") 

	SerpentXCell = "cell belowcorecoolantcell 0 belowcorecoolantmat -radialsystem systembottom -" + lowsurf + " \n"

	mi.write(SerpentXCell)

	if LowerShieldLength > 0:

		if LowerReflectorLength > 0:

			SerpentCell = "cell lowershieldcell      0 lowershieldmat      -fuelradial" + str(Batches) + "  lowershield    -lowerreflector \n"

		elif LowerReflectorLength <= 0 and LowerGasPlenumLength > 0:

			SerpentCell = "cell lowershieldcell      0 lowershieldmat      -fuelradial" + str(Batches) + "  lowershield    -lowergasplenum \n"

		elif LowerReflectorLength <= 0 and LowerGasPlenumLength <= 0:

			SerpentCell = "cell lowershieldcell      0 lowershieldmat      -fuelradial" + str(Batches) + "  lowershield    -fuelaxial1 \n"

		mi.write(SerpentCell)

	if LowerReflectorLength > 0:

		if LowerGasPlenumLength > 0:
			
			SerpentCell = "cell lowerreflectorcell   0 lowerreflectormat   -fuelradial" + str(Batches) + "  lowerreflector -lowergasplenum \n"
		
		else:

			SerpentCell = "cell lowerreflectorcell   0 lowerreflectormat   -fuelradial" + str(Batches) + "  lowerreflector -fuelaxial1     \n"			

		mi.write(SerpentCell)

	if LowerGasPlenumLength > 0:

		SerpentCell = "cell lowergasplenumcell   0 lowergasplenummat   -fuelradial" + str(Batches) + "  lowergasplenum -fuelaxial1     \n"
		mi.write(SerpentCell)

	mi.write("\n")		

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Core cells ################################################## //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")	

	i = 0
	for batch in range(Batches):

		for axial in range(SerpentAxialZones):
		
			if batch == 0:

				SerpentCell = "cell " + CellNames[i] + " 0 " + CellNames[i] + "             -fuelradial" + str(batch+1) + " fuelaxial" + str(axial+1) + " -fuelaxial" + str(axial+2) + "     % Batch: " + str(batch+1) + "/" + str(Batches) + ", Axial: " + str(axial+1) + "/" + str(SerpentAxialZones) + "\n"

			else:

				SerpentCell = "cell " + CellNames[i] + " 0 " + CellNames[i] + " fuelradial" + str(batch) + " -fuelradial" + str(batch+1) + " fuelaxial" + str(axial+1) + " -fuelaxial" + str(axial+2) + "     % Batch: " + str(batch+1) + "/" + str(Batches) + ", Axial: " + str(axial+1) + "/" + str(SerpentAxialZones) + "\n"					

			i += 1
			mi.write(SerpentCell)

	mi.write("\n")

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Outer radial cells ########################################## //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")	

	if BelowCoreSerpentLength > 0:

		if RadialReflectorRows > 0:
	
			SerpentCell = "cell belowcoreradialreflectorcell 0 belowcoreradialreflectormat fuelradial" + str(Batches) + " -radialreflector " + lowsurf + " -fuelaxial1 \n"
			mi.write(SerpentCell)
	
			SerpentCell = "cell belowcoreradialshieldcell 0 belowcoreradialshieldmat radialreflector -radialshield " + lowsurf + " -fuelaxial1 \n"
			mi.write(SerpentCell)
	
	if RadialReflectorRows > 0:

		for axial in range(SerpentAxialZones):
				
			SerpentCell = "cell radialreflectorcell" + str(axial) + " 0 radialreflectormat" + str(axial) + " fuelradial" + str(Batches) + " -radialreflector fuelaxial" + str(axial+1) + " -fuelaxial" + str(axial+2) + "\n"
			mi.write(SerpentCell)
		
		mi.write("\n")
	
	if RadialReflectorRows > 0:
	
		for axial in range(SerpentAxialZones):
				
			SerpentCell = "cell radialshieldcell" + str(axial) + " 0 radialshieldmat" + str(axial) + " radialreflector -radialshield fuelaxial" + str(axial+1) + " -fuelaxial" + str(axial+2) + "\n"
			mi.write(SerpentCell)
		
		mi.write("\n")

	if AboveCoreSerpentLength > 0:

		if RadialReflectorRows > 0:
	
			SerpentCell = "cell abovecoreradialreflectorcell 0 abovecoreradialreflectormat fuelradial" + str(Batches) + " -radialreflector fuelaxial" + str(SerpentAxialZones+1) + " -" + upsurf + "  \n"
			mi.write(SerpentCell)
		
			mi.write("\n")
	
		if RadialShieldRows > 0:
	
			SerpentCell = "cell abovecoreradialshieldcell 0 abovecoreradialshieldmat radialreflector -radialshield fuelaxial" + str(SerpentAxialZones+1) + " -" + upsurf + "  \n"
			mi.write(SerpentCell)
		
			mi.write("\n")

	if RadialShieldRows > 0:

		SerpentCell = "cell radialoutercoolantcell 0 outsidecoolantmat radialshield -radialsystem " + lowsurf + " -" + upsurf + " \n"	
	
	elif RadialShieldRows == 0 and RadialReflectorRows > 0:

		SerpentCell = "cell radialoutercoolantcell 0 outsidecoolantmat radialreflector -radialsystem " + lowsurf + " -" + upsurf + " \n"	

	else:

		SerpentCell = "cell radialoutercoolantcell 0 outsidecoolantmat fuelradial" + str(Batches) + " -radialsystem" + lowsurf + " -" + upsurf + " \n"	

	mi.write(SerpentCell)
	mi.write("\n")

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Upper cells ################################################# //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")	

	if UpperGasPlenumLength > 0:

		SerpentCell = "cell uppergasplenumcell   0 uppergasplenummat   -fuelradial" + str(Batches) + "  fuelaxial" + str(SerpentAxialZones+1) + " -upperreflector    \n"
		mi.write(SerpentCell)

	if UpperReflectorLength > 0:

		if UpperGasPlenumLength > 0:

			if UpperShieldLength > 0:
			
				SerpentCell = "cell upperreflectorcell   0 upperreflectormat   -fuelradial" + str(Batches) + "  upperreflector -uppershield \n"
		
			else:

				SerpentCell = "cell upperreflectorcell   0 upperreflectormat   -fuelradial" + str(Batches) + "  upperreflector -uppershield \n"

		else:

			if UpperShieldLength > 0:
			
				SerpentCell = "cell upperreflectorcell   0 upperreflectormat   -fuelradial" + str(Batches) + " fuelaxial" + str(SerpentAxialZones+1) + " -uppershield \n"
		
			else:

				SerpentCell = "cell upperreflectorcell   0 upperreflectormat   -fuelradial" + str(Batches) + "  fuelaxial" + str(SerpentAxialZones+1) + " -uppershield \n"

		mi.write(SerpentCell)

	if UpperShieldLength > 0:

		if UpperReflectorLength > 0:

			if UpperGasPlenumLength > 0:

				SerpentCell = "cell uppershieldcell      0 uppershieldmat      -fuelradial" + str(Batches) + "  uppershield    -coretop \n"

			else:

				SerpentCell = "cell uppershieldcell      0 uppershieldmat      -fuelradial" + str(Batches) + "  uppershield    -coretop \n"

		else:

			if UpperGasPlenumLength > 0:

				SerpentCell = "cell uppershieldcell      0 uppershieldmat      -fuelradial" + str(Batches) + "  upperreflector    -coretop \n"

			else:

				SerpentCell = "cell uppershieldcell      0 uppershieldmat      -fuelradial" + str(Batches) + " fuelaxial" + str(SerpentAxialZones+1) + " -coretop \n"

		mi.write(SerpentCell)
		mi.write("\n")		

	SerpentXCell = "cell abovecorecoolantcell 0 abovecorecoolantmat -radialsystem " + upsurf + " -systemtop \n"

	mi.write(SerpentXCell)
	mi.write("\n")	

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Outside cells ############################################### //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")		

	A = "cell outdowninner 0 outside -systembottom  -radialsystem              \n"
	B = "cell outdownouter 0 outside -systembottom   radialsystem              \n"
	C = "cell outupinner   0 outside  systemtop     -radialsystem              \n"
	D = "cell outupouter   0 outside  systemtop      radialsystem              \n"
	E = "cell outxradial   0 outside  systembottom  -systemtop    radialsystem \n"

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write(D)
	mi.write(E)
	mi.write("\n")


	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Include materials ########################################### //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")	

	A = "include \"" + Name + "_mburn\"     \n"
	B = "include \"" + Name + "_nonfuel\"   \n"

	if EDIS != "on":
		mi.write(A)
		
	mi.write(B)

	mi.write("\n")	

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### XS-paths #################################################### //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")

	mi.write("set acelib \"" + SerpentACElibpath + "\"\n")
	mi.write("set declib \"" + SerpentDEClibpath + "\"\n")
	mi.write("set nfylib \"" + SerpentNFYlibpath + "\"\n")

	mi.write("\n")
	mi.write("\n")	


	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Criticality ################################################# //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 
	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")	

	A = "set pop " + str(SerpentCylNeutrons) + " " + str(SerpentCylActiveCycles) + " " + str(SerpentCylInactiveCycles) + "\n"

	mi.write(A)
	mi.write("\n")

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Power ####################################################### //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 
	
	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")
	mi.write("set power " + str(Power) + "\n")
	mi.write("\n")

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Power distribution detector ################################# //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")

	i = 1

	for Cell in CellNames:
	
		A = "det Power" + Cell + " dm " + Cell + " dr -8 void"
		mi.write(A)
		mi.write("\n")
		i += 1	

	mi.write("\n")

	A = "% ################################################################################### //// ######## //// ####### \n"
	B = "% ##################### Flux distribution detector ################################## //// ######## //// ####### \n"
	C = "% ################################################################################### //// ######## //// ####### \n" 

	mi.write(A)
	mi.write(B)
	mi.write(C)
	mi.write("\n")

	i = 1

	for Cell in CellNames:
	
		A = "det Flux" + Cell + " dm " + Cell
		mi.write(A)
		mi.write("\n")
		i += 1	

	mi.write("\n")

	if SerpentCylPlotting == "on":

		A = "% ################################################################################### //// ######## //// ####### \n"
		B = "% ##################### Plotting #################################################### //// ######## //// ####### \n"
		C = "% ################################################################################### //// ######## //// ####### \n" 
	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write("\n")
	
		mi.write("plot 1 {0:02.0f}".format(10*SystemOuterRadius*2) + " {0:02.0f}".format(10*(AxialLevelSystemTop-AxialLevelSystemBottom)) + " \n")
		mi.write("plot 3 1000 1000 " + str(AxialLevelFuelBottom+0.1) + "\n")
		mi.write("\n")

	if SerpentDepletion == "on":

		if EDIS != "on":

			A = "% ################################################################################### //// ######## //// ####### \n"
			B = "% ##################### Depletion ################################################### //// ######## //// ####### \n"
			C = "% ################################################################################### //// ######## //// ####### \n" 
		
			mi.write(A)
			mi.write(B)
			mi.write(C)
			mi.write("\n")
	
			if SerpentDepletionPCC == "off":
	
				mi.write("set pcc 0 \n")
	
			#mi.write("set ures 1 \n")
			#mi.write("set fpcut 5e-2          \n")
			#mi.write("set stabcut 1e-2        \n")
			#mi.write("set ttacut  1e-12       \n")
			#mi.write("set xsfcut  1e-2        \n")
	
			BurnupStep = SerpentDepletionEnd / SerpentDepletionSteps
	
			if SerpentDepletionType == "Burnup":
		
				A = "dep bustep \n" 
				mi.write(A)
		
			elif SerpentDepletionType == "Days":
				
				A = "dep daystep \n" 
				mi.write(A)
		
			for x in range(SerpentDepletionSteps):
		
				B = str(BurnupStep)
				mi.write(B + "\n")
		
			mi.write("\n")
			mi.write("set inventory \n")
		
			for isotope in SerpentInventory:
		
				mi.write(isotope + "\n")

	if SerpentDPA == "on":

		mi.write("\n")

		A = "% ################################################################################### //// ######## //// ####### \n"
		B = "% ##################### DPA Flux Detectors ########################################## //// ######## //// ####### \n"
		C = "% ################################################################################### //// ######## //// ####### \n" 
	
		mi.write(A)
		mi.write(B)
		mi.write(C)
		mi.write("\n")
	
		EnergyGroups = ["1.00E-30",
						"1.00E-10",
						"1.00E-09",
						"1.00E-08",
						"2.30E-08",
						"5.00E-08",
						"7.60E-08",
						"1.15E-07",
						"1.70E-07",
						"2.55E-07",
						"3.80E-07",
						"5.50E-07",
						"8.40E-07",
						"1.28E-06",
						"1.90E-06",
						"2.80E-06",
						"4.25E-06",
						"6.30E-06",
						"9.20E-06",
						"1.35E-05",
						"2.10E-05",
						"3.00E-05",
						"4.50E-05",
						"6.90E-05",
						"1.00E-04",
						"1.35E-04",
						"1.70E-04",
						"2.20E-04",
						"2.80E-04",
						"3.60E-04",
						"4.50E-04",
						"5.75E-04",
						"7.60E-04",
						"9.60E-04",
						"1.28E-03",
						"1.60E-03",
						"2.00E-03",
						"2.70E-03",
						"3.40E-03",
						"4.50E-03",
						"5.50E-03",
						"7.20E-03",
						"9.20E-03",
						"1.20E-02",
						"1.50E-02",
						"1.90E-02",
						"2.55E-02",
						"3.20E-02",
						"4.00E-02",
						"5.25E-02",
						"6.60E-02",
						"0.088",
						"0.11",
						"0.135",
						"0.16",
						"0.19",
						"0.22",
						"0.225",
						"0.29",
						"0.32",
						"0.36",
						"0.4",
						"0.45",
						"0.5",
						"0.55",
						"0.6",
						"0.66",
						"0.72",
						"0.78",
						"0.84",
						"0.92",
						"1.0",
						"1.2",
						"1.4",
						"1.6",
						"1.8",
						"2.0",
						"2.3",
						"2.6",
						"2.9",
						"3.3",
						"3.7",
						"4.1",
						"4.5",
						"5.0",
						"5.5",
						"6.0",
						"6.7",
						"7.4",
						"8.2",
						"9.0",
						"10",
						"11",
						"12",
						"13",
						"14",
						"15",
						"16",
						"17",
						"18",
						"19"]	

		EnergyDetector = 'ene dpa 1'
	
		mi.write(EnergyDetector)
		mi.write("\n")
	
		for line in EnergyGroups:
	
			mi.write(line + " \n")
	
		mi.write("\n")
	
		i = 1
	
		for mat in CellNames:
	
			A = "det " + str(i) + " dm " + mat + " de dpa"
			mi.write(A)
			mi.write("\n")
			i += 1

	mi.write("% --- Reduce energy grid size:\n")
	mi.write("set egrid 5E-3 1E-5 10.0\n")
	mi.write("% --- Cut-offs:\n")
	mi.write("set fpcut   1E-9\n")
	mi.write("set stabcut 1E-12\n")
	mi.write("set ttacut  1E-18\n")
	mi.write("set xsfcut  1E-6\n")

	mi.close()
					
