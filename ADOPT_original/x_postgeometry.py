# -*- coding: UTF-8 -*-
import math

def rodinfo(CTR, Diameter, CladdingMinimumThickness, FuelSmearDensity, RelativeWirePitch, i):

	if i > 2:

		# Check if the cladding thickness calculated by CTR is larger than minimum constraint
		if CTR * Diameter * 1000 > CladdingMinimumThickness:
			CladdingThickness = CTR * Diameter
		else:
			CladdingThickness = CladdingMinimumThickness/1000

	else:
	
		CladdingThickness = CladdingMinimumThickness/1000
	
	# Define inner cladding diameter and radius
	CladdingOuterDiameter = Diameter
	CladdingOuterRadius   = CladdingOuterDiameter / 2
	CladdingInnerDiameter = CladdingOuterDiameter - 2 * CladdingThickness
	CladdingInnerRadius   = CladdingInnerDiameter / 2

	# Define fuel diameter and radius
	FreshFuelDiameter = math.sqrt(FuelSmearDensity/100) * CladdingInnerDiameter

	# Define inner radius for annular fuels
	InnerFuelRadius   = math.sqrt(1 - FuelSmearDensity/100) * CladdingInnerRadius
	InnerFuelDiameter = 2 * InnerFuelRadius

	FreshFuelRadius       = FreshFuelDiameter / 2
	
	# Define gap diameters and radii
	GapInnerDiameter      = FreshFuelDiameter
	GapInnerRadius        = GapInnerDiameter / 2
	GapOuterDiameter      = CladdingInnerDiameter
	GapOuterRadius        = GapOuterDiameter / 2
	
	# Wire lead length
	WirePitch             = RelativeWirePitch * Diameter	

	return(CladdingThickness, CladdingOuterDiameter, CladdingOuterRadius, CladdingInnerDiameter, CladdingInnerRadius, \
		   FreshFuelDiameter, FreshFuelRadius, GapInnerDiameter, GapInnerRadius, GapOuterDiameter, GapOuterRadius, WirePitch,
		   InnerFuelRadius, InnerFuelDiameter)

