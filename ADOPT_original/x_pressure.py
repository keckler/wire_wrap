# -*- coding: UTF-8 -*-

import math

def flowsplit(BareSingleInteriorChannelFlowArea,SingleInteriorChannelFlowArea,BareSingleInteriorChannelWettedPerimeter,
              SingleInteriorChannelWettedPerimeter,BareSingleInteriorChannelHydraulicDiameter,
              SingleInteriorChannelHydraulicDiameter,BelowCoreInteriorReynolds,LaminarReynolds, Pitch, Diameter,
              BelowCoreChannelLength, AverageCoolantVelocity, CoolantInletDensity, SingleInteriorChannelProjectedWireArea,
              WireDiameter, WirePitch, BundleAverageBelowCoreReynolds, RelativeWirePitch,  SingleEdgeChannelProjectedWireArea, 
              BareSingleEdgeChannelFlowArea, SingleCornerChannelProjectedWireArea, BareSingleCornerChannelFlowArea, 
              SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, S1, S2, S3, SingleAverageHydraulicDiameter,
              SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, InteriorChannelsPerAssembly,
			  EdgeChannelsPerAssembly, CornerChannelsPerAssembly, ChannelsPerAssembly):

	# The cos-theta factor describing the angle of the wire compared to the rod
	CT = WirePitch * (WirePitch ** 2 + math.pi ** 2 * (Diameter + WireDiameter) ** 2) ** (-0.1e1 / 0.2e1)

	# The angle itself (in radians)
	WireAngle = math.acos(CT)

	# Check
	if BundleAverageBelowCoreReynolds < LaminarReynolds:
	
		m = 1
		WireDrag           = (41.3 - 196.0 * (WireDiameter/Diameter) + 561.0 * (WireDiameter/Diameter) ** 2 ) * (WirePitch/Diameter) ** (-0.85)
		EdgeWireSweeping   = 0.3 * (20.0 * math.log10(RelativeWirePitch) - 7.0)
		CornerWireSweeping = 0.3 * (20.0 * math.log10(RelativeWirePitch) - 7.0)

		if Pitch/Diameter < 1.1:
	
			ai =  26.00
			bi =  888.2
			ci = -3334.0

			ae =  26.18
			be =  554.5
			ce = -1480.0

			ac =  26.98
			bc =  1636.0
			cc = -10050.0
	
		else:
	
			ai =  62.97
			bi =  216.9
			ci = -190.2

			ae =  44.40
			be =  256.7
			ce = -267.6

			ac =  87.26
			bc =  38.59
			cc = -55.12

	else:
	
		m = 0.18

		WireDrag           = (29.5 - 140 * (WireDiameter/Diameter) + 401.0 * (WireDiameter/Diameter) ** 2 ) * (WirePitch/Diameter) ** (-0.85)
		EdgeWireSweeping   = 20.0 * math.log10(RelativeWirePitch) - 7.0
		CornerWireSweeping = 20.0 * math.log10(RelativeWirePitch) - 7.0


		if Pitch/Diameter < 1.1:
	
			ai =  0.09378
			bi =  1.398
			ci = -8.664

			ae =  0.09377
			be =  0.8732
			ce = -3.341

			ac =  0.1004
			bc =  1.625
			cc = -11.85
	
		else:
	
			ai =  0.1458
			bi =  0.03632
			ci = -0.03333

			ae =  0.1430
			be =  0.04199
			ce = -0.04428

			ac =  0.1499
			bc =  0.006706
			cc = -0.009567

	InteriorChannelBareFrictionMultiplier = ai + bi * (Pitch / Diameter - 1) + ci * (Pitch / Diameter - 1) ** 2
	EdgeChannelBareFrictionMultiplier     = ae + be * (Pitch / Diameter - 1) + ce * (Pitch / Diameter - 1) ** 2
	CornerChannelBareFrictionMultiplier   = ac + bc * (Pitch / Diameter - 1) + cc * (Pitch / Diameter - 1) ** 2

	# INTERIOR
	F1i = InteriorChannelBareFrictionMultiplier * (BareSingleInteriorChannelWettedPerimeter/SingleInteriorChannelWettedPerimeter) 
	F2i = (3 * SingleInteriorChannelProjectedWireArea/BareSingleInteriorChannelFlowArea)
	F3i = (SingleInteriorChannelHydraulicDiameter/WirePitch)
	F4i = (SingleInteriorChannelHydraulicDiameter/WireDiameter) 
	F5i = WireDrag * F2i * F3i * F4i ** m

	Cf1 = F1i + F5i

	t = (3-m)/2

	# EDGE
	F1e = EdgeWireSweeping * (SingleEdgeChannelProjectedWireArea/BareSingleEdgeChannelFlowArea) * (math.tan(WireAngle) ** 2)
	Cf2 = EdgeChannelBareFrictionMultiplier * ((1 + F1e) ** t)
    
	# CORNER
	F1c = CornerWireSweeping * (SingleCornerChannelProjectedWireArea/BareSingleCornerChannelFlowArea) * (math.tan(WireAngle) ** 2)
	Cf3 = CornerChannelBareFrictionMultiplier * ((1 + F1c) ** t)

	y = (1+m)/(2-m)
	x = 1/(2-m)

    ## Flow split between interior and egde channels
	X1X2 = ((SingleInteriorChannelHydraulicDiameter/SingleEdgeChannelHydraulicDiameter) ** y) * ((Cf2/Cf1) ** x)

    ## Flow split between corner and edge channels
	X3X2 = ((SingleCornerChannelHydraulicDiameter/SingleEdgeChannelHydraulicDiameter) ** y) * ((Cf2/Cf3) ** x)

	## Bundle flow distribution
	X2 = 1/(S2 + X1X2 * S1 + X3X2 * S3)
	X1 = X1X2 * X2
	X3 = X3X2 * X2

	X1 = X1.real
	X2 = X2.real
	X3 = X3.real

	## Resulting channel coolant velocities
	InteriorChannelCoolantVelocity = X1 * AverageCoolantVelocity	
	EdgeChannelCoolantVelocity     = X2 * AverageCoolantVelocity	
	CornerChannelCoolantVelocity   = X3 * AverageCoolantVelocity	

	## Define the peak constraining bundle velocity
	Velocities = [InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity]
	CalculatedPeakCoolantVelocity = max(Velocities)

	return(InteriorChannelCoolantVelocity, EdgeChannelCoolantVelocity, CornerChannelCoolantVelocity, CalculatedPeakCoolantVelocity, \
		   Cf1, Cf2, Cf3, X1, X2, X3, BundleAverageBelowCoreReynolds)

