def systemgeometry(LowerCoolantPlenaLength, BelowCoreChannelLength, FuelLength, AboveCoreChannelLength,
				   IHXLength, IHXToTop, ThermalCenterElevation, InternalRadialComponentWidth, CoreDiameter,
				   SystemDiameter, PrimaryVesselThickness):

	CoreAssemblyLength  = BelowCoreChannelLength + FuelLength + AboveCoreChannelLength
	TotalSystemDiameter = SystemDiameter + InternalRadialComponentWidth*2 + PrimaryVesselThickness*2
	TotalSystemHeight   = LowerCoolantPlenaLength + CoreAssemblyLength + ThermalCenterElevation + (IHXLength/2) + IHXToTop
	
	return(TotalSystemHeight, TotalSystemDiameter)