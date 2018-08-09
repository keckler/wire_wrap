import sys

def reyinf(Pitch, Diameter, CoolantAxialInteriorReynolds, CoolantAxialEdgeReynolds, CoolantAxialCornerReynolds, FuelLength, \
	       InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly):

	# Reynolds validity range of the friction correlation
	LowerReynoldsValidityRange = 50
	UpperReynoldsValidityRange = 1e6

	# P/D validity range of the friction correlation
	LowerPDValidityRange = 1.000
	UpperPDValidityRange = 1.420

	PD = Pitch/Diameter
	
	# Transitions of flow regimes
	LaminarReynolds   = 300 * 10 ** (1.7 * (Pitch / Diameter - 1))
	TurbulentReynolds = 10000 * 10 ** (0.7 * (Pitch / Diameter -1))

	#print(LaminarReynolds)
	#print(TurbulentReynolds)
	
	# Reynolds numbers in the channels below the core
	BelowCoreInteriorReynolds = CoolantAxialInteriorReynolds.get(-FuelLength/2)
	BelowCoreEdgeReynolds     = CoolantAxialEdgeReynolds.get(-FuelLength/2)
	BelowCoreCornerReynolds   = CoolantAxialCornerReynolds.get(-FuelLength/2)

	BundleAverageBelowCoreReynolds = (BelowCoreInteriorReynolds * InteriorChannelsPerAssembly + BelowCoreEdgeReynolds * EdgeChannelsPerAssembly + BelowCoreCornerReynolds * CornerChannelsPerAssembly) / (InteriorChannelsPerAssembly + EdgeChannelsPerAssembly + CornerChannelsPerAssembly)
		
	if BundleAverageBelowCoreReynolds < LaminarReynolds:

		FlowRegime = "Laminar"
	
	elif BundleAverageBelowCoreReynolds > LaminarReynolds and BundleAverageBelowCoreReynolds < TurbulentReynolds:
	
		FlowRegime = "Transition"
	
	else:

		FlowRegime = "Turbulent"

	# Reynolds numbers in the channels above the core
	AboveCoreInteriorReynolds = CoolantAxialInteriorReynolds.get(FuelLength/2)
	AboveCoreEdgeReynolds     = CoolantAxialEdgeReynolds.get(FuelLength/2)
	AboveCoreCornerReynolds   = CoolantAxialCornerReynolds.get(FuelLength/2)

	# Determine the minimum and maximum interior channel Reynolds number
	MinimumInteriorChannelReynolds = min(CoolantAxialInteriorReynolds.values())
	MaximumInteriorChannelReynolds = max(CoolantAxialInteriorReynolds.values())

	# Determine the minimum and maximum edge channel Reynolds number
	MinimumEdgeChannelReynolds     = min(CoolantAxialEdgeReynolds.values())
	MaximumEdgeChannelReynolds     = max(CoolantAxialEdgeReynolds.values())

	# Determine the minimum and maximum corner channel Reynolds number
	MinimumCornerChannelReynolds   = min(CoolantAxialCornerReynolds.values())
	MaximumCornerChannelReynolds   = max(CoolantAxialCornerReynolds.values())

	if BundleAverageBelowCoreReynolds < LowerReynoldsValidityRange:
	
		ct = open("results/Error.txt", 'a')
		x = "Reynolds number outside of validity range (lower)"
		ct.write(x)
		sys.exit(x)
	
	if BundleAverageBelowCoreReynolds > UpperReynoldsValidityRange:

		ct = open("results/Error.txt", 'a')
		x = "Interior channel Reynolds number outside of validity range (higher)"
		ct.write(x)
		sys.exit(x)

	if PD > UpperPDValidityRange:
	
		ct = open("results/Error.txt", 'a')
		x = "Pitch/Diameter is larger than fricton-factor validity range"
		ct.write(x)
		sys.exit(x)

	if PD < LowerPDValidityRange:
	
		ct = open("results/Error.txt", 'a')
		x = "Pitch/Diameter is smaller than fricton-factor validity range"
		ct.write(x)
		#sys.exit(x)
	
	return(LowerReynoldsValidityRange, UpperReynoldsValidityRange, LaminarReynolds, TurbulentReynolds, \
		   BelowCoreInteriorReynolds, BelowCoreEdgeReynolds, BelowCoreCornerReynolds, AboveCoreInteriorReynolds, \
		   AboveCoreEdgeReynolds, AboveCoreCornerReynolds, BundleAverageBelowCoreReynolds, FlowRegime)


def averagereyinf(Pitch, Diameter, CoolantAxialAverageInteriorReynolds, CoolantAxialAverageEdgeReynolds, CoolantAxialAverageCornerReynolds, FuelLength, \
	       InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly, RadialPowerPeaking):
	
	# Reynolds numbers in the channels below the core
	AverageBelowCoreInteriorReynolds = CoolantAxialAverageInteriorReynolds.get(-FuelLength/2)
	AverageBelowCoreEdgeReynolds     = CoolantAxialAverageEdgeReynolds.get(-FuelLength/2)
	AverageBelowCoreCornerReynolds   = CoolantAxialAverageCornerReynolds.get(-FuelLength/2)

	AverageBundleAverageBelowCoreReynolds = (AverageBelowCoreInteriorReynolds * InteriorChannelsPerAssembly + AverageBelowCoreEdgeReynolds * EdgeChannelsPerAssembly + AverageBelowCoreCornerReynolds * CornerChannelsPerAssembly) / (InteriorChannelsPerAssembly + EdgeChannelsPerAssembly + CornerChannelsPerAssembly)

	# Reynolds numbers in the channels above the core
	AverageAboveCoreInteriorReynolds = CoolantAxialAverageInteriorReynolds.get(FuelLength/2)
	AverageAboveCoreEdgeReynolds     = CoolantAxialAverageEdgeReynolds.get(FuelLength/2)
	AverageAboveCoreCornerReynolds   = CoolantAxialAverageCornerReynolds.get(FuelLength/2)
	
	return(AverageBelowCoreInteriorReynolds, AverageBelowCoreEdgeReynolds, AverageBelowCoreCornerReynolds, AverageAboveCoreInteriorReynolds, \
		   AverageAboveCoreEdgeReynolds, AverageAboveCoreCornerReynolds, AverageBundleAverageBelowCoreReynolds)