def channelpressuredrop(Cf1,Cf2,Cf3,InteriorChannelCoolantVelocity,EdgeChannelCoolantVelocity,CornerChannelCoolantVelocity, BelowCoreInteriorReynolds,
	             BelowCoreEdgeReynolds, BelowCoreCornerReynolds, CoolantAxialInteriorReynolds, CoolantAxialEdgeReynolds, CoolantAxialCornerReynolds,
	             FuelLength, BelowCoreChannelLength, AboveCoreChannelLength, FlowRegime, TemperaturePoints, CoolantAxialDensity, CoolantAxialKinematicViscosity, \
	             CoolantInletDensity,SingleInteriorChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter):

	BundleChannelLength = BelowCoreChannelLength + FuelLength + AboveCoreChannelLength

	if FlowRegime == "Laminar":

		m = 1

	else:
	
		m = 0.18	

	InteriorChannelFrictionFactor = Cf1/BelowCoreInteriorReynolds ** m
	EdgeChannelFrictionFactor     = Cf2/BelowCoreEdgeReynolds ** m
	CornerChannelFrictionFactor   = Cf3/BelowCoreCornerReynolds ** m

	InteriorChannelPressureDrop = (0.5 * InteriorChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * InteriorChannelCoolantVelocity ** 2)	/ SingleInteriorChannelHydraulicDiameter
	EdgeChannelPressureDrop     = (0.5 * EdgeChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * EdgeChannelCoolantVelocity ** 2)	/ SingleEdgeChannelHydraulicDiameter
	CornerChannelPressureDrop   = (0.5 * CornerChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * CornerChannelCoolantVelocity ** 2)	/ SingleCornerChannelHydraulicDiameter

	#AverageInteriorChannelPressureDrop = (0.5 * InteriorChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * (InteriorChannelCoolantVelocity/RadialPowerPeaking) ** 2)	/ SingleInteriorChannelHydraulicDiameter
	#AverageEdgeChannelPressureDrop     = (0.5 * EdgeChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * (EdgeChannelCoolantVelocity/RadialPowerPeaking) ** 2)	/ SingleEdgeChannelHydraulicDiameter
	#AverageCornerChannelPressureDrop   = (0.5 * CornerChannelFrictorFactor * BundleChannelLength * CoolantInletDensity * (CornerChannelCoolantVelocity/RadialPowerPeaking) ** 2)	/ SingleCornerChannelHydraulicDiameter

	ChannelPressureDrop = max([InteriorChannelPressureDrop, EdgeChannelPressureDrop, CornerChannelPressureDrop])	
	#AverageChannelPressureDrop = max([AverageInteriorChannelPressureDrop, AverageEdgeChannelPressureDrop, AverageCornerChannelPressureDrop])

	return(ChannelPressureDrop, InteriorChannelFrictionFactor, EdgeChannelFrictionFactor, CornerChannelFrictionFactor)


