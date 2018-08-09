def THinitialguess(CoolantVelocityConstraint, MinimumPinRows, CladdingOuterTemperatureConstraint, CoolantOutletTemperatureMode,
				   CoolantOutletTemperature, AverageCoolantVelocity0, CoolantTemperatureConstraint):

	AverageCoolantVelocity   = AverageCoolantVelocity0
	FuelPinRows              = MinimumPinRows 

	if CoolantOutletTemperatureMode == "Calculated":
	
		CoolantOutletTemperature = CoolantTemperatureConstraint

	else:

		CoolantOutletTemperature = CoolantOutletTemperature

	return(AverageCoolantVelocity, FuelPinRows, CoolantOutletTemperature)