# coding=utf-8
from x_prop import *

def collapsetoserpent(CoolantAxialTemperature, CoolantAxialEdgeTemperature, CoolantAxialCornerTemperature,
	                  InteriorChannelsPerAssembly, EdgeChannelsPerAssembly, CornerChannelsPerAssembly,
	                  ChannelsPerAssembly, TemperaturePoints, FuelLength, SerpentAxialZones,
	                  CladdingOuterWallAxialTemperature, CladdingInnerWallAxialTemperature, 
	                  FuelRimAxialTemperature, FuelInnerAxialTemperature, AxialTemperaturePoints, Coolant,
	                  Fuel, Cladding, Duct, Bond, ColdFillGasPressure, ReflectorPinMaterial, ShieldPinMaterial,
	                  MetallicFuelPlutoniumFraction, MetallicFuelNonActinideMassFraction, 
	                  SingleInteriorChannelFlowArea, SingleEdgeChannelFlowArea, SingleCornerChannelFlowArea,
	                  AssemblyFlowArea, FTDF, ShieldPinPorosity, CoolantTemperaturePerturbation, DuctTemperaturePerturbation,
	                  CladdingTemperaturePerturbation, FuelTemperaturePerturbation, MetallicFuelUraniumFraction, Burnup, FuelExpansion,
	                  FreshFuelRadius, CladdingInnerRadius):

	AverageAxialCoolantTemperature  = {}	
	AverageAxialCladdingTemperature = {}
	AverageAxialBondTemperature     = {}	
	AverageAxialFuelTemperature     = {}

	RelFlowInterior = SingleInteriorChannelFlowArea * InteriorChannelsPerAssembly / AssemblyFlowArea
	RelFlowEdge     = SingleEdgeChannelFlowArea * EdgeChannelsPerAssembly / AssemblyFlowArea
	RelFlowCorner   = SingleCornerChannelFlowArea * CornerChannelsPerAssembly / AssemblyFlowArea

	for z in TemperaturePoints:
		
		ACT =     RelFlowInterior * CoolantAxialTemperature[z]  \
			   +  RelFlowEdge     * CoolantAxialEdgeTemperature[z] \
			   +  RelFlowCorner   * CoolantAxialCornerTemperature[z]

		ACLT = (CladdingInnerWallAxialTemperature[z] + CladdingOuterWallAxialTemperature[z]) / 2

		AFT  = (FuelInnerAxialTemperature[z] + FuelRimAxialTemperature[z])/2

		ABT  = (FuelRimAxialTemperature[z] + CladdingInnerWallAxialTemperature[z])/2

		ACT2  = {z : ACT}
		ACLT2 = {z : ACLT}
		AFT2  = {z : AFT}
		ABT2  = {z : ABT}

		AverageAxialCoolantTemperature.update(ACT2)	
		AverageAxialCladdingTemperature.update(ACLT2)
		AverageAxialFuelTemperature.update(AFT2)
		AverageAxialBondTemperature.update(ABT2)

	z = -FuelLength/2

	FI = []

	for k,v in FuelInnerAxialTemperature.items():

		FI.append(v)

	FO = []

	for k,v in FuelRimAxialTemperature.items():

		FO.append(v)

	TPoints = len(TemperaturePoints)
	AverageRimTemperature        = sum(FO) / TPoints
	AverageCenterFuelTemperature = sum(FI) / TPoints
	AverageFuelDeltaT = (AverageCenterFuelTemperature - AverageRimTemperature)

	SerpentTemporaryTemperaturePoints = []

	# Calculate until reaching the top of fuel (here, the axial mid-level of fuel is z = 0)
	while z < FuelLength/2 + FuelLength/SerpentAxialZones:
	
		# Rounding the number
		z = round(z,5)
	
		# Collect the evalution point to the list
		SerpentTemporaryTemperaturePoints.append(z)

		# Increment the evaluation point
		z += FuelLength/SerpentAxialZones

	SerpentTemperaturePoints = []

	for i in range(SerpentAxialZones):

		A = round(SerpentTemporaryTemperaturePoints[i],3)
		B = round(SerpentTemporaryTemperaturePoints[i+1],3)
		C = round(((A + B)/2),3)

		SerpentTemperaturePoints.append(C)

	SerpentAxialIAGapTemperature    = []
	SerpentAxialDuctTemperature     = []
	SerpentAxialCoolantTemperature  = []
	SerpentAxialCladdingTemperature = []
	SerpentAxialBondTemperature     = []
	SerpentAxialFuelTemperature     = []

	MaxDiff = 1.5/(AxialTemperaturePoints)

	for SerpentTemperaturePoint in SerpentTemperaturePoints:

		for THTemperaturePoint in TemperaturePoints:
	
			PointDiff = abs(SerpentTemperaturePoint - THTemperaturePoint)
			
			if PointDiff < MaxDiff:

				SerpentAxialIAGapTemperature.append(CoolantAxialEdgeTemperature[THTemperaturePoint]-3)
				SerpentAxialDuctTemperature.append(CoolantAxialEdgeTemperature[THTemperaturePoint])
				SerpentAxialCoolantTemperature.append(AverageAxialCoolantTemperature[THTemperaturePoint])
				SerpentAxialCladdingTemperature.append(AverageAxialCladdingTemperature[THTemperaturePoint])
				SerpentAxialFuelTemperature.append(AverageAxialFuelTemperature[THTemperaturePoint])
				SerpentAxialBondTemperature.append(AverageAxialBondTemperature[THTemperaturePoint])

				break

	SerpentAxialCladdingDensity = []
	SerpentPerturbedAxialCladdingDensity = []

	for Temperature in SerpentAxialCladdingTemperature:

		CladdingProperties     = nonfuelsolidproperties(material=Cladding, temperature=Temperature, fastflux=1, stress=1, dpa=1, porosity=1)
		SerpentCladdingDensity = CladdingProperties.density

		if CladdingTemperaturePerturbation == "Void" or CladdingTemperaturePerturbation == "void":

			SerpentPerturbedCladdingDensity = 1e-30

		else:

			PerturbedCladdingProperties = nonfuelsolidproperties(material=Cladding, temperature=(Temperature + CladdingTemperaturePerturbation), fastflux=1, stress=1, dpa=1, porosity=1)
			SerpentPerturbedCladdingDensity = PerturbedCladdingProperties.density			

		SerpentAxialCladdingDensity.append(SerpentCladdingDensity)
		SerpentPerturbedAxialCladdingDensity.append(SerpentPerturbedCladdingDensity)

	AverageCladdingDensity = sum(SerpentAxialCladdingDensity)/len(SerpentTemperaturePoints)

	SerpentAxialDuctDensity = []
	SerpentPerturbedAxialDuctDensity = []

	for Temperature in SerpentAxialDuctTemperature:

		DuctProperties     = nonfuelsolidproperties(material=Duct, temperature=Temperature, fastflux=1, stress=1, dpa=1, porosity=1)
		SerpentDuctDensity = DuctProperties.density

		if DuctTemperaturePerturbation == "Void" or DuctTemperaturePerturbation == "void":

			SerpentPerturbedDuctDensity = 1e-30

		else:

			PerturbedDuctProperties = nonfuelsolidproperties(material=Duct, temperature=(Temperature + DuctTemperaturePerturbation), fastflux=1, stress=1, dpa=1, porosity=1)
			SerpentPerturbedDuctDensity = PerturbedDuctProperties.density			

		SerpentAxialDuctDensity.append(SerpentDuctDensity)
		SerpentPerturbedAxialDuctDensity.append(SerpentPerturbedDuctDensity)	

	AverageDuctDensity = sum(SerpentAxialDuctDensity)/len(SerpentTemperaturePoints)

	SerpentAxialReflectorDensity = []

	print(SerpentAxialDuctTemperature)

	for Temperature in SerpentAxialDuctTemperature:

		ReflectorProperties     = nonfuelsolidproperties(material=ReflectorPinMaterial, temperature=Temperature, fastflux=1, stress=1, dpa=1, porosity=1)
		SerpentReflectorDensity = ReflectorProperties.density

		SerpentAxialReflectorDensity.append(SerpentReflectorDensity)		

	SerpentAxialShieldDensity = []

	for Temperature in SerpentAxialDuctTemperature:

		ShieldProperties     = nonfuelsolidproperties(material=ShieldPinMaterial, temperature=Temperature, fastflux=1, stress=1, dpa=1, porosity=ShieldPinPorosity)
		SerpentShieldDensity = ShieldProperties.density

		SerpentAxialShieldDensity.append(SerpentShieldDensity)		

	SerpentAxialCoolantDensity = []
	SerpentPerturbedAxialCoolantDensity = []

	for Temperature in SerpentAxialCoolantTemperature:

		CoolantProperties     = nonsolids(material=Coolant, temperature=Temperature, pressure=0)
		SerpentCoolantDensity = CoolantProperties.density

		if CoolantTemperaturePerturbation == "Void" or CoolantTemperaturePerturbation == "void":

			SerpentPerturbedCoolantDensity = 1e-30

		else:

			PerturbedCoolantProperties     = nonsolids(material=Coolant, temperature=Temperature+CoolantTemperaturePerturbation, pressure=0)
			SerpentPerturbedCoolantDensity = PerturbedCoolantProperties.density

		SerpentAxialCoolantDensity.append(SerpentCoolantDensity)
		SerpentPerturbedAxialCoolantDensity.append(SerpentPerturbedCoolantDensity)

	SerpentAxialIAGapDensity = []
	SerpentPerturbedAxialIAGapDensity = []

	for Temperature in SerpentAxialIAGapTemperature:

		IAGapProperties     = nonsolids(material=Coolant, temperature=Temperature, pressure=0)
		SerpentIAGapDensity = IAGapProperties.density

		if CoolantTemperaturePerturbation == "Void" or CoolantTemperaturePerturbation == "void":

			SerpentPerturbedIAGapDensity = 1e-30

		else:

			PerturbedIAGapProperties     = nonsolids(material=Coolant, temperature=Temperature+CoolantTemperaturePerturbation, pressure=0)
			SerpentPerturbedIAGapDensity = PerturbedIAGapProperties.density

		SerpentAxialIAGapDensity.append(SerpentIAGapDensity)
		SerpentPerturbedAxialIAGapDensity.append(SerpentPerturbedIAGapDensity)

	SerpentAxialBondDensity = []

	for Temperature in SerpentAxialBondTemperature:

		BondProperties     = nonsolids(material=Bond, temperature=Temperature, pressure=ColdFillGasPressure)
		SerpentBondDensity = BondProperties.density

		SerpentAxialBondDensity.append(SerpentBondDensity)		

	AverageBondDensity = sum(SerpentAxialBondDensity)/len(SerpentTemperaturePoints)

	SerpentAxialFuelDensity = []
	SerpentPerturbedAxialFuelDensity = []

	FreeExpansionDensity = 1e-30

	for Temperature in SerpentAxialFuelTemperature:

		FuelProperties     = fuelproperties(material=Fuel, temperature=Temperature, FTDF=FTDF, expansion="all", WU=MetallicFuelUraniumFraction, WPu=MetallicFuelPlutoniumFraction, Wzr=MetallicFuelNonActinideMassFraction, Burnup=Burnup, mode=1, indensity=1, intemperature=1)
		SerpentFuelDensity = FuelProperties.density
		AlphaFuel          = FuelProperties.averagelinearthermalexpansioncoefficient

		if FuelTemperaturePerturbation != "void" and FuelTemperaturePerturbation != "Void":	

			PerturbedFuelProperties = fuelproperties(material=Fuel, temperature=(Temperature + FuelTemperaturePerturbation), FTDF=FTDF, expansion=FuelExpansion, WU=MetallicFuelUraniumFraction, WPu=MetallicFuelPlutoniumFraction, Wzr=MetallicFuelNonActinideMassFraction, Burnup=Burnup, mode="perturbation", indensity=SerpentFuelDensity, intemperature=Temperature)
			FreeExpansionDensity = PerturbedFuelProperties.density
			SerpentPerturbedFuelDensity = FreeExpansionDensity

			if FuelExpansion != "none" and FuelExpansion != "Axial" and FuelExpansion != "axial" and FuelExpansion != "AXIAL":

				FuelRadiusX = FreshFuelRadius * (1 + AlphaFuel*FuelTemperaturePerturbation)

				if FuelRadiusX > CladdingInnerRadius:
	
					FuelRadius = CladdingInnerRadius
					SerpentPerturbedFuelDensity = (FuelRadius ** 2) / (FuelRadiusX ** 2) * FreeExpansionDensity
	
				else:
	
					SerpentPerturbedFuelDensity = FreeExpansionDensity

		else:	

			SerpentPerturbedFuelDensity = 1e-30
			FreeExpansionDensity = 1e-30

		SerpentAxialFuelDensity.append(SerpentFuelDensity)	
		SerpentPerturbedAxialFuelDensity.append(SerpentPerturbedFuelDensity)		

	AverageFuelDensity           = sum(SerpentAxialFuelDensity)/len(SerpentTemperaturePoints)
	PerturbedAverageFuelDensity  = sum(SerpentPerturbedAxialFuelDensity)/len(SerpentTemperaturePoints)	
	FuelAverageTemperature       = sum(SerpentAxialFuelTemperature)/SerpentAxialZones

	return(SerpentAxialIAGapTemperature, SerpentAxialDuctTemperature, SerpentAxialCoolantTemperature,
		   SerpentAxialCladdingTemperature, SerpentAxialBondTemperature, SerpentAxialFuelTemperature,
		   SerpentAxialCoolantDensity, SerpentAxialIAGapDensity, SerpentAxialCladdingDensity,
		   SerpentAxialDuctDensity, SerpentAxialBondDensity, SerpentAxialFuelDensity,
		   SerpentTemperaturePoints, SerpentAxialReflectorDensity, SerpentAxialShieldDensity, AverageBondDensity, 
		   AverageDuctDensity, AverageCladdingDensity, SerpentPerturbedAxialCoolantDensity,
		   SerpentPerturbedAxialFuelDensity, FuelAverageTemperature, AverageFuelDeltaT, SerpentPerturbedAxialCladdingDensity,
		   AverageFuelDensity, FreeExpansionDensity, PerturbedAverageFuelDensity)