def averagechannelpressuredrop(Cf1,Cf2,Cf3,InteriorChannelCoolantVelocity,EdgeChannelCoolantVelocity,CornerChannelCoolantVelocity, AverageBelowCoreInteriorReynolds,
	                           AverageBelowCoreEdgeReynolds, AverageBelowCoreCornerReynolds, CoolantAxialAverageInteriorReynolds, CoolantAxialAverageEdgeReynolds, CoolantAxialAverageCornerReynolds,
	                           FuelLength, BelowCoreChannelLength, AboveCoreChannelLength, FlowRegime, TemperaturePoints, CoolantAxialDensity, CoolantAxialKinematicViscosity, \
	                           CoolantInletDensity,SingleInteriorChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, RadialPowerPeaking):

	BundleChannelLength = BelowCoreChannelLength + FuelLength + AboveCoreChannelLength

	if FlowRegime == "Laminar":

		m = 1

	else:
	
		m = 0.18	

	AverageInteriorChannelFrictionFactor = Cf1/AverageBelowCoreInteriorReynolds ** m
	AverageEdgeChannelFrictionFactor     = Cf2/AverageBelowCoreEdgeReynolds ** m
	AverageCornerChannelFrictionFactor   = Cf3/AverageBelowCoreCornerReynolds ** m

	AverageInteriorChannelPressureDrop = (0.5 * AverageInteriorChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * (InteriorChannelCoolantVelocity/RadialPowerPeaking) ** 2)	/ SingleInteriorChannelHydraulicDiameter
	AverageEdgeChannelPressureDrop     = (0.5 * AverageEdgeChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * (EdgeChannelCoolantVelocity/RadialPowerPeaking) ** 2)	/ SingleEdgeChannelHydraulicDiameter
	AverageCornerChannelPressureDrop   = (0.5 * AverageCornerChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * (CornerChannelCoolantVelocity/RadialPowerPeaking) ** 2)	/ SingleCornerChannelHydraulicDiameter

	AverageChannelPressureDrop = max([AverageInteriorChannelPressureDrop, AverageEdgeChannelPressureDrop, AverageCornerChannelPressureDrop])

	return(AverageChannelPressureDrop, AverageInteriorChannelFrictionFactor, AverageEdgeChannelFrictionFactor, AverageCornerChannelFrictionFactor)


