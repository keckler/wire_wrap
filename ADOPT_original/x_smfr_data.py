import os

def smfrdata(Name, SerpentDepletionSteps, SerpentDepletion, CoreLatticeIDs):

	ResultsFile     = Name + "_geometry_reference_res.m"
	ResultsFileData = []

	AssemblyPeakingVector = []
	PinPeakingVector      = []

	KeffVector = []
	BeffVector = []

	if not SerpentDepletion == "on":

		SerpentDepletionSteps = 1

	i = 0
	
	if os.path.exists(ResultsFile) == True and os.path.isfile(ResultsFile) == True:

		# Open the results file, make it readable, choose encoding at Unicode
		with open(ResultsFile, 'r', encoding='utf-8') as results:

			for line in results:             # Iterate over all lines in the results file

				i += 1
				ResultsFileData.append(line) # Add the lines to a new list

				for ID in CoreLatticeIDs:

					APF = "PEAKF" + str(ID)

					if APF in line:        # Find the assembly-level peaking factor
	
						VAL = float(line[57:68])
						AssemblyPeakingVector.append(VAL)

				if "IMP_KEFF" in line:
	
					KeffVector.append(float(line[47:58]))
					KeffErr = float(line[60:66])

				if "BETA_EFF" in line:
				
					BeffVector.append(float(line[47:58]))	
					BeffErr = float(line[60:66])				

	Runs = len(AssemblyPeakingVector)/len(CoreLatticeIDs)

	AxiallyAveragedRadialPowerPeak = []

	for run in range(int(Runs)):

		Avep = 0

		for axie in range(len(CoreLatticeIDs)):
	
			Val = AssemblyPeakingVector[axie+run]
			Avep += Val

		AxiallyAveragedRadialPowerPeak.append(Avep/len(CoreLatticeIDs))	

	MaxKeff = max(KeffVector)
	MinKeff = min(KeffVector)

	BOCKeff = KeffVector[0]
	EOCKeff = KeffVector[len(KeffVector)-1]

	MaxBeff = max(BeffVector)
	MinBeff = min(BeffVector)

	BOCBeff = BeffVector[0]
	EOCBeff = BeffVector[len(BeffVector)-1]

	KeffCycleSwing = (EOCKeff-BOCKeff)/BOCKeff
	KeffPeakSwing  = (MaxKeff-MinKeff)/MinKeff

	if len(AxiallyAveragedRadialPowerPeak) > 0:

		RadialPowerPeaking = max(AxiallyAveragedRadialPowerPeak)

	else:

		RadialPowerPeaking = 1

	return(RadialPowerPeaking, MaxKeff, MinKeff, BOCKeff, EOCKeff, KeffCycleSwing, KeffPeakSwing, MaxBeff, MinBeff, BOCBeff, EOCBeff, KeffErr, BeffErr)

