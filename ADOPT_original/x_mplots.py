from pylab import *
import os

def mplotting(CoolantTemperatureZ2, CoolantEdgeTemperatureZ2,CoolantEdgeHeatCapacityZ2,CoolantEdgeDensityZ2,
	          CoolantEdgeDynamicViscosityZ2, CoolantEdgeConductivityZ2, CoolantEdgeKinematicViscosityZ2,CoolantCornerTemperatureZ2,
	          CoolantCornerHeatCapacityZ2,CoolantCornerDensityZ2, CoolantCornerDynamicViscosityZ2,CoolantCornerConductivityZ2,
	          CoolantCornerKinematicViscosityZ2, CoolantHeatCapacityZ2, CoolantDensityZ2,CoolantDynamicViscosityZ2,CoolantConductivityZ2,
	          CoolantKinematicViscosityZ2, CoolantInteriorPecletZ2, CoolantEdgePecletZ2,CoolantCornerPecletZ2,CoolantInteriorNusseltZ2,
	          CoolantEdgeNusseltZ2,CoolantCornerNusseltZ2, CoolantInteriorHeatTransferCoefficientZ2,CoolantEdgeHeatTransferCoefficientZ2,
	          CoolantCornerHeatTransferCoefficientZ2, CoolantInteriorReynoldsZ2,CoolantEdgeReynoldsZ2,CoolantCornerReynoldsZ2,
	          CladdingOuterWallTemperatureZ2, matplotlibpath, FuelLength, TemperaturePointsZ, FuelInnerAxialTemperatureZ2,
	          FuelRimAxialTemperatureZ2, CladdingInnerWallTemperatureZ2, PeakFuelInnerTemperature, PeakFuelInnerTemperateAxialPosition):

	SkipInitialPoints = 3
	FigureDPI         = 300
	FigureXsize       = 10
	FigureYsize       = 6
	Linewidth         = 2.5
	Linecolor         = "black"
	Linestyle         = "-"

	plotpath = matplotlibpath + "/"
	plotcoolantpath = matplotlibpath + "/coolant_properties/"
	plottemp = matplotlibpath + "/temperatures/"

	if not os.path.exists(plotcoolantpath): os.makedirs(plotcoolantpath)
	if not os.path.exists(plottemp): os.makedirs(plottemp)

	TemperaturePointsZ                  = TemperaturePointsZ[SkipInitialPoints:]
	FuelInnerAxialTemperatureZ2         = FuelInnerAxialTemperatureZ2[SkipInitialPoints:]
	FuelRimAxialTemperatureZ2           = FuelRimAxialTemperatureZ2[SkipInitialPoints:]
	CladdingInnerWallTemperatureZ2      = CladdingInnerWallTemperatureZ2[SkipInitialPoints:]
	CladdingOuterWallTemperatureZ2      = CladdingOuterWallTemperatureZ2[SkipInitialPoints:]
	CoolantTemperatureZ2                = CoolantTemperatureZ2[SkipInitialPoints:]
	CoolantDensityZ2                    = CoolantDensityZ2[SkipInitialPoints:]
	CoolantHeatCapacityZ2               = CoolantHeatCapacityZ2[SkipInitialPoints:]
	CoolantDynamicViscosityZ2           = CoolantDynamicViscosityZ2[SkipInitialPoints:]
	CoolantConductivityZ2               = CoolantConductivityZ2[SkipInitialPoints:]
	CoolantKinematicViscosityZ2         = CoolantKinematicViscosityZ2[SkipInitialPoints:]
	CoolantInteriorPecletZ2             = CoolantInteriorPecletZ2[SkipInitialPoints:]
	CoolantInteriorNusseltZ2            = CoolantInteriorNusseltZ2[SkipInitialPoints:]
	CoolantInteriorReynoldsZ2           = CoolantInteriorReynoldsZ2[SkipInitialPoints:]
	InteriorHeatTransferCoefficientZ2   = CoolantInteriorHeatTransferCoefficientZ2[SkipInitialPoints:]
  
	CoolantEdgeTemperatureZ2            = CoolantEdgeTemperatureZ2[SkipInitialPoints:]
	CoolantEdgeDensityZ2                = CoolantEdgeDensityZ2[SkipInitialPoints:]
	CoolantEdgeHeatCapacityZ2           = CoolantEdgeHeatCapacityZ2[SkipInitialPoints:]
	CoolantEdgeDynamicViscosityZ2       = CoolantEdgeDynamicViscosityZ2[SkipInitialPoints:]
	CoolantEdgeConductivityZ2           = CoolantEdgeConductivityZ2[SkipInitialPoints:]
	CoolantEdgeKinematicViscosityZ2     = CoolantEdgeKinematicViscosityZ2[SkipInitialPoints:]
	CoolantEdgePecletZ2                 = CoolantEdgePecletZ2[SkipInitialPoints:]
	CoolantEdgeNusseltZ2                = CoolantEdgeNusseltZ2[SkipInitialPoints:]
	CoolantEdgeReynoldsZ2               = CoolantEdgeReynoldsZ2[SkipInitialPoints:]
	EdgeHeatTransferCoefficientZ2       = CoolantEdgeHeatTransferCoefficientZ2[SkipInitialPoints:]	

	CoolantCornerTemperatureZ2          = CoolantCornerTemperatureZ2[SkipInitialPoints:]
	CoolantCornerDensityZ2              = CoolantCornerDensityZ2[SkipInitialPoints:]
	CoolantCornerHeatCapacityZ2         = CoolantCornerHeatCapacityZ2[SkipInitialPoints:]
	CoolantCornerDynamicViscosityZ2     = CoolantCornerDynamicViscosityZ2[SkipInitialPoints:]
	CoolantCornerConductivityZ2         = CoolantCornerConductivityZ2[SkipInitialPoints:]
	CoolantCornerKinematicViscosityZ2   = CoolantCornerKinematicViscosityZ2[SkipInitialPoints:]
	CoolantCornerPecletZ2               = CoolantCornerPecletZ2[SkipInitialPoints:]
	CoolantCornerNusseltZ2              = CoolantCornerNusseltZ2[SkipInitialPoints:]
	CoolantCornerReynoldsZ2             = CoolantCornerReynoldsZ2[SkipInitialPoints:]
	CornerHeatTransferCoefficientZ2     = CoolantCornerHeatTransferCoefficientZ2[SkipInitialPoints:]		

	################################################################################################### //// ######## //// #######
	##################### Plot temperatures ########################################################### //// ######## //// #######
	################################################################################################### //// ######## //// #######

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)

	Ymin = 0.95 * min(CoolantTemperatureZ2)
	Ymax = 1.10 * max(FuelInnerAxialTemperatureZ2)

	Xmax = FuelLength * 1.05
	Xmin = -FuelLength * 0.05

	Xpeak = PeakFuelInnerTemperateAxialPosition + FuelLength/2
	Ypeak = PeakFuelInnerTemperature - 273.15

	plot(TemperaturePointsZ, FuelInnerAxialTemperatureZ2, color="red", linewidth=2.5, linestyle="-", label="Fuel centerline")
	plot(TemperaturePointsZ, FuelRimAxialTemperatureZ2, color="green", linewidth=2.5, linestyle="-", label="Fuel outer rim")
	plot(TemperaturePointsZ, CladdingInnerWallTemperatureZ2, color="black", linewidth=2.5, linestyle="-", label="Cladding inner wall")
	plot(TemperaturePointsZ, CladdingOuterWallTemperatureZ2, color="0.75", linewidth=2.5, linestyle="-", label="Cladding outer wall")
	plot(TemperaturePointsZ, CoolantTemperatureZ2, color="blue", linewidth=2.5, linestyle="-", label="Bulk coolant")

	plot([Xpeak,Xpeak],[Ymin,Ypeak], color ='red', linewidth=2.5, linestyle="--")
	scatter([Xpeak,],[Ypeak,], 50, color ='red')

	legend(loc='upper left')
	ylim(Ymin, Ymax)
	xlim(Xmin, Xmax)

	xlabel("Axial position in active core (m)")
	ylabel("Temperature (deg. C)")

	grid(True)

	annotate(r'{0:02.1f}'.format(Ypeak) + ' deg. C',
    xy=(Xpeak, Ypeak), xycoords='data',
    xytext=(+10, +30), textcoords='offset points', fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

	savefig(plottemp + "InteriorChannelTemperatures.png",dpi=FigureDPI)

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant density ######################################################## //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantDensityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Density (kg/m^3)")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorDensity.png",dpi=FigureDPI)

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant heat capacity ################################################## //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantHeatCapacityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Heat capacity (J/kg*K)")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorHeatCapacity.png",dpi=FigureDPI)

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot dynamic viscosity ###################################################### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantDynamicViscosityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Dynamic viscosity (Pa*s)")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorDynamicViscosity.png",dpi=FigureDPI)

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant conductivity ################################################### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantConductivityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Coolant conductivity (W/(m*K))")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorConductivity.png",dpi=FigureDPI)

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot kinematic viscosity #################################################### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantKinematicViscosityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Coolant kinematic viscosity (Pa * s / K)")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorKinematicViscosity.png",dpi=FigureDPI)

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant interior channel Peclet ######################################## //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantInteriorPecletZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Coolant interior channel Peclet number")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorPeclet.png",dpi=FigureDPI)	

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant interior channel Nusselt ####################################### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantInteriorNusseltZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Coolant interior channel Nusselt number")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorNusselt.png",dpi=FigureDPI)	

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant interior channel Reynolds ###################################### //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, CoolantInteriorReynoldsZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Coolant interior channel Reynolds number")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorReynolds.png",dpi=FigureDPI)	

	close()

	################################################################################################### //// ######## //// #######
	##################### Plot coolant-to-cladding heat transfer coefficient ########################## //// ######## //// #######
	################################################################################################### //// ######## //// #######	

	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	plot(TemperaturePointsZ, InteriorHeatTransferCoefficientZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)

	xlabel("Axial position in active core (m)")
	ylabel("Heat transfer coefficient (W/m^2)")

	grid(True)

	savefig(plotcoolantpath + "CoolantInteriorHeatTransferCoefficient.png",dpi=FigureDPI)	

	close()

	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant density ######################################################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeDensityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Density (kg/m^3)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeDensity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant heat capacity ################################################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeHeatCapacityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Heat capacity (J/kg*K)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeHeatCapacity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot dynamic viscosity ###################################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeDynamicViscosityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Dynamic viscosity (Pa*s)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeDynamicViscosity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant conductivity ################################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeConductivityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant conductivity (W/(m*K))")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeConductivity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot kinematic viscosity #################################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeKinematicViscosityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant kinematic viscosity (Pa * s / K)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeKinematicViscosity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant interior channel Peclet ######################################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgePecletZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant interior channel Peclet number")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgePeclet.png",dpi=FigureDPI)	
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant interior channel Nusselt ####################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeNusseltZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant interior channel Nusselt number")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeNusselt.png",dpi=FigureDPI)	
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant interior channel Reynolds ###################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantEdgeReynoldsZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant interior channel Reynolds number")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeReynolds.png",dpi=FigureDPI)	
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant-to-cladding heat transfer coefficient ########################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, EdgeHeatTransferCoefficientZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Heat transfer coefficient (W/m^2)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantEdgeHeatTransferCoefficient.png",dpi=FigureDPI)		
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant density ######################################################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerDensityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Density (kg/m^3)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerDensity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant heat capacity ################################################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerHeatCapacityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Heat capacity (J/kg*K)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerHeatCapacity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot dynamic viscosity ###################################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerDynamicViscosityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Dynamic viscosity (Pa*s)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerDynamicViscosity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant conductivity ################################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerConductivityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant conductivity (W/(m*K))")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerConductivity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot kinematic viscosity #################################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerKinematicViscosityZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant kinematic viscosity (Pa * s / K)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerKinematicViscosity.png",dpi=FigureDPI)
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant interior channel Peclet ######################################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerPecletZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant interior channel Peclet number")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerPeclet.png",dpi=FigureDPI)	
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant interior channel Nusselt ####################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerNusseltZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant interior channel Nusselt number")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerNusselt.png",dpi=FigureDPI)	
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant interior channel Reynolds ###################################### //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CoolantCornerReynoldsZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Coolant interior channel Reynolds number")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerReynolds.png",dpi=FigureDPI)	
#	
	#	close()
#	
	#	################################################################################################### //// ######## //// #######
	#	##################### Plot coolant-to-cladding heat transfer coefficient ########################## //// ######## //// #######
	#	################################################################################################### //// ######## //// #######	
#	
	#	figure(figsize=(FigureXsize,FigureYsize), dpi=FigureDPI)
	#	plot(TemperaturePointsZ, CornerHeatTransferCoefficientZ2, color=Linecolor, linewidth=Linewidth, linestyle=Linestyle)
#	
	#	xlabel("Axial position in active core (m)")
	#	ylabel("Heat transfer coefficient (W/m^2)")
#	
	#	grid(True)
#	
	#	savefig(plotcoolantpath + "CoolantCornerHeatTransferCoefficient.png",dpi=FigureDPI)	
#	
	#	close()
