def tempplot(FuelLength, Name, mlabpath):

	temps = open(mlabpath + "/hotchannel_temperatures.m", 'w')
	
	temps.write("coolant_temperature;")
	temps.write("cladding_outer_temperature;")
	temps.write("cladding_inner_temperature;")
	temps.write("fuel_outer_temperature;")
	temps.write("fuel_inner_temperature;")
	temps.write("\n")
	temps.write("figure1 = figure;")
	temps.write("axes1 = axes('Parent',figure1,'YGrid','on','XGrid','on','FontSize',24,'FontName','Times New Roman');")
	temps.write("xlim(axes1,[" + str(-FuelLength/2) + " " + str(FuelLength/2) + "]);")
	temps.write("box(axes1,'on');hold(axes1,'all');")
	temps.write("plot1 = plot(z,cz,z,cot,z,cit,z,git,z,fit,'Parent',axes1,'LineWidth',3);")
	temps.write("set(plot1(1),'DisplayName','Bulk coolant');set(plot1(2),'DisplayName','Cladding outer wall','Color',[0 0 0]);set(plot1(3),'Color',[0 0.498039215803146 0],'DisplayName','Cladding inner wall');set(plot1(4),'Color',[0.0392156876623631 0.141176477074623 0.415686279535294],'DisplayName','Fuel rim');set(plot1(5),'Color',[1 0 0],'DisplayName','Fuel centerline');xlabel('Core axial position (m)','FontSize',30,'FontName','Times New Roman');ylabel('Temperature (deg. C)','FontSize',30,'FontName','Times New Roman');legend1 = legend(axes1,'show');set(legend1,'Location','NorthEastOutside');")
	
	temps.close	