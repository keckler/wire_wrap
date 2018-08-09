# -*- coding: UTF-8 -*-

import math

def preoutput(InletPressureDrop, OutletPressureDrop, ChannelPressureDrop, NonCorePressureDropMultiplier,
	          CoreOuterRadius, AssemblyPitch, RadialReflectorRows, RadialShieldRows, FuelLength, SystemDiameter,
	          BelowCoreChannelLength, AboveCoreChannelLength, Power, CoreFissileMass, CoreFuelMass,
	          FuelVolumeFraction, FuelAverageDensity, CoolantAverageDensity, ActiveCoolantVolumeFraction,
	          InterAssemblyVolumeFraction, AverageInletPressureDrop, AverageOutletPressureDrop, 
	          AverageChannelPressureDrop, AverageBondDensity, AverageDuctDensity, AverageCladdingDensity,
	          GapVolumeFraction, CladdingVolumeFraction, DuctVolumeFraction):

	CorePD         = (InletPressureDrop+OutletPressureDrop+ChannelPressureDrop)/1e3
	TotPD          = ((InletPressureDrop+OutletPressureDrop+ChannelPressureDrop)/1e3) * (1 + NonCorePressureDropMultiplier)
	AverageCorePD  = (AverageInletPressureDrop+AverageOutletPressureDrop+AverageChannelPressureDrop)/1e3
	CoreVolume     = (CoreOuterRadius ** 2) * math.pi * FuelLength
	SystemHeight   = BelowCoreChannelLength + FuelLength + AboveCoreChannelLength
	SystemVolume   = ((SystemDiameter/200) ** 2) * math.pi * SystemHeight
	VolumetricPowerDensity = Power / CoreVolume / 1e6

	SpecificPower        = Power / CoreFuelMass / 1e3
	SpecificFissilePower = Power / CoreFissileMass / 1e3

	FuelMassDensityGCC      = FuelVolumeFraction * FuelAverageDensity
	CoolantMassDensityGCC   = (ActiveCoolantVolumeFraction + InterAssemblyVolumeFraction) * CoolantAverageDensity / 1000	
	BondMassDensityGCC      = GapVolumeFraction * AverageBondDensity
	CladdingMassDensityGCC  = CladdingVolumeFraction * AverageCladdingDensity
	DuctMassDensityGCC      = DuctVolumeFraction * AverageDuctDensity
	CoreMassDensityGCC = FuelMassDensityGCC + BondMassDensityGCC + CladdingMassDensityGCC + CoolantMassDensityGCC + DuctMassDensityGCC    

	FuelMassFraction     = FuelMassDensityGCC     / CoreMassDensityGCC
	CoolantMassFraction  = CoolantMassDensityGCC  / CoreMassDensityGCC
	BondMassFraction     = BondMassDensityGCC     / CoreMassDensityGCC
	CladdingMassFraction = CladdingMassDensityGCC / CoreMassDensityGCC
	DuctMassFraction     = DuctMassDensityGCC     / CoreMassDensityGCC

	FuelMass     = FuelMassDensityGCC     * CoreVolume
	BondMass     = BondMassDensityGCC     * CoreVolume * 1000
	CladdingMass = CladdingMassDensityGCC * CoreVolume * 1000
	DuctMass     = DuctMassDensityGCC     * CoreVolume * 1000
	CoolantMass  = CoolantMassDensityGCC  * CoreVolume * 1000

	return (CorePD, TotPD, CoreVolume, SystemVolume, SystemHeight, VolumetricPowerDensity, SpecificPower, SpecificFissilePower, AverageCorePD,
			FuelMassDensityGCC, CoolantMassDensityGCC, BondMassDensityGCC, CladdingMassDensityGCC, DuctMassDensityGCC, CoreMassDensityGCC,
			BondMass, CladdingMass, DuctMass, CoolantMass, FuelMass, FuelMassFraction, CoolantMassFraction, BondMassFraction, CladdingMassFraction,
			DuctMassFraction)