def decnatreyinf(Pitch, Diameter, CoolantDecNatAxialInteriorReynolds, CoolantDecNatAxialEdgeReynolds, CoolantDecNatAxialCornerReynolds, FuelLength, \
	             InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly):

	# Reynolds validity range of the friction correlation
	LowerReynoldsValidityRange = 50
	UpperReynoldsValidityRange = 1e6

	# P/D validity range of the friction correlation
	LowerPDValidityRange = 1.000
	UpperPDValidityRange = 1.420

	PD = Pitch/Diameter
	
	# Transitions of flow regimes
	LaminarReynolds   = 300 * 10 ** (1.7 * (Pitch / Diameter - 1))
	TurbulentReynolds = 10000 * 10 ** (0.7 * (Pitch / Diameter -1))
	
	# Reynolds numbers in the channels below the core
	BelowCoreDecNatInteriorReynolds = CoolantDecNatAxialInteriorReynolds.get(-FuelLength/2)
	BelowCoreDecNatEdgeReynolds     = CoolantDecNatAxialEdgeReynolds.get(-FuelLength/2)
	BelowCoreDecNatCornerReynolds   = CoolantDecNatAxialCornerReynolds.get(-FuelLength/2)

	BundleAverageDecNatBelowCoreReynolds = (BelowCoreDecNatInteriorReynolds * InteriorChannelsPerAssembly + BelowCoreDecNatEdgeReynolds * EdgeChannelsPerAssembly + BelowCoreDecNatCornerReynolds * CornerChannelsPerAssembly) / (InteriorChannelsPerAssembly + EdgeChannelsPerAssembly + CornerChannelsPerAssembly)
		
	if BundleAverageDecNatBelowCoreReynolds < LaminarReynolds:

		FlowRegimeDecNat = "Laminar"
	
	elif BundleAverageDecNatBelowCoreReynolds > LaminarReynolds and BundleAverageDecNatBelowCoreReynolds < TurbulentReynolds:
	
		FlowRegimeDecNat = "Transition"
	
	else:

		FlowRegimeDecNat = "Turbulent"

	# Reynolds numbers in the channels above the core
	AboveCoreDecNatInteriorReynolds = CoolantDecNatAxialInteriorReynolds.get(FuelLength/2)
	AboveCoreDecNatEdgeReynolds     = CoolantDecNatAxialEdgeReynolds.get(FuelLength/2)
	AboveCoreDecNatCornerReynolds   = CoolantDecNatAxialCornerReynolds.get(FuelLength/2)

	# Determine the minimum and maximum interior channel Reynolds number
	MinimumInteriorChannelReynolds = min(CoolantDecNatAxialInteriorReynolds.values())
	MaximumInteriorChannelReynolds = max(CoolantDecNatAxialInteriorReynolds.values())

	# Determine the minimum and maximum edge channel Reynolds number
	MinimumEdgeChannelReynolds     = min(CoolantDecNatAxialEdgeReynolds.values())
	MaximumEdgeChannelReynolds     = max(CoolantDecNatAxialEdgeReynolds.values())

	# Determine the minimum and maximum corner channel Reynolds number
	MinimumCornerChannelReynolds   = min(CoolantDecNatAxialCornerReynolds.values())
	MaximumCornerChannelReynolds   = max(CoolantDecNatAxialCornerReynolds.values())

	if BundleAverageDecNatBelowCoreReynolds < LowerReynoldsValidityRange:
	
		ct = open("results/Error.txt", 'a')
		x = "Reynolds number outside of validity range (lower)"
		ct.write(x)
		sys.exit(x)
	
	if BundleAverageDecNatBelowCoreReynolds > UpperReynoldsValidityRange:

		ct = open("results/Error.txt", 'a')
		x = "Interior channel Reynolds number outside of validity range (higher)"
		ct.write(x)
		sys.exit(x)

	if PD > UpperPDValidityRange:
	
		ct = open("results/Error.txt", 'a')
		x = "Pitch/Diameter is larger than fricton-factor validity range"
		ct.write(x)
		sys.exit(x)

	if PD < LowerPDValidityRange:
	
		ct = open("results/Error.txt", 'a')
		x = "Pitch/Diameter is smaller than fricton-factor validity range"
		ct.write(x)
		#sys.exit(x)
	
	return(BelowCoreDecNatInteriorReynolds, BelowCoreDecNatEdgeReynolds, BelowCoreDecNatCornerReynolds, AboveCoreDecNatInteriorReynolds, \
		   AboveCoreDecNatEdgeReynolds, AboveCoreDecNatCornerReynolds, BundleAverageDecNatBelowCoreReynolds, FlowRegimeDecNat)	
