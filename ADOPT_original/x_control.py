import math

def control(FTF, DuctThickness, BUControlDuctGap, BUControlPinsPerAssembly, BUControlAreaFraction,
			BUControlSmearDensity, BUControlCTR):

	FTFControlOuterWall = FTF - BUControlDuctGap*2/10
	FTFControlInnerWall = FTFControlOuterWall - DuctThickness/10
	
	ControlInnerSideLength = FTFControlInnerWall/2
	ControlOuterSideLength = FTFControlOuterWall/2

	InnerControlArea = (math.sqrt(3) / 2) * ((FTFControlInnerWall/100) ** 2)

	ControlArea = InnerControlArea * BUControlAreaFraction
	ControlPinRows = ((1/2) + (1/6) * math.sqrt(-3 + 12 * BUControlPinsPerAssembly))-1

	ControlPinDiameter = 100 * (2 * math.sqrt(math.pi * BUControlPinsPerAssembly * ControlArea) / (math.pi * BUControlPinsPerAssembly))
	ControlPinPitch    = 100 * (((FTFControlInnerWall/100) + (ControlPinDiameter/100))/(math.sqrt(3) * ControlPinRows + 2))

	ControlCladdingThickness = BUControlCTR * ControlPinDiameter

	ControlPinOuterRadius = ControlPinDiameter / 2
	ControlPinInnerRadius = ControlPinOuterRadius - ControlCladdingThickness

	ControlPinSlugRadius = math.sqrt(BUControlSmearDensity) * ControlPinInnerRadius

	return(ControlPinOuterRadius, ControlPinInnerRadius, ControlPinPitch, ControlPinSlugRadius,
		   ControlInnerSideLength, ControlOuterSideLength)

def scram(FTF, DuctThickness, ScramDuctGap, ScramPinsPerAssembly, ScramAreaFraction,
			ScramSmearDensity, ScramCTR):

	FTFControlOuterWall = FTF - ScramDuctGap*2/10
	FTFControlInnerWall = FTFControlOuterWall - DuctThickness/10
	
	ScramInnerSideLength = FTFControlInnerWall/2
	ScramOuterSideLength = FTFControlOuterWall/2

	InnerControlArea = (math.sqrt(3) / 2) * ((FTFControlInnerWall/100) ** 2)

	ControlArea = InnerControlArea * ScramAreaFraction
	ControlPinRows = ((1/2) + (1/6) * math.sqrt(-3 + 12 * ScramPinsPerAssembly))-1

	ScramPinDiameter = 100 * (2 * math.sqrt(math.pi * ScramPinsPerAssembly * ControlArea) / (math.pi * ScramPinsPerAssembly))
	ScramPinPitch    = 100 * (((FTFControlInnerWall/100) + (ScramPinDiameter/100))/(math.sqrt(3) * ControlPinRows + 2))

	ScramCladdingThickness = ScramCTR * ScramPinDiameter

	ScramPinOuterRadius = ScramPinDiameter / 2
	ScramPinInnerRadius = ScramPinOuterRadius - ScramCladdingThickness

	ScramPinSlugRadius = math.sqrt(ScramSmearDensity) * ScramPinInnerRadius

	return(ScramPinOuterRadius, ScramPinInnerRadius, ScramPinPitch, ScramPinSlugRadius,
		   ScramInnerSideLength, ScramOuterSideLength)	