def flowinfo(Pitch, Diameter, WireDiameter, WirePitch, InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly,
			 FTF, PinsPerAssembly):

	# Wire correction angle
	CT = WirePitch * (WirePitch ** 2 + math.pi ** 2 * (Diameter + WireDiameter) ** 2) ** (-0.1e1 / 0.2e1)

	# Wire correction for flow area in interior and egde channels
	CT_A1 = (math.pi * WireDiameter ** 2) / (8 * CT)

	# Wire correction for flow area in corner channels	
	CT_A3 = (math.pi * WireDiameter ** 2) / (24 * CT)

	# Wire correction for wetted perimeter in interior and egde channels
	CT_P1 = (math.pi * WireDiameter) / (2 * CT)

   	# Wire correction for wetted perimeter in corner channels	
	CT_P3 = (math.pi * WireDiameter) / (6 * CT)	

	# Flow area per interior channel excluding wires
	BareSingleInteriorChannelFlowArea = ((math.sqrt(3)/4) * Pitch ** 2 - (math.pi * Diameter ** 2) / 8)

	# Flow area per interior channel
	SingleInteriorChannelFlowArea      = BareSingleInteriorChannelFlowArea - CT_A1

	# Flow area per edge channel excluding wires
	BareSingleEdgeChannelFlowArea     = Pitch * ((Diameter / 2) + WireDiameter) - ((math.pi * Diameter ** 2) / 8)
	
	# Flow area per edge channel
	SingleEdgeChannelFlowArea          = BareSingleEdgeChannelFlowArea - CT_A1
	
	# Flow area per corner channel excluding wires
	BareSingleCornerChannelFlowArea   = ((1/math.sqrt(3)) * (Diameter/2 + WireDiameter) ** 2 - (math.pi * Diameter ** 2) / 24)

	# Flow area per corner channel
	SingleCornerChannelFlowArea        = BareSingleCornerChannelFlowArea - CT_A3

	# Wetted perimeter per interior channel
	BareSingleInteriorChannelWettedPerimeter = math.pi * Diameter / 2
	
	# Wetted perimeter per interior channel
	SingleInteriorChannelWettedPerimeter     = BareSingleInteriorChannelWettedPerimeter + CT_P1

	# Wetted perimeter per edge channel
	BareSingleEdgeChannelWettedPerimeter     = Pitch + (math.pi * Diameter / 2)
	
	# Wetted perimeter per edge channel
	SingleEdgeChannelWettedPerimeter         = BareSingleEdgeChannelWettedPerimeter + CT_P1

	# Wetted perimeter per corner channel
	BareSingleCornerChannelWettedPerimeter   = ((math.pi * Diameter / 6) + 2 * (Pitch - Diameter/2) / math.sqrt(3))
	
	# Wetted perimeter per corner channel
	SingleCornerChannelWettedPerimeter       = BareSingleCornerChannelWettedPerimeter + CT_P3

	# Hydraulic diameter per interior channel excluding wires
	BareSingleInteriorChannelHydraulicDiameter = 4 * BareSingleInteriorChannelFlowArea / BareSingleInteriorChannelWettedPerimeter
	
	# Hydraulic diameter per interior channel
	SingleInteriorChannelHydraulicDiameter     = 4 * SingleInteriorChannelFlowArea     / SingleInteriorChannelWettedPerimeter

	# Hydraulic diameter per edge channel excluding wires
	BareSingleEdgeChannelHydraulicDiameter     = 4 * BareSingleEdgeChannelFlowArea     / BareSingleEdgeChannelWettedPerimeter
	
	# Hydraulic diameter per edge channel
	SingleEdgeChannelHydraulicDiameter         = 4 * SingleEdgeChannelFlowArea         / SingleEdgeChannelWettedPerimeter

	# Hydraulic diameter per corner channel
	BareSingleCornerChannelHydraulicDiameter   = 4 * BareSingleCornerChannelFlowArea   / BareSingleCornerChannelWettedPerimeter	
	
	# Hydraulic diameter per corner channel
	SingleCornerChannelHydraulicDiameter       = 4 * SingleCornerChannelFlowArea       / SingleCornerChannelWettedPerimeter	

	# Projected wire area in interior channels
	SingleInteriorChannelProjectedWireArea     = math.pi * (Diameter + WireDiameter) * WireDiameter / 6

	# Projected wire area in edge channels
	SingleEdgeChannelProjectedWireArea         = math.pi * (Diameter + WireDiameter) * WireDiameter / 4

	# Projected wire area in corner channels
	SingleCornerChannelProjectedWireArea       = SingleInteriorChannelProjectedWireArea 

	# Flow plit info
	SingleAverageFlowArea = (SingleInteriorChannelFlowArea * InteriorChannelsPerAssembly + SingleEdgeChannelFlowArea * SingleEdgeChannelFlowArea + SingleCornerChannelFlowArea * CornerChannelsPerAssembly) / (InteriorChannelsPerAssembly + EdgeChannelsPerAssembly + CornerChannelsPerAssembly)

	# Flow plit info
	AssemblyFlowArea = SingleInteriorChannelFlowArea * InteriorChannelsPerAssembly + SingleEdgeChannelFlowArea * EdgeChannelsPerAssembly + SingleCornerChannelFlowArea * CornerChannelsPerAssembly

	# Total bundle wetted perimeter
	AssemblyWettedPerimeter = (SingleInteriorChannelWettedPerimeter * InteriorChannelsPerAssembly + SingleEdgeChannelWettedPerimeter * EdgeChannelsPerAssembly + SingleCornerChannelWettedPerimeter * CornerChannelsPerAssembly)

	# Relative importance of channels
	S1 = InteriorChannelsPerAssembly * SingleInteriorChannelFlowArea / AssemblyFlowArea
	S2 = EdgeChannelsPerAssembly     * SingleEdgeChannelFlowArea     / AssemblyFlowArea
	S3 = CornerChannelsPerAssembly   * SingleCornerChannelFlowArea   / AssemblyFlowArea

	# Bundle averaged hydraulic diameter
	SingleAverageHydraulicDiameter = (SingleInteriorChannelHydraulicDiameter * InteriorChannelsPerAssembly + SingleEdgeChannelHydraulicDiameter * SingleEdgeChannelHydraulicDiameter + SingleCornerChannelHydraulicDiameter * CornerChannelsPerAssembly) / (InteriorChannelsPerAssembly + EdgeChannelsPerAssembly + CornerChannelsPerAssembly)

	# Bundle hydraulic diameter
	BundleHydraulicDiameter = 4 * AssemblyFlowArea / AssemblyWettedPerimeter

	return(BareSingleInteriorChannelFlowArea, SingleInteriorChannelFlowArea, BareSingleEdgeChannelFlowArea, SingleEdgeChannelFlowArea, \
		   BareSingleCornerChannelFlowArea, SingleCornerChannelFlowArea, BareSingleInteriorChannelWettedPerimeter, \
		   SingleInteriorChannelWettedPerimeter, BareSingleEdgeChannelWettedPerimeter, SingleEdgeChannelWettedPerimeter, \
		   BareSingleCornerChannelWettedPerimeter, SingleCornerChannelWettedPerimeter, BareSingleInteriorChannelHydraulicDiameter, \
		   SingleInteriorChannelHydraulicDiameter, BareSingleEdgeChannelHydraulicDiameter, SingleEdgeChannelHydraulicDiameter, \
		   BareSingleCornerChannelHydraulicDiameter, SingleCornerChannelHydraulicDiameter, SingleInteriorChannelProjectedWireArea, \
		   SingleEdgeChannelProjectedWireArea, SingleCornerChannelProjectedWireArea, S1, S2, S3, SingleAverageHydraulicDiameter, AssemblyFlowArea, \
		   AssemblyWettedPerimeter, BundleHydraulicDiameter)