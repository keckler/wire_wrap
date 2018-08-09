import os

def fixdepfuel(MOCBUmatFile, EOCBUmatFile, Name, SerpentPerturbedAxialFuelDensity, SerpentAxialFuelDensity, FuelAverageDensity):

	filename = MOCBUmatFile

	FILELIST = [""]
	smrdep = open(Name + "_material_MOC_fuel", 'w', encoding='utf-8')

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				if "mat" in line:

					lengthofline = len(line)

					x = 0

					LineR = ""

					while x < lengthofline:

						if line[x] == "p":

							y = x

							while line[y] != " ":

								y = y + 1

							x = y 

						else:

							LineR = LineR + line[x]

						x += 1

					FILELIST.append(LineR)

				else:

					FILELIST.append(line) # Add the lines to a new list

	for x in FILELIST:

		smrdep.write(x)

	smrdep.close()


	axz = len(SerpentPerturbedAxialFuelDensity)

	FILELIST = [""]
	smrdep = open(Name + "_material_MOC_fuel_perturbed", 'w', encoding='utf-8')

	filename = MOCBUmatFile

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			i = 0
	
			for line in results: # Iterate over all lines in the results file
	
				if "mat" in line:

					FILELIST.append(line[0:23])

					for q in range(len(line)):

						if line[q] == "-":

							startdens = q+1

					for i in range(axz):

						if "ax" + str(i) in line:

							ii = i

					nowdens = float((line[startdens:len(line)]))	
					NEW_REF_DENSITY = SerpentPerturbedAxialFuelDensity[ii]
					OLD_REF_DENSITY = FuelAverageDensity#SerpentAxialFuelDensity[ii]	
					RelativeDensityReduction = NEW_REF_DENSITY / OLD_REF_DENSITY
					NewActualDensity = RelativeDensityReduction * nowdens
					NEW_DENSITY = " -{0:02.5f}".format(NewActualDensity)
 	
					FILELIST.append(NEW_DENSITY)
					FILELIST.append("\n")
	
				else:
	
					FILELIST.append(line) # Add the lines to a new list

	for x in FILELIST:

		smrdep.write(x)

	smrdep.close()

	FILELIST = [""]
	smrdep = open(Name + "_material_MOC_fuel_doppler", 'w', encoding='utf-8')

	filename = MOCBUmatFile

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				if "mat" in line:

					lengthofline = len(line)

					x = 0

					LineR = ""

					while x < lengthofline:

						if line[x] == "p":

							y = x

							while line[y] != " ":

								y = y + 1

							x = y 

						else:

							LineR = LineR + line[x]

						x += 1

					FILELIST.append(LineR)

				else:

					lengthofline = len(line)
					x = 0
					LineR = ""
					newtemp =""
					L=""

					while x < lengthofline:

						if line[x] == "c":

							currenttemp = line[x-2:x]

							if currenttemp == "03":

								newtemp == "12c"

							elif currenttemp == "06":

								newtemp = "15c"

							elif currenttemp == "09":

								newtemp = "18c"

							LineR = line[0:x-2]

							L = LineR + newtemp + line[x+1:lengthofline]

						x += 1

					FILELIST.append(L) # Add the lines to a new list

	for x in FILELIST:

		smrdep.write(x)

	smrdep.close()


	filename = EOCBUmatFile

	#print(filename)

	FILELIST = [""]
	smrdep = open(Name + "_material_EOC_fuel", 'w', encoding='utf-8')

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				if "mat" in line:

					lengthofline = len(line)

					x = 0

					LineR = ""

					while x < lengthofline:

						if line[x] == "p":

							y = x

							while line[y] != " ":

								y = y + 1

							x = y 

						else:

							LineR = LineR + line[x]

						x += 1

					FILELIST.append(LineR)

				else:

					FILELIST.append(line) # Add the lines to a new list

	for x in FILELIST:

		smrdep.write(x)

	smrdep.close()	

	filename = EOCBUmatFile

	FILELIST = [""]
	smrdep = open(Name + "_material_EOC_fuel_perturbed", 'w', encoding='utf-8')

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			i = 0
	
			for line in results: # Iterate over all lines in the results file
	
				if "mat" in line:

					FILELIST.append(line[0:23])

					for q in range(len(line)):

						if line[q] == "-":

							startdens = q+1

					for i in range(axz):

						if "ax" + str(i) in line:

							ii = i

					nowdens = float((line[startdens:len(line)]))	
					NEW_REF_DENSITY = SerpentPerturbedAxialFuelDensity[ii]
					OLD_REF_DENSITY = FuelAverageDensity #SerpentAxialFuelDensity[ii]	
					RelativeDensityReduction = NEW_REF_DENSITY / OLD_REF_DENSITY
					NewActualDensity = RelativeDensityReduction * nowdens
					NEW_DENSITY = " -{0:02.5f}".format(NewActualDensity)
 	
					FILELIST.append(NEW_DENSITY)
					FILELIST.append("\n")
	
				else:
	
					FILELIST.append(line) # Add the lines to a new list

	for x in FILELIST:

		smrdep.write(x)

	smrdep.close()	

	filename = EOCBUmatFile

	FILELIST = [""]
	smrdep = open(Name + "_material_EOC_fuel_doppler", 'w', encoding='utf-8')

	# Check if the input file (still) exists
	if os.path.exists(filename) == True and os.path.isfile(filename) == True:

		# Open the inpit file to read
		with open(filename, 'r', encoding='utf-8') as results:

			for line in results: # Iterate over all lines in the results file

				if "mat" in line:

					lengthofline = len(line)

					x = 0

					LineR = ""

					while x < lengthofline:

						if line[x] == "p":

							y = x

							while line[y] != " ":

								y = y + 1

							x = y 

						else:

							LineR = LineR + line[x]

						x += 1

					FILELIST.append(LineR)

				else:

					lengthofline = len(line)
					x = 0
					LineR = ""
					newtemp =""
					L=""

					while x < lengthofline:

						if line[x] == "c":

							currenttemp = line[x-2:x]

							if currenttemp == "03":

								newtemp == "12c"

							elif currenttemp == "06":

								newtemp = "15c"

							elif currenttemp == "09":

								newtemp = "18c"

							LineR = line[0:x-2]

							L = LineR + newtemp + line[x+1:lengthofline]

						x += 1

					FILELIST.append(L) # Add the lines to a new list

	for x in FILELIST:

		smrdep.write(x)

	smrdep.close()
