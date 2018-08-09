#from pylab import *
#import matplotlib.pyplot as plt
import os
import collections

def powers2(detfile, CellNames, Batches, Power, SerpentAxialZones, SerpentCoreRadius, Plotting,
			matplotlibpath, step, x):

	NeutronRun = x
	
	#print("NeutronRun")
	#print(NeutronRun)
	#print("Burnupstep")
	#print(step)

	Lines = {}
	Filedata = []
	i = 0

	with open(detfile, 'r', encoding='utf-8') as results:

		for line in results:

			i += 1
			Filedata.append(line)

			for Cell in CellNames:

				CheckCell = "DETPower" + Cell

				if CheckCell in line:

					X = {Cell : i}
					Lines.update(X)

	PowerDistribution = {}

	for k,v in Lines.items():

		CellPower = float(Filedata[v][52:63])/1e6
		CellPowerID = {k : CellPower}

		PowerDistribution.update(CellPowerID)

	RadialPowerDistribution = {}

	for Batch in range(Batches):

		T1 = "Batch" + str(Batch+1) + "Axial"

		RadialBatchPower = 0
		RadialPowers = []

		for k,v in PowerDistribution.items():

			if T1 in k:
	
				RadialBatchPower += v

			RadialPowers.append(RadialBatchPower)
			AA = {Batch+1 : RadialBatchPower}	
			RadialPowerDistribution.update(AA)

	RPP = []

	for k,v in RadialPowerDistribution.items():

		RPP.append(v)

	AverageRadialPower = Power / Batches / 1e6
	MaximumRadialPower = max(RPP)
	RadialPowerPeaking = MaximumRadialPower / AverageRadialPower

	RadY  = []
	RadpY = []

	for k,v in RadialPowerDistribution.items():

		RadY.append(v)
		RadpY.append(v/(Power/Batches/1e6))

		if v == MaximumRadialPower:

			MaximumRadialPowerPosition = k		

	AxialPowers = []
	AXXP = {}

	for k,v in PowerDistribution.items():

		T1 = "Batch" + str(MaximumRadialPowerPosition) + "Axial"

		if T1 in k:

			AxialPowers.append(v)
			AXLP = {k : v}
			AXXP.update(AXLP)

	AXP  = []
	AXPY = []

	for x in range(SerpentAxialZones):
	
		AXP.append(x+1)

		T1 = "Batch" + str(MaximumRadialPowerPosition) + "Axial" + str(x+1)

		for k,v in AXXP.items():

			if T1 in k:

				AXPY.append(v)

	AXP.append(SerpentAxialZones+1)

	AXPYY = []

	for axp in AXPY:

		AXPYY.append(axp)

	AXPYY.append(AXPY[SerpentAxialZones-1])

	MaximumAxialPower = max(AxialPowers)
	AverageAxialPower = sum(AxialPowers)/SerpentAxialZones
	AxialPowerPeaking = MaximumAxialPower/AverageAxialPower

	PinAxialPowerPeaking = AxialPowerPeaking

	SR  = [0.0]
	RR  = [0.0]
	RR2 = [0.0]

	for rad in SerpentCoreRadius:

		SR.append(rad)

	for powx in RadY:
	
		RR.append(powx)	

	for powx2 in RadpY:
	
		RR2.append(powx2)	

	if Plotting == "on":

		FigureDPI         = 300
		FigureXsize       = 10
		FigureYsize       = 6
		Linewidth         = 2.5
		Linecolor         = "black"
		Linestyle         = "-"
	
		plotpowerpath = matplotlibpath + "/radial_power/"
		if not os.path.exists(plotpowerpath): os.makedirs(plotpowerpath)

		plotpowerpathx = plotpowerpath + "/iter" + str(NeutronRun) + "/"
		if not os.path.exists(plotpowerpathx): os.makedirs(plotpowerpathx)

		plotpowerpeakpath = matplotlibpath + "/radial_powerpeak/"
		if not os.path.exists(plotpowerpeakpath): os.makedirs(plotpowerpeakpath)

		plotpowerpeakpathx = plotpowerpeakpath + "/iter" + str(NeutronRun) + "/"
		if not os.path.exists(plotpowerpeakpathx): os.makedirs(plotpowerpeakpathx)

		plotpoweraxpeakpath = matplotlibpath + "/axial_power/"
		if not os.path.exists(plotpoweraxpeakpath): os.makedirs(plotpoweraxpeakpath)

		plotpoweraxpeakpathx = plotpoweraxpeakpath + "/iter" + str(NeutronRun) + "/"
		if not os.path.exists(plotpoweraxpeakpathx): os.makedirs(plotpoweraxpeakpathx)

		figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
		plt.step(SR,RR, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
		xlabel("Radial distance from the center of the active core [m]")
		ylabel("Batch power [MW] (" + str(Batches) + " batches)")
		grid(True)
		savefig(plotpowerpathx + "PowerProfile_dep" + str(step) + ".png",dpi=FigureDPI)		
		close()

		figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
		plt.step(AXPYY,AXP, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
		xlabel("Segment power [MW] (" + str(SerpentAxialZones) + " segments per Batch)")
		ylabel("Axial segment at peak radial power position")
		grid(True)
		xlim(0)
		savefig(plotpoweraxpeakpathx + "PowerProfile_dep" + str(step) + ".png",dpi=FigureDPI)		
		close()

		figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
		plt.step(SR, RR2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
		xlabel("Radial distance from the center of the active core [m]")
		ylabel("Local power / Average power")
		grid(True)

		Ymin = 0
		Ymax = 1.4

		ylim(Ymin, Ymax)

		savefig(plotpowerpeakpathx + "PowerPeakProfile_dep" + str(step) + ".png",dpi=FigureDPI)		
		close()

	return(RadialPowerPeaking, PinAxialPowerPeaking) 

def flux2(detfile, CellNames, Batches, SerpentAxialZones, CellVolume, ResidenceTime):

	Lines = {}
	Filedata = []
	i = 0

	with open(detfile, 'r', encoding='utf-8') as results:

		for line in results:

			i += 1
			Filedata.append(line)

			for Cell in CellNames:

				CheckCell = "DETFlux" + Cell

				if CheckCell in line:

					X = {Cell : i}
					Lines.update(X)

	FluxDistribution = {}
	CellFluxs = []

	TotalFlux = 0
	TotFlux   = 0

	for k,v in Lines.items():

		CellFlux = float(Filedata[v][52:63])/CellVolume
		CellFlux2 = float(Filedata[v][52:63])
		CellFluxs.append(CellFlux)
		CellFluxID = {k : CellFlux}

		TotalFlux += CellFlux
		TotFlux += CellFlux2

		FluxDistribution.update(CellFluxID)

	PeakFlux = max(CellFluxs)
	PeakFluence = PeakFlux * ResidenceTime * 24 * 3600

	RadialFluxDistribution = {}
	RadialFluxs = []

	for Batch in range(Batches):

		T1 = "Batch" + str(Batch+1) + "Axial"

		RadialBatchFlux = 0

		for k,v in FluxDistribution.items():

			if T1 in k:
	
				RadialBatchFlux += v
	
		RadialBatchFlux = RadialBatchFlux / SerpentAxialZones
		RadialFluxs.append(RadialBatchFlux)
		AA = {Batch+1 : RadialBatchFlux}	
		RadialFluxDistribution.update(AA)

	AverageFlux = TotalFlux / (Batches * SerpentAxialZones)

	MaximumRadialFlux = max(RadialFluxs)
	RadialFluxPeaking = MaximumRadialFlux / AverageFlux

	for k,v in RadialFluxDistribution.items():

		if v == MaximumRadialFlux:

			MaximumRadialFluxPosition = k		

	AxialFluxs = []

	for k,v in FluxDistribution.items():

		T1 = "Batch" + str(MaximumRadialFluxPosition) + "Axial"

		if T1 in k:

			AxialFluxs.append(v)

	MaximumAxialFlux = max(AxialFluxs)
	AverageAxialFlux = sum(AxialFluxs)/SerpentAxialZones
	AxialFluxPeaking = MaximumAxialFlux/AverageAxialFlux

	PinAxialFluxPeaking = AxialFluxPeaking

	return(PeakFlux, PeakFluence) 

def getres(resfile, SerpentDepletion, Plotting, depfile, SerpentDepletionSteps,x, matplotlibpath):

	KeffVector = []
	BeffVector = []
	MaxKeff = 1
	MinKeff = 1

	if not SerpentDepletion == "on":

		SerpentDepletionSteps = 1

	if os.path.exists(resfile) == True and os.path.isfile(resfile) == True:

		# Open the results file, make it readable, choose encoding at Unicode
		with open(resfile, 'r', encoding='utf-8') as results:

			for line in results:             # Iterate over all lines in the results file

				if "IMP_KEFF" in line:

					KeffVector.append(float(line[47:58]))
					KeffErr = float(line[60:66])

				if "BETA_EFF" in line:
				
					BeffVector.append(float(line[47:58]))	
					BeffErr = float(line[60:66])				

		MaxBeff = max(BeffVector)
		MinBeff = min(BeffVector)

		BOCBeff = BeffVector[0]
		EOCBeff = BeffVector[len(BeffVector)-1]

		MaxKeff = max(KeffVector)
		MinKeff = min(KeffVector)

		BOCKeff = KeffVector[0]
		EOCKeff = KeffVector[len(KeffVector)-1]

		KeffCycleSwing = (EOCKeff-BOCKeff)/BOCKeff
		KeffPeakSwing  = (MaxKeff-MinKeff)/MinKeff

	DaysVector = []
	BUVector   = []

	if SerpentDepletion == "on" and Plotting == "on":

		FigureDPI         = 300
		FigureXsize       = 10
		FigureYsize       = 6
		Linewidth         = 2.5
		Linecolor         = "black"
		Linestyle         = "-"
		vallength = 11

		if os.path.exists(depfile) == True and os.path.isfile(depfile) == True:

			# Open the depletion file, make it readable, choose encoding at Unicode
			with open(depfile, 'r', encoding='utf-8') as results:		

				for line in results:

					if "DAYS = [" in line:
	
						for step in range(SerpentDepletionSteps+1):
	
							startx = 9 + 12 * step
							endx   = startx + vallength
	
							DaysVector.append(float(line[startx:endx])/365)

					if "BU = [" in line:
	
						for step in range(SerpentDepletionSteps+1):
	
							startx = 7 + 12 * step
							endx   = startx + vallength
	
							BUVector.append(float(line[startx:endx]))

		plotkeffpath = matplotlibpath + "/keff/"
		if not os.path.exists(plotkeffpath): os.makedirs(plotkeffpath)
	
		figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
		plt.errorbar(DaysVector, KeffVector, yerr=KeffErr, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
		xlabel("Years of full-power operation")
		ylabel("K-effective")
		grid(True)
		xlim(-1)
		savefig(plotkeffpath + "keff_years_iter" + str(x) + ".png",dpi=FigureDPI)		
		close()
	
		figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
		plt.errorbar(BUVector, KeffVector, yerr=KeffErr, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
		xlabel("Average fuel burnup (MWd/kg-actinide)")
		ylabel("K-effective")
		grid(True)
		xlim(-1)
		savefig(plotkeffpath + "keff_BU_iter" + str(x) + ".png",dpi=FigureDPI)		
		close()

	return(MaxKeff, MinKeff, BOCKeff, EOCKeff, MaxBeff, MinBeff, BOCBeff, EOCBeff, KeffCycleSwing, KeffPeakSwing, KeffErr, BeffErr)


def getresvoid(resfile):

	VoidKeff    = 0
	VoidKeffErr = 0

	if os.path.exists(resfile) == True and os.path.isfile(resfile) == True:

		# Open the results file, make it readable, choose encoding at Unicode
		with open(resfile, 'r', encoding='utf-8') as results:

			for line in results:             # Iterate over all lines in the results file

				if "IMP_KEFF" in line:

					VoidKeff    = (float(line[47:58]))
					VoidKeffErr = float(line[60:66])

	return(VoidKeff, VoidKeffErr)


def getcoeff(resfile):

	PerturbedKeff    = 0
	PerturbedKeffErr = 0

	if os.path.exists(resfile) == True and os.path.isfile(resfile) == True:

		# Open the results file, make it readable, choose encoding at Unicode
		with open(resfile, 'r', encoding='utf-8') as results:

			for line in results:             # Iterate over all lines in the results file

				if "IMP_KEFF" in line:

					PerturbedKeff    = (float(line[47:58]))
					PerturbedKeffErr = float(line[60:66])

	return(PerturbedKeff, PerturbedKeffErr)

def getdet(detfile, CellNames, CellVolume, CycleTime, Cladding):

	if Cladding == "HT9":
	
		IronMF       = 84.55/100
		ChromiumMF   = 12/100
		CarbonMF     = 0.2/100
		MolybdenumMF = 1/100
		SiliconMF    = 0.4/100
		WolframMF    = 0.5/100
		VanadiumMF   = 0.25/100
		ManganeseMF  = 0.6/100
		NickelMF     = 0.5/100
	
	elif Cladding == "SiC":

		IronMF       = 0
		ChromiumMF   = 0
		CarbonMF     = 30/100
		MolybdenumMF = 0
		SiliconMF    = 70/100
		WolframMF    = 0
		VanadiumMF   = 0
		ManganeseMF  = 0
		NickelMF     = 0

	elif Cladding == "D9":

		IronMF       = 65.87/100
		ChromiumMF   = 15.10/100
		CarbonMF     = 0.09/100
		MolybdenumMF = 1.22/100
		SiliconMF    = 0.44/100
		WolframMF    = 0
		VanadiumMF   = 0
		ManganeseMF  = 1.8/100
		NickelMF     = 14.96/100

	Iron=[77.3000,
	24.4000,
	12.8000,
	8.6000,
	6.4000,
	5.2000,
	4.3000,
	3.5000,
	2.9000,
	2.4000,
	1.9000,
	1.6000,
	1.3000,
	1.1000,
	0.9000,
	0.7000,
	0.6000,
	0.5000,
	0.4000,
	0.3000,
	0.3000,
	0.2000,
	0.2000,
	0.1000,
	0.1000,
	0.1000,
	0.1000,
	0.1000,
	0.1000,
	0.1000,
	1.3000,
	3.1000,
	6.7000,
	4.8000,
	5.1000,
	5.7000,
	6.3000,
	8.2000,
	8.3000,
	16.7000,
	37.1000,
	14.9000,
	11.6000,
	9.7000,
	5.5000,
	267.6000,
	81.6000,
	65.1000,
	65.8000,
	131.4000,
	118.4000,
	112.7000,
	215.3000,
	158.5000,
	220.1000,
	182.7000,
	173.7000,
	135.1000,
	251.4000,
	465.2000,
	430.4000,
	364.0000,
	332.2000,
	341.8000,
	196.4000,
	488.9000,
	742.2000,
	440.2000,
	409.7000,
	509.5000,
	500.9000,
	645.4000,
	735.8000,
	764.6000,
	951.5000,
	937.5000,
	1120.5000,
	1235.5000,
	1334.5000,
	1352.5000,
	1495.5000,
	1582.5000,
	1685.5000,
	1764.6000,
	1830.6000,
	1892.6000,
	1966.7000,
	2033.7000,
	2145.8000,
	2256.9000,
	2376.0000,
	2474.1000,
	2585.2000,
	2713.5000,
	2902.7000,
	2932.0000,
	2927.3000,
	2976.5000,
	3072.6000,
	3163.6000]
	
	Silicon = [11.0400,
	3.5200,
	1.7600,
	1.2800,
	0.9600,
	0.8000,
	0.6400,
	0.4800,
	0.4800,
	0.3200,
	0.3200,
	0.1600,
	0.1600,
	0.1600,
	0.1600,
	0.1600,
	0.1600,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.4800,
	0.8000,
	1.1200,
	1.2800,
	1.4400,
	1.7600,
	2.0800,
	2.7200,
	3.3600,
	4.1600,
	5.4400,
	6.8800,
	8.9600,
	10.8800,
	13.7600,
	17.1200,
	21.2800,
	26.2400,
	32.4800,
	39.2000,
	48.0000,
	42.0800,
	229.4400,
	100.9600,
	83.3600,
	54.2400,
	40.8000,
	1006.5600,
	1457.6000,
	984.3200,
	823.3600,
	788.4800,
	768.6400,
	789.2800,
	811.0400,
	844.9600,
	1021.4400,
	1081.6000,
	835.2000,
	900.8000,
	1107.3600,
	1900.8000,
	1310.5600,
	1764.6400,
	1043.6800,
	1405.6000,
	1625.4400,
	1677.4400,
	2328.4800,
	1572.6400,
	1936.6400,
	1981.7600,
	1816.9600,
	1629.9200,
	1948.1600,
	2165.1200,
	2490.2400,
	2208.4800,
	2364.4800,
	2154.7200,
	2102.8800,
	2704.9600,
	2647.2000,
	2695.3600,
	2746.5600,
	2823.6800,
	2901.9200,
	3059.0400,
	3065.1200,
	3106.4000,
	3136.4800,
	3134.5600,
	3197.7600,
	3203.8400]
	
	Chromium = [131.2000,
	41.5000,
	21.7000,
	14.6000,
	10.9000,
	8.9000,
	7.3000,
	6.0000,
	4.9000,
	4.0000,
	3.3000,
	2.7000,
	2.2000,
	1.8000,
	1.5000,
	1.2000,
	1.0000,
	0.8000,
	0.7000,
	0.5000,
	0.5000,
	0.4000,
	0.3000,
	0.3000,
	0.2000,
	0.2000,
	0.2000,
	0.2000,
	0.1000,
	0.1000,
	1.0000,
	1.9000,
	2.7000,
	3.3000,
	6.6000,
	6.5000,
	13.1000,
	33.4000,
	43.0000,
	53.3000,
	55.5000,
	24.7000,
	17.7000,
	16.1000,
	19.4000,
	33.8000,
	30.5000,
	115.3000,
	77.0000,
	44.6000,
	320.2000,
	142.4000,
	362.2000,
	243.3000,
	226.3000,
	267.7000,
	204.3000,
	165.5000,
	236.9000,
	201.2000,
	429.5000,
	406.0000,
	360.8000,
	411.2000,
	313.2000,
	290.8000,
	526.0000,
	506.9000,
	642.6000,
	508.5000,
	563.3000,
	824.0000,
	995.4000,
	986.6000,
	935.3000,
	1177.1000,
	1285.2000,
	1432.2000,
	1420.1000,
	1512.0000,
	1615.0000,
	1701.9000,
	1827.8000,
	1875.7000,
	1929.6000,
	1981.5000,
	2041.5000,
	2115.4000,
	2171.4000,
	2236.5000,
	2349.6000,
	2470.8000,
	2646.2000,
	2731.6000,
	2786.1000,
	2907.8000,
	2932.3000,
	2957.3000,
	2967.6000,
	2990.7000]
	
	Carbon = [0.2581,
	0.1290,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	0.0000,
	1.0323,
	1.9355,
	2.4516,
	2.7097,
	3.2258,
	3.7419,
	4.6452,
	5.8065,
	7.3548,
	9.2903,
	11.4839,
	14.7097,
	18.8387,
	24.0000,
	29.8065,
	37.2903,
	47.2258,
	59.7419,
	74.3226,
	91.2258,
	115.3548,
	143.6129,
	173.0323,
	211.6129,
	256.1290,
	309.9355,
	367.8710,
	421.0323,
	469.2903,
	514.5806,
	556.2581,
	593.9355,
	626.8387,
	653.8065,
	676.1290,
	697.1613,
	715.4839,
	730.4516,
	741.1613,
	748.1290,
	752.6452,
	753.9355,
	751.4839,
	750.9677,
	744.2581,
	735.7419,
	717.6774,
	687.6129,
	656.7742,
	627.4839,
	601.5484,
	647.8710,
	588.6452,
	718.9677,
	749.9355,
	938.4516,
	791.7419,
	677.8065,
	508.7742,
	468.5161,
	433.6774,
	453.5484,
	391.3548,
	665.4194,
	406.0645,
	394.0645,
	431.3548,
	513.4194,
	504.9032,
	496.9032,
	504.6452,
	555.2258,
	571.3548,
	552.1290,
	588.2581,
	601.0323]
	
	Manganese = [400.1000,
	126.5000,
	66.2000,
	44.4000,
	33.4000,
	27.1000,
	22.2000,
	18.2000,
	14.9000,
	12.3000,
	10.1000,
	8.2000,
	6.7000,
	5.5000,
	4.5000,
	3.7000,
	3.1000,
	2.6000,
	2.2000,
	1.8000,
	1.6000,
	1.4000,
	1.4000,
	1.5000,
	1.7000,
	2.5000,
	6.0000,
	94.0000,
	11.4000,
	1.2000,
	2.5000,
	6.0000,
	66.7000,
	9.1000,
	40.8000,
	312.4000,
	79.6000,
	21.0000,
	9.9000,
	51.0000,
	167.0000,
	52.9000,
	16.5000,
	16.2000,
	120.8000,
	72.9000,
	233.3000,
	99.0000,
	154.7000,
	176.6000,
	140.0000,
	420.4000,
	195.3000,
	235.2000,
	328.2000,
	261.7000,
	169.5000,
	274.5000,
	258.5000,
	296.9000,
	361.8000,
	419.1000,
	349.7000,
	404.3000,
	451.3000,
	447.8000,
	459.9000,
	509.0000,
	613.3000,
	618.4000,
	742.3000,
	896.6000,
	951.9000,
	1024.5000,
	1089.5000,
	1140.6000,
	1193.6000,
	1278.7000,
	1384.7000,
	1475.7000,
	1599.7000,
	1540.8000,
	1597.8000,
	1690.8000,
	1756.8000,
	1824.8000,
	1914.8000,
	1996.8000,
	1993.9000,
	2046.0000,
	2184.2000,
	2374.4000,
	2495.6000,
	2578.8000,
	2597.9000,
	2705.9000,
	2797.8000,
	2847.7000,
	2939.5000,
	3046.3000]
	
	Nickel = [171.5000,
	54.2000,
	28.4000,
	19.0000,
	14.3000,
	11.6000,
	9.5000,
	7.8000,
	6.4000,
	5.3000,
	4.3000,
	3.5000,
	2.8000,
	2.3000,
	1.9000,
	1.6000,
	1.3000,
	1.1000,
	0.9000,
	0.7000,
	0.6000,
	0.5000,
	0.4000,
	0.3000,
	0.3000,
	0.3000,
	0.2000,
	0.2000,
	0.2000,
	0.2000,
	1.6000,
	4.9000,
	7.6000,
	8.8000,
	9.8000,
	12.1000,
	15.9000,
	29.9000,
	40.9000,
	26.1000,
	20.2000,
	54.9000,
	177.1000,
	305.9000,
	102.3000,
	104.1000,
	87.4000,
	70.2000,
	146.8000,
	199.0000,
	140.1000,
	111.3000,
	232.1000,
	269.5000,
	363.5000,
	337.1000,
	336.1000,
	371.7000,
	393.8000,
	320.0000,
	351.5000,
	407.9000,
	398.4000,
	342.6000,
	489.3000,
	420.8000,
	401.0000,
	524.9000,
	549.8000,
	540.0000,
	597.5000,
	803.8000,
	806.9000,
	775.3000,
	820.3000,
	915.4000,
	1020.3000,
	1138.3000,
	1130.4000,
	1273.4000,
	1321.4000,
	1604.5000,
	1686.6000,
	1798.8000,
	1869.9000,
	2075.1000,
	2189.3000,
	2237.5000,
	2316.6000,
	2566.6000,
	2694.5000,
	2819.4000,
	2895.2000,
	2965.1000,
	3001.9000,
	3034.9000,
	3090.9000,
	3246.9000,
	3336.0000,
	3376.1000]
	
	Molybdenum = [14.2000,
	4.4667,
	2.3333,
	1.6000,
	1.2000,
	0.9333,
	0.8000,
	0.6667,
	0.5333,
	0.4667,
	0.3333,
	0.2667,
	0.2667,
	0.2000,
	0.1333,
	0.1333,
	0.1333,
	1.6667,
	0.0667,
	0.1333,
	17.9333,
	11.1333,
	1.0000,
	11.6667,
	0.7333,
	0.0667,
	0.2000,
	1.6000,
	2.6000,
	2.4667,
	0.8000,
	0.9333,
	5.6000,
	5.6667,
	18.9333,
	30.9333,
	37.6667,
	40.2000,
	44.3333,
	50.2667,
	59.1333,
	70.0667,
	82.8667,
	97.3333,
	116.9333,
	136.9333,
	154.4000,
	169.8000,
	167.0000,
	143.5333,
	95.3333,
	113.4667,
	133.9333,
	154.6667,
	174.6667,
	194.1333,
	215.5333,
	234.4667,
	253.4667,
	273.5333,
	294.0667,
	314.6000,
	337.8000,
	355.3333,
	372.2000,
	387.8667,
	400.4667,
	413.5333,
	424.0667,
	433.5333,
	472.7333,
	513.0667,
	557.8000,
	593.9333,
	614.6000,
	634.3333,
	653.8667,
	684.8667,
	721.5333,
	755.7333,
	789.3333,
	829.4000,
	882.7333,
	946.3333,
	1006.0000,
	1069.9333,
	1128.9333,
	1222.8667,
	1326.8000,
	1422.6667,
	1496.5333,
	1598.4667,
	1690.3333,
	1718.2000,
	1729.0000,
	1792.8667,
	1840.8000,
	1936.6667,
	2058.6667,
	2142.6000]
	
	Vanadium = [172.8000,
	54.7000,
	28.6000,
	19.2000,
	14.4000,
	11.7000,
	9.6000,
	7.8000,
	6.4000,
	5.3000,
	4.3000,
	3.5000,
	2.9000,
	2.4000,
	1.9000,
	1.6000,
	1.3000,
	1.1000,
	0.9000,
	0.7000,
	0.6000,
	0.5000,
	0.4000,
	0.4000,
	1.8000,
	0.5000,
	0.2000,
	0.2000,
	0.2000,
	0.2000,
	1.4000,
	2.6000,
	3.8000,
	5.2000,
	5.7000,
	8.3000,
	19.3000,
	233.5000,
	159.8000,
	249.7000,
	74.3000,
	254.6000,
	309.1000,
	236.2000,
	135.5000,
	92.4000,
	57.6000,
	60.3000,
	141.1000,
	197.2000,
	84.6000,
	310.4000,
	242.2000,
	406.4000,
	386.1000,
	329.0000,
	314.3000,
	441.7000,
	400.1000,
	313.8000,
	337.1000,
	394.0000,
	306.2000,
	346.9000,
	440.1000,
	507.7000,
	432.7000,
	479.7000,
	670.3000,
	677.0000,
	739.6000,
	873.6000,
	986.6000,
	1145.4000,
	1178.4000,
	1301.4000,
	1340.4000,
	1456.4000,
	1500.5000,
	1592.5000,
	1612.5000,
	1653.6000,
	1697.6000,
	1714.7000,
	1775.7000,
	1865.7000,
	1922.8000,
	1966.8000,
	2059.8000,
	2162.8000,
	2256.8000,
	2269.9000,
	2476.0000,
	2606.1000,
	2700.2000,
	2760.2000,
	2848.3000,
	2914.4000,
	2976.4000,
	3032.5000]
	
	Wolfram = [3.9996,
	1.2758,
	0.6619,
	0.4434,
	0.3210,
	0.2666,
	0.2303,
	0.1886,
	0.1705,
	0.1523,
	0.1079,
	0.0897,
	0.0897,
	0.1251,
	14.7177,
	0.9858,
	3.0373,
	0.0426,
	1.5266,
	11.6254,
	0.2789,
	2.2578,
	0.0127,
	1.2257,
	0.6496,
	1.1951,
	0.5625,
	0.4557,
	0.4790,
	0.1851,
	0.3712,
	0.3194,
	0.3566,
	0.2532,
	0.1788,
	0.1896,
	0.1452,
	0.1388,
	3.4713,
	6.5525,
	8.5771,
	9.0551,
	9.8606,
	10.8347,
	12.3486,
	13.9622,
	15.4670,
	17.0380,
	18.2688,
	18.8876,
	25.3337,
	37.3888,
	41.5257,
	45.9393,
	50.6158,
	55.5997,
	60.6861,
	65.4098,
	70.8447,
	76.8255,
	84.0108,
	91.8529,
	99.6795,
	107.6903,
	116.6842,
	126.6173,
	136.6151,
	147.2904,
	159.5431,
	171.9998,
	188.8005,
	204.6974,
	213.6192,
	228.4434,
	243.4900,
	261.7694,
	279.3975,
	295.2862,
	312.9328,
	336.7670,
	358.9393,
	382.3227,
	410.2893,
	440.8430,
	471.2983,
	503.1669,
	548.5020,
	565.4468,
	637.2215,
	698.6569,
	743.0837,
	778.2014,
	811.9296,
	847.1139,
	881.7446,
	920.0912,
	972.5563,
	1028.6749,
	1086.1882,
	1132.4118]

	# COLLECT GROUP-WISE FLUX AND FLUENCE -------------------------------------------------------------

	detfiledata = []
	i = 0
	ic = []
	totalzones = len(CellNames)
	
	with open(detfile, 'r', encoding='utf-8') as results:
	
		for line in results:
	
			detfiledata.append(line)
			i += 1
	
			for zone in range(totalzones):
	
				detectorname = "DET" + str(zone+1) + " = ["
	
				if detectorname in line:
	
					ic.append(i)	

	GroupedFlux        = {}
	GroupedFluence     = {}
	SumFluxZone        = {}
	SumFluenceZone     = {}
	SumFastFluxZone    = {}
	SumFastFluenceZone = {}

	BuSeconds = CycleTime * 24 * 3600
	Groups = 99

	PeakGFluence = []

	for zone in range(totalzones):
	
		B = []
		C = []

		for x in range(Groups):
		
			row = ic[zone] + x

			X0 = detfiledata[row+1][52:63]
			X1 = float(X0)
			A  = X1/CellVolume
			AA = A * BuSeconds
	
			B.append(A)
			C.append(AA)
	
		SumFlux    = sum(B)
		SumFluence = sum(C)

		SumFastFlux    = sum(B[53:100])
		SumFastFluence = sum(C[53:100])

		PeakGFluence.append(SumFastFluence)

		GFLX = {CellNames[zone] : B}
		GFLE = {CellNames[zone] : C}
	
		GroupedFlux.update(GFLX)
		GroupedFluence.update(GFLE)

		GFLXx = {CellNames[zone] : SumFlux}
		GFLEx = {CellNames[zone] : SumFluence}
	
		SumFluxZone.update(GFLXx)
		SumFluenceZone.update(GFLEx)
	
		GFLXxx = {CellNames[zone] : SumFastFlux}
		GFLExx = {CellNames[zone] : SumFastFluence}
	
		SumFastFluxZone.update(GFLXxx)
		SumFastFluenceZone.update(GFLExx)				

	PeakFastFluence = max(PeakGFluence)

	# CALCULATE 1-GROUP DPA ---------------------------------------------------------------------------

	DPAcollect = {}
	DPAx = []
	
	for name in CellNames:
	
		Iron1G        = []
		Chromium1G    = []
		Carbon1G      = []
		Molybdenum1G  = []
		Silicon1G     = []
		Wolfram1G     = []
		Vanadium1G    = []
		Manganese1G   = []
		Nickel1G      = []
	
		ZoneFluence = GroupedFluence.get(name)
		
		for i in range(Groups):
		
			Iron1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Chromium1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Carbon1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Molybdenum1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Silicon1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Wolfram1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Vanadium1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Manganese1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
			Nickel1G.append(Iron[i] * ZoneFluence[i] * 1e-24)
		
		IronSum       = sum(Iron1G)*IronMF
		ChromiumSum   = sum(Chromium1G)*ChromiumMF
		CarbonSum     = sum(Carbon1G)*CarbonMF
		MolybdenumSum = sum(Molybdenum1G)*MolybdenumMF
		SiliconSum    = sum(Silicon1G)*SiliconMF
		WolframSum    = sum(Wolfram1G)*WolframMF
		VanadiumSum   = sum(Vanadium1G)*VanadiumMF
		ManganeseSum  = sum(Manganese1G)*ManganeseMF
		NickelSum     = sum(Nickel1G)*NickelMF
	
		DPAsum = IronSum + ChromiumSum + CarbonSum + MolybdenumSum + SiliconSum + WolframSum + VanadiumSum + ManganeseSum + NickelSum
	
		DPAi = {name : DPAsum}
		DPAcollect.update(DPAi)
		DPAx.append(DPAsum)

	maxDPA = max(DPAx)

	for k,v in DPAcollect.items():

		if v == maxDPA:

			maxDPAcell = k

	A = "Peak " + Cladding + " cycle DPA {0:02.2f}".format(maxDPA) + " (cell: " + maxDPAcell + ")"
	
	return(SumFluenceZone, SumFluxZone, SumFastFluxZone, SumFastFluenceZone, DPAcollect, maxDPA, maxDPAcell, PeakFastFluence)

def getdep(depfile, SerpentDepletionSteps, CellNames, SerpentInventory, Batches, SerpentAxialZones, 
		   CellVolume, matplotlibpath, SerpentCoreRadius, SerpentDepletionEnd, Plotting):

	SkipInitialPoints = 3
	FigureDPI         = 300
	FigureXsize       = 10
	FigureYsize       = 6
	Linewidth         = 2.5
	Linecolor         = "black"
	Linestyle         = "-"

	plotpath = matplotlibpath + "/"
	plotpowerpath = matplotlibpath + "/power_profile/"

	if not os.path.exists(plotpowerpath): os.makedirs(plotpowerpath)

	depfileData    = []
	Cells          = Batches * SerpentAxialZones
	NumberIsotopes = len(SerpentInventory)
	RadialPowerPeaking = 1
	PeakFlux = 1
	AverageFlux = 1

	if os.path.exists(depfile) == True and os.path.isfile(depfile) == True:

		# Open the results file, make it readable, choose encoding at Unicode
		with open(depfile, 'r', encoding='utf-8') as results:

			i = 0
			DepletionLines = []
			FluxLines      = []
			AdensLines     = []

			# Iterate over all lines in the results file
			for line in results:            
	
				i += 1

				# Add the lines to a new list
				depfileData.append(line) 
	
				for Cell in CellNames:

					FISSXS = "MAT_" + Cell + "_FISSXS = ["
					FLUX   = "MAT_" + Cell + "_FLUX = ["
					ADENS   = "MAT_" + Cell + "_ADENS = ["
	
					if FISSXS in line:

						DepletionLines.append(i)

					if FLUX in line:

						FluxLines.append(i)

					if ADENS in line:

						AdensLines.append(i)

		OneGroupFISSXS  = []
		OneGroupFISSXSd = {}
		OneGroupFLUX    = []
		OneGroupFLUXd   = {}
		AverageFlux     = []
		Adensd          = {}
		FLUENCE         = []
		FLUENCEd        = {} 

		for data in range(Cells):

			StepFlux = 0

			for step in range(SerpentDepletionSteps):

				WhereDataStart = 1 + 12 * step
				WhereDataEnd   = WhereDataStart + 11
			
				A1 = DepletionLines[data]
				B1 = depfileData[A1]
				C1 = float(B1[WhereDataStart:WhereDataEnd])
				D1 = CellNames[data] + "_dep_" + str(step+1) + "_"
				E1 = {D1 : C1}
		
				OneGroupFISSXS.append(C1)
				OneGroupFISSXSd.update(E1)
		
				A2 = FluxLines[data]
				B2 = depfileData[A2]
				C2 = float(B2[WhereDataStart:WhereDataEnd])
				D2 = CellNames[data] + "_dep_" + str(step+1) + "_"
				E2 = {D2 : C2}
		
				OneGroupFLUX.append(C2)
				OneGroupFLUXd.update(E2)

				A3 = AdensLines[data]
				B3 = depfileData[A3]
				C3 = float(B3[WhereDataStart:WhereDataEnd])
				D3 = CellNames[data] + "_dep_" + str(step+1) + "_"
				E3 = {D3 : C3}

				Adensd.update(E3)

				A4 = FluxLines[data]
				B4 = depfileData[A4]
				C4 = float(B4[WhereDataStart:WhereDataEnd]) * SerpentDepletionEnd * 24 * 3600
				D4 = CellNames[data] + "_dep_" + str(step+1) + "_"
				E4 = {D4 : C4}
		
				FLUENCE.append(C4)
				FLUENCEd.update(E4)

				StepFlux += C2
				AverageFlux.append(StepFlux / Cells / CellVolume / 1e14)

		PeakFluence = max(FLUENCE) / CellVolume / 1e23
		PeakFlux    = max(OneGroupFLUX) / CellVolume / 1e14
		AverageFlux = sum(AverageFlux)/len(AverageFlux)

		RadDepPowers = {}
	
		for step in range(SerpentDepletionSteps):
	
			TotPower = 0
			TotFlux  = 0
			TotFXS = 0
			Powers   = []
			RadPowers = []
			RadFluxs  = []
			RadFXs = []

			for batch in range(Batches):
		
				BATch = "Batch" + str(batch+1)
				Dep = "_dep_" + str(step+1) + "_"
		
				RadPower = 0
				RadFlux  = 0
				RadXS = 0
		
				for k,v in OneGroupFISSXSd.items():
		
					if BATch in k and Dep in k:
		
						FissionXS = v
						Flux      = OneGroupFLUXd.get(k)
						AdensX    = Adensd.get(k)

						Power     = FissionXS * Flux * AdensX #* 203 * 1.6 * 1e-19
		
						TotPower += Power
						RadPower += Power
						RadFlux  += Flux
						TotFlux  += Flux
						RadXS    += v
						TotFXS   += v
		
						Powers.append(Power)

				X = "Batch" + str(batch+1) + "_dep" + str(step+1) + "_"
				RDP = {X : RadPower}
				RadDepPowers.update(RDP)

				RadFluxs.append(RadFlux)
				RadFXs.append(RadXS)

		DepPow = {}

		for step in range(SerpentDepletionSteps):

			Q = 0

			for batch in range(Batches):
				
				X = "Batch" + str(batch+1) + "_dep" + str(step+1) + "_"
				A = RadDepPowers.get(X)

				Q += A

			BP = {step : Q}
			DepPow.update(BP)

		RadDepPowers = collections.OrderedDict(sorted(RadDepPowers.items()))

		CoreRadii = [0]

		for item in SerpentCoreRadius:
		
			CoreRadii.append(item)

		BatchCenter = []

		for item in range(len(CoreRadii) -1):

			CenterPos = (CoreRadii[item] + CoreRadii[item+1])/2

			BatchCenter.append(CenterPos*100)

		BatchP2 = []

	MaxPowC = []

	for step in range(SerpentDepletionSteps):
	
		TotalStepPower = DepPow.get(step)
		AverageStepPower = TotalStepPower / Batches
		StepID = "_dep" + str(step+1) + "_"
	
		BatchP = 0
	
		Maxie = []
	
		for k,v in RadDepPowers.items():
	
			if StepID in k:
	
				BatchP += v
	
				Maxie.append(v/AverageStepPower)
				MaxPow = max(Maxie)
				MaxPowC.append(MaxPow)		

		if Plotting == "on":

			################################################################################################### //// ######## //// #######
			##################### Plot power profile ########################################################### //// ######## //// #######
			################################################################################################### //// ######## //// #######
			
			figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
			
			Ymin = 0
			Ymax = 1.10 * max(Maxie)
			
			Xmax = 100 * max(SerpentCoreRadius) * 1.05
			Xmin = 0
	
			ConX =  [0,BatchCenter[0]]
			ConY = [Maxie[0], Maxie[0]]
	
			Con2X = [BatchCenter[Batches-1], 100*SerpentCoreRadius[Batches-1]]
			Con2Y = [Maxie[Batches-1], Maxie[Batches-1]]
	
			Con3X = 100 * SerpentCoreRadius[Batches-1]
			Con3Y = Maxie[Batches-1]
	
			plot(BatchCenter, Maxie, 'bo', ConX, ConY,'s', Con2X, Con2Y, Con3X, Con3Y, 's', BatchCenter, Maxie, color="red", linewidth=0.5, linestyle="-")
	
			#plot([Xpeak,Xpeak],[Ymin,Ypeak], color ='red', linewidth=2.5, linestyle="--")
			#scatter([Xpeak,],[Ypeak,], 50, color ='red')
	
			ylim(Ymin, Ymax)
			xlim(Xmin, Xmax)
			
			xlabel("Radial distance from the center of the active core (cm)")
			ylabel("Local power / Average power")
			
			grid(True)
			
			savefig(plotpowerpath + "PowerProfile_dep" + str(step) + ".png",dpi=FigureDPI)
			
			close()

	RadialPowerPeaking = max(MaxPowC)	

	return(RadialPowerPeaking, PeakFlux, AverageFlux, PeakFluence)
