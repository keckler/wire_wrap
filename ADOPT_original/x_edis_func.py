space = "##    "
pserp = "##        - Running Serpent neutron transport and depletion..."
ok    = "##    OK."
import time
import os
import sys

##################################################################################
####                                                                          ####
#### Function: checkinputtypes                                                ####
#### Description: Makes sure that all inputs given in Settings.py are         ####
####              in the correct form                                         ####
####                                                                          ####
#### Last updated: 2013-06-19, 3.01 AM                                        ####
####                                                                          ####
##################################################################################

def checkinputtypes(filename, version, mpi, nodes, keff_convergence, mat_convergence, iter_convergence, mat_checks, criticality, eqcycle_days, eqcycle_busteps, resultspath):


	print(" ")
	print("-----------------------------------------")
	print("      STARTING EDIS RUN                  ")
	print("-----------------------------------------")

	serp = open(resultspath + "/EDIS_console.txt", 'w', encoding='utf-8')

	sx = "##    ________________________________"	
	s0 = "##    |                              |"	
	s1 = "##    |    ______ _____  _  _____    |"
	s2 = "##    |   |  ____|  __ \(_)/ ____|   |"
	s3 = "##    |   | |__  | |  | |_| (___     |"
	s4 = "##    |   |  __| | |  | | |\___ \    |"
	s5 = "##    |   | |____| |__| | |____) |   |"
	s6 = "##    |   |______|_____/|_|_____/    |"
	s7 = "##    |                              |"
	s7x= "##    |    August 2013               |"
	s9 = "##    |______________________________|"
	s7 = "##    |                              |"
	s91= "##    |    E: staffanq@gmail.com     |"
	s9x= "##    |______________________________|"

	serp.write(sx)	
	serp.write("\n")
	serp.write(s0)	                           
	serp.write("\n")
	serp.write(s1)
	serp.write("\n")
	serp.write(s2)
	serp.write("\n")
	serp.write(s3)
	serp.write("\n")
	serp.write(s4)
	serp.write("\n")
	serp.write(s5)
	serp.write("\n")
	serp.write(s6)
	serp.write("\n")
	serp.write(s7)
	serp.write("\n")
	serp.write(s7x)
	serp.write("\n")
	serp.write(s9)
	serp.write("\n")
	serp.write(s7)
	serp.write("\n")
	serp.write(s91)
	serp.write("\n")
	serp.write(s9x)
	serp.write("\n")
	serp.write(space)
	serp.write("\n")
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking the user settings...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")

	while isinstance(filename,str) != True:
		print ("The Serpent input file-path is not entered as a string!")
		filename = input("Enter a new Serpent input file-path: ")
	
	while isinstance(version,int) != True and isinstance(version,float) != True:
		print ("The Serpent version is not entered correctly!")
		version = input("Enter a new Serpent version (either 1 or 2): ")
	
	while isinstance(mpi,str) != True:
		print ("The choice of whether to run parallell or not was not correctly!")
		mpi = input("Run MPI (either on or off): ")
	
	while isinstance(criticality,str) != True:
		print ("The choice of whether to find critical eq. cycle was not correctly!")
		criticality = input("Find critical eq. cycle (either on or off): ")

	while isinstance(nodes,int) != True:
		print ("The number of MPI-nodes was not entered as an integer!")
		nodes = int(input("MPI-nodes (as an integer!): "))
	
	while isinstance(keff_convergence,int) != True and isinstance(keff_convergence,float) != True:
		print ("The k_eff convergence setting was not entered correctly!")
		keff_convergence = float(input("K_eff convergence (as some form of number!): "))
	
	while isinstance(mat_convergence,int) != True and isinstance(mat_convergence,float) != True:
		print ("The material convergence setting was not entered correctly!")
		mat_convergence = float(input("Material convergence (as some form of number!): "))
	
	while isinstance(iter_convergence,int) != True and isinstance(iter_convergence,float) != True:
		print ("The max. iteration setting was not entered correctly!")
		iter_convergence = float(input("Max. iteration setting (as some form of number!): "))
	
	while isinstance(mat_checks,list) != True:
		print ("The materials for convergence evaluation were not entered correctly!")
		#mat_checknumber = float(input("Material to check (ex: ["U235"]): "))

	while isinstance(eqcycle_days,int) != True and isinstance(eqcycle_days,float) != True:
		print ("The eq-cycle burnup days setting was not entered correctly!")
		eqcycle_days = float(input("Eq-cycle burnup-days guess (as some form of number!): "))

	while isinstance(eqcycle_busteps,int) != True and isinstance(eqcycle_busteps,float) != True:
		print ("The eq-cycle burnup step setting was not entered correctly!")
		eqcycle_busteps = float(input("Eq-cycle burnup step setting (as some form of number!): "))

	return (filename, version, mpi, nodes, keff_convergence, mat_convergence, iter_convergence, mat_checks, criticality, eqcycle_days, eqcycle_busteps)

##################################################################################
####                                                                          ####
#### Function: checkinputfile                                                 ####
#### Description: Makes sure that all the Serpent input file as given         ####
####              in Settings.py exists                                       ####
####                                                                          ####
#### Last updated: 2013-06-19, 3.01 AM                                        ####
####                                                                          ####
##################################################################################

def checkinputfile(filename, resultspath):

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Identifying the Serpent input file...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")
	serp.close()

	print(" ")
	print("  Identifying the Serpent input file...")

	# Check if the Serpent input file exists
	while os.path.exists(filename) != True or os.path.isfile(filename) != True:
		print ("##    ERROR! Your Serpent input file-path does not exist!")
		filename = input("##    -- Enter a new Serpent input file-path: ")

	print("  OK.")

	return filename

##################################################################################
####                                                                          ####
#### Function: runserpent_single                                              ####
#### Description: Runs Serpent on a single core                               ####
####                                                                          ####
#### Last updated: 2013-06-19, 3.03 AM                                        ####
####                                                                          ####
##################################################################################

def runserpent_single(filename,version,sss1filename,sss2filename):

	import subprocess

	if version == 1:
		runline = sss1filename + " " + filename +  " > serpent_output.txt"
	else:
		runline = sss2filename + " " + filename + " > serpent_output.txt"

	subprocess.check_output([runline, "-l"], shell = True)

##################################################################################
####                                                                          ####
#### Function: runserpent_mpi                                                 ####
#### Description: Runs Serpent on a multiple cores                            ####
####                                                                          ####
#### Last updated: 2013-06-19, 3.04 AM                                        ####
####                                                                          ####
##################################################################################

def runserpent_mpi(filename,version,nodes,sss1filename,sss2filename):

	import subprocess

	if version == 1:
		runline = "mpirun -np " + str(nodes) + " " + sss1filename + " " + filename + " > serpent_output.txt"
	else:
		runline = "mpirun -np " + str(nodes) + " " + sss2filename + " " + filename + " > serpent_output.txt"

	subprocess.check_output([runline, "-l"], shell = True)

##################################################################################
####                                                                          ####
#### Function: read_results                                                   ####
#### Description: Reads the Serpent results file (filename_res.m)             ####
####              and collects the results of IMP_KEFF                        ####
####                                                                          ####
#### Last updated: 2013-06-19, 3.05 AM                                        ####
####                                                                          ####
##################################################################################