def decnatflowsplit(BareSingleInteriorChannelFlowArea,SingleInteriorChannelFlowArea,BareSingleInteriorChannelWettedPerimeter,
                    SingleInteriorChannelWettedPerimeter,BareSingleInteriorChannelHydraulicDiameter,
                    SingleInteriorChannelHydraulicDiameter,BelowCoreDecNatInteriorReynolds,LaminarReynolds, Pitch, Diameter,
                    BelowCoreChannelLength, AverageDecNatCoolantVelocity, CoolantInletDensity, SingleInteriorChannelProjectedWireArea,
                    WireDiameter, WirePitch, BundleAverageDecNatBelowCoreReynolds, RelativeWirePitch,  SingleEdgeChannelProjectedWireArea, 
                    BareSingleEdgeChannelFlowArea, SingleCornerChannelProjectedWireArea, BareSingleCornerChannelFlowArea, 
                    SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea, S1, S2, S3, SingleAverageHydraulicDiameter,
                    SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, InteriorChannelsPerAssembly,
				    EdgeChannelsPerAssembly, CornerChannelsPerAssembly, ChannelsPerAssembly, FlowRegimeDecNat, TurbulentReynolds,
				    BelowCoreDecNatEdgeReynolds, BelowCoreDecNatCornerReynolds, BundleHydraulicDiameter):

	#print(LaminarReynolds)
	#print(TurbulentReynolds)

	# Nullified
	Cf1DecNat = 0
	Cf2DecNat = 0
	Cf3DecNat = 0

	# The cos-theta factor describing the angle of the wire compared to the rod
	CT = WirePitch * (WirePitch ** 2 + math.pi ** 2 * (Diameter + WireDiameter) ** 2) ** (-0.1e1 / 0.2e1)

	# The angle itself (in radians)
	WireAngle = math.acos(CT)

	# Wire-drag constants TURBULENT
	TWireDrag   = (29.5 - 140 * (WireDiameter/Diameter) + 401.0 * (WireDiameter/Diameter) ** 2 ) * (WirePitch/Diameter) ** (-0.85)
	TEdgeWireSweeping   = 20.0 * math.log10(RelativeWirePitch) - 7.0
	TCornerWireSweeping = TEdgeWireSweeping

	# Wire-drag constants LAMINAR
	LWireDrag           = 1.4 * TWireDrag
	LEdgeWireSweeping   = 0.3 * TEdgeWireSweeping
	LCornerWireSweeping = LEdgeWireSweeping

	# LAMINAR
	mlam = 1
	tlam = (3-mlam)/2
	ylam = (1+mlam)/(2-mlam)
	xlam = 1/(2-mlam)

	if Pitch/Diameter < 1.1:
	
		ail =  26.00
		bil =  888.2
		cil = -3334.0

		ael =  26.18
		bel =  554.5
		cel = -1480.0

		acl =  26.98
		bcl =  1636.0
		ccl = -10050.0
	
	else:
	
		ail =  62.97
		bil =  216.9
		cil = -190.2

		ael =  44.40
		bel =  256.7
		cel = -267.6

		acl =  87.26
		bcl =  38.59
		ccl = -55.12

	LaminarInteriorChannelBareFrictionMultiplier = ail + bil * (Pitch / Diameter - 1) + cil * (Pitch / Diameter - 1) ** 2
	LaminarEdgeChannelBareFrictionMultiplier     = ael + bel * (Pitch / Diameter - 1) + cel * (Pitch / Diameter - 1) ** 2
	LaminarCornerChannelBareFrictionMultiplier   = acl + bcl * (Pitch / Diameter - 1) + ccl * (Pitch / Diameter - 1) ** 2	

	# INTERIOR
	F1il = LaminarInteriorChannelBareFrictionMultiplier * (BareSingleInteriorChannelWettedPerimeter/SingleInteriorChannelWettedPerimeter) 
	F2il = (3 * SingleInteriorChannelProjectedWireArea/BareSingleInteriorChannelFlowArea)
	F3il = (SingleInteriorChannelHydraulicDiameter/WirePitch)
	F4il = (SingleInteriorChannelHydraulicDiameter/WireDiameter) 
	F5il = LWireDrag * F2il * F3il * F4il ** mlam
	Cf1l = F1il + F5il
	
	# EDGE
	F1el = LEdgeWireSweeping * (SingleEdgeChannelProjectedWireArea/BareSingleEdgeChannelFlowArea) * (math.tan(WireAngle) ** 2)
	Cf2l = LaminarEdgeChannelBareFrictionMultiplier * ((1 + F1el) ** tlam)
    
	# CORNER
	F1cl = LCornerWireSweeping * (SingleCornerChannelProjectedWireArea/BareSingleCornerChannelFlowArea) * (math.tan(WireAngle) ** 2)
	Cf3l = LaminarCornerChannelBareFrictionMultiplier * ((1 + F1cl) ** tlam)

    ## Flow split between interior and egde channels
	X1X2l = ((SingleInteriorChannelHydraulicDiameter/SingleEdgeChannelHydraulicDiameter) ** ylam) * ((Cf2l/Cf1l) ** xlam)

    ## Flow split between corner and edge channels
	X3X2l = ((SingleCornerChannelHydraulicDiameter/SingleEdgeChannelHydraulicDiameter) ** ylam) * ((Cf2l/Cf3l) ** xlam)

	## Laminar Bundle flow distribution
	X2l = 1/(S2 + X1X2l * S1 + X3X2l * S3)
	X1l = X1X2l * X2l
	X3l = X3X2l * X2l

	## TURBULENT
	mturb = 0.18
	tturb = (3-mturb)/2	
	yturb = (1+mturb)/(2-mturb)
	xturb = 1/(2-mturb)

	if Pitch/Diameter < 1.1:
	
		ait =  0.09378
		bit =  1.398
		cit = -8.664

		aet =  0.09377
		bet =  0.8732
		cet = -3.341

		act =  0.1004
		bct =  1.625
		cct = -11.85
	
	else:
	
		ait =  0.1458
		bit =  0.03632
		cit = -0.03333

		aet =  0.1430
		bet =  0.04199
		cet = -0.04428

		act =  0.1499
		bct =  0.006706
		cct = -0.009567

	TurbulentInteriorChannelBareFrictionMultiplier = ait + bit * (Pitch / Diameter - 1) + cit * (Pitch / Diameter - 1) ** 2
	TurbulentEdgeChannelBareFrictionMultiplier     = aet + bet * (Pitch / Diameter - 1) + cet * (Pitch / Diameter - 1) ** 2
	TurbulentCornerChannelBareFrictionMultiplier   = act + bct * (Pitch / Diameter - 1) + cct * (Pitch / Diameter - 1) ** 2		

	# INTERIOR
	F1it = TurbulentInteriorChannelBareFrictionMultiplier * (BareSingleInteriorChannelWettedPerimeter/SingleInteriorChannelWettedPerimeter) 
	F2it = (3 * SingleInteriorChannelProjectedWireArea/BareSingleInteriorChannelFlowArea)
	F3it = (SingleInteriorChannelHydraulicDiameter/WirePitch)
	F4it = (SingleInteriorChannelHydraulicDiameter/WireDiameter) 
	F5it = TWireDrag * F2it * F3it * F4it ** mturb
	Cf1t = F1it + F5it
	
	# EDGE
	F1et = TEdgeWireSweeping * (SingleEdgeChannelProjectedWireArea/BareSingleEdgeChannelFlowArea) * (math.tan(WireAngle) ** 2)
	Cf2t = TurbulentEdgeChannelBareFrictionMultiplier * ((1 + F1et) ** tturb)
    
	# CORNER
	F1ct = TCornerWireSweeping * (SingleCornerChannelProjectedWireArea/BareSingleCornerChannelFlowArea) * (math.tan(WireAngle) ** 2)
	Cf3t = TurbulentCornerChannelBareFrictionMultiplier * ((1 + F1ct) ** tturb)

    ## Flow split between interior and egde channels
	X1X2t = ((SingleInteriorChannelHydraulicDiameter/SingleEdgeChannelHydraulicDiameter) ** yturb) * ((Cf2t/Cf1t) ** xturb)

    ## Flow split between corner and edge channels
	X3X2t = ((SingleCornerChannelHydraulicDiameter/SingleEdgeChannelHydraulicDiameter) ** yturb) * ((Cf2t/Cf3t) ** xturb)

	## Turbulent bundle flow distribution
	X2t = 1/(S2 + X1X2t * S1 + X3X2t * S3)
	X1t = X1X2t * X2t
	X3t = X3X2t * X2t

	#print(FlowRegimeDecNat)

	if FlowRegimeDecNat == "Laminar":

		X1DecNat = X1l
		X2DecNat = X2l
		X3DecNat = X3l

		Cf1DecNat = Cf1l
		Cf2DecNat = Cf2l
		Cf3DecNat = Cf3l 

	elif FlowRegimeDecNat == "Turbulent":

		X1DecNat = X1t
		X2DecNat = X2t
		X3DecNat = X3t

		Cf1DecNat = Cf1t
		Cf2DecNat = Cf2t
		Cf3DecNat = Cf3t 

	elif FlowRegimeDecNat == "Transition":

		mtrans = 0.18
		Gamma  = 1/(2-mtrans)
		Beta   = 0.05
		PSI    = math.log10(BundleAverageDecNatBelowCoreReynolds/LaminarReynolds) / math.log10(TurbulentReynolds/LaminarReynolds)

		E1     = 1/(2-mtrans)
		E2     = (mtrans + 1)/(2-mtrans)
		E3     = mtrans/(2-mtrans)
		E4     = Gamma/(2-mtrans)

		T1_interior = Cf1l/(SingleInteriorChannelHydraulicDiameter ** 2)
		T2_interior = BundleHydraulicDiameter / BundleAverageDecNatBelowCoreReynolds
		T3_interior = (1-PSI) ** Gamma
		T4_interior = (Cf1t ** E1) / (SingleInteriorChannelHydraulicDiameter ** E2)

		T1_edge     = Cf2l/(SingleEdgeChannelHydraulicDiameter ** 2)
		T2_edge     = BundleHydraulicDiameter / BundleAverageDecNatBelowCoreReynolds
		T3_edge     = (1-PSI) ** Gamma
		T4_edge     = (Cf2t ** E1) / (SingleEdgeChannelHydraulicDiameter ** E2)

		T1_corner   = Cf3l/(SingleCornerChannelHydraulicDiameter ** 2)
		T2_corner   = BundleHydraulicDiameter / BundleAverageDecNatBelowCoreReynolds
		T3_corner   = (1-PSI) ** Gamma
		T4_corner   = (Cf3t ** E1) / (SingleCornerChannelHydraulicDiameter ** E2)

		X1_inter    = T1_interior * T2_interior * T3_interior + Beta * T4_interior * (T2_interior ** E3) * (PSI ** E4)
		X2_inter    = T1_edge     * T2_edge     * T3_edge     + Beta * T4_edge     * (T2_edge     ** E3) * (PSI ** E4)
		X3_inter    = T1_corner   * T2_corner   * T3_corner   + Beta * T4_corner   * (T2_corner   ** E3) * (PSI ** E4)

		X1X2trans   = X2_inter/X1_inter
		X3X2trans   = X2_inter/X3_inter

		## Transition bundle flow distribution
		X2DecNat = 1/(S2 + X1X2trans * S1 + X3X2trans * S3)
		X1DecNat = X1X2trans * X2DecNat
		X3DecNat = X3X2trans * X2DecNat

	LaminarInteriorReynolds   = X1l * (SingleInteriorChannelHydraulicDiameter / BundleHydraulicDiameter) * LaminarReynolds
	LaminarEdgeReynolds       = X2l * (SingleEdgeChannelHydraulicDiameter     / BundleHydraulicDiameter) * LaminarReynolds
	LaminarCornerReynolds     = X3l * (SingleCornerChannelHydraulicDiameter   / BundleHydraulicDiameter) * LaminarReynolds

	#print("Laminar trans")
	#print(LaminarInteriorReynolds)
	#print(LaminarEdgeReynolds)
	#print(LaminarCornerReynolds)

	TurbulentInteriorReynolds = X1t * (SingleInteriorChannelHydraulicDiameter / BundleHydraulicDiameter) * TurbulentReynolds
	TurbulentEdgeReynolds     = X2t * (SingleEdgeChannelHydraulicDiameter     / BundleHydraulicDiameter) * TurbulentReynolds
	TurbulentCornerReynolds   = X3t * (SingleCornerChannelHydraulicDiameter   / BundleHydraulicDiameter) * TurbulentReynolds

	#print("Turbulent trans")
	#print(TurbulentInteriorReynolds)
	#print(TurbulentEdgeReynolds)
	#print(TurbulentCornerReynolds)

	InteriorIntermittancyFactor = math.log10(BelowCoreDecNatInteriorReynolds / LaminarInteriorReynolds) / math.log10(TurbulentInteriorReynolds / LaminarInteriorReynolds)
	EdgeIntermittancyFactor     = math.log10(BelowCoreDecNatEdgeReynolds     / LaminarEdgeReynolds)     / math.log10(TurbulentEdgeReynolds     / LaminarEdgeReynolds)
	CornerIntermittancyFactor   = math.log10(BelowCoreDecNatCornerReynolds   / LaminarCornerReynolds)   / math.log10(TurbulentCornerReynolds   / LaminarCornerReynolds)

	## Resulting channel coolant velocities
	InteriorDecNatChannelCoolantVelocity = X1DecNat * AverageDecNatCoolantVelocity	
	EdgeDecNatChannelCoolantVelocity     = X2DecNat * AverageDecNatCoolantVelocity	
	CornerDecNatChannelCoolantVelocity   = X3DecNat * AverageDecNatCoolantVelocity

	#print("LAMINAR X")
	#print(X1l)
	#print(X2l)
	#print(X3l)
	#print("TURBULENT X")
	#print(X1t)
	#print(X2t)
	#print(X3t)	
	#print("TRANSITION X")
	#print(X1DecNat)
	#print(X2DecNat)
	#print(X3DecNat)
