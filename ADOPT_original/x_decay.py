def decayheatflow(Pitch, Diameter, MassFlowArea, CycleTime, PeakPinPower, CoolantInletDensity, CoolantTemperatureRise, CoolantInletHeatCapacity, DecayHeatTime):

	CycleTime = CycleTime * 24 * 3600

	DecayHeat = 0.1e0 * ((DecayHeatTime + 10) ** (-0.2e0)) - 0.1e0 * ((DecayHeatTime + CycleTime + 10) ** (-0.2e0)) - 0.87e-1 * ((DecayHeatTime + 20000000) ** (-0.2e0)) + 0.87e-1 * ((DecayHeatTime + CycleTime + 20000000) ** (-0.2e0))
	DecayHeatRemovalFlowVelocity = (DecayHeat * PeakPinPower) / (MassFlowArea * CoolantInletDensity * CoolantTemperatureRise * CoolantInletHeatCapacity)

	return(DecayHeat, DecayHeatRemovalFlowVelocity)