def read_results(filename, KEFF_LIST, KEFFSD_LIST, iteration, stage, stage1_iterations, stage2_iterations, serptime, where, resultspath):

	# Find the path to the Serpent results file
	respath = filename + "_res.m"

	# Starting value for a counter for the lines of the file
	i = 0

	# Empty list for the results file
	RESLIST      = []
	KEFF_LIST1   = []
	KEFFSD_LIST1 = []

	SL = resultspath + "/EDIS_" + where + "_KEFF.txt"

	# Open the results file, make it readable, choose encoding at Unicode
	if os.path.exists(respath) == True and os.path.isfile(respath) == True:

		with open(respath, 'r', encoding='utf-8') as results:

			slurp = open(SL, 'a', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				RESLIST.append(line) # Add the lines to a new list

				if "IMP_KEFF" in line: # Find the implicit estimate of multiplication factor

					KEFF   = float(RESLIST[i][47:58]) # The location of the value for IMP_KEFF
					KEFFSD = float(RESLIST[i][59:67]) # The location of the value for SD of IMP_KEFF
	
					KEFF_LIST1.append(KEFF) # Add IMP_KEFF values to the list
					KEFFSD_LIST1.append(KEFFSD) # Add IMP_KEFF SD values to the list

					AX = "{0:05.5f}".format(KEFF)

					slurp.write(AX)
					slurp.write(" ")

				i += 1 # Increment the line counter 

			slurp.write("\n")
			slurp.close()
	
			# Define BOEC and EOEC values
			BOEC_KEFF   = KEFF_LIST1[0]
			BOEC_KEFFSD = KEFFSD_LIST1[0]
			EOEC_KEFF   = KEFF_LIST1[len(KEFF_LIST1)-1]
			EOEC_KEFFSD = KEFFSD_LIST1[len(KEFFSD_LIST1)-1]
	
			# Calculate the burnup reactivity swing and standard deviation
			SWING       = EOEC_KEFF - BOEC_KEFF
			SWINGSD     = (BOEC_KEFFSD**2 + EOEC_KEFFSD**2)**0.5
	
			# Make printable outputs for BOEC, EOEC and reactivity swing
			BOEC_KEFFp = "The BOEC multiplication factor is {0:05.5f} +/- {1:05.5f}".format(BOEC_KEFF,BOEC_KEFFSD)
			EOEC_KEFFp = "The EOEC multiplication factor is {0:05.5f} +/- {1:05.5f}".format(EOEC_KEFF,EOEC_KEFFSD)
			SWINGp     = "The burnup reactivity swing is {0:02.2f} +/- {1:02.2f} [pcm]".format(SWING*1e5,SWINGSD*1e5)

			serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')

			if stage == 1:

				X   = "##    - STAGE-1 iteration " + str(iteration+1) + " of " + str(stage1_iterations) + " (finished in " + serptime + ") - "
				XY  = "  STAGE-1 iteration " + str(iteration+1) + " of " + str(stage1_iterations)
				XY2 = " (finished in " + serptime + ")"

			elif stage == 2:

				X  = "##    - STAGE-2 iteration " + str(iteration+1) + " of " + str(stage1_iterations+stage2_iterations) + " (finished in " + serptime + ") - "
				XY = "  STAGE-2 iteration " + str(iteration+1) + " of " + str(stage1_iterations+stage2_iterations) + " (finished in " + serptime + ")"
				XY2 = " (finished in " + serptime + ")"

			serp.write(X)
			serp.write("\n")

			print(XY)
			print(XY2)
			print(" ")

			KEFF_LIST.append(KEFF_LIST1)
			KEFFSD_LIST.append(KEFFSD_LIST1)

			if len(KEFF_LIST) > 1:

				X1 = (KEFF_LIST[iteration])
				X2 = (KEFF_LIST[iteration-1])

			# Return the list of multiplication factor information to the main program
			return (KEFF_LIST, KEFFSD_LIST, BOEC_KEFFp, EOEC_KEFFp, SWINGp)

	else:

		serp = open("EDIS_error.txt", 'a', encoding='utf-8')
		serp.write("There is no results file!")
		serp.close()

		sys.exit("Error occured, check EDIS_error.txt")

	serp.close()

##################################################################################
####                                                                          ####
#### Function: delete_results                                                 ####
#### Description: Deletes the Serpent results files                           ####
####                                                                          ####
#### Last updated: 2013-06-19, 3.05 AM                                        ####
####                                                                          ####
##################################################################################

def delete_results(filename, eqcycle_busteps, resultspath):

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Deleting old output...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")
	serp.close()

	# Find the path to the Serpent results file
	respath = filename + "_res.m"

	# Find the path to the Serpent depletion file
	deppath = filename + "_dep.m"

	# Find the path to the Serpent output file
	outpath = filename + ".out"

	# Find the path to the Serpent seed file
	seedpath = filename + ".seed"	

	# Delete the results file
	while os.path.exists(respath) == True and os.path.isfile(respath) == True:
		os.remove(respath)

	# Delete the depletion file
	while os.path.exists(deppath) == True and os.path.isfile(deppath) == True:
		os.remove(deppath)

	# Delete the output file
	while os.path.exists(outpath) == True and os.path.isfile(outpath) == True:
		os.remove(outpath)

	# Delete the seed file
	while os.path.exists(seedpath) == True and os.path.isfile(seedpath) == True:
		os.remove(seedpath)

	for i in range(eqcycle_busteps):
		depm = filename + ".bumat" + str(i)
		while os.path.exists(depm) == True and os.path.isfile(depm) == True:
			os.remove(depm)

##################################################################################
####                                                                          ####
#### Function: delete_edisfiles                                               ####
#### Description: Deletes the EDIS output files                               ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.54 AM                                        ####
####                                                                          ####
##################################################################################

def delete_edisfiles(resultspath):

	path1 = resultspath + "/EDIS_console.txt"
	path2 = resultspath + "/EDIS_warning.txt"
	path3 = resultspath + "/EDIS_error.txt"

	# Delete the results file
	while os.path.exists(path1) == True and os.path.isfile(path1) == True:
		os.remove(path1)

	while os.path.exists(path2) == True and os.path.isfile(path2) == True:
		os.remove(path2)

	while os.path.exists(path3) == True and os.path.isfile(path3) == True:
		os.remove(path3)

##################################################################################
####                                                                          ####
#### Function: findburnables                                                  ####
#### Description: Finds burnable materials                                    ####
####                                                                          ####
#### Last updated: 2013-06-19, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def findburnables(s1file, resultspath):

	filename = s1file

	# Make empty list to fill with input file
	FILELIST  = []
	FILELIST2 = []
	MATNAMES  = []
	i = 0
	b = 0
	c = 0

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking for burnable materials...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")

	print(" ")
	print("  Checking for burnable materials...")
	print("  OK")

	matpath = s1file + "_mburn"

	# Check if the materials input file exists
	if os.path.exists(matpath) == True and os.path.isfile(matpath) == True:

		# Open the inpit file to read
		with open(matpath, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				FILELIST.append(line) # Add the lines to a new list
				x = 5

				if "mat" and "burn " in line: # Find the implicit estimate of multiplication factor
					
					b += 1 # Adds the number of burnable materials

					for letter in FILELIST[i][4:]:

						if letter == " ":
							MATNAMES.append(FILELIST[i][4:x-1])
							break
							
						x += 1

				i += 1 # Increment the line counter 

		if b < 2:

			serp = open("EDIS_error.txt", 'a', encoding='utf-8')
			serp.write("Can't shuffle with less than 2 burnable materials!")

			sys.exit("Error occured, check EDIS_error.txt")

		else:
			NumMat = "##    OK. (" + str(b) + " materials available for shuffling)"

	else:
		pmm = "##    ERROR! The file containing materials to shuffle (" + matpath +") was not found!"

		pmm2 = "The file containing materials to shuffle (" + matpath +") was not found!"
		serp = open("EDIS_error.txt", 'a', encoding='utf-8')
		serp.write(pmm2)
		serp.close()

		sys.exit("Error occured, check EDIS_error.txt")

	# Check if the main input file exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				FILELIST2.append(line) # Add the lines to a new list

				if "burn " in line:
					
					c += 1 # Adds the number of burnable materials

				i += 1 # Increment the line counter 

			if c > 0:

				serp = open("EDIS_warning.txt", 'a', encoding='utf-8')
				serp.write("You have burnable materials in the main input file")
				serp.write("\n")
				serp.write("Make sure these materials are not apart of the shuffling scheme")
				serp.write("\n")
				serp.close()

	return (MATNAMES,b)

##################################################################################
####                                                                          ####
#### Function: findprintm                                                     ####
#### Description: Finds whether set printm has been activated                 ####
####                                                                          ####
#### Last updated: 2013-06-19, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def findprintm(filename, resultspath):

	# Make empty list to fill with input file
	FILELIST  = []
	i = 0
	ppm = 0

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking material printing settings...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")

	print(" ")
	print("  Checking material printing settings...")
	print("  OK.")

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				FILELIST.append(line) # Add the lines to a new list

				if "set printm 1" in line: # Find the implicit estimate of multiplication factor

					ppm = 1

		if ppm != 1:

			serp = open(filename, 'a', encoding='utf-8')
				
			serp.write("\n")
			serp.write("set printm 1\n")
			
			serp.close()

##################################################################################
####                                                                          ####
#### Function: add_depletion                                                  ####
#### Description: Adds a depletion script if none is present                  ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.33 AM                                        ####
####                                                                          ####
##################################################################################

def add_depletion(filename, eqcycle_days, eqcycle_busteps, resultspath):

	# Make empty list to fill with input file
	FILELIST  = []
	i = 0
	ppm = 0

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking depletion settings...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")

	print("  ")
	print("  Checking depletion settings...")
	print("  OK.")

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				FILELIST.append(line) # Add the lines to a new list

				if "dep " in line: # Find the implicit estimate of multiplication factor
					ppm = 1

			if ppm == 1:

				A = "##    ERROR! Serpent input file should not contain depletion settings!"
				A1 = "Serpent input file should not contain depletion settings!"

				serp = open("EDIS_error.txt", 'a', encoding='utf-8')
				serp.write(A)
				serp.close()

				sys.exit("Error occured, check EDIS_error.txt")

			else:

				# Open the inpit file to read
				serp = open(filename, 'a', encoding='utf-8')
		
				serp.write("\n")
				serp.write("dep daystep ")

				daystep = float(eqcycle_days/eqcycle_busteps)

				for d in range(eqcycle_busteps):
					AA = str(daystep) + " "
					serp.write(AA)			
				serp.close()

##################################################################################
####                                                                          ####
#### Function: findpowernorm                                                  ####
#### Description: Finds whether some power normalization is set               ####
####                                                                          ####
#### Last updated: 2013-06-19, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def findpowernorm(filename, resultspath):

	# Make empty list to fill with input file
	FILELIST  = []
	i = 0
	ppm = 0

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking for source normalization...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")

	print("  ")
	print("  Checking for source normalization...")

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				FILELIST.append(line) # Add the lines to a new list

				sourcenormalization = ["set genrate", "set srcrate", "set fissrate", "set absrate", "set lossrate", "set flux", "set power", "set powdens"]

				if sourcenormalization[0] in line: # Find the implicit estimate of multiplication factor
					ppm = 1
				elif sourcenormalization[1] in line:
					ppm = 1
				elif sourcenormalization[2] in line:
					ppm = 1
				elif sourcenormalization[3] in line:
					ppm = 1
				elif sourcenormalization[4] in line:
					ppm = 1
				elif sourcenormalization[5] in line:
					ppm = 1
				elif sourcenormalization[6] in line:
					ppm = 1
				elif sourcenormalization[7] in line:
					ppm = 1

			if ppm != 1:

				serp = open("EDIS_error.txt", 'a', encoding='utf-8')
				serp.write("Source normalization method not found, burnup is unlikely to work!")
				serp.close()

				sys.exit("Error occured, check EDIS_error.txt")

			else:

				print("  OK.")


##################################################################################
####                                                                          ####
#### Function: setinventory                                                   ####
#### Description: Adds the nuclide inventory to the input file                ####
####                                                                          ####
#### Last updated: 2013-06-19, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def setinventory(filename,mat_checks, version, resultspath):

	FILELIST = []
	inv = 0
	i = 0

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking nuclide inventory...")
	serp.write("\n")

	print("  ")
	print("  Checking nuclide inventory...")
	print("  OK.")

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				FILELIST.append(line) # Add the lines to a new list

				if "set inventory" in line:
					inv = 1
		
			i += 1

			if inv != 1:

				serp = open(filename, 'a', encoding='utf-8')
		
				serp.write("\n")
				serp.write("set inventory ")

				for isotope in mat_checks:
					serp.write(isotope)
					serp.write(" ")

				if version == 1:
					actinv = "act"
					serp.write(actinv)
					fpinv = " fp"
					serp.write(fpinv)
					serp.write("\n")
		
				pm = "##    OK. (" + str(len(mat_checks)) + " isotopes added to nuclide inventory)"

				#serp.write(pm)
				#serp.write("\n")

	serp.close()

##################################################################################
####                                                                          ####
#### Function: makeinput_stage1                                               ####
#### Description: Creates a crude statistics input file                       ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def makeinput_stage1(filename, stage1_neutrons, stage1_activecycles, stage1_inactivecycles):

	FILELIST = []
	i = 0

	matfilename_source = filename + "_mburn"
	matfilename_target = filename + "_stage1_mburn"

	# Check if the input file (still) exists
	if os.path.exists(matfilename_source) == True and os.path.isfile(matfilename_source) == True:

		# Open the inpit file to read
		with open(matfilename_source, 'r', encoding='utf-8') as results:
	
			serpmat = open(matfilename_target, 'w', encoding='utf-8')
	
			for line in results: # Iterate over all lines in the results file
	
				serpmat.write(line)
	
			serpmat.close()

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			s1file = filename + "_stage1"

			if os.path.exists(s1file) == True and os.path.isfile(s1file) == True:
				os.remove(s1file)

			serp = open(s1file, 'w', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				FILELIST.append(line)

				if "set pop" and "set nbuf" and "set pcc" and matfilename_source not in line:

					serp.write(FILELIST[i]) # Add the lines to a new list
			
					i += 1

			kcode = "set pop " + str(stage1_neutrons) + " " + str(stage1_activecycles) + " " + str(stage1_inactivecycles)
			pcc = "set pcc 0"
			buf = "set nbuf 1000"

			serp.write("\n")
			serp.write(pcc)
			serp.write("\n")
			serp.write(buf)
			serp.write("\n")
			serp.write(kcode)
			serp.write("\n")

			includemat = "include \"" + matfilename_target + "\""

			serp.write(includemat)

			serp.close()

	return s1file

##################################################################################
####                                                                          ####
#### Function: makeinput_stage2                                               ####
#### Description: Creates a second crude statistics input file                ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def makeinput_stage2(orgfilename, stage2_neutrons, stage2_activecycles, stage2_inactivecycles):

	geomfile_source    = orgfilename + "_stage1"
	geomfile_target    = orgfilename + "_stage2"
	matfilename_source = orgfilename + "_stage1_mburn"
	matfilename_target = orgfilename + "_stage2_mburn"

	# Check if the input file (still) exists
	if os.path.exists(matfilename_source) == True and os.path.isfile(matfilename_source) == True:

		# Open the inpit file to read
		with open(matfilename_source, 'r', encoding='utf-8') as results:
	
			serpmat = open(matfilename_target, 'w', encoding='utf-8')
	
			for line in results: # Iterate over all lines in the results file
	
				serpmat.write(line)
	
			serpmat.close()

	# Check if the input file (still) exists
	if os.path.exists(geomfile_source) == True and os.path.isfile(geomfile_source) == True:

		# Open the inpit file to read
		with open(geomfile_source, 'r', encoding='utf-8') as results:

			if os.path.exists(geomfile_target) == True and os.path.isfile(geomfile_target) == True:
				os.remove(geomfile_target)

			serp = open(geomfile_target, 'w', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				if "set pop" in line:

					pop=1

				elif matfilename_source in line:

					inc=1

				else:

					serp.write(line) # Add the lines to a new list

			kcode = "set pop " + str(stage2_neutrons) + " " + str(stage2_activecycles) + " " + str(stage2_inactivecycles)
			
			serp.write("\n")
			serp.write(kcode)
			serp.write("\n")

			includemat = "include \"" + matfilename_target + "\""

			serp.write(includemat)

			serp.close()

	return geomfile_target

##################################################################################
####                                                                          ####
#### Function: checkmaterials                                                 ####
#### Description: Finds the atomic density of materials to be checked         ####
####                                                                          ####
#### Last updated: 2013-06-19, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def checkmaterials(filename, matnames, isotope_checks, iteration, Materialinfo, version, where, printconvergence, resultspath):

	# EMPTY VECTORS
	FILELIST       = [] # Load the file in to a variable
	adens_matnames = [] # Get the atom density names
	i              = 0  # Start the counter for materials
	
	# EMPTY LIST/DICTIONARY
	matinfo = {}
	
	# Path to the depletion output file
	path = filename + "_dep.m"
	
	# Check if the depletion output file exists
	if os.path.exists(path) == True and os.path.isfile(path) == True:
	
		# Open the inpit file to read
		with open(path, 'r', encoding='utf-8') as results:
			
			for line in results: # Iterate over all lines in the results file
	
				FILELIST.append(line) # Add the lines to a new list
	
				for name in matnames:
	
					A = "MAT_" + name + "_ADENS = ["
	
					if A in line:
	
						STARTrow = i+1
						mati = {name : STARTrow}
						matinfo.update(mati)
	
				i += 1

	if printconvergence == 1:

		convpath = resultspath + "/materialconvergence"
		if not os.path.exists(convpath): os.makedirs(convpath)

	# Collect all the material atom densities in each cell at the given iteration
	for zone in matnames:
	
		STARTx = matinfo.get(zone)
		x0 = 0
	
		for isotope in isotope_checks:
			
			ADENS = float(FILELIST[STARTx+x0][0:12])
			IDx = zone + "_" + isotope + "_iter" + str(iteration)
	
			Ax = {IDx : ADENS}
			Materialinfo.update(Ax)

			if printconvergence == 1:

				A = convpath + "/EDIS_" + where + "_" + zone + "_" + isotope + ".txt"
				serp = open(A, 'a', encoding='utf-8')
				serp.write(str(ADENS))
				serp.write("\n")
	
			x0 += 1

	if printconvergence == 1:

		serp.write("\n")
		serp.close()

	return Materialinfo

##################################################################################
####                                                                          ####
#### Function: checkshuffle                                                   ####
#### Description: Finds out what material goes in and out                     ####
####                                                                          ####
#### Last updated: 2013-06-21, 2.37 PM                                        ####
####                                                                          ####
##################################################################################

def checkshuffle(shufflescheme, resultspath):

	matKEYS    = []
	matVALUES  = []
	IN         = []
	OUT        = []   
	shuffmat   = []
	exmat      = []


	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Analyzing shuffling scheme...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")

	print("  ")
	print("  Analyzing shuffling scheme...")
	print("  OK.")

	AA = sorted((shufflescheme.keys()))
	BB = sorted((shufflescheme.values()))

	for zone in AA:

		if zone not in BB:
			IN.append(zone)
		else:
			shuffmat.append(zone)

	for zone in BB:

		if zone not in AA:
			OUT.append(zone)
		else:
			exmat.append(zone)

	return (IN, OUT, shuffmat)

##################################################################################
####                                                                          ####
#### Function: shuffle                                                        ####
#### Description: Shuffles!                                                   ####
####                                                                          ####
#### Last updated: 2013-06-19, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def shuffle(filename, shufflescheme, eqcycle_busteps, VOLUMES, matnames, IN, shuffledmats, stage, orgfilename, critty, version):

	matKEYS    = []
	matVALUES  = [] 
	FILELIST   = []
	FILELIST2  = []
	SFUEL      = []
	SFUEL2     = []

	i1 = 0
	i2 = 0
	i3 = 0

	if critty == 0:

		if stage == 2:
	
			targetname = orgfilename +"_stage2_mburn"
	
		else:
	
			targetname  = orgfilename + "_stage1_mburn"

	elif critty == 1:

		if stage == 2:
	
			targetname = orgfilename +"_lin2_mburn"
	
		else:
	
			targetname  = orgfilename + "_lin1_mburn"

	elif critty == 2:

		if stage == 2:
	
			targetname = orgfilename +"_eq2_mburn"
	
		else:
	
			targetname  = orgfilename + "_eq1_mburn"

	sourcename  = filename + ".bumat" + str(eqcycle_busteps)
	source1name = filename + ".bumat0"

	#print(source1name)
	#print(sourcename)
	
	if os.path.exists(targetname) == True and os.path.isfile(targetname) == True:
		os.remove(targetname)

	serp = open(targetname, 'w', encoding='utf-8')

	with open(source1name, 'r', encoding='utf-8') as results:

		for line in results: # Iterate over all lines in the file

			FILELIST.append(line)

			for starterfuel in IN:

				if starterfuel + " " in line:

					if version == 2:
						SFUEL.append(line.rstrip("\n") + " burn 1")
					else:
						SFUEL.append(line.rstrip("\n") + " burn 1 vol " + VOLUMES.get(starterfuel))
					i1 += 1
	
		for L in FILELIST:

			for starterzone in IN:

				if starterzone + " " in L:

					serp.write(SFUEL[i3])
					serp.write("\n")

					for linex in FILELIST[:][i2+1:]:

						if "mat " in linex:
							
							i3 +=1
							break

						else:
							
							serp.write(linex)

			i2 += 1	

	i1 = 0
	i2 = 0
	i3 = 0

	with open(sourcename, 'r', encoding='utf-8') as results2:

			for line in results2: # Iterate over all lines in the file
	
				FILELIST2.append(line)
	
				for fuel in shuffledmats:
	
					if fuel + " " in line:
	
						old = fuel
						new = shufflescheme[fuel]

						MESS = "The material of " + old.rstrip("core") + " is now in " + new.rstrip("core")

						print(MESS)

						C = line.replace(old,new)

						if version == 2:
							SFUEL2.append(C.rstrip("\n") + " burn 1 ")
						else:
							SFUEL2.append(C.rstrip("\n") + " burn 1 vol " + VOLUMES.get(fuel))
						i1 += 1

			for L in FILELIST2:

				for shufflezone in shuffledmats:
	
					if shufflezone + " " in L:

						serp.write(SFUEL2[i3])
						serp.write("\n")
	
						for linex in FILELIST2[:][i2+1:]:
	
							if "mat " in linex:
								
								i3 +=1
	
								break
	
							else:
								
								serp.write(linex)

				i2 += 1	

	i6 = 0
	SWITCH = []

	for unlucky in shufflescheme:

		if unlucky in IN:

			A = {unlucky : shufflescheme[unlucky]}

			for line in FILELIST2:

				if unlucky + " " in line:

					SWITCHAROO = line.replace(unlucky, A[unlucky]) 

					if version == 2:
						SWITCH.append(SWITCHAROO.rstrip("\n") + " burn 1")
					else:
						SWITCH.append(SWITCHAROO.rstrip("\n") + " burn 1 vol " + VOLUMES.get(unlucky))

	i2 = 0
	i3 = 0

	for L in FILELIST2:

		for shufflezone in IN:
		
			if shufflezone + " " in L:
		
				serp.write(SWITCH[i3])
				serp.write("\n")
		
				for linex in FILELIST2[:][i2+1:]:
		
					if "mat " in linex:

						i3 +=1
						break
		
					else:

						serp.write(linex)
	
		i2 += 1	

	serp.close()

##################################################################################
####                                                                          ####
#### Function: findvolume                                                     ####
#### Description: Finds material volume                                       ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def findvolume(filename, matnames, IN, shuffledmats, resultspath):

	# Make empty list to fill with input file
	VOLUMELIST   = []

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write("##    Checking burnable volumes...")
	serp.write("\n")
	serp.write(ok)
	serp.write("\n")
	serp.close()

	print("  ")
	print("  Checking burnable volumes...")
	print("  OK.")

	matpath = filename + "_mburn"

	VOLLIST = {}

	# Check if the materials input file exists
	if os.path.exists(matpath) == True and os.path.isfile(matpath) == True:

		# Open the file to read
		with open(matpath, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				for material in matnames:

					if material + " " in line:

						A = line.find("vol ")
						x = A + 4
						x0 = x

						for letter in line[x0:]:

							if letter != " ":
								x += 1
							else:
								break
		
						VOLUMELIST.append(line[x0:x])
						VOLCC = {material : line[x0:x]}
						VOLLIST.update(VOLCC)

	return (VOLLIST)

##################################################################################
####                                                                          ####
#### Function: materialerror                                                  ####
#### Description: Finds material errors                                       ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def materialerror(Materialinfo, matnames, isotope_checks, iteration, resultspath):

	Materror = {}

	for zone in matnames:
	
		for isotope in isotope_checks:
	
			Before = zone + "_" + isotope + "_iter" + str(iteration-1)
			Now    = zone + "_" + isotope + "_iter" + str(iteration)
	
			adens_before   = Materialinfo.get(Before)
			adens_now      = Materialinfo.get(Now)

			adens_diff     = abs(adens_now - adens_before)
			adens_fracdiff = adens_diff/adens_now
	
			IDx = zone + "_" + isotope + "_iter" + str(iteration)
	
			Ax = {IDx : adens_fracdiff}
			Materror.update(Ax)

	# Find the maximum atom density difference
	densdiffcollect = []
	
	for ID, densdiff in Materror.items():
	
		densdiffcollect.append(densdiff)
	
	MaxDensDiff = max(densdiffcollect)
	
	for ID, densdiff in Materror.items():
	
		if densdiff == MaxDensDiff:
	
			MaxDensID = ID
	
	for zone in matnames:
	
		if zone in MaxDensID:
	
			MaxDensZone = zone
	
	for isotope in isotope_checks:
	
		if isotope in MaxDensID:
	
			MaxDensIsotope = isotope
	
	A = "##    Largest material discrepancy is " + MaxDensIsotope + " in zone " + MaxDensZone + ", error is {0:02.2%}".format(MaxDensDiff)
	
	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(A)
	serp.write("\n")
	serp.write(space)
	serp.write("\n")
	serp.close()
	
	return MaxDensDiff

##################################################################################
####                                                                          ####
#### Function: definekefferror                                                ####
#### Description: Calculates the error in k_eff                               ####
####                                                                          ####
#### Last updated: 2013-06-27, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def definekefrerror(eqcycle_busteps, iteration, KEFF_LIST, Name, resultspath):

	E = []
	D = []
	
	for i in range(eqcycle_busteps):
	
		A = KEFF_LIST[iteration][i]
		B = KEFF_LIST[iteration-1][i]
		C = abs((A - B)/A)
		D.append(C)
		E.append([i, C])
		
	keff_max = max(D)
	
	for thing in E:
	
		if thing[1] == keff_max:
	
			keff_max_bustep = thing[0]
	
	A = "##    Largest k_eff discrepancy is {0:02.2%}".format(keff_max) + " at burnup step " + str(keff_max_bustep + 1)

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write(space)
	serp.write("\n")
	serp.write(A)
	serp.write("\n")
	serp.close()

	return keff_max

##################################################################################
####                                                                          ####
#### Function: stage1notes                                                    ####
#### Description: Prints information on stage 1                               ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def stage1notes(resultspath):

	info1 = "##    RUNNING STAGE-1 ANALYSIS"

	print(" ")
	print("  Checks complete.")
	print(" ")
	print("-----------------------------------------")
	print("      RUNNING STAGE-1 ANALYSIS           ")
	print("-----------------------------------------")
	print(" ")

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	serp.write("##")
	serp.write("\n")
	serp.write("##    Preparing for STAGE-1 conditioning...")
	serp.write("\n")
	serp.write("##         - Adjusting neutron population")
	serp.write("\n")
	serp.write("##         - Switching off predictor/corrector")
	serp.write("\n")
	serp.write("##         - Adjusting buffer size")
	serp.write("\n")
	serp.write("##")
	serp.write("\n")
	serp.write(info1)
	serp.write("\n")
	serp.write("##")
	serp.write("\n")
	serp.close()

##################################################################################
####                                                                          ####
#### Function: convergednotes                                                 ####
#### Description: Prints information on convergence                           ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def convergednotes(firstconvtime, keffmin, keffmax, eqcycle_kefftarget, eqdays, batches, where, medfilespath, finalfilespath, resultspath):

	# Get the depletion data
	if where == "stage1":

		printpath  = medfilespath

	elif where == "stage2":

		printpath  = medfilespath

	elif where == "lin1":

		printpath  = medfilespath
 
	elif where == "lin2":

		printpath  = medfilespath

	elif where == "eq1":

		printpath = finalfilespath

	elif where == "eq2":

		printpath  = finalfilespath

	diffkeff = abs((keffmin-eqcycle_kefftarget)/eqcycle_kefftarget)
	
	import math
	residencetime = eqdays * batches
	
	if residencetime < 365:
	
		restime = "{0:01.0f}".format(eqdays)
	
	else:
	
		years = int(math.floor(residencetime/365))
		days  = residencetime - 365*years
		restime = "{0:01.0f}".format(years) + " years and {0:01.0f}".format(days) + " days"
	
	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')
	
	sp1 = "///----------------------------------------------------------------------///"
	sp2 = "|                                                                       "
	sp3 = "|     System reached target convergence in " + firstconvtime                     
	sp4 = "|                                                                     "
	sp5 = "|     Eq. cycle time was set at {0:01.0f}".format(eqdays) + " days"
	sp6 = "|     Fuel residence time is " + restime
	sp7 = "|                                                                     "
	sp8 = "|     Min/max cycle k_eff is {0:05.5f}".format(keffmin) + " / {0:05.5f}".format(keffmax) 
	sp9 = "|     Error in min. k_eff compared to target is {0:02.2%}".format(diffkeff)
	sp10= "|                                                                       "
	
	serp.write(sp1)
	serp.write("\n")
	serp.write(sp2)
	serp.write("\n")
	serp.write(sp3)
	serp.write("\n")
	serp.write(sp4)
	serp.write("\n")
	serp.write(sp5)
	serp.write("\n")
	serp.write(sp6)
	serp.write("\n")
	serp.write(sp7)
	serp.write("\n")
	serp.write(sp8)
	serp.write("\n")
	serp.write(sp9)
	serp.write("\n")
	serp.write(sp10)
	
	serp.close()

	Afile = resultspath + "/EDIS_" + where + "_info.txt"
	serp1 = open(Afile, 'a', encoding='utf-8')

	serp1.write(sp1)
	serp1.write("\n")
	serp1.write(sp2)
	serp1.write("\n")
	serp1.write(sp3)
	serp1.write("\n")
	serp1.write(sp4)
	serp1.write("\n")
	serp1.write(sp5)
	serp1.write("\n")
	serp1.write(sp6)
	serp1.write("\n")
	serp1.write(sp7)
	serp1.write("\n")
	serp1.write(sp8)
	serp1.write("\n")
	serp1.write(sp9)
	serp1.write("\n")
	serp1.write(sp10)
	serp1.write("\n")
	serp1.write(sp1)
	serp1.write("\n")
	serp1.write("\n")
	serp1.close()

##################################################################################
####                                                                          ####
#### Function: stage2notes                                                    ####
#### Description: Prints information on stage 2                               ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def stage2notes(S1time, resultspath):

	info1 = "##    RUNNING STAGE-2 ANALYSIS"

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')

	serp.write(space)
	serp.write("\n")
	serp.write("##    ---------------------------------------------------------------")
	serp.write("\n")

	AA = "##    STAGE-1 conditioning complete in " + S1time 

	serp.write(AA)
	serp.write("\n")
	serp.write("##    ---------------------------------------------------------------")
	serp.write("\n")
	serp.write(space)
	serp.write("\n")
	serp.write("##    Preparing for STAGE-2 conditioning...")
	serp.write("\n")
	serp.write("##         - Adjusting neutron population")
	serp.write("\n")
	serp.write("##         - Switching off predictor/corrector")
	serp.write("\n")
	serp.write("##         - Adjusting buffer size")
	serp.write("\n")
	serp.write("##")
	serp.write("\n")
	serp.write(info1)
	serp.write("\n")
	serp.write("##")
	serp.write("\n")
	serp.close()

	print("  RUNNING STAGE-2 ANALYSIS")
	print(" ")

##################################################################################
####                                                                          ####
#### Function: precriticalnotes                                               ####
#### Description: Prints information on the guessed critical eq. cycle        ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def precriticalnotes(keff0min, keff1min, eqcycle_days, eqcycle_days1, eqcycle_days2, resultspath):
	
	sp3 = "|     2nd run, eq. cycle time of " + str(eqcycle_days1) + " days had a min. k_eff of " + str(keff1min)
	sp4 = "|     Aiming at critical eq. cycle at a cycle of around " + str(int(round(eqcycle_days2))) + " days"
	sp5 = "|                                                                         "
	sp6 = "|     Starting a new STAGE-1 eq. cycle run with the updated cycle time"
	sp7 = "|"
	sp8 = "///----------------------------------------------------------------------///"

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')

	serp.write("\n")
	serp.write(sp3)
	serp.write("\n")
	serp.write(sp4)
	serp.write("\n")
	serp.write(sp5)
	serp.write("\n")
	serp.write(sp6)
	serp.write("\n")
	serp.write(sp7)
	serp.write("\n")
	serp.write(sp8)
	serp.write("\n")
	serp.write(space)
	serp.write("\n")

	serp.close()

##################################################################################
####                                                                          ####
#### Function: finishednotes                                                  ####
#### Description: Prints information on the final results                     ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def finishednotes(EqTime, resultspath):
	
	sp0 = "|     Total calculation time was " + EqTime
	sp1 = "|                                                                         "
	sp2 = "|     To improve results, use better statistics, tighter convergence criteria"
	sp3 = "|     and more burnup steps!"
	sp4 = "|     "
	sp5 = "|     Thank you for using EDIS! (Every day I'm shuffling!)"
	sp6= "|"
	sp7= "///----------------------------------------------------------------------///"

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')

	serp.write("\n")
	serp.write(sp0)
	serp.write("\n")
	serp.write(sp1)
	serp.write("\n")
	serp.write(sp2)
	serp.write("\n")
	serp.write(sp3)
	serp.write("\n")
	serp.write(sp4)
	serp.write("\n")
	serp.write(sp5)
	serp.write("\n")
	serp.write(sp6)
	serp.write("\n")
	serp.write(sp7)

	serp.close()

##################################################################################
####                                                                          ####
#### Function: runcriticality                                                 ####
#### Description: Finds the critical eq-cycle                                 ####
####                                                                          ####
#### Last updated: 2013-07-19, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def runcriticality(eqcycle_busteps, eqcycle_days, keff0, keff1, criticalitytries, eqcycle_kefftarget, eqcycle_days1, resultspath):

	A  = ""
	AA = ""
	E0 = []
	E1 = []
	A0 = []
	A1 = []
	
	keff_target = eqcycle_kefftarget
	
	for i in range(eqcycle_busteps):
	
		A0 = keff0[i]
		E0.append([i, A0])
		
	keff_max = max(E0)
	keff_min = min(E0)
	 
	if criticalitytries == 0:
	
		if keff_min[1] < keff_target:
		
			AA = "Eq. cycle is subcritical at burnup step " + str(keff_min[0]+1)

		else:

			AA = "Eq. cycle is supercritical throughout the burnup cycle"
		
		if keff_max[0] == 0:
		
			A = "Negative burnup reactivity swing, decreasing cycle length"
			eqcycle_days1 = eqcycle_days/1.25
		
		elif keff_max[0] == eqcycle_busteps-1:
		
			A = "Positive burnup reactivity swing, increasing cycle length"
			eqcycle_days1 = eqcycle_days*1.25
		
		else:
			
			A = "Parabolic reactivity swing, core-redesign suggested"

		sp3 = "|     " + A                       
		sp7 = "|     Cycle time changed from " + str(eqcycle_days) + " days to " + str(eqcycle_days1) + " days"
		sp5 = "|                                                                         "		
		sp6 = "|     Starting a new STAGE-1 eq. cycle run with the updated cycle time    "
		sp8 = "|                                                                           "
		sp9 = "///----------------------------------------------------------------------///"		
	
		serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')

		serp.write("\n")
		serp.write(sp3)
		serp.write("\n")
		serp.write(sp7)
		serp.write("\n")
		serp.write(sp5)
		serp.write("\n")
		serp.write(sp6)
		serp.write("\n")
		serp.write(sp8)
		serp.write("\n")
		serp.write(sp9)
		serp.write("\n")
		serp.write(space)
		serp.write("\n")

		serp.close()

	elif criticalitytries == 1:
	
		keff0_min = min(keff0)
		keff1_min = min(keff1)
	
		y1 = keff0_min
		y2 = keff1_min
	
		x1 = eqcycle_days
		x2 = eqcycle_days1
	
		dy = y2 - y1
		dx = x2 - x1
	
		dydx = dy/dx
	
		daychange = (keff_target - y1)/dydx
	
		eqcycle_days1 = x1 + daychange
		
	return (eqcycle_days1)	

##################################################################################
####                                                                          ####
#### Function: makeinput_critcycle1                                           ####
#### Description: Creates a second crude statistics input file                ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def makeinput_critcycle1(orgfilename, eqcycle_days1, eqcycle_busteps):

	geomfile_source    = orgfilename + "_stage1"
	geomfile_target    = orgfilename + "_lin1"
	matfilename_source = orgfilename + "_stage2_mburn"
	matfilename_target = orgfilename + "_lin1_mburn"

	# Check if the input file (still) exists
	if os.path.exists(matfilename_source) == True and os.path.isfile(matfilename_source) == True:

		ok = 1

	else:

		matfilename_source = orgfilename + "_stage1_mburn"

	# Open the inpit file to read
	with open(matfilename_source, 'r', encoding='utf-8') as results:
	
		serpmat = open(matfilename_target, 'w', encoding='utf-8')
	
		for line in results: # Iterate over all lines in the results file
	
			serpmat.write(line)
	
		serpmat.close()

	# Check if the input file (still) exists
	if os.path.exists(geomfile_source) == True and os.path.isfile(geomfile_source) == True:

		# Open the inpit file to read
		with open(geomfile_source, 'r', encoding='utf-8') as results:

			if os.path.exists(geomfile_target) == True and os.path.isfile(geomfile_target) == True:
				os.remove(geomfile_target)

			serp = open(geomfile_target, 'w', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				if "dep" in line:

					dep=1

				elif "include" in line:

					inc=1

				else:

					serp.write(line) # Add the lines to a new list

			serp.write("\n")
			serp.write("dep daystep ")

			daystep = float(eqcycle_days1/eqcycle_busteps)
			for d in range(eqcycle_busteps):
				AA = str(daystep) + " "
				serp.write(AA)	

			includemat = "include \"" + matfilename_target + "\""
			serp.write("\n")
			serp.write(includemat)
			serp.write("\n")
			serp.write("include 'BnB_nonfuel'")
			serp.close()

	return geomfile_target

##################################################################################
####                                                                          ####
#### Function: makeinput_critcycle2                                           ####
#### Description: Creates a second crude statistics input file                ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def makeinput_critcycle2(orgfilename, eqcycle_days1, eqcycle_busteps, stage2_neutrons, stage2_activecycles, stage2_inactivecycles):

	geomfile_source    = orgfilename + "_lin1"
	geomfile_target    = orgfilename + "_lin2"
	matfilename_source = orgfilename + "_lin1_mburn"
	matfilename_target = orgfilename + "_lin2_mburn"

	# Check if the input file (still) exists
	if os.path.exists(matfilename_source) == True and os.path.isfile(matfilename_source) == True:

		# Open the inpit file to read
		with open(matfilename_source, 'r', encoding='utf-8') as results:
	
			serpmat = open(matfilename_target, 'w', encoding='utf-8')
	
			for line in results: # Iterate over all lines in the results file
	
				serpmat.write(line)
	
			serpmat.close()

	# Check if the input file (still) exists
	if os.path.exists(geomfile_source) == True and os.path.isfile(geomfile_source) == True:

		# Open the inpit file to read
		with open(geomfile_source, 'r', encoding='utf-8') as results:

			if os.path.exists(geomfile_target) == True and os.path.isfile(geomfile_target) == True:
				os.remove(geomfile_target)

			serp = open(geomfile_target, 'w', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				if "include" in line:

					inc=1

				elif "pop" in line:

					pop = 1

				else:

					serp.write(line) # Add the lines to a new list

			kcode = "set pop " + str(stage2_neutrons) + " " + str(stage2_activecycles) + " " + str(stage2_inactivecycles)
			
			serp.write("\n")
			serp.write(kcode)
			serp.write("\n")

			serp.write("\n")
			includemat = "include \"" + matfilename_target + "\""
			serp.write(includemat)
			serp.write("\n")
			serp.write("include 'BnB_nonfuel'")
			serp.close()

	return geomfile_target

##################################################################################
####                                                                          ####
#### Function: makeinput_eqcycle1                                             ####
#### Description: Creates a second crude statistics input file                ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def makeinput_eqcycle1(orgfilename, eqcycle_days2, eqcycle_busteps):

	geomfile_source    = orgfilename + "_lin1"
	geomfile_target    = orgfilename + "_eq1"

	matfilename_source = orgfilename + "_lin2_mburn"

	if os.path.exists(matfilename_source) != True or os.path.isfile(matfilename_source) != True:

		matfilename_source = orgfilename + "_lin1_mburn"

	matfilename_target = orgfilename + "_eq1_mburn"

	# Open the inpit file to read
	with open(matfilename_source, 'r', encoding='utf-8') as results:
	
		serpmat = open(matfilename_target, 'w', encoding='utf-8')
	
		for line in results: # Iterate over all lines in the results file
	
			serpmat.write(line)
	
		serpmat.close()

	# Check if the input file (still) exists
	if os.path.exists(geomfile_source) == True and os.path.isfile(geomfile_source) == True:

		# Open the inpit file to read
		with open(geomfile_source, 'r', encoding='utf-8') as results:

			if os.path.exists(geomfile_target) == True and os.path.isfile(geomfile_target) == True:
				os.remove(geomfile_target)

			serp = open(geomfile_target, 'w', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				if "dep" in line:

					dep=1

				elif "include" in line:

					inc=1

				else:

					serp.write(line) # Add the lines to a new list

			serp.write("\n")
			serp.write("dep daystep ")

			daystep = float(eqcycle_days2/eqcycle_busteps)
			for d in range(eqcycle_busteps):
				AA = str(daystep) + " "
				serp.write(AA)	

			includemat = "include \"" + matfilename_target + "\""
			serp.write("\n")
			serp.write(includemat)
			serp.write("\n")
			serp.write("include 'BnB_nonfuel'")
			serp.close()

	return geomfile_target

##################################################################################
####                                                                          ####
#### Function: makeinput_eqcycle2                                             ####
#### Description: Creates a second crude statistics input file                ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def makeinput_eqcycle2(orgfilename, eqcycle_days2, eqcycle_busteps, stage2_neutrons, stage2_activecycles, stage2_inactivecycles):

	geomfile_source    = orgfilename + "_eq1"
	geomfile_target    = orgfilename + "_eq2"
	matfilename_source = orgfilename + "_eq1_mburn"
	matfilename_target = orgfilename + "_eq2_mburn"

	# Check if the input file (still) exists
	if os.path.exists(matfilename_source) == True and os.path.isfile(matfilename_source) == True:

		# Open the inpit file to read
		with open(matfilename_source, 'r', encoding='utf-8') as results:
	
			serpmat = open(matfilename_target, 'w', encoding='utf-8')
	
			for line in results: # Iterate over all lines in the results file
	
				serpmat.write(line)
	
			serpmat.close()

	# Check if the input file (still) exists
	if os.path.exists(geomfile_source) == True and os.path.isfile(geomfile_source) == True:

		# Open the inpit file to read
		with open(geomfile_source, 'r', encoding='utf-8') as results:

			if os.path.exists(geomfile_target) == True and os.path.isfile(geomfile_target) == True:
				os.remove(geomfile_target)

			serp = open(geomfile_target, 'w', encoding='utf-8')

			for line in results: # Iterate over all lines in the results file

				if "include" in line:

					inc=1

				elif "pop" in line:

					pop = 1

				else:

					serp.write(line) # Add the lines to a new list

			kcode = "set pop " + str(stage2_neutrons) + " " + str(stage2_activecycles) + " " + str(stage2_inactivecycles)
			
			serp.write("\n")
			serp.write(kcode)
			serp.write("\n")

			serp.write("\n")
			includemat = "include \"" + matfilename_target + "\""
			serp.write(includemat)
			serp.write("\n")
			serp.write("include 'BnB_nonfuel'")
			serp.close()

	return geomfile_target

##################################################################################
####                                                                          ####
#### Function: timediffcalc                                                   ####
#### Description: Prints time differences in a nice way                       ####
####                                                                          ####
#### Last updated: 2013-06-21, 4.55 AM                                        ####
####                                                                          ####
##################################################################################

def timediffcalc(After, Before):
	
	import math
	
	timediff = abs(After-Before)
	
	A = "TBD"

	hourdiff = timediff / 3600
	mindiff  = timediff / 60
	secdiff  = timediff	
	
	if secdiff >= 1 and mindiff < 1:
	
		if int(round(secdiff)) == 1:
	
			S = " second"
	
		else: 
	
			S = " seconds"
	
		A = str(int(round(secdiff))) + S
	
	if mindiff >= 1 and hourdiff < 1:
	
		mindiff = int(math.floor(mindiff))
		secdiff = secdiff - mindiff*60
	
		if int(round(secdiff)) == 1:
	
			S = " second"
	
		else: 
	
			S = " seconds"
	
		if int(round(mindiff)) == 1:
		
			M = " minute"
		
		else: 
		
			M = " minutes"	
	
		A = str(int(round(mindiff))) + M + " and " + str(int(round(secdiff))) + S
	
	if hourdiff >= 1:
	
		hourdiff = int(math.floor(hourdiff))
		mindiff  = int(math.floor(mindiff - hourdiff*60))
		secdiff  = secdiff - hourdiff*3600 - mindiff*60
	
		if int(round(hourdiff)) == 1:
		
			H = " hour"
		
		else: 
		
			H = " hours"
	
		if int(round(mindiff)) == 1:
		
			M = " minute"
		
		else: 
		
			M = " minutes"	
	
		if int(round(secdiff)) == 1:
	
			S = " second"
	
		else: 
	
			S = " seconds"
	
		A = str(int(round(hourdiff))) + H + ", " + str(int(round(mindiff))) + M + " and " + str(int(round(secdiff))) + S
	
	return(A)

##################################################################################
####                                                                          ####
#### Function: stage2finished                                                 ####
#### Description: Creates celebratory message                                 ####
####                                                                          ####
#### Last updated: 2013-07-24, 7.28 PM                                        ####
####                                                                          ####
##################################################################################

def stage2finished(S2time, resultspath):

	serp = open(resultspath + "/EDIS_console.txt", 'a', encoding='utf-8')

	serp.write("##    ---------------------------------------------------------------")
	serp.write("\n")

	AA = "##    STAGE-2 conditioning complete in " + S2time 

	serp.write(AA)
	serp.write("\n")
	serp.write("##    ---------------------------------------------------------------")
	serp.write("\n")
	serp.write(space)
	serp.write("\n")
	serp.close()

##################################################################################
####                                                                          ####
#### Function: fima                                                           ####
#### Description: Calculates FIMA                                             ####
####                                                                          ####
#### Last updated: 2013-08-27, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def fima(AxialZones, eqcycle_batches, orgfilename, where, shufflescheme, matnames, version):

	zones = AxialZones * eqcycle_batches
	
	# Get the depletion data
	mpath = orgfilename + "_" + where + "_mburn"
	
	# Define the shuffling scheme
	Feedfuel = []
	Dischargefuel = []
	
	for name in matnames:
	
		if name not in shufflescheme.values():
	
			Feedfuel.append(name)
	
		if name not in shufflescheme.keys():
	
			Dischargefuel.append(name)
	
	outfile = []
	matIDs = {}
	
	with open(mpath, 'r', encoding='utf-8') as results:
	
		i = 0
	
		for line in results:
	
			outfile.append(line)
			i += 1
	
			for zone in matnames:
	
				zoneid = "mat  " + zone + "  "
	
				if zoneid in line:
	
					lookupid = {zone : i}
					matIDs.update(lookupid)
	
	ZoneIsotopeIDs = {}
	
	maxvc = []
	
	for k, v in matIDs.items():
	
		maxvc.append(v)
	
	maxcore = max(maxvc)
	
	for k, v in matIDs.items():
	
		if v == maxcore:
	
			MaxCore = k
	
	totlength = len(outfile)
	row = 1	
	
	IsotopicZoneAtomDensity = {}
	
	for k, v in matIDs.items():
	
		i = 0
		isotoperow = " "
		futurerow = " "
		atomdensity = {}
	
		IDs = []
	
		if k == MaxCore:
	
			while row < totlength-1:
	
				row = v+i
		
				isotoperow = outfile[row]
				ID    = isotoperow[10:16]
		
				if version == 2:
					adensvalue = float(isotoperow[22:43])
				else:
					adensvalue = float(isotoperow[22:34])

				IDs.append(ID)
				atomdensity.update({ID : adensvalue})
		
				i += 1
	
		else:
	
			while "mat" not in futurerow:
				
				row = v+i
		
				isotoperow = outfile[row]
				futurerow = outfile[row+1]

				ID    = isotoperow[10:16]
		
				if version == 2:
					adensvalue = float(isotoperow[22:43])
				else:
					adensvalue = float(isotoperow[22:34])

				IDs.append(ID)
				atomdensity.update({ID : adensvalue})
		
				i += 1
	
		atomdensityzonecollect = {k : atomdensity}
		IsotopicZoneAtomDensity.update(atomdensityzonecollect)
	
		IDsx = {k : IDs}
		ZoneIsotopeIDs.update(IDsx)
	
	ActinideAtomDensity = {}
	
	for cell in matnames:
		
			amf = []
			aaf = []
		
			X = ZoneIsotopeIDs.get(cell)
		
			for isotope in X[0:len(X)-1]:
			
				A = float(isotope)
				
				if A >= 90000:
				
					af = IsotopicZoneAtomDensity.get(cell)
					af2 = af.get(isotope)
					aaf.append(af2)
	
			sumaact = sum(aaf)
			adensf = {cell : sumaact}
			ActinideAtomDensity.update(adensf)
	
	BurnupFIMA = {}
	
	for level in range(AxialZones):
	
		Feed      = Feedfuel[level]
		Discharge = Dischargefuel[level]
	
		FeedAD = ActinideAtomDensity.get(Feed)
		DischargeAD = ActinideAtomDensity.get(Discharge)
	
	
		FIMA = (FeedAD - DischargeAD)/FeedAD
		BUfima = {level : FIMA}
		BurnupFIMA.update(BUfima)
	
	return (BurnupFIMA)

##################################################################################
####                                                                          ####
#### Function: bustuff                                                        ####
#### Description: Calculates peaking and burnup                               ####
####                                                                          ####
#### Last updated: 2013-08-11, 7.59 AM                                        ####
####                                                                          ####
##################################################################################

def bustuff(orgfilename, matnames, eqcycle_busteps, eqcycle_days, VOLUMES, isotope_checks, AxialZones, version, eqcycle_batches, shufflescheme, where, orgfilespath, medfilespath, finalfilespath, converged):

	zones = AxialZones * eqcycle_batches

	final = 0

	# Get the depletion data
	if where == "stage1":
	
		respath    = orgfilename + "_stage1_dep.m"
		dotrespath = orgfilename + "_stage1_res.m"
		outpath    = orgfilename + "_stage1.out"
		printpath  = medfilespath

	elif where == "stage2":

		respath    = orgfilename + "_stage2_dep.m"
		dotrespath = orgfilename + "_stage2_res.m"
		outpath    = orgfilename + "_stage2.out"
		printpath  = medfilespath

	elif where == "lin1":

		respath    = orgfilename + "_lin1_dep.m"
		dotrespath = orgfilename + "_lin1_res.m"
		outpath    = orgfilename + "_lin1.out"
		printpath  = medfilespath
 
	elif where == "lin2":

		respath    = orgfilename + "_lin2_dep.m"
		dotrespath = orgfilename + "_lin2_res.m"
		outpath    = orgfilename + "_lin2.out"
		printpath  = medfilespath

	elif where == "eq1":

		respath    = orgfilename + "_eq1_dep.m"
		dotrespath = orgfilename + "_eq1_res.m"
		outpath    = orgfilename + "_eq1.out"

		if converged == 1:

			printpath = finalfilespath
			final = 1

		else:

			printpath = medfilespath

	elif where == "eq2":

		final = 1
		respath    = orgfilename + "_eq2_dep.m"
		dotrespath = orgfilename + "_eq2_res.m"
		outpath    = orgfilename + "_eq2.out"
		printpath  = finalfilespath

	# Define the shuffling scheme
	Feedfuel = []
	Dischargefuel = []
	
	for name in matnames:
	
		if name not in shufflescheme.values():
	
			Feedfuel.append(name)
	
		if name not in shufflescheme.keys():
	
			Dischargefuel.append(name)

	outfile = []
	matIDs = {}
	i = 0

	if version == 2:

		with open(outpath, 'r', encoding='utf-8') as results:
		
			for line in results:
		
				outfile.append(line)
				i += 1
		
				for zone in matnames:
		
					zoneid = "Material \"" + zone + "\""
		
					if zone in line:
		
						lookupid = {zone : i}
						matIDs.update(lookupid)
		
		# Collect zone atom density, mass density and mass
		ZoneMassDensity = {}
		ZoneMass        = {}
		
		for k,v in matIDs.items():
		
			mdens  = outfile[v+2][16:26]
			mdensi = {k : float(mdens)}
			ZoneMassDensity.update(mdensi)
		
			mass  = outfile[v+4][8:18]
			massi = {k : float(mass)/1e3}
			ZoneMass.update(massi)
		
		# Collect isotopic information
		IsotopicZoneAtomFraction = {}
		IsotopicZoneMassFraction = {}
		IsotopicZoneMass         = {}
		ZoneIsotopeIDs           = {}
		
		for k, v in matIDs.items():
		
			i = 0
			isotoperow = " "
			adensc = {}
			afracc = {}
			mfracc = {}
			massc  = {}
		
			IDs = []
		
			while "sum" not in isotoperow:
		
				row = v+14+i
				isotoperow = outfile[row]
		
				ID    = isotoperow[1:6]
				IDs.append(ID)
		
				afrac = float(isotoperow[43:55])
				mfrac = float(isotoperow[56:67])
		
				mass  = mfrac * ZoneMass.get(k)
		
				afracc.update({ID : afrac})
				mfracc.update({ID : mfrac})
				massc.update({ID : mass})
		
				i += 1
		
			afracx = {k : afracc}
			IsotopicZoneAtomFraction.update(afracx)
		
			massx = {k : mfracc}
			IsotopicZoneMassFraction.update(massx)
		
			masscx = {k : massc}
			IsotopicZoneMass.update(masscx)
		
			IDsx = {k : IDs}
			ZoneIsotopeIDs.update(IDsx)
		
		ActinideMassFraction = {}
		ActinideMass = {}
		
		for cell in matnames:
		
			amf = []
			aaf = []
		
			X = ZoneIsotopeIDs.get(cell)
		
			for isotope in X[0:len(X)-1]:
			
				A = float(isotope)
				
				if A >= 90000:
			
					mf = IsotopicZoneMassFraction.get(cell)
					mf2 = mf.get(isotope)
					amf.append(mf2)
	
			sumact = sum(amf)
			actiemf = {cell : sumact}
		
			ActinideMassFraction.update(actiemf)
			ActinideMassx = {cell : sumact * ZoneMass.get(cell)}
			ActinideMass.update(ActinideMassx)

	# Start-things for calc-loops
	detfile = []
	i = 0
	ic = []
	lengthvalues = 11
	
	startx  = 15 + eqcycle_busteps*(lengthvalues+1)
	stopx   = startx + lengthvalues
	
	startx1 = 7 + eqcycle_busteps*(lengthvalues+1)
	stopx1  = startx1 + lengthvalues
	
	# Get the burnup per zone
	Burnupinfo = {}
	
	with open(respath, 'r', encoding='utf-8') as results:
	
		for line in results:
	
			totbuname = "BU = [ "
		
			if totbuname in line:
		
				totalcycleburnup = float(line[startx1:stopx1])
	
			detfile.append(line)
			i += 1
	
			# Get zone-by-zone burnup
			for zone in matnames:
	
				if version == 1:
	
					detectorname = "MAT_" + zone + "_BURNUP = ["
					
					if detectorname in line:
	
						ic.append(i)
	
				else:
	
					detectorname = "MAT_" + zone + "_BURNUP = [ "
					sideoff = len(detectorname)
					start = sideoff + eqcycle_busteps*(lengthvalues+1)
					stop  = start + lengthvalues
	
					if detectorname in line:
			
						A = float(line[start:stop])
						Burnup = {zone : A}
						Burnupinfo.update(Burnup)
	
	# Collect burnupinfo for version-1 output
	if version == 1:
	
		start = 1 + eqcycle_busteps*(lengthvalues+1)
		stop  = start + lengthvalues
	
		for startpoint in ic:
		
			for cell in matnames:
	
				if cell in detfile[startpoint-1]:
	
					nowcell = cell
	
			AA = float(detfile[startpoint][start:stop])
			Burnup = {nowcell : AA}
			Burnupinfo.update(Burnup)
	
	TotalAverageDischargeBurnup1 = eqcycle_batches * totalcycleburnup
	
	# Figure out shuffling cycles
	cycles = {}
	
	for i in range(AxialZones):
	
		ColCyl = []
	
		A = Feedfuel[i]
		B = shufflescheme[A]
	
		x = 0
	
		ColCyl.append(A)
	
		while B not in Dischargefuel:
		
			A = B
			B = shufflescheme[A]
			ColCyl.append(A)
			x += 1
	
		ColCyl.append(B)
		ColCycl = {i : ColCyl}
		cycles.update(ColCycl)
	
	# Figure out cells for radial zones averaged axially
	Axiallycollected = {}
	
	for y in range(eqcycle_batches):
	
		B = []
		
		for axz in range(AxialZones):
	
			A = cycles.get(axz)
			B.append(A[y])
		
		radax = {y : B}
		Axiallycollected.update(radax)
	
	# Figure out cells for axial zones averaged radially
	Radiallycollected = {}
	
	for y in range(AxialZones):
	
		A = []
		
		for axz in range(eqcycle_batches):
	
			a = eqcycle_batches * y + axz
			A.append(matnames[a])
		
		radax = {y : A}
		Radiallycollected.update(radax)
	
	# Calculate radially averaged axial eq. cycle burnup 
	Axialpowers = {}
	
	for ax in range(AxialZones):
	
		A = Radiallycollected.get(ax)
		B = []
	
		for ra in range(eqcycle_batches):
		
			B.append(Burnupinfo.get(A[ra]))
		
		radsum = { ax : sum(B) }
		Axialpowers.update(radsum)
	
	# Calculate axially averaged radial eq. cycle burnup 
	Radialpowers = {}
	
	for radz in range(eqcycle_batches):
	
		A = Axiallycollected.get(radz)
		B = []
	
		for ax2 in range(AxialZones):
	
			B.append(Burnupinfo.get(A[ax2]))
	
		radsum = { radz : sum(B) }
		Radialpowers.update(radsum)
	
	# Calculate axial burnup peaking (est. power peaking)
	A = []
	
	for k,v in Axialpowers.items():
	
		A.append(v)
	
	B = sum(A)
	AverageAxialBU = B/AxialZones
	MaxAxialBU = max(A)
	AxialPeak = MaxAxialBU/AverageAxialBU	
	
	# Calculate radial burnup peaking (est. power peaking)
	A = []
	
	for k,v in Radialpowers.items():
	
		A.append(v)
	
	B = sum(A)
	AverageRadialBU = B/eqcycle_batches
	MaxRadialBU = max(A)
	RadialPeak = MaxRadialBU/AverageRadialBU
	
	# Get the actinide and FP atom density in each cell
	if version == 1:
	
		ActinideAdens = {}
		FPAdens       = {}
	
		i = 0
		distactinide = len(isotope_checks)-1
		distfp       = len(isotope_checks)
	
		for line in detfile:
	
			for cell in matnames:
	
				cello = "MAT_" + cell + "_ADENS = ["
	
				if cello in line:
	
					nowcell  = cell
					ACTINIDE = []
					FP       = []
	
					for s in range((eqcycle_busteps)+1):
	
						start = 1 + s*(lengthvalues+1)
						stop  = start + lengthvalues
	
						startrowact = i+distactinide+2
						startrowfp  = i+distactinide+3
	
						ACTINIDE.append(float(detfile[startrowact][start:stop]))
						FP.append(float(detfile[startrowfp][start:stop]))
	
					actc = {nowcell : ACTINIDE}
					fpc = {nowcell : FP}
	
					ActinideAdens.update()
					FPAdens.update()
	
			i += 1
	
	# Get the actinide and FP mass density in each cell
	if version == 1:
	
		ActinideMassDens  = {}
		FPMassDens        = {}
	
		i = 0
		distactinide = len(isotope_checks)-1
		distfp       = len(isotope_checks)
	
		for line in detfile:
	
			for cell in matnames:
	
				cello = "MAT_" + cell + "_MDENS = ["
	
				if cello in line:
	
					nowcell  = cell
					ACTINIDE = []
					FP       = []
	
					for s in range((eqcycle_busteps)+1):
	
						start = 1 + s*(lengthvalues+1)
						stop  = start + lengthvalues
	
						startrowact = i+distactinide+2
						startrowfp  = i+distactinide+3
	
						actmdens = float(detfile[startrowact][start:stop])
						fpmdens  = float(detfile[startrowfp][start:stop])
	
						ACTINIDE.append(actmdens)
						FP.append(fpmdens)
	
					actc = {nowcell : ACTINIDE}
					fpc = {nowcell : FP}
	
					ActinideMassDens.update(actc)
					FPMassDens.update(fpc)
	
			i += 1
	
	# Actinide and FP mass in each cell
	if version == 1:
	
		ActinideMass = {}
		FPMass       = {}
	
		for name in matnames:
	
			acmm = []
			afmm = []
	
			for bustep in range(eqcycle_busteps+1):
			
				A1  = ActinideMassDens.get(name)[bustep]
				A2  = float(VOLUMES.get(name))
				acm = A1 * A2 / 1000
				acmm.append(acm)
			
				A1  = FPMassDens.get(name)[bustep]
				A2  = float(VOLUMES.get(name))
				afm = A1 * A2 / 1000
				afmm.append(afm)
	
			ActinideMassx = {name : acmm}
			FPMassx       = {name : afmm}
	
			ActinideMass.update(ActinideMassx)
			FPMass.update(FPMassx)  
	
	# Calculate exact power-peaking from burnup
	if version == 1:
	
		Powerc = []
		Powerinfo = {}
	
		for cell in matnames:
	
			Burnup = Burnupinfo.get(cell)
			Mass   = ActinideMass.get(cell)
			Mass   = sum(Mass)/(eqcycle_busteps+1)
	
			Time   = eqcycle_days
			Power = Burnup * Mass / Time
	
			Powerc.append(Power)
			Powercc = {cell : Power}
			Powerinfo.update(Powercc)
	
		Totalpower   = sum(Powerc)
		Averagepower = Totalpower / zones
		Maxpower     = max(Powerc)
		PowerPeak    = Maxpower / Averagepower
	
		# Calculate axially averaged eq. cycle burnup 
		RadialpowersX = {}
	
		for radz in range(eqcycle_batches):
	
			A = Axiallycollected.get(radz)
			B = []
		
			for ax2 in range(AxialZones):
		
				B.append(Powerinfo.get(A[ax2]))
		
			radsum = { radz : sum(B) }
			RadialpowersX.update(radsum)
	
		# Calculate radial burnup peaking (est. power peaking)
		A = []
		
		for k,v in RadialpowersX.items():
		
			A.append(v)
		
		B = sum(A)
		AverageRadialBU = B/eqcycle_batches
		MaxRadialBU = max(A)
		RadialPeakX = MaxRadialBU/AverageRadialBU
	
	# Calculate the burnup throughout the shuffling scheme
	CycleBUs = {}
	
	for axiallevel in range(AxialZones):
	
		LevelsD = []
	
		for zone in range(eqcycle_batches):
	
			WhichOne = cycles.get(axiallevel)[zone]
			RightBU = Burnupinfo.get(WhichOne)
			LevelsD.append(RightBU)
	
		SumLevel = sum(LevelsD)
		LevelsBU = {axiallevel : SumLevel}
		CycleBUs.update(LevelsBU)
	
	# Calculates average and peak discharge burnup

	# 1. Thermal power - (given from res.m file)

	with open(dotrespath, 'r', encoding='utf-8') as results:

		searchforpower = "TOT_POWER"

		for line in results:

			if searchforpower in line:

				Power = float(line[47:58])/1e6

	# 2. Number of batches - eqcycle_batches

	# 3. HM load per fuel charge zone (given from .out file)

	MX = []

	for zone in Feedfuel:

		MX.append(ActinideMass.get(zone))

	ActinideChargeMass = sum(MX)

	# 4. MW-days - eqcycle_days * power

	MWdays = eqcycle_days * Power

	# 7. Average BU - 6 / 5

	AverageBU = MWdays / ActinideChargeMass

	# 8. Peak BU - Peaking factor from CycleBUs * Average BU

	bux = []

	#PRINT THE OUTPUT TO FINAL FILE
	if final != 1:
		Afile = resultspath + "/EDIS_" + where + "_info.txt"
	else:
		Afile = resultspath + "/EDIS_final.txt"

	serp = open(Afile, 'a', encoding='utf-8')

	sp0 = "--------------------------------------------"

	serp.write(sp0)
	serp.write("\n")

	sp0 = "-- Eq. cycle discharge burnup --------------"

	serp.write(sp0)
	serp.write("\n")

	sp0 = "--------------------------------------------"

	serp.write(sp0)
	serp.write("\n")
	serp.write("\n")

	AVEp = " - Average discharge burnup: {0:02.2f}".format(AverageBU) + " MWd/kg-actinide ({0:02.2%}".format((AverageBU/950)) + " FIMA)"

	serp.write(AVEp)

	serp.write("\n")
	serp.write("\n")

	for zone, bu in CycleBUs.items():
	
		bux.append(bu)
	
	TAB = sum(bux)/AxialZones
	
	BUU = []

	for zone in bux:

		BUU.append((zone/TAB) * AverageBU)

	for level in range(AxialZones):

		#BuF = BurnupFIMA.get(level)
		sp1 = " - Axial zone " + str(level+1) + ": {0:02.2f}".format(BUU[level]) + " MWd/kg-actinide ({0:02.2%}".format((BUU[level]/950)) + " FIMA)"
		serp.write(sp1)
		serp.write("\n")

	serp.write("\n")
	sp2 = " - Axial power peak {0:02.2f}".format(AxialPeak)

	if version == 1:
		sp3 = " - Radial power peak {0:02.2f}".format(RadialPeakX) + " (max/ave)"
	else:
		sp3 = " - Radial power peak {0:02.2f}".format(RadialPeak) + "  (max/ave)"

	serp.write(sp2)
	serp.write("\n")
	serp.write(sp3)
	serp.write("\n")
	serp.write("\n")
	
	##Check U-238 content
	#U = ["92235","92238"]
	#D3 = []
	#
	#for cell in Feedfuel:
	#
	#	D = IsotopicZoneMass.get(cell)
	#	D2 = []
	#
	#	for isotope in U:
	#
	#		D1 = D.get(isotope)
	#		D2.append(D1)
	#
	#	D3.append(sum(D2))
	#
	#FeedUmass = sum(D3)
	#D3 = []
	#
	#U = ["92232","92233","92234","92235","92236","92237","92238","92239"]
	#
	#for cell in Dischargefuel:
	#
	#	D = IsotopicZoneMass.get(cell)
	#	D2 = []
	#
	#	for isotope in U:
	#
	#		D1 = D.get(isotope)
	#		D2.append(D1)
	#
	#	D3.append(sum(D2))
	#
	#DischargeUmass = sum(D3)
	#
	#sp0 = "--------------------------------------------"
	#
	#serp.write(sp0)
	#serp.write("\n")
	#
	#sp0 = "-- Eq. cycle material evolution ------------"
	#
	#serp.write(sp0)
	#serp.write("\n")
	#sp0 = "--------------------------------------------"
	#
	#serp.write(sp0)
	#serp.write("\n")
	#serp.write("\n")
	#
	#
	#s0  = "Uranium"
	#s0x = "----------------------"
	#if FeedUmass < 1e-3:
	#	s1 = " - Feed mass: No uranium in the feed fuel"
	#else:
	#	s1 = " - Feed mass: {0:02.0f}".format(FeedUmass) + " kg"
	#s2 = " - Discharge mass: {0:02.0f}".format(DischargeUmass) + " kg"
	#
	#DiffU = FeedUmass - DischargeUmass
	#DiffPrU = DiffU/FeedUmass
	#
	#if DiffU > 0:
	#	s3 = " - Cycle change: {0:01.0f}".format(DiffU) + " kgs consumed"
	#else:
	#	s3 = " - Cycle change: {0:02.0f}".format(-DiffU) + " kgs produced"
	#
	#serp.write(s0)
	#serp.write("\n")
	#serp.write(s0x)
	#serp.write("\n")
	#serp.write(s1)
	#serp.write("\n")
	#serp.write(s2)
	#serp.write("\n")
	#serp.write(s3)
	#serp.write("\n")
	#
	#s1 = " - Discharge isotope-vector (ax. ave, mass fraction):"
	#
	#serp.write(s1)
	#serp.write("\n")
	#
	#for isotope in U:
	#
	#	D1 = []
	#
	#	for cell in Dischargefuel:
	#
	#		D = IsotopicZoneMass.get(cell)
	#		D1.append(D.get(isotope))
	#
	#	D2 = sum(D1)
	#	MassFrac = D2/DischargeUmass
	#
	#	sp = "  - " + isotope + ": {0:02.2%}".format(MassFrac)
	#
	#	if MassFrac >= 1e-4:
	#		serp.write(sp)
	#		serp.write("\n")
	#
	#serp.write("\n")
	#
	## Check Pu-content
	#Pu = ["94238","94239","94240","94241","94242"]
	#D3 = []
	#
	#for cell in Feedfuel:
	#
	#	D = IsotopicZoneMass.get(cell)
	#	D2 = []
	#
	#	for isotope in Pu:
	#
	#		D1 = D.get(isotope)
	#		D2.append(D1)
	#
	#	D3.append(sum(D2))
	#
	#FeedPumass = sum(D3)
	#D3 = []
	#
	#Pu = ["94236","94237","94238","94239","94240","94241","94242","94243","94244","94246"]
	#
	#for cell in Dischargefuel:
	#
	#	D = IsotopicZoneMass.get(cell)
	#	D2 = []
	#
	#	for isotope in Pu:
	#
	#		D1 = D.get(isotope)
	#		D2.append(D1)
	#
	#	D3.append(sum(D2))
	#
	#DischargePumass = sum(D3)
	#
	#s0 = "Plutonium"
	#s0x = "----------------------"
	#if FeedPumass < 1e-3:
	#	s1 = " - Feed mass: No Pu in the feed fuel"
	#else:
	#	s1 = " - Feed mass: {0:02.0f}".format(FeedPumass) + " kg"
	#s2 = " - Discharge mass: {0:02.0f}".format(DischargePumass) + " kg"
	#
	#DiffPu = FeedPumass - DischargePumass
	#
	#if DiffPu > 0:
	#	s3 = " - Cycle change: {0:01.0f}".format(DiffPu) + " kgs consumed"
	#else:
	#	s3 = " - Cycle change: {0:02.0f}".format(-DiffPu) + " kgs produced"
	#
	#serp.write(s0)
	#serp.write("\n")
	#serp.write(s0x)
	#serp.write("\n")
	#serp.write(s1)
	#serp.write("\n")
	#serp.write(s2)
	#serp.write("\n")
	#serp.write(s3)
	#serp.write("\n")
	#
	#s1 = " - Discharge isotope-vector (ax. ave, mass fraction):"
#
	#serp.write(s1)
	#serp.write("\n")
	#
	#for isotope in Pu:
	#
	#	D1 = []
	#
	#	for cell in Dischargefuel:
	#
	#		D = IsotopicZoneMass.get(cell)
	#		D1.append(D.get(isotope))
	#
	#	D2 = sum(D1)
	#	MassFrac = D2/DischargePumass
	#
	#	sp = "  - " + isotope + ": {0:02.2%}".format(MassFrac)
	#
	#	if MassFrac >= 1e-4:
	#		serp.write(sp)
	#		serp.write("\n")
#
	#serp.close()

##################################################################################
####                                                                          ####
#### Function: bustuff1                                                       ####
#### Description: Does burnup stuff in Serpent 1                              ####
####                                                                          ####
#### Last updated: 2013-07-24, 7.28 PM                                        ####
####                                                                          ####
##################################################################################

def bustuff1(orgfilename, AxialZones, eqcycle_batches, where, shufflescheme, VOLUMES, matnames, eqcycle_days, eqcycle_busteps,resultspath):

	Avogadro = 6.022*1e23
	lengthvalues = 11
	
	# ATOM INFO
	Atominfo = {
	"90227" : 227.02770,
        "90228" : 228.02874,
        "90229" : 229.03176,
        "90230" : 230.03313,
	"90232" : 232.03833,
	"90233" : 233.04195,
	"90234" : 234.04356,
	"91231" : 231.03571,
	"91232" : 232.03833,
	"91233" : 233.03993,
	"92232" : 232.03712,
	"92233" : 233.03964,
	"92234" : 234.04093,
	"92235" : 235.04395,
	"92236" : 236.04556,
	"92237" : 237.04878,
	"92238" : 238.05078,
	"92239" : 239.05430,
	"92240" : 240.05661,
	"92241" : 241.06034,
	"93235" : 235.04415,
	"93236" : 236.04676,
	"93237" : 237.04816,
	"93238" : 238.05098,
	"93239" : 239.05258,
	"94236" : 236.04576,
	"94237" : 237.04836,
	"94238" : 238.04947,
	"94239" : 239.05218,
	"94240" : 240.05420,
	"94241" : 241.04873,
	"94242" : 242.05841,
	"94243" : 243.06203,
	"94244" : 244.06465,
	"94246" : 246.06986,
	"95241" : 241.05680,
	"95242" : 242.05952,
	"95342" : 242.05952,
	"95243" : 243.06143,
	"95244" : 244.06465,
	"95344" : 244.06465,
	"96240" : 240.0555190,
	"96241" : 241.0576467,
	"96242" : 242.05841,
	"96243" : 243.06103,
	"96244" : 244.06263,
	"96245" : 245.06525,
	"96246" : 246.06685,
	"96247" : 247.07046,
	"96248" : 248.07207,
	"96249" : 249.07570,
	"96250" : 250.07830,
	"97249" : 249.07973,
	"97250" : 250.07830,
	"98249" : 249.07973,
	"98250" : 250.07628,
	"98251" : 251.07991,
	"98252" : 252.08151,
	"98253" : 253.08413,
	"98254" : 254.08775,
	"99253" : 253.08413,
	"99254" : 254.08775,
	"99255" : 255.09036}
	# END ATOM INFO
	
	zones = AxialZones * eqcycle_batches
	final = 0
	matfile = orgfilename + "_" + where + "_mburn"
	dotrespath = orgfilename + "_" + where + "_res.m"
	dotdep = orgfilename + "_" + where + "_dep.m"
	
	# Define the shuffling scheme
	Feedfuel = []
	Dischargefuel = []
	
	for name in matnames:
	
		if name not in shufflescheme.values():
	
			Feedfuel.append(name)
	
		if name not in shufflescheme.keys():
	
			Dischargefuel.append(name)
	
	outfile = []
	matIDs = {}
	CellMassDensity = {}
	i = 0
	
	with open(matfile, 'r', encoding='utf-8') as results:
			
		for line in results:
		
			outfile.append(line)
			i += 1
		
			for zone in matnames:
		
				zoneid = " " + zone + " "
		
				if zoneid in line:
	
					# Define what line in the file we find the information on this zone
					lookupid = {zone : i}
					matIDs.update(lookupid)
	
					# Where to look for mass density
					Ax = 5
					Ax2 = Ax  + len(zone)
					Ax3 = Ax2 + 3
					Ax4 = Ax3 + 11
	
					# Define the cell-averaged material mass density (g/cc)
					mdens = float(line[Ax3:Ax4])
					
					mdensID = {zone : mdens}
					CellMassDensity.update(mdensID)
	
	AllMassDensity = {}
	X = []
	
	for k,v in matIDs.items():
	
		X.append(v)
	
	X.append(len(outfile)-1)
	
	# Collect the mass density of each isotope in each cell
	Check1 = "-"
	for k,v in matIDs.items():
	
		i = 1
		forbidden  = "mat"
		linenumber = v+i
		lineinfo   = outfile[linenumber]
		MDCC = {}
	
		while linenumber not in X:
		
			linenumber = v+i
			Isotope     = outfile[linenumber][11:16]
			MassDensity = outfile[linenumber][23:34]
	
			if Check1 in MassDensity:
	
				AMf = float(MassDensity)
				MDC = {Isotope : AMf}
				MDCC.update(MDC)
	
			i += 1
	
		AMD = {k : MDCC}
		AllMassDensity.update(AMD)
	
	# Collect the mass of each isotope in each cell
	AllMasses = {}
	for cells in matnames:
	
		Q = AllMassDensity.get(cells)
		CellDensity = CellMassDensity.get(cells)
		IMCC = {}
	
		for k,v in Q.items():
	
			IsotopeMass = v * CellDensity * float(VOLUMES[cells])
			IMC = {k : IsotopeMass}
			IMCC.update(IMC)
	
		IMC1C = {cells : IMCC}
		AllMasses.update(IMC1C)
	
	# Collect the actinide mass in each cell
	CellActinideMasses = {}
	CellActinideAtoms = {}
	AllIsotopeAtoms = {}
	ActinideAtoms = {}
	
	for cells in matnames:
	
		X = AllMasses.get(cells)
		AM = 0
		AA = 0
	
		AtomsCC = {}
	
		for k,v in X.items():
		
			if int(k) > 90000:
	
				Atoms = v * Avogadro / Atominfo.get(k)
				AtomsC = {k : Atoms}
				AtomsCC.update(AtomsC)
	
				AM += v
				AA += Atoms
	
			AllIsotopeAtom = {cells : AtomsCC}
			AllIsotopeAtoms.update(AllIsotopeAtom)
	
		ActinideMass  = {cells : AM/1000}
		ActinideAtoms = {cells : AA}
		CellActinideMasses.update(ActinideMass)
		CellActinideAtoms.update(ActinideAtoms)
	
	# 1. Thermal power - (given from res.m file)
	
	with open(dotrespath, 'r', encoding='utf-8') as results:
	
		searchforpower = "TOT_POWER"
	
		for line in results:
	
			if searchforpower in line:
	
				Power = float(line[47:58])/1e6
	
	# 2. Number of batches - eqcycle_batches
	
	# 3. HM load per fuel charge zone (given from .out file)
	
	MX = []
	
	for zone in Feedfuel:
	
		AA = CellActinideMasses.get(zone)
		BB = CellMassDensity.get(zone) * float(VOLUMES[cells]) / 1000
		MX.append(AA)
	
	ActinideChargeMass = sum(MX)
	
	# 4. MW-days - eqcycle_days * power
	
	MWdays = eqcycle_days * Power
	
	# 7. Average BU - 6 / 5
	
	AverageBU = MWdays / ActinideChargeMass
	
	# 8. Peak BU - Peaking factor from CycleBUs * Average BU
	
	# Check FIMA by mass
	FIMAburnup = {}
	AVEB1 = 0
	
	cycles = {}
	
	for i in range(AxialZones):
	
		ColCyl = []
	
		A = Feedfuel[i]
		B = shufflescheme[A]
		x = 0
	
		ColCyl.append(A)
	
		while B not in Dischargefuel:
		
			A = B
			B = shufflescheme[A]
			ColCyl.append(A)
	
			x += 1
	
		A = Dischargefuel[i]
		ColCyl.append(B)
		ColCycl = {i : ColCyl}
		cycles.update(ColCycl)
	
	for level in range(AxialZones):
	
		BUL = []
		F = Feedfuel[level]
		FAM = CellActinideMasses.get(F)
	
		FAA = CellActinideAtoms.get(F)
	
	
		for cell in cycles.get(level):
	
			DAM = CellActinideMasses.get(cell)
			DAA = CellActinideAtoms.get(cell)
	
			BUX = (FAM-DAM)/FAM
			BUA = ((FAA-DAA)/FAA)
	
			if BUX < 0:
				BUX = 0
			if BUA < 0:
				BUA = 0
	
			BUL.append(BUA)
		
			X = {cell : BUA}
			FIMAburnup.update(X)
	
	XXX = []
	
	for level in range(AxialZones):
	
		XX = Dischargefuel[level]
		X  = FIMAburnup.get(XX)
		XXX.append(X)
	
	AverageFIMAburnup = sum(XXX)/AxialZones
	AxialPeak         = max(XXX)/AverageFIMAburnup
	
	MWDsCollect = {}
	DischargeFIMA = {}
	
	for level in range(AxialZones):
	
		XX = Dischargefuel[level]
	
		Dischargeb = {level : FIMAburnup.get(XX)}
		DischargeFIMA.update(Dischargeb)
	
		PY = FIMAburnup.get(XX)/AverageFIMAburnup
	
		MWDP = PY * AverageBU
		X = {level : MWDP}
		MWDsCollect.update(X)
	
	# Figure out cells for radial zones averaged axially
	Axiallycollected = {}
	
	for y in range(eqcycle_batches):
	
		B = []
		
		for axz in range(AxialZones):
	
			A = cycles.get(axz)
			B.append(A[y])
		
		radax = {y : B}
		Axiallycollected.update(radax)
	
	# Calculate axially averaged radial burnup 
	RadialBU = {}
	ALLC = 0
	
	for radialzone in range(eqcycle_batches):
	
		A = Axiallycollected.get(radialzone)
		B = 0
	
		#print("Radial: " + str(radialzone))
	
		for ax2 in range(AxialZones):
	
			#print("Axial: " + str(ax2))
			B += FIMAburnup.get(A[ax2])
			#print("Cell: " + A[ax2])
			#print("BU: " + str(FIMAburnup.get(A[ax2])*100))
			
		#print("-------------")	
		ALLC += B/AxialZones
		radsum = { radialzone : B/AxialZones}
		RadialBU.update(radsum)
	
	FullCoreAverageBU = ALLC/eqcycle_batches
	
	#print(RadialBU)
	#print(FullCoreAverageBU)
	
	# Get the burnup per zone
	Burnupinfo = {}
	detfile = []
	i = 0
	ic = []
	
	startx1 = 7 + eqcycle_busteps*(lengthvalues+1)
	stopx1  = startx1 + lengthvalues
	
	with open(dotdep, 'r', encoding='utf-8') as results:
	
		for line in results:
	
			totbuname = "BU = [ "
		
			if totbuname in line:
		
				totalcycleburnup = float(line[startx1:stopx1])
	
			detfile.append(line)
			i += 1
	
			# Get zone-by-zone burnup
			for zone in matnames:
	
				detectorname = "MAT_" + zone + "_BURNUP = ["
				
				if detectorname in line:
	
					ic.append(i)
	
	# Collect burnupinfo for version-1 output
	start = 1 + eqcycle_busteps*(lengthvalues+1)
	stop  = start + lengthvalues
	
	for startpoint in ic:
	
		for cell in matnames:
	
			if cell in detfile[startpoint-1]:
	
				nowcell = cell
	
		AA = float(detfile[startpoint][start:stop])
		Burnup = {nowcell : AA}
		Burnupinfo.update(Burnup)
	
	# Calculate axially averaged radial eq. cycle burnup 
	Radialpowers = {}
	
	for radz in range(eqcycle_batches):
	
		A = Axiallycollected.get(radz)
		B = []
	
		for ax2 in range(AxialZones):
	
			B.append(Burnupinfo.get(A[ax2]))
	
		radsum = { radz : sum(B) }
		Radialpowers.update(radsum)
	
	# Calculate radial burnup peaking (est. power peaking)
	A = []
	
	for k,v in Radialpowers.items():
	
		A.append(v)
	
	B = sum(A)
	AverageRadialBU = B/eqcycle_batches
	MaxRadialBU = max(A)
	RadialPeak = MaxRadialBU/AverageRadialBU
	
	#PRINT THE OUTPUT TO FINAL FILE
	if final != 1:
		Afile = resultspath + "/EDIS_" + where + "_info.txt"
	else:
		Afile = resultspath + "/EDIS_final.txt"
	
	serp = open(Afile, 'a', encoding='utf-8')
	
	sp0 = "--------------------------------------------"
	
	serp.write(sp0)
	serp.write("\n")
	
	sp0 = "-- Eq. cycle discharge burnup --------------"
	
	serp.write(sp0)
	serp.write("\n")
	
	sp0 = "--------------------------------------------"
	
	serp.write(sp0)
	serp.write("\n")
	serp.write("\n")
	
	AVEp = "  Average discharge burnup: {0:02.2f}".format(AverageBU) + " MWd/kg-actinide ({0:02.2%}".format((AverageFIMAburnup)) + " FIMA)"
	
	serp.write(AVEp)
	
	serp.write("\n")
	sp2 = "  Axial power peak: {0:02.2f}".format(AxialPeak) + " (max/ave)"
	serp.write(sp2)
	serp.write("\n")
	sp2 = "  Radial power peak: {0:02.2f}".format(RadialPeak) + " (max/ave)"
	serp.write(sp2)
	serp.write("\n")
	serp.write("\n")
	
	for level in range(AxialZones):
	
		sp1 = " - Axial zone " + str(level+1) + ": {0:02.2f}".format(MWDsCollect.get(level)) + " MWd/kg-actinide ({0:02.2%}".format((DischargeFIMA.get(level))) + " FIMA)"
		serp.write(sp1)
		serp.write("\n")

##################################################################################
####                                                                          ####
#### Function: cleanupfiles                                                   ####
#### Description: Cleans the serpent input/output files                       ####
####                                                                          ####
#### Last updated: 2013-07-24, 7.28 PM                                        ####
####                                                                          ####
##################################################################################

def cleanupfiles(orgfilename, eqcycle_busteps, orgfilespath, medfilespath, finalfilespath, resultspath):

	import shutil

	# Copy the final files ----------------------------------------------------------------------------

	finalgeomfile_source = orgfilename + "_eq2"
	finalgeomfile_target = finalfilespath + "/" + orgfilename + "_eq2"

	if os.path.exists(finalgeomfile_source) != True:
		finalgeomfile_source = orgfilename + "_eq1"
		finalgeomfile_target = finalfilespath + "/" + orgfilename + "_eq1"

	if os.path.exists(finalgeomfile_source) == True:
		shutil.copy2(finalgeomfile_source, finalgeomfile_target)
		os.remove(finalgeomfile_source)

	finalmatfile_source = orgfilename + "_eq2_mburn"
	finalmatfile_target = finalfilespath + "/" + orgfilename + "_eq2_mburn"

	if os.path.exists(finalmatfile_source) != True:
		finalmatfile_source = orgfilename + "_eq1_mburn"
		finalmatfile_target = finalfilespath + "/" + orgfilename + "_eq1_mburn"

	if os.path.exists(finalmatfile_source) == True:
		shutil.copy2(finalmatfile_source, finalmatfile_target)
		os.remove(finalmatfile_source)

	finalresfile_source = orgfilename + "_eq2_res.m"
	finalresfile_target = finalfilespath + "/" + orgfilename + "_eq2_res.m"

	if os.path.exists(finalresfile_source) != True:
		finalresfile_source = orgfilename + "_eq1_res.m"
		finalresfile_target = finalfilespath + "/" + orgfilename + "_eq1_res.m"

	if os.path.exists(finalresfile_source) == True:
		shutil.copy2(finalresfile_source, finalresfile_target)
		os.remove(finalresfile_source)

	finaldepfile_source = orgfilename + "_eq2_dep.m"
	finaldepfile_target = finalfilespath + "/" + orgfilename + "_eq2_dep.m"

	if os.path.exists(finaldepfile_source) != True:
		finaldepfile_source = orgfilename + "_eq1_dep.m"
		finaldepfile_target = finalfilespath + "/" + orgfilename + "_eq1_dep.m"

	if os.path.exists(finaldepfile_source) == True:
		shutil.copy2(finaldepfile_source, finaldepfile_target)
		os.remove(finaldepfile_source)

	finaloutfile_source = orgfilename + "_eq2.out"
	finaloutfile_target = finalfilespath + "/" + orgfilename + "_eq2.out"

	if os.path.exists(finaloutfile_source) != True:
		finaloutfile_source = orgfilename + "_eq1.out"
		finaloutfile_target = finalfilespath + "/" + orgfilename + "_eq1.out"

	if os.path.exists(finaloutfile_source) == True:
		shutil.copy2(finaloutfile_source, finaloutfile_target)
		os.remove(finaloutfile_source)

	for a in range(eqcycle_busteps+1):

		A = finalgeomfile_source + ".bumat" + str(a)
		B = finalfilespath + "/" + A

		if os.path.exists(A) == True:
			shutil.copy2(A, B)
			os.remove(A)

	# END Copy the final files ------------------------------------------------------------------------

	### FIRST EQ. STEP --------------------------------------------------------------------------------

	finalgeomfile_source = orgfilename + "_eq1"
	finalgeomfile_target = medfilespath + "/" + orgfilename + "_eq1"

	if os.path.exists(finalgeomfile_source) == True:
		shutil.copy2(finalgeomfile_source, finalgeomfile_target)
		os.remove(finalgeomfile_source)

	finalmatfile_source = orgfilename + "_eq1_mburn"
	finalmatfile_target = medfilespath + "/" + orgfilename + "_eq1_mburn"

	if os.path.exists(finalmatfile_source) == True:
		shutil.copy2(finalmatfile_source, finalmatfile_target)
		os.remove(finalmatfile_source)

	finalresfile_source = orgfilename + "_eq1_res.m"
	finalresfile_target = medfilespath + "/" + orgfilename + "_eq1_res.m"

	if os.path.exists(finalresfile_source) == True:
		shutil.copy2(finalresfile_source, finalresfile_target)
		os.remove(finalresfile_source)

	finaldepfile_source = orgfilename + "_eq1_dep.m"
	finaldepfile_target = medfilespath + "/" + orgfilename + "_eq1_dep.m"

	if os.path.exists(finaldepfile_source) == True:
		shutil.copy2(finaldepfile_source, finaldepfile_target)
		os.remove(finaldepfile_source)

	finaloutfile_source = orgfilename + "_eq1.out"
	finaloutfile_target = medfilespath + "/" + orgfilename + "_eq1.out"

	if os.path.exists(finaloutfile_source) == True:
		shutil.copy2(finaloutfile_source, finaloutfile_target)
		os.remove(finaloutfile_source)

	for a in range(eqcycle_busteps+1):

		A = finalgeomfile_source + ".bumat" + str(a)
		B = medfilespath + "/" + A

		if os.path.exists(A) == True:
			shutil.copy2(A, B)
			os.remove(A)

	### END FIRST EQ. STEP ----------------------------------------------------------------------------

	### Second lin file -------------------------------------------------------------------------------

	finalgeomfile_source = orgfilename + "_lin2"
	finalgeomfile_target = medfilespath + "/" + orgfilename + "_lin2"

	if os.path.exists(finalgeomfile_source) == True:
		shutil.copy2(finalgeomfile_source, finalgeomfile_target)
		os.remove(finalgeomfile_source)

	finalmatfile_source = orgfilename + "_lin2_mburn"
	finalmatfile_target = medfilespath + "/" + orgfilename + "_lin2_mburn"

	if os.path.exists(finalmatfile_source) == True:
		shutil.copy2(finalmatfile_source, finalmatfile_target)
		os.remove(finalmatfile_source)

	finalresfile_source = orgfilename + "_lin2_res.m"
	finalresfile_target = medfilespath + "/" + orgfilename + "_lin2_res.m"

	if os.path.exists(finalresfile_source) == True:
		shutil.copy2(finalresfile_source, finalresfile_target)
		os.remove(finalresfile_source)

	finaldepfile_source = orgfilename + "_lin2_dep.m"
	finaldepfile_target = medfilespath + "/" + orgfilename + "_lin2_dep.m"

	if os.path.exists(finaldepfile_source) == True:
		shutil.copy2(finaldepfile_source, finaldepfile_target)
		os.remove(finaldepfile_source)

	finaloutfile_source = orgfilename + "_lin2.out"
	finaloutfile_target = medfilespath + "/" + orgfilename + "_lin2.out"

	if os.path.exists(finaloutfile_source) == True:
		shutil.copy2(finaloutfile_source, finaloutfile_target)
		os.remove(finaloutfile_source)

	for a in range(eqcycle_busteps+1):

		A = finalgeomfile_source + ".bumat" + str(a)
		B = medfilespath + "/" + A

		if os.path.exists(A) == True:
			shutil.copy2(A, B)
			os.remove(A)

	### END Second lin file ---------------------------------------------------------------------------

	### First lin file --------------------------------------------------------------------------------

	finalgeomfile_source = orgfilename + "_lin1"
	finalgeomfile_target = medfilespath + "/" + orgfilename + "_lin1"

	if os.path.exists(finalgeomfile_source) == True:
		shutil.copy2(finalgeomfile_source, finalgeomfile_target)
		os.remove(finalgeomfile_source)

	finalmatfile_source = orgfilename + "_lin1_mburn"
	finalmatfile_target = medfilespath + "/" + orgfilename + "_lin1_mburn"

	if os.path.exists(finalmatfile_source) == True:
		shutil.copy2(finalmatfile_source, finalmatfile_target)
		os.remove(finalmatfile_source)

	finalresfile_source = orgfilename + "_lin1_res.m"
	finalresfile_target = medfilespath + "/" + orgfilename + "_lin1_res.m"

	if os.path.exists(finalresfile_source) == True:
		shutil.copy2(finalresfile_source, finalresfile_target)
		os.remove(finalresfile_source)

	finaldepfile_source = orgfilename + "_lin1_dep.m"
	finaldepfile_target = medfilespath + "/" + orgfilename + "_lin1_dep.m"

	if os.path.exists(finaldepfile_source) == True:
		shutil.copy2(finaldepfile_source, finaldepfile_target)
		os.remove(finaldepfile_source)

	finaloutfile_source = orgfilename + "_lin1.out"
	finaloutfile_target = medfilespath + "/" + orgfilename + "_lin1.out"

	if os.path.exists(finaloutfile_source) == True:
		shutil.copy2(finaloutfile_source, finaloutfile_target)
		os.remove(finaloutfile_source)

	for a in range(eqcycle_busteps+1):

		A = finalgeomfile_source + ".bumat" + str(a)
		B = medfilespath + "/" + A

		if os.path.exists(A) == True:
			shutil.copy2(A, B)
			os.remove(A)

	### END First lin file ----------------------------------------------------------------------------

	### STAGE-2 file ----------------------------------------------------------------------------------

	finalgeomfile_source = orgfilename + "_stage2"
	finalgeomfile_target = medfilespath + "/" + orgfilename + "_stage2"

	if os.path.exists(finalgeomfile_source) == True:
		shutil.copy2(finalgeomfile_source, finalgeomfile_target)
		os.remove(finalgeomfile_source)

	finalmatfile_source = orgfilename + "_stage2_mburn"
	finalmatfile_target = medfilespath + "/" + orgfilename + "_stage2_mburn"

	if os.path.exists(finalmatfile_source) == True:
		shutil.copy2(finalmatfile_source, finalmatfile_target)
		os.remove(finalmatfile_source)

	finalresfile_source = orgfilename + "_stage2_res.m"
	finalresfile_target = medfilespath + "/" + orgfilename + "_stage2_res.m"

	if os.path.exists(finalresfile_source) == True:
		shutil.copy2(finalresfile_source, finalresfile_target)
		os.remove(finalresfile_source)

	finaldepfile_source = orgfilename + "_stage2_dep.m"
	finaldepfile_target = medfilespath + "/" + orgfilename + "_stage2_dep.m"

	if os.path.exists(finaldepfile_source) == True:
		shutil.copy2(finaldepfile_source, finaldepfile_target)
		os.remove(finaldepfile_source)

	finaloutfile_source = orgfilename + "_stage2.out"
	finaloutfile_target = medfilespath + "/" + orgfilename + "_stage2.out"

	if os.path.exists(finaloutfile_source) == True:
		shutil.copy2(finaloutfile_source, finaloutfile_target)
		os.remove(finaloutfile_source)

	for a in range(eqcycle_busteps+1):

		A = finalgeomfile_source + ".bumat" + str(a)
		B = medfilespath + "/" + A

		if os.path.exists(A) == True:
			shutil.copy2(A, B)
			os.remove(A)

	### END STAGE-2 file ------------------------------------------------------------------------------

	### STAGE-1 file ----------------------------------------------------------------------------------

	finalgeomfile_source = orgfilename + "_stage1"
	finalgeomfile_target = medfilespath + "/" + orgfilename + "_stage1"

	if os.path.exists(finalgeomfile_source) == True:
		shutil.copy2(finalgeomfile_source, finalgeomfile_target)
		os.remove(finalgeomfile_source)

	finalmatfile_source = orgfilename + "_stage1_mburn"
	finalmatfile_target = medfilespath + "/" + orgfilename + "_stage1_mburn"

	if os.path.exists(finalmatfile_source) == True:
		shutil.copy2(finalmatfile_source, finalmatfile_target)
		os.remove(finalmatfile_source)

	finalresfile_source = orgfilename + "_stage1_res.m"
	finalresfile_target = medfilespath + "/" + orgfilename + "_stage1_res.m"

	if os.path.exists(finalresfile_source) == True:
		shutil.copy2(finalresfile_source, finalresfile_target)
		os.remove(finalresfile_source)

	finaldepfile_source = orgfilename + "_stage1_dep.m"
	finaldepfile_target = medfilespath + "/" + orgfilename + "_stage1_dep.m"

	if os.path.exists(finaldepfile_source) == True:
		shutil.copy2(finaldepfile_source, finaldepfile_target)
		os.remove(finaldepfile_source)

	finaloutfile_source = orgfilename + "_stage1.out"
	finaloutfile_target = medfilespath + "/" + orgfilename + "_stage1.out"

	if os.path.exists(finaloutfile_source) == True:
		shutil.copy2(finaloutfile_source, finaloutfile_target)
		os.remove(finaloutfile_source)

	for a in range(eqcycle_busteps+1):

		A = finalgeomfile_source + ".bumat" + str(a)
		B = medfilespath + "/" + A

		if os.path.exists(A) == True:
			shutil.copy2(A, B)
			os.remove(A)

	### END STAGE-1 file ------------------------------------------------------------------------------

	finalseed = orgfilename + "_eq2.seed"

	if os.path.exists(finalseed) == True:	
		os.remove(finalseed)

	finalddep = orgfilename + "_eq2.dep"

	if os.path.exists(finalddep) == True:	
		os.remove(finalddep)

	eq1seed = orgfilename + "_eq1.seed"

	if os.path.exists(eq1seed) == True:	
		os.remove(eq1seed)

	eq1ddep = orgfilename + "_eq1.dep"

	if os.path.exists(eq1ddep) == True:	
		os.remove(eq1ddep)

	lin2seed = orgfilename + "_lin2.seed"

	if os.path.exists(lin2seed) == True:	
		os.remove(lin2seed)

	lin2ddep = orgfilename + "_lin2.dep"

	if os.path.exists(lin2ddep) == True:	
		os.remove(lin2ddep)

	lin1seed = orgfilename + "_lin1.seed"

	if os.path.exists(lin1seed) == True:	
		os.remove(lin1seed)

	lin1ddep = orgfilename + "_lin1.dep"

	if os.path.exists(lin1ddep) == True:	
		os.remove(lin1ddep)

	stage2seed = orgfilename + "_stage2.seed"

	if os.path.exists(stage2seed) == True:	
		os.remove(stage2seed)

	stage2ddep = orgfilename + "_stage2.dep"

	if os.path.exists(stage2ddep) == True:	
		os.remove(stage2ddep)

	stage1seed = orgfilename + "_stage1.seed"

	if os.path.exists(stage1seed) == True:	
		os.remove(stage1seed)

	stage1ddep = orgfilename + "_stage1.dep"

	if os.path.exists(stage1ddep) == True:	
		os.remove(stage1ddep)

	# Original files copy

	# EDIS-files

	es_old  = "edis_settings.py"
	es_new  = orgfilespath + "/" + es_old

	ef_old  = "edis_func.py"
	ef_new  = orgfilespath + "/" + ef_old

	efd_old = "edis_dpa_func.py"
	efd_new = orgfilespath + "/" + efd_old

	e_old   = "edis.py"
	e_new   = orgfilespath + "/" + e_old

	if os.path.exists(es_old) == True:
		shutil.copy2(es_old, es_new)
		os.remove(es_old)

	if os.path.exists(ef_old) == True:
		shutil.copy2(ef_old, ef_new)
		os.remove(ef_old)

	if os.path.exists(efd_old) == True:
		shutil.copy2(efd_old, efd_new)
		os.remove(efd_old)

	if os.path.exists(e_old) == True:
		shutil.copy2(e_old, e_new)
		os.remove(e_old)

	# Start serpent files

	i1 = orgfilename
	i2 = orgfilespath + "/" + i1

	m1 = orgfilename + "_mburn"
	m2 = orgfilespath + "/" + m1

	if os.path.exists(i1) == True:
		shutil.copy2(i1, i2)
		os.remove(i1)

	if os.path.exists(m1) == True:
		shutil.copy2(m1, m2)
		os.remove(m1)
	
