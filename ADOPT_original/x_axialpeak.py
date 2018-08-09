import math
import sys

def axialpeaking(PinAxialPowerPeaking):

	## INFO: Converts the axial power peaking factor to a unit useful for chopped cosine power distribution
	
	AxialPeakError       = 100   # Initial error for the calculation
	
	AxialPeakConvergence = 1e-5  # Convergence criteria for matching the peaking factors
	
	if PinAxialPowerPeaking < (math.pi/2) and PinAxialPowerPeaking > 1:

		AxialPeak            = 1     # Initial estimate of the new peaking factor

		while AxialPeakError > AxialPeakConvergence:
		
			AxialPeak             = AxialPeak + 1e-7
			AxialPeak_Calculated  = math.pi / AxialPeak / math.sin(math.pi / AxialPeak / 2) / 2
			AxialPeakError        = abs(AxialPeak_Calculated-PinAxialPowerPeaking)
		
		PinAxialPowerPeaking = AxialPeak # Set the new peaking factor to the calculated value

	elif PinAxialPowerPeaking > (math.pi/2) and PinAxialPowerPeaking < 1.9189:

		AxialPeak            = math.pi/6    # Initial estimate of the new peaking factor

		while AxialPeakError > AxialPeakConvergence:
		
			AxialPeak             = AxialPeak + 1e-7
			AxialPeak_Calculated  = 0.1e1 / (-0.2e1 * AxialPeak * math.sin(math.pi / AxialPeak / 0.2e1) + math.cos(math.pi / AxialPeak / 0.2e1) * math.pi) * (-0.1e1 + math.cos(math.pi / AxialPeak / 0.2e1)) * math.pi
			AxialPeakError        = abs(AxialPeak_Calculated-PinAxialPowerPeaking)

		PinAxialPowerPeaking = AxialPeak # Set the new peaking factor to the calculated value

	else: 

		sys.exit("Axial power peaking outside of valid range")

	return(PinAxialPowerPeaking)