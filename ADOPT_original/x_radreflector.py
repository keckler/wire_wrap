import math

def radialreflector(ReflectorPinMaterial, ReflectorPinVolumeFraction, InnerAssemblyArea, ReflectorPinsPerAssembly, FTF, ReflectorSlugSmearDensity,
	                ReflectorSlugCTR):

	ReflectorArea = InnerAssemblyArea * ReflectorPinVolumeFraction
	ReflectorPinRows = ((1/2) + (1/6) * math.sqrt(-3 + 12 * ReflectorPinsPerAssembly))-1

	ReflectorPinDiameter = 100 * (2 * math.sqrt(math.pi * ReflectorPinsPerAssembly * ReflectorArea) / (math.pi * ReflectorPinsPerAssembly))
	ReflectorPinPitch    = 100 * (((FTF/100) + (ReflectorPinDiameter/100))/(math.sqrt(3) * ReflectorPinRows + 2))

	ReflectorCladdingThickness = ReflectorSlugCTR * ReflectorPinDiameter

	ReflectorPinOuterRadius = ReflectorPinDiameter / 2
	ReflectorPinInnerRadius = ReflectorPinOuterRadius - ReflectorCladdingThickness

	ReflectorPinSlugRadius = math.sqrt(ReflectorSlugSmearDensity) * ReflectorPinInnerRadius

	return(ReflectorPinOuterRadius, ReflectorPinInnerRadius, ReflectorPinPitch, ReflectorPinSlugRadius)