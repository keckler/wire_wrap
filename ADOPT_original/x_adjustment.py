# -*- coding: UTF-8 -*-

################################################################################################### //// ######## //// #######
########### adjust.py -- Last modified: 2013-11-22                                   ############## //// ######## //// #######
################################################################################################### //// ######## //// #######

################################################################################################################## //// #######
########### Function: adjust() -- Last modified: 2013-11-22                          ############################# //// #######
################################################################################################################## //// #######
###########                                                                                               ######## //// #######
###########   Description:                                                                                ######## //// #######
###########   --------------------                                                                        ######## //// #######
###########   Changes calculation variables when constraints are violated.                                ######## //// #######
###########   - If flow velocity, pressure drop or natural circulation FOM1* constraints are violated,    ######## //// #######
###########     coolant velocity is reduced.                                                              ######## //// #######
###########   - If cladding inner-wall or fuel centerline temperature constraints are violated, the       ######## //// #######
###########     number of pins per assembly is increased.                                                 ######## //// #######
###########   - If cladding outer-wall temperature constraint is violated, the coolant outlet temperature ######## //// #######
###########     is reduced.                                                                               ######## //// #######
###########                                                                                               ######## //// #######
################################################################################################################## //// ####### 

def adjust(CalculatedPeakCoolantVelocity, CoolantVelocityConstraint, CorePressureDropConstraint, AverageCoolantVelocity, 
		   VelocityPrecision, CladdingOuterTemperatureConstraint, TemperatureConvergence, FuelTemperatureConstraint, 
		   CladdingInnerTemperatureConstraint, PeakCladdingInnerWallTemperature, PeakCladdingOuterWallTemperature, 
		   PeakFuelInnerTemperature, CoolantOutletTemperature, FuelPinRows, ChannelPressureDrop, CoolantOutletTemperatureMode, 
		   TotalPressureDrop, NaturalCirculationThermalCenterElevation, NaturalCirculationFOM1Constraint):

	################################################################################################### //// ######## //// #######
	###########   Check flow-related constraints, if violated, reduce flow velocity by          ####### //// ######## //// #######
	###########   the value "VelocityPrecision" which is set in the settings file               ####### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	if CalculatedPeakCoolantVelocity > CoolantVelocityConstraint or TotalPressureDrop > CorePressureDropConstraint or NaturalCirculationThermalCenterElevation > NaturalCirculationFOM1Constraint:

		AverageCoolantVelocity -= VelocityPrecision

	################################################################################################### //// ######## //// #######
	###########   Check peak velocity constraint, if passed with 2 "VelocityPrecision" margin,  ####### //// ######## //// #######
	###########   set the message sent to the console output to PASS                            ####### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	elif CalculatedPeakCoolantVelocity < CoolantVelocityConstraint - 2 * VelocityPrecision:

		xflowvelocity = "PASS"
		xpressuredrop = "PASS"

	################################################################################################### //// ######## //// #######
	###########   Cover all the bases by setting the messages to "PASS" if no violations were   ####### //// ######## //// #######
	###########   discovered.                                                                   ####### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	else:

		xflowvelocity = "PASS"
		xpressuredrop = "PASS"

	################################################################################################### //// ######## //// #######
	###########   Check cladding outer wall temperature constraint, if violated, reduce the     ####### //// ######## //// #######
	###########   coolant outlet temperature by "TemperatureConvergence" from the settings file ####### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	if PeakCladdingOuterWallTemperature > CladdingOuterTemperatureConstraint:

		CoolantOutletTemperature -= TemperatureConvergence

		FailMargin = PeakCladdingOuterWallTemperature-CladdingOuterTemperatureConstraint
		xclado = "FAIL (+{0:02.1f}".format(FailMargin) + " deg. C)"

	################################################################################################### //// ######## //// #######
	###########   If the coolant outlet temperature is set to be calculated, and the cladding   ####### //// ######## //// #######
	###########   outer temperature constraint is not violated, increase the coolant outlet     ####### //// ######## //// #######
	###########   temperature by "TemperatureConvergence" until the constraint is met.          ####### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	elif PeakCladdingOuterWallTemperature < CladdingOuterTemperatureConstraint - 2 * TemperatureConvergence:

		if CoolantOutletTemperatureMode == "Calculated":
			CoolantOutletTemperature += TemperatureConvergence
		xclado = "PASS"

	else:

		xclado = "PASS"

	# FUEL AND INNER CLADDING WALL TEMPERATURES
	if PeakCladdingInnerWallTemperature > CladdingInnerTemperatureConstraint or PeakFuelInnerTemperature > FuelTemperatureConstraint:

		FuelPinRows += 1

	else:

		xfueltemp = "PASS"	
		xcladi = "PASS"	

	# INNER CLADDING WALL MESSAGE
	if PeakCladdingInnerWallTemperature > CladdingInnerTemperatureConstraint:
		FailMargin = PeakCladdingInnerWallTemperature-CladdingInnerTemperatureConstraint
		xcladi = "FAIL (+{0:02.1f}".format(FailMargin) + ")"		
	else:
		xcladi = "PASS"

	# FUEL TEMPERATURE MESSAGE
	if PeakFuelInnerTemperature > FuelTemperatureConstraint:

		FailMargin = PeakFuelInnerTemperature-FuelTemperatureConstraint
		xfueltemp = "FAIL (+{0:02.1f}".format(FailMargin) + " deg. C)"
	else:
		xfueltemp = "PASS"	

	# COOLANT VELOCITY MESSAGE
	if CalculatedPeakCoolantVelocity > CoolantVelocityConstraint:
		FailMargin = CalculatedPeakCoolantVelocity/CoolantVelocityConstraint -1
		xflowvelocity = "FAIL (+{0:02.2%}".format(FailMargin) + ")"
	else:
		xflowvelocity = "PASS"

	# PRESSURE DROP MESSAGE
	if TotalPressureDrop > CorePressureDropConstraint:	
		FailMargin = TotalPressureDrop/CorePressureDropConstraint -1
		xpressuredrop = "FAIL (+{0:02.2%}".format(FailMargin) + ")"
	else:
		xpressuredrop = "PASS"

	# FOM1 MESSAGE
	if NaturalCirculationThermalCenterElevation > NaturalCirculationFOM1Constraint:	
		FailMargin = NaturalCirculationThermalCenterElevation/NaturalCirculationFOM1Constraint -1
		xfom1 = "FAIL (+{0:02.2%}".format(FailMargin) + ")"
	else:
		xfom1 = "PASS"

	return(FuelPinRows, AverageCoolantVelocity, CoolantOutletTemperature,xpressuredrop, xflowvelocity,xfueltemp,xcladi,xclado, xfom1)