#
	#print("LAMINAR Cf")
	#print(Cf1l)
	#print(Cf2l)
	#print(Cf3l)
	#print("TURBULENT Cf")
	#print(Cf1t)
	#print(Cf2t)
	#print(Cf3t)	

	#print(Cf1l)
	#print(Cf2l)
	#print(Cf3l)
#
	#print(Cf1t)
	#print(Cf2t)
	#print(Cf3t)	

	return(InteriorDecNatChannelCoolantVelocity, EdgeDecNatChannelCoolantVelocity, CornerDecNatChannelCoolantVelocity,
		   Cf1DecNat, Cf2DecNat, Cf3DecNat, X1DecNat, X2DecNat, X3DecNat, InteriorIntermittancyFactor, EdgeIntermittancyFactor,   
		   CornerIntermittancyFactor, Cf1t, Cf2t, Cf3t, Cf1l, Cf2l, Cf3l)	

def inletoutletpressuredrop(CoolantInletDensity, AverageCoolantVelocity, BundleAverageBelowCoreReynolds):

	Kinlet = 1/(0.025 * BundleAverageBelowCoreReynolds ** 0.5)
	Koutlet = 0.35 * BundleAverageBelowCoreReynolds ** 0.15

	InletPressureDrop  = 0.5 * Kinlet * CoolantInletDensity * AverageCoolantVelocity ** 2
	OutletPressureDrop = 0.5 * Koutlet * CoolantInletDensity * AverageCoolantVelocity ** 2

	return(InletPressureDrop, OutletPressureDrop)

