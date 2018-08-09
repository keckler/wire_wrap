import math

def naturalcirculation(Coolant, ChannelPressureDrop, NonCorePressureDropMultiplier, AverageCoolantOutletTemperature, 
					   CoolantInletTemperature, CoolantInletDensity, ThermalCenterElevation,
					   CoolantOutletDensity, CycleTime, Power, InletPressureDrop, OutletPressureDrop):

	g = 9.82

	CycleTime = CycleTime * 24 * 3600

	AverageCoolantTemperatureRise = AverageCoolantOutletTemperature - CoolantInletTemperature
	CoolantVolumetricExpansion = -(-CoolantOutletDensity + CoolantInletDensity) / CoolantOutletDensity / (-AverageCoolantOutletTemperature + CoolantInletTemperature)

	TotalPressureDrop = (ChannelPressureDrop + InletPressureDrop + OutletPressureDrop) * (1 + NonCorePressureDropMultiplier)
	NaturalCirculation = math.sqrt( (g * CoolantInletDensity * CoolantVolumetricExpansion * AverageCoolantTemperatureRise * ThermalCenterElevation) / TotalPressureDrop)	

	return(NaturalCirculation)

def decaynaturalcirculation(Coolant, ChannelPressureDropDecNat, NonCorePressureDropMultiplier, AverageCoolantOutletTemperature, 
					   		CoolantInletTemperature, CoolantInletDensity, ThermalCenterElevation, CoolantOutletDensity, CycleTime, 
					   		Power, DecayHeat, PumpResistanceFraction, InletDecNatPressureDrop, OutletDecNatPressureDrop):

	g = 9.82

	AverageCoolantTemperatureRise = AverageCoolantOutletTemperature - CoolantInletTemperature
	CoolantVolumetricExpansion = -(-CoolantOutletDensity + CoolantInletDensity) / CoolantOutletDensity / (-AverageCoolantOutletTemperature + CoolantInletTemperature)

	TotalPressureDropDecNat = (ChannelPressureDropDecNat + InletDecNatPressureDrop + OutletDecNatPressureDrop) * (1 + NonCorePressureDropMultiplier + PumpResistanceFraction)
	NaturalCirculationThermalCenterElevation = TotalPressureDropDecNat / (g * CoolantInletDensity * CoolantVolumetricExpansion * AverageCoolantTemperatureRise)
	PumpPressureDrop = PumpResistanceFraction * (ChannelPressureDropDecNat + InletDecNatPressureDrop + OutletDecNatPressureDrop)

	return(NaturalCirculationThermalCenterElevation, TotalPressureDropDecNat, PumpPressureDrop)

