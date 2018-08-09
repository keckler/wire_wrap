import math

def energydetector(Name, LowerGridDPA, InnerLowerGridPlateVolume, CladdingDPA, SerpentAxialZones):

	EnergyGroups = [
	"1.00E-30",
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
	
	AA = Name + "_dpa"

	a = open(AA, 'w')

	a.write("\n")
	a.write("% Energy detector structure for DPA-calculation\n")
	a.write("\n")
	a.write(EnergyDetector)
	a.write("\n")
	
	for line in EnergyGroups:
	
		a.write(line + " \n")
	
	a.write("\n")

	if LowerGridDPA == "on":

		a.write("% Detector for center of the lower grid plate flux \n")	
		AA = "det lowergridplateflux dc lowergridplatecellinner de dpa"#dv " + str(InnerLowerGridPlateVolume) + "\n"
		#AA = "det name dm fuelmat_ax1_batch1 de dpa"
		a.write(AA)
		a.write("\n")

	if CladdingDPA == "on":

		for i in range(SerpentAxialZones):

			a.write("% Detector for center of the lower grid plate flux \n")	
			AA = "det claddingflux" + str(i+1) + " dm corecladdingmat_ax" + str(i+1) + "_batch1 de dpa"#dv " + str(InnerLowerGridPlateVolume) + "\n"
			#AA = "det name dm fuelmat_ax1_batch1 de dpa"
			a.write(AA)
			a.write("\n")	

	a.close()	

def calculatepa(Name, Where, InnerLowerGridPlateVolume, CycleTime, LowerGridPlateSteel, CladdingDPA, Cladding, FuelLength,
				SerpentAxialZones, CladdingOuterRadius, CladdingInnerRadius, PinPerAssembly,x):

	AA = "results/" + Name + "/CoreInfo_dpa_" + str(x) + ".txt"
	a = open(AA, 'w')

	##################################################### //// ######## //// #######
	#####################  User settings          ####### //// ######## //// #######
	##################################################### //// ######## //// #######
	
	DetectorFile = Name + "_geometry_reference_det0.m" # Path to the detector .m-file

	print(CladdingInnerRadius*100)
	print(CladdingOuterRadius*100)

	CladdingArea   = math.pi * ((CladdingOuterRadius*100) ** 2) - math.pi * ((CladdingInnerRadius*100) ** 2) # cm^2
	CladdingLength = FuelLength * 100 / SerpentAxialZones # cm
	CladdingVolume = CladdingArea * CladdingLength * PinPerAssembly # cm^3

	print(CladdingArea)
	print(CladdingLength)
	print(CladdingVolume)

	if Where == "LowerGridDPA":

		DetectorName = "lowergridplateflux" # Name of your detector in the detector file
		CellVolume   = InnerLowerGridPlateVolume # In cm^3
		Material     = LowerGridPlateSteel     # HT9 / SiC / D9 / FeCrAl		

	elif Where == "CladdingDPA":

		DetectorName = []

		for i in range(SerpentAxialZones):

			DetectorName.append("claddingflux" + str(i+1))

		CellVolume   = CladdingVolume
		Material     = Cladding

	print(DetectorName)

	ExposureTime = CycleTime * 24 * 60 * 60  # In seconds

	print(CladdingVolume)
	
	##################################################### //// ######## //// #######
	#####################  DPA-calc               ####### //// ######## //// #######
	##################################################### //// ######## //// #######
	
	CellNames = ["cell"] # Dummy name 
	
	if Material == "HT9":
	
		IronMF       = 84.55/100
		ChromiumMF   = 12/100
		CarbonMF     = 0.2/100
		MolybdenumMF = 1/100
		SiliconMF    = 0.4/100
		WolframMF    = 0.5/100
		VanadiumMF   = 0.25/100
		ManganeseMF  = 0.6/100
		NickelMF     = 0.5/100
		AluminiumMF  = 0
	
	elif Material == "SiC":
	
		IronMF       = 0
		ChromiumMF   = 0
		CarbonMF     = 30/100
		MolybdenumMF = 0
		SiliconMF    = 70/100
		WolframMF    = 0
		VanadiumMF   = 0
		ManganeseMF  = 0
		NickelMF     = 0
		AluminiumMF  = 0
	
	elif Material == "D9":
	
		IronMF       = 65.87/100
		ChromiumMF   = 15.10/100
		CarbonMF     = 0.09/100
		MolybdenumMF = 1.22/100
		SiliconMF    = 0.44/100
		WolframMF    = 0
		VanadiumMF   = 0
		ManganeseMF  = 1.8/100
		NickelMF     = 14.96/100
		AluminiumMF  = 0
	
	elif Material == "FeCrAl":
	
		IronMF       = 70.70/100
		AluminiumMF  = 5.800/100
		ChromiumMF   = 23.50/100
		SiliconMF    = 0
		CarbonMF     = 0
		MolybdenumMF = 0
		WolframMF    = 0
		VanadiumMF   = 0
		ManganeseMF  = 0
		NickelMF     = 0
	
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
	
	Aluminium = [17.78,
	5.63,
	2.96,
	1.93,
	1.48,
	1.19,
	1.04,
	0.74,
	0.59,
	0.59,
	0.44,
	0.30,
	0.30,
	0.30,
	0.15,
	0.15,
	0.15,
	0.15,
	0.15,
	0.00,
	0.00,
	0.00,
	0.00,
	0.00,
	0.00,
	0.00,
	0.30,
	0.44,
	0.74,
	0.74,
	0.89,
	1.04,
	1.33,
	1.63,
	2.07,
	2.67,
	3.41,
	4.30,
	5.48,
	13.04,
	8.59,
	10.37,
	12.44,
	12.15,
	11.85,
	33.48,
	485.93,
	121.48,
	78.07,
	362.22,
	520.74,
	269.48,
	910.37,
	524.30,
	635.70,
	466.81,
	509.63,
	853.19,
	540.30,
	766.81,
	1010.22,
	942.96,
	1015.11,
	1051.11,
	1098.07,
	941.63,
	1198.07,
	1470.07,
	1239.11,
	1041.04,
	1301.04,
	1282.07,
	1483.11,
	1540.15,
	1548.15,
	1812.15,
	1695.11,
	1752.15,
	1820.15,
	1863.11,
	1910.07,
	1877.19,
	1915.11,
	1999.11,
	2026.22,
	2067.26,
	2067.41,
	2123.56,
	2135.85,
	2160.15,
	2251.41,
	2378.81,
	2498.22,
	2558.67,
	2623.26,
	2672.89,
	2692.89,
	2696.74,
	2684.89,
	2665.04]
	
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
	
	if Where == "LowerGridDPA":

		# COLLECT GROUP-WISE FLUX AND FLUENCE -------------------------------------------------------------
		
		detfiledata = []
		i = 0
		ic = []
		totalzones = len(CellNames)
		
		with open(DetectorFile, 'r', encoding='utf-8') as results:
		
			for line in results:
		
				detfiledata.append(line)
				i += 1
		
				for zone in range(totalzones):
		
					detectorname = DetectorName + " = ["
		
					if detectorname in line:
		
						ic.append(i)	
		
		GroupedFlux        = {}
		GroupedFluence     = {}
		SumFluxZone        = {}
		SumFluenceZone     = {}
		SumFastFluxZone    = {}
		SumFastFluenceZone = {}
		
		BuSeconds = ExposureTime
		Groups = 99
		
		PeakGFluence = []
		
		for zone in range(totalzones):
		
			FluxCollect = []
			FluenceCollect = []
		
			for x in range(Groups):
			
				row = ic[zone] + x
		
				X0 = detfiledata[row+1][52:63]
				X1 = float(X0)
				A  = X1/CellVolume
				AA = A * BuSeconds
		
				FluxCollect.append(A)
				FluenceCollect.append(AA)
		
			SumFlux    = sum(FluxCollect)
			SumFluence = sum(FluenceCollect)
		
			SumFastFlux    = sum(FluxCollect[53:100])
			SumFastFluence = sum(FluenceCollect[53:100])
		
			PeakGFluence.append(SumFastFluence)
		
			GFLX = {CellNames[zone] : FluxCollect}
			GFLE = {CellNames[zone] : FluenceCollect}
		
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
		
		RelFlux = []
		
		for item in FluxCollect:
		
			A = item/SumFlux
			RelFlux.append(A)
		
		PeakFastFluence = max(PeakGFluence)
		
		# CALCULATE 1-GROUP DPA ---------------------------------------------------------------------------
		
		Iron1G        = []
		Chromium1G    = []
		Carbon1G      = []
		Molybdenum1G  = []
		Silicon1G     = []
		Wolfram1G     = []
		Vanadium1G    = []
		Manganese1G   = []
		Nickel1G      = []
		Aluminium1G   = []
		
		for i in range(Groups):
		
			Iron1G.append(Iron[i]             * RelFlux[i])
			Chromium1G.append(Chromium[i]     * RelFlux[i])
			Carbon1G.append(Carbon[i]         * RelFlux[i])
			Molybdenum1G.append(Molybdenum[i] * RelFlux[i])
			Silicon1G.append(Silicon[i]       * RelFlux[i])
			Wolfram1G.append(Wolfram[i]       * RelFlux[i])
			Vanadium1G.append(Vanadium[i]     * RelFlux[i])
			Manganese1G.append(Manganese[i]   * RelFlux[i])
			Nickel1G.append(Nickel[i]         * RelFlux[i])
			Aluminium1G.append(Aluminium[i]   * RelFlux[i])
		
		XS_Fe = sum(Iron1G)
		XS_Cr = sum(Chromium1G)
		XS_C  = sum(Carbon1G)
		XS_Mo = sum(Molybdenum1G)
		XS_Si = sum(Silicon1G)
		XS_W  = sum(Wolfram1G)
		XS_V  = sum(Vanadium1G)
		XS_Mn = sum(Manganese1G)
		XS_Ni = sum(Nickel1G)
		XS_Al = sum(Aluminium1G)
		
		IronSum       = XS_Fe * IronMF
		ChromiumSum   = XS_Cr * ChromiumMF
		CarbonSum     = XS_C  * CarbonMF
		MolybdenumSum = XS_Mo * MolybdenumMF
		SiliconSum    = XS_Si * SiliconMF
		WolframSum    = XS_W  * WolframMF
		VanadiumSum   = XS_V  * VanadiumMF
		ManganeseSum  = XS_Mn * ManganeseMF
		NickelSum     = XS_Ni * NickelMF
		AluminiumSum  = XS_Al * AluminiumMF
		
		DPAXSsum = IronSum + ChromiumSum + CarbonSum + MolybdenumSum + SiliconSum + WolframSum + VanadiumSum + ManganeseSum + NickelSum
		
		Iron1G        = []
		Chromium1G    = []
		Carbon1G      = []
		Molybdenum1G  = []
		Silicon1G     = []
		Wolfram1G     = []
		Vanadium1G    = []
		Manganese1G   = []
		Nickel1G      = []
		Aluminium1G   = []
		
		for i in range(Groups):
		
			Iron1G.append(Iron[i]             * FluenceCollect[i] * 1e-24)
			Chromium1G.append(Chromium[i]     * FluenceCollect[i] * 1e-24)
			Carbon1G.append(Carbon[i]         * FluenceCollect[i] * 1e-24)
			Molybdenum1G.append(Molybdenum[i] * FluenceCollect[i] * 1e-24)
			Silicon1G.append(Silicon[i]       * FluenceCollect[i] * 1e-24)
			Wolfram1G.append(Wolfram[i]       * FluenceCollect[i] * 1e-24)
			Vanadium1G.append(Vanadium[i]     * FluenceCollect[i] * 1e-24)
			Manganese1G.append(Manganese[i]   * FluenceCollect[i] * 1e-24)
			Nickel1G.append(Nickel[i]         * FluenceCollect[i] * 1e-24)
			Aluminium1G.append(Aluminium[i]   * FluenceCollect[i] * 1e-24)
		
		IronSum       = sum(Iron1G)       * IronMF
		ChromiumSum   = sum(Chromium1G)   * ChromiumMF
		CarbonSum     = sum(Carbon1G)     * CarbonMF
		MolybdenumSum = sum(Molybdenum1G) * MolybdenumMF
		SiliconSum    = sum(Silicon1G)    * SiliconMF
		WolframSum    = sum(Wolfram1G)    * WolframMF
		VanadiumSum   = sum(Vanadium1G)   * VanadiumMF
		ManganeseSum  = sum(Manganese1G)  * ManganeseMF
		NickelSum     = sum(Nickel1G)     * NickelMF
		AluminiumSum  = sum(Aluminium1G)  * AluminiumMF
		
		DPA = IronSum + ChromiumSum + CarbonSum + MolybdenumSum + SiliconSum + WolframSum + VanadiumSum + ManganeseSum + NickelSum

		a.write("\n")
		a.write("Lower grid plate DPA information\n")
		a.write("--------------------------------\n")
		a.write("\n")		
		a.write("The cumulative peak fast fluence in the grid plate is: {0:02.3e}".format(PeakFastFluence) + " n/cm^2 \n")
		a.write("The 1-group DPA cross-section for the grid plate is: {0:02.1f}".format(DPAXSsum) + " barns \n")
		a.write("The peak dpa in the grid plate is: {0:02.2f}".format(DPA) + "\n")
		a.write("\n")

	elif Where == "CladdingDPA":

		for q in range(len(DetectorName)):

			Dname = DetectorName[q]

			print(Dname)

			# COLLECT GROUP-WISE FLUX AND FLUENCE -------------------------------------------------------------
			
			detfiledata = []
			i = 0
			ic = []
			totalzones = len(CellNames)
			
			with open(DetectorFile, 'r', encoding='utf-8') as results:
			
				for line in results:
			
					detfiledata.append(line)
					i += 1
			
					detectorname = Dname + " = ["
			
					if detectorname in line:
			
						ic.append(i)	
			
			GroupedFlux        = {}
			GroupedFluence     = {}
			SumFluxZone        = {}
			SumFluenceZone     = {}
			SumFastFluxZone    = {}
			SumFastFluenceZone = {}
			
			BuSeconds = ExposureTime
			Groups = 99
			
			PeakGFluence = []
			
			for zone in range(totalzones):
			
				FluxCollect = []
				FluenceCollect = []
			
				for x in range(Groups):
				
					row = ic[zone] + x
			
					X0 = detfiledata[row+1][52:63]
					X1 = float(X0)
					A  = X1/CellVolume
					AA = A * BuSeconds
			
					FluxCollect.append(A)
					FluenceCollect.append(AA)
			
				SumFlux    = sum(FluxCollect)
				SumFluence = sum(FluenceCollect)
			
				SumFastFlux    = sum(FluxCollect[53:100])
				SumFastFluence = sum(FluenceCollect[53:100])
			
				PeakGFluence.append(SumFastFluence)
			
				GFLX = {CellNames[zone] : FluxCollect}
				GFLE = {CellNames[zone] : FluenceCollect}
			
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
			
			RelFlux = []
			
			for item in FluxCollect:
			
				A = item/SumFlux
				RelFlux.append(A)
			
			PeakFastFluence = max(PeakGFluence)
			
			# CALCULATE 1-GROUP DPA ---------------------------------------------------------------------------
			
			Iron1G        = []
			Chromium1G    = []
			Carbon1G      = []
			Molybdenum1G  = []
			Silicon1G     = []
			Wolfram1G     = []
			Vanadium1G    = []
			Manganese1G   = []
			Nickel1G      = []
			Aluminium1G   = []
			
			for i in range(Groups):
			
				Iron1G.append(Iron[i]             * RelFlux[i])
				Chromium1G.append(Chromium[i]     * RelFlux[i])
				Carbon1G.append(Carbon[i]         * RelFlux[i])
				Molybdenum1G.append(Molybdenum[i] * RelFlux[i])
				Silicon1G.append(Silicon[i]       * RelFlux[i])
				Wolfram1G.append(Wolfram[i]       * RelFlux[i])
				Vanadium1G.append(Vanadium[i]     * RelFlux[i])
				Manganese1G.append(Manganese[i]   * RelFlux[i])
				Nickel1G.append(Nickel[i]         * RelFlux[i])
				Aluminium1G.append(Aluminium[i]   * RelFlux[i])
			
			XS_Fe = sum(Iron1G)
			XS_Cr = sum(Chromium1G)
			XS_C  = sum(Carbon1G)
			XS_Mo = sum(Molybdenum1G)
			XS_Si = sum(Silicon1G)
			XS_W  = sum(Wolfram1G)
			XS_V  = sum(Vanadium1G)
			XS_Mn = sum(Manganese1G)
			XS_Ni = sum(Nickel1G)
			XS_Al = sum(Aluminium1G)
			
			IronSum       = XS_Fe * IronMF
			ChromiumSum   = XS_Cr * ChromiumMF
			CarbonSum     = XS_C  * CarbonMF
			MolybdenumSum = XS_Mo * MolybdenumMF
			SiliconSum    = XS_Si * SiliconMF
			WolframSum    = XS_W  * WolframMF
			VanadiumSum   = XS_V  * VanadiumMF
			ManganeseSum  = XS_Mn * ManganeseMF
			NickelSum     = XS_Ni * NickelMF
			AluminiumSum  = XS_Al * AluminiumMF
			
			DPAXSsum = IronSum + ChromiumSum + CarbonSum + MolybdenumSum + SiliconSum + WolframSum + VanadiumSum + ManganeseSum + NickelSum
			
			Iron1G        = []
			Chromium1G    = []
			Carbon1G      = []
			Molybdenum1G  = []
			Silicon1G     = []
			Wolfram1G     = []
			Vanadium1G    = []
			Manganese1G   = []
			Nickel1G      = []
			Aluminium1G   = []
			
			for i in range(Groups):
			
				Iron1G.append(Iron[i]             * FluenceCollect[i] * 1e-24)
				Chromium1G.append(Chromium[i]     * FluenceCollect[i] * 1e-24)
				Carbon1G.append(Carbon[i]         * FluenceCollect[i] * 1e-24)
				Molybdenum1G.append(Molybdenum[i] * FluenceCollect[i] * 1e-24)
				Silicon1G.append(Silicon[i]       * FluenceCollect[i] * 1e-24)
				Wolfram1G.append(Wolfram[i]       * FluenceCollect[i] * 1e-24)
				Vanadium1G.append(Vanadium[i]     * FluenceCollect[i] * 1e-24)
				Manganese1G.append(Manganese[i]   * FluenceCollect[i] * 1e-24)
				Nickel1G.append(Nickel[i]         * FluenceCollect[i] * 1e-24)
				Aluminium1G.append(Aluminium[i]   * FluenceCollect[i] * 1e-24)
			
			IronSum       = sum(Iron1G)       * IronMF
			ChromiumSum   = sum(Chromium1G)   * ChromiumMF
			CarbonSum     = sum(Carbon1G)     * CarbonMF
			MolybdenumSum = sum(Molybdenum1G) * MolybdenumMF
			SiliconSum    = sum(Silicon1G)    * SiliconMF
			WolframSum    = sum(Wolfram1G)    * WolframMF
			VanadiumSum   = sum(Vanadium1G)   * VanadiumMF
			ManganeseSum  = sum(Manganese1G)  * ManganeseMF
			NickelSum     = sum(Nickel1G)     * NickelMF
			AluminiumSum  = sum(Aluminium1G)  * AluminiumMF
			
			DPA = IronSum + ChromiumSum + CarbonSum + MolybdenumSum + SiliconSum + WolframSum + VanadiumSum + ManganeseSum + NickelSum		

			a.write("\n")
			a.write("Cladding DPA information, axial zone " + str(q+1) + "/" + str(SerpentAxialZones) + " \n")
			a.write("--------------------------------------------\n")
			a.write("\n")		
			a.write("The cumulative peak fast fluence in the cladding is: {0:02.3e}".format(PeakFastFluence) + " n/cm^2 \n")
			a.write("The 1-group DPA cross-section for the cladding is: {0:02.1f}".format(DPAXSsum) + " barns \n")
			a.write("The peak dpa in the cladding is: {0:02.2f}".format(DPA) + "\n")
			a.write("\n")
	
	a.close()