def averageinletoutletpressuredrop(CoolantInletDensity, AverageCoolantVelocity, AverageBundleAverageBelowCoreReynolds, RadialPowerPeaking):

	Kinlet = 1/(0.025 * AverageBundleAverageBelowCoreReynolds ** 0.5)
	Koutlet = 0.35 * AverageBundleAverageBelowCoreReynolds ** 0.15

	AverageInletPressureDrop  = 0.5 * Kinlet * CoolantInletDensity * (AverageCoolantVelocity/RadialPowerPeaking) ** 2
	AverageOutletPressureDrop = 0.5 * Koutlet * CoolantInletDensity * (AverageCoolantVelocity/RadialPowerPeaking) ** 2

	return(AverageInletPressureDrop, AverageOutletPressureDrop)

def decnatinletoutletpressuredrop(CoolantInletDensity, AverageDecNatCoolantVelocity, BundleAverageDecNatBelowCoreReynolds):

	Kinlet = 1/(0.025 * BundleAverageDecNatBelowCoreReynolds ** 0.5)
	Koutlet = 0.35 * BundleAverageDecNatBelowCoreReynolds ** 0.15

	InletDecNatPressureDrop  = 0.5 * Kinlet * CoolantInletDensity * AverageDecNatCoolantVelocity ** 2
	OutletDecNatPressureDrop = 0.5 * Koutlet * CoolantInletDensity * AverageDecNatCoolantVelocity ** 2

	return(InletDecNatPressureDrop, OutletDecNatPressureDrop)

