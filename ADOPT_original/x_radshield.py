import math

def shieldreflector(ShieldPinMaterial, ShieldPinVolumeFraction, InnerAssemblyArea, ShieldPinsPerAssembly, FTF, ShieldSlugSmearDensity,
	                ShieldSlugCTR):

	ShieldArea = InnerAssemblyArea * ShieldPinVolumeFraction
	ShieldPinRows = ((1/2) + (1/6) * math.sqrt(-3 + 12 * ShieldPinsPerAssembly))-1

	ShieldPinDiameter = 100 * (2 * math.sqrt(math.pi * ShieldPinsPerAssembly * ShieldArea) / (math.pi * ShieldPinsPerAssembly))
	ShieldPinPitch    = 100 * (((FTF/100) + (ShieldPinDiameter/100))/(math.sqrt(3) * ShieldPinRows + 2))

	ShieldCladdingThickness = ShieldSlugCTR * ShieldPinDiameter

	ShieldPinOuterRadius = ShieldPinDiameter / 2
	ShieldPinInnerRadius = ShieldPinOuterRadius - ShieldCladdingThickness

	ShieldPinSlugRadius = math.sqrt(ShieldSlugSmearDensity) * ShieldPinInnerRadius

	return(ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius)