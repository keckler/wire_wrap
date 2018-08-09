import math

def innershieldradius(CladdingInnerRadius, AxialShieldSlugSmearDensity):

	AxialShieldPinRadius = math.sqrt(AxialShieldSlugSmearDensity) * CladdingInnerRadius

	return(AxialShieldPinRadius)

def innerreflectorradius(CladdingInnerRadius, AxialReflectorSlugSmearDensity):

	AxialReflectorPinRadius = math.sqrt(AxialReflectorSlugSmearDensity) * CladdingInnerRadius

	return(AxialReflectorPinRadius)	