def decnatchannelpressuredrop(Cf1DecNat,Cf2DecNat,Cf3DecNat,InteriorDecNatChannelCoolantVelocity,EdgeDecNatChannelCoolantVelocity,CornerDecNatChannelCoolantVelocity, BelowCoreDecNatInteriorReynolds,
	             BelowCoreDecNatEdgeReynolds, BelowCoreDecNatCornerReynolds, CoolantDecNatAxialInteriorReynolds, CoolantDecNatAxialEdgeReynolds, CoolantDecNatAxialCornerReynolds,
	             FuelLength, BelowCoreChannelLength, AboveCoreChannelLength, FlowRegimeDecNat, TemperaturePoints, CoolantAxialDensity, CoolantAxialKinematicViscosity, \
	             CoolantInletDensity,SingleInteriorChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, InteriorIntermittancyFactor, EdgeIntermittancyFactor,    
		         CornerIntermittancyFactor, Cf1t, Cf2t, Cf3t, Cf1l, Cf2l, Cf3l):

	BundleChannelLength = BelowCoreChannelLength + FuelLength + AboveCoreChannelLength

	if FlowRegimeDecNat == "Transition":

		m = 1
		f1l = Cf1l/BelowCoreDecNatInteriorReynolds ** m
		f2l = Cf2l/BelowCoreDecNatEdgeReynolds     ** m
		f3l = Cf3l/BelowCoreDecNatCornerReynolds   ** m

		m = 0.18	
		f1t = Cf1t/BelowCoreDecNatInteriorReynolds ** m
		f2t = Cf2t/BelowCoreDecNatEdgeReynolds     ** m
		f3t = Cf3t/BelowCoreDecNatCornerReynolds   ** m

		#print(f1l)
		#print(f2l)
		#print(f3l)
		#print(f1t)
		#print(f2t)
		#print(f3t)

		# Transition friction factors
		DecNatInteriorChannelFrictionFactor = f1l * ((1 - InteriorIntermittancyFactor) ** (1/3)) * (1 - (InteriorIntermittancyFactor ** 13)) + f1t * (InteriorIntermittancyFactor ** (1/3))
		DecNatEdgeChannelFrictionFactor     = f2l * ((1 - EdgeIntermittancyFactor)     ** (1/3)) * (1 - (EdgeIntermittancyFactor ** 13)) + f2t * (EdgeIntermittancyFactor     ** (1/3))
		DecNatCornerChannelFrictionFactor   = f3l * ((1 - CornerIntermittancyFactor)   ** (1/3)) * (1 - (CornerIntermittancyFactor ** 13)) + f3t * (CornerIntermittancyFactor   ** (1/3))

	elif FlowRegimeDecNat == "Laminar":

		m = 1
		DecNatInteriorChannelFrictionFactor = Cf1DecNat/BelowCoreDecNatInteriorReynolds ** m
		DecNatEdgeChannelFrictionFactor     = Cf2DecNat/BelowCoreDecNatEdgeReynolds ** m
		DecNatCornerChannelFrictionFactor   = Cf3DecNat/BelowCoreDecNatCornerReynolds ** m

	else:
	
		m = 0.18	
		DecNatInteriorChannelFrictionFactor = Cf1DecNat/BelowCoreDecNatInteriorReynolds ** m
		DecNatEdgeChannelFrictionFactor     = Cf2DecNat/BelowCoreDecNatEdgeReynolds ** m
		DecNatCornerChannelFrictionFactor   = Cf3DecNat/BelowCoreDecNatCornerReynolds ** m

	#print("trans f")
	#print(DecNatInteriorChannelFrictionFactor)
	#print(DecNatEdgeChannelFrictionFactor)
	#print(DecNatCornerChannelFrictionFactor)

	InteriorChannelPressureDrop = (0.5 * DecNatInteriorChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * InteriorDecNatChannelCoolantVelocity ** 2)	/ SingleInteriorChannelHydraulicDiameter
	EdgeChannelPressureDrop     = (0.5 * DecNatEdgeChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * EdgeDecNatChannelCoolantVelocity ** 2)	/ SingleEdgeChannelHydraulicDiameter
	CornerChannelPressureDrop   = (0.5 * DecNatCornerChannelFrictionFactor * BundleChannelLength * CoolantInletDensity * CornerDecNatChannelCoolantVelocity ** 2)	/ SingleCornerChannelHydraulicDiameter

	ChannelPressureDropDecNat = max([InteriorChannelPressureDrop, EdgeChannelPressureDrop, CornerChannelPressureDrop])	

	return(ChannelPressureDropDecNat, DecNatInteriorChannelFrictionFactor, DecNatEdgeChannelFrictionFactor, DecNatCornerChannelFrictionFactor)	

	