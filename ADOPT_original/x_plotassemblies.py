def plota(FreshFuelRadius, CladdingInnerRadius, CladdingOuterRadius, Pitch, InnerAssemblySideLength, 
	      DuctedAssemblySideLength, Name, AssemblyHexagonSideLength, PinsPerAssembly):

	print("SERPENT -- Plotting fuel assembly")

	fname = Name + "_fuelass" 
	smr = open(fname, 'w')
	
	smr.write("\n \n")
	smr.write("pin 1            % fuel pin \n")
	smr.write("fuel1 {0:02.7f}".format(FreshFuelRadius*100)     + "  % fuel pellet outer radius \n")
	smr.write("gap   {0:02.7f}".format(CladdingInnerRadius*100) + "  % cladding inner radius    \n")
	smr.write("clad  {0:02.7f}".format(CladdingOuterRadius*100) + "  % cladding outer radius    \n")
	smr.write("coolant      % coolant outside of clad  \n")
	smr.write("\n")
	
	smr.write("pin 9            % dummy pin for filling of lattice\n")
	smr.write("coolant \n")
	smr.write("\n")
	smr.write("\n")

	if PinsPerAssembly == 19:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 1 1 1 9 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 1 1 1 1 9 9 9 9 9 \n")
		smr.write("        9 9 9 9 9 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("          9 9 9 9 9 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("           9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 37:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 1 1 1 1 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 1 1 1 1 1 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("        9 9 9 9 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("         9 9 9 9 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("           9 9 9 9 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 61:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 1 1 1 1 1 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 1 1 1 1 1 1 9 9 9 \n")
		smr.write("      9 9 9 9 9 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("       9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("        9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("         9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("          9 9 9 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 91:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 1 1 1 1 1 1 9 9 \n")
		smr.write("    9 9 9 9 9 9 1 1 1 1 1 1 1 9 9 \n")
		smr.write("     9 9 9 9 9 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("      9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("       9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("        9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("         9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("          9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("           9 9 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("             9 9 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	elif PinsPerAssembly == 127:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("          9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("           9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("            9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	elif PinsPerAssembly == 169:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("        9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("         9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("          9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("           9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("            9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("             9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 217:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("        9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("         9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("          9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("           9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("            9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("             9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("              9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("               9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 271:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("        9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("             9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("              9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("               9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 331:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("          9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("           9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("            9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("               9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("                9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                  9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                   9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif PinsPerAssembly == 397:
	
		smr.write("lat  10 2   0.0 0.0 25 25 {0:02.7f}".format(Pitch*100) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("               9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("                9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("                 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                  9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                   9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                    9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                     9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                      9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                       9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                        9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                         9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	smr.write("surf 1 hexyc 0.0 0.0 {0:02.7f}".format(InnerAssemblySideLength)   + "  % Wrapper tube inner radius\n")
	smr.write("surf 2 hexyc 0.0 0.0 {0:02.7f}".format(DuctedAssemblySideLength)  + "  % Wrapper tube outer radius\n")
	smr.write("surf 3 hexyc 0.0 0.0 {0:02.7f}".format(AssemblyHexagonSideLength) + "\n")

	smr.write("surf 4 pz -10 \n")
	smr.write("surf 5 pz  10 \n")

	smr.write("cell  1  0  fill 10    -1          4 -5 %\n")
	smr.write("cell  4  0  duct        1    -2    4 -5 %\n")
	smr.write("cell  5  0  coolant     2    -3    4 -5 %\n")
	smr.write("cell 94  0  outside           3    4 -5 %\n")
	smr.write("cell 95  0  outside           3   -4    %\n")
	smr.write("cell 96  0  outside           3    5    %\n")
	smr.write("cell 97  0  outside          -3   -4    %\n")
	smr.write("cell 98  0  outside          -3    5    %\n")
	
	smr.write("plot 3 5000 5000\n")	

	smr.write("mat fuel1 -10.43 rgb 255 28 0 \n")
	smr.write("   8016.12c 2.00\n")
	smr.write("  92235.12c 0.20\n")
	smr.write("  92238.12c 0.80\n")

	smr.write("mat gap -10.43\n")
	smr.write("   8016.12c 2.00\n")
	
	smr.write("mat clad -7.9    rgb 1 1 1                % Cladding steel (15-15Ti)\n")
	smr.write("  6000.06c   -0.09\n")
	smr.write(" 14000.06c   -0.85\n")
	smr.write(" 22000.06c   -0.40\n")
	smr.write(" 24000.06c  -14.50\n")
	smr.write(" 25055.06c   -1.50\n")
	smr.write(" 26000.06c  -65.35\n")
	smr.write(" 28000.06c  -15.50\n")
	smr.write(" 42000.06c   -1.50\n")

	smr.write("mat duct -7.6    rgb 1 1 1                % Wrapper tube steel (T91)\n")
	smr.write(" 14028.06c  -0.5000\n")
	smr.write(" 23000.06c  -0.2000\n")
	smr.write(" 24050.06c  -0.3757\n")
	smr.write(" 24052.06c  -7.5330\n")
	smr.write(" 24053.06c  -0.8706\n")
	smr.write(" 24054.06c  -0.2207\n")
	smr.write(" 25055.06c  -0.6000\n")
	smr.write(" 26054.06c  -5.0380\n")
	smr.write(" 26056.06c -81.2131\n")
	smr.write(" 26057.06c  -1.8926\n")
	smr.write(" 26058.06c  -0.2564\n")
	smr.write(" 28058.06c  -0.1348\n")
	smr.write(" 28060.06c  -0.0534\n")
	smr.write(" 28061.06c  -0.0024\n")
	smr.write(" 28062.06c  -0.0076\n")
	smr.write(" 28064.06c  -0.0018\n")
	smr.write(" 41093.06c  -0.1000\n")
	smr.write(" 42092.06c  -0.1422\n")
	smr.write(" 42094.06c  -0.0905\n")
	smr.write(" 42095.06c  -0.1575\n")
	smr.write(" 42096.06c  -0.1667\n")
	smr.write(" 42097.06c  -0.0965\n")
	smr.write(" 42098.06c  -0.2465\n")
	smr.write(" 42100.06c  -0.1000\n")	
	
	smr.write("mat coolant -10.545 rgb 163 198 239 \n")
	smr.write("82204.06c  -0.0061\n")
	smr.write("82206.06c  -0.1074\n")
	smr.write("82207.06c  -0.0985\n")
	smr.write("82208.06c  -0.2328\n")
	smr.write("set pop 1000 10 10\n")
	smr.write("set acelib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7u_MP.xsdata\"\n")
	smr.write("set declib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.dec\"\n")
	smr.write("set nfylib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.nfy\"\n")	

	return fname

def plotr(ReflectorPinOuterRadius, ReflectorPinInnerRadius, ReflectorPinPitch, ReflectorPinSlugRadius, InnerAssemblySideLength, 
	      DuctedAssemblySideLength, Name, AssemblyHexagonSideLength, PinsPerAssembly, ReflectorPinsPerAssembly):

	print("SERPENT -- Plotting reflector assembly")

	radname = Name + "_reflass" 
	smr = open(radname, 'w')
	
	smr.write("\n \n")
	smr.write("pin 1            % fuel pin \n")
	smr.write("fuel1 {0:02.7f}".format(ReflectorPinSlugRadius)  + "  % fuel pellet outer radius \n")
	smr.write("void  {0:02.7f}".format(ReflectorPinInnerRadius) + "  % cladding inner radius    \n")
	smr.write("clad  {0:02.7f}".format(ReflectorPinOuterRadius) + "  % cladding outer radius    \n")
	smr.write("coolant      % coolant outside of clad  \n")
	smr.write("\n")
	
	smr.write("pin 9            % dummy pin for filling of lattice\n")
	smr.write("coolant \n")
	smr.write("\n")
	smr.write("\n")

	if ReflectorPinsPerAssembly == 19:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 1 1 1 9 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 1 1 1 1 9 9 9 9 9 \n")
		smr.write("        9 9 9 9 9 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("          9 9 9 9 9 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("           9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 37:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 1 1 1 1 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 1 1 1 1 1 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("        9 9 9 9 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("         9 9 9 9 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("           9 9 9 9 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 61:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 1 1 1 1 1 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 1 1 1 1 1 1 9 9 9 \n")
		smr.write("      9 9 9 9 9 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("       9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("        9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("         9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("          9 9 9 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 91:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 1 1 1 1 1 1 9 9 \n")
		smr.write("    9 9 9 9 9 9 1 1 1 1 1 1 1 9 9 \n")
		smr.write("     9 9 9 9 9 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("      9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("       9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("        9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("         9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("          9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("           9 9 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("             9 9 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	elif ReflectorPinsPerAssembly == 127:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("          9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("           9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("            9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	elif ReflectorPinsPerAssembly == 169:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("        9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("         9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("          9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("           9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("            9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("             9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 217:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("        9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("         9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("          9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("           9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("            9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("             9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("              9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("               9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 271:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("        9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("             9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("              9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("               9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 331:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("          9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("           9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("            9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("               9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("                9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                  9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                   9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ReflectorPinsPerAssembly == 397:
	
		smr.write("lat  10 2   0.0 0.0 25 25 {0:02.7f}".format(ReflectorPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("               9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("                9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("                 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                  9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                   9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                    9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                     9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                      9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                       9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                        9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                         9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")		

	smr.write("surf 1 hexyc 0.0 0.0 {0:02.7f}".format(InnerAssemblySideLength)   + "  % Wrapper tube inner radius\n")
	smr.write("surf 2 hexyc 0.0 0.0 {0:02.7f}".format(DuctedAssemblySideLength)  + "  % Wrapper tube outer radius\n")
	smr.write("surf 3 hexyc 0.0 0.0 {0:02.7f}".format(AssemblyHexagonSideLength) + "\n")

	smr.write("surf 4 pz -10 \n")
	smr.write("surf 5 pz  10 \n")

	smr.write("cell  1  0  fill 10    -1          4 -5 %\n")
	smr.write("cell  4  0  duct        1    -2    4 -5 %\n")
	smr.write("cell  5  0  coolant     2    -3    4 -5 %\n")
	smr.write("cell 94  0  outside           3    4 -5 %\n")
	smr.write("cell 95  0  outside           3   -4    %\n")
	smr.write("cell 96  0  outside           3    5    %\n")
	smr.write("cell 97  0  outside          -3   -4    %\n")
	smr.write("cell 98  0  outside          -3    5    %\n")
	
	smr.write("plot 3 5000 5000\n")	

	smr.write("mat fuel1 -10.43\n")
	smr.write("   8016.12c 2.00\n")
	smr.write("  92235.12c 0.20\n")
	smr.write("  92238.12c 0.80\n")
	
	smr.write("mat clad -7.9  rgb 1 1 1                  % Cladding steel (15-15Ti)\n")
	smr.write("  6000.06c   -0.09\n")
	smr.write(" 14000.06c   -0.85\n")
	smr.write(" 22000.06c   -0.40\n")
	smr.write(" 24000.06c  -14.50\n")
	smr.write(" 25055.06c   -1.50\n")
	smr.write(" 26000.06c  -65.35\n")
	smr.write(" 28000.06c  -15.50\n")
	smr.write(" 42000.06c   -1.50\n")

	smr.write("mat duct -7.6 rgb 1 1 1                   % Wrapper tube steel (T91)\n")
	smr.write(" 14028.06c  -0.5000\n")
	smr.write(" 23000.06c  -0.2000\n")
	smr.write(" 24050.06c  -0.3757\n")
	smr.write(" 24052.06c  -7.5330\n")
	smr.write(" 24053.06c  -0.8706\n")
	smr.write(" 24054.06c  -0.2207\n")
	smr.write(" 25055.06c  -0.6000\n")
	smr.write(" 26054.06c  -5.0380\n")
	smr.write(" 26056.06c -81.2131\n")
	smr.write(" 26057.06c  -1.8926\n")
	smr.write(" 26058.06c  -0.2564\n")
	smr.write(" 28058.06c  -0.1348\n")
	smr.write(" 28060.06c  -0.0534\n")
	smr.write(" 28061.06c  -0.0024\n")
	smr.write(" 28062.06c  -0.0076\n")
	smr.write(" 28064.06c  -0.0018\n")
	smr.write(" 41093.06c  -0.1000\n")
	smr.write(" 42092.06c  -0.1422\n")
	smr.write(" 42094.06c  -0.0905\n")
	smr.write(" 42095.06c  -0.1575\n")
	smr.write(" 42096.06c  -0.1667\n")
	smr.write(" 42097.06c  -0.0965\n")
	smr.write(" 42098.06c  -0.2465\n")
	smr.write(" 42100.06c  -0.1000\n")	
	
	smr.write("mat coolant -10.545 rgb 163 198 239 \n")
	smr.write("82204.06c  -0.0061\n")
	smr.write("82206.06c  -0.1074\n")
	smr.write("82207.06c  -0.0985\n")
	smr.write("82208.06c  -0.2328\n")
	smr.write("set pop 1000 10 10\n")
	smr.write("set acelib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7u_MP.xsdata\"\n")
	smr.write("set declib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.dec\"\n")
	smr.write("set nfylib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.nfy\"\n")	

	return radname

def plotsh(ShieldPinOuterRadius, ShieldPinInnerRadius, ShieldPinPitch, ShieldPinSlugRadius, InnerAssemblySideLength, 
	      DuctedAssemblySideLength, Name, AssemblyHexagonSideLength, PinsPerAssembly, ShieldPinsPerAssembly):

	print("SERPENT -- Plotting shield assembly")

	shname = Name + "_shieldlass" 
	smr = open(shname, 'w')
	
	smr.write("\n \n")
	smr.write("pin 1            % fuel pin \n")
	smr.write("fuel1 {0:02.7f}".format(ShieldPinSlugRadius)  + "  % fuel pellet outer radius \n")
	smr.write("void  {0:02.7f}".format(ShieldPinInnerRadius) + "  % cladding inner radius    \n")
	smr.write("clad  {0:02.7f}".format(ShieldPinOuterRadius) + "  % cladding outer radius    \n")
	smr.write("coolant      % coolant outside of clad  \n")
	smr.write("\n")
	
	smr.write("pin 9            % dummy pin for filling of lattice\n")
	smr.write("coolant \n")
	smr.write("\n")
	smr.write("\n")

	if ShieldPinsPerAssembly == 19:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 1 1 1 9 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 1 1 1 1 9 9 9 9 9 \n")
		smr.write("        9 9 9 9 9 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("          9 9 9 9 9 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("           9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ShieldPinsPerAssembly == 37:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 1 1 1 1 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 1 1 1 1 1 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("        9 9 9 9 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("         9 9 9 9 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("           9 9 9 9 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ShieldPinsPerAssembly == 61:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 1 1 1 1 1 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 1 1 1 1 1 1 9 9 9 \n")
		smr.write("      9 9 9 9 9 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("       9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("        9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("         9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("          9 9 9 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("            9 9 9 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("             9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ShieldPinsPerAssembly == 91:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 1 1 1 1 1 1 9 9 \n")
		smr.write("    9 9 9 9 9 9 1 1 1 1 1 1 1 9 9 \n")
		smr.write("     9 9 9 9 9 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("      9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("       9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("        9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("         9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("          9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("           9 9 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("             9 9 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	elif ShieldPinsPerAssembly == 127:

		smr.write("lat  10 2   0.0 0.0 15 15 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")
		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("          9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("           9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("            9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	

	elif ShieldPinsPerAssembly == 169:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("        9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("         9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("          9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("           9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("            9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("             9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("              9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("               9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 9 9 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ShieldPinsPerAssembly == 217:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("        9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("         9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("          9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("           9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("            9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("             9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("              9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("               9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 9 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ShieldPinsPerAssembly == 271:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("      9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("       9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("        9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("         9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("          9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("           9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("            9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("             9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("              9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("               9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                  9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                   9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 9 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	elif ShieldPinsPerAssembly == 331:
	
		smr.write("lat  10 2   0.0 0.0 23 23 {0:02.7f}".format(ShieldPinPitch) + "  % Fuel pin lattice\n")

		smr.write(" 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("  9 9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("   9 9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("    9 9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("     9 9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("      9 9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("       9 9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("        9 9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("         9 9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("          9 9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("           9 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("            9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 \n")
		smr.write("             9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 \n")
		smr.write("              9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 \n")
		smr.write("               9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 \n")
		smr.write("                9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 \n")
		smr.write("                 9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 \n")
		smr.write("                  9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 \n")
		smr.write("                   9 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 \n")
		smr.write("                    9 1 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 \n")	
		smr.write("                     9 1 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 \n")			
		smr.write("                      9 1 1 1 1 1 1 1 1 1 1 1 9 9 9 9 9 9 9 9 9 9 9 \n")
		smr.write("                       9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 \n")

	smr.write("surf 1 hexyc 0.0 0.0 {0:02.7f}".format(InnerAssemblySideLength)   + "  % Wrapper tube inner radius\n")
	smr.write("surf 2 hexyc 0.0 0.0 {0:02.7f}".format(DuctedAssemblySideLength)  + "  % Wrapper tube outer radius\n")
	smr.write("surf 3 hexyc 0.0 0.0 {0:02.7f}".format(AssemblyHexagonSideLength) + "\n")

	smr.write("surf 4 pz -10 \n")
	smr.write("surf 5 pz  10 \n")

	smr.write("cell  1  0  fill 10    -1          4 -5 %\n")
	smr.write("cell  4  0  duct        1    -2    4 -5 %\n")
	smr.write("cell  5  0  coolant     2    -3    4 -5 %\n")
	smr.write("cell 94  0  outside           3    4 -5 %\n")
	smr.write("cell 95  0  outside           3   -4    %\n")
	smr.write("cell 96  0  outside           3    5    %\n")
	smr.write("cell 97  0  outside          -3   -4    %\n")
	smr.write("cell 98  0  outside          -3    5    %\n")
	
	smr.write("plot 3 5000 5000\n")	

	smr.write("mat fuel1 -10.43 rgb 255 28 0 \n")
	smr.write("   8016.12c 2.00\n")
	smr.write("  92235.12c 0.20\n")
	smr.write("  92238.12c 0.80\n")
	
	smr.write("mat clad -7.9  rgb 1 1 1                  % Cladding steel (15-15Ti)\n")
	smr.write("  6000.06c   -0.09\n")
	smr.write(" 14000.06c   -0.85\n")
	smr.write(" 22000.06c   -0.40\n")
	smr.write(" 24000.06c  -14.50\n")
	smr.write(" 25055.06c   -1.50\n")
	smr.write(" 26000.06c  -65.35\n")
	smr.write(" 28000.06c  -15.50\n")
	smr.write(" 42000.06c   -1.50\n")

	smr.write("mat duct -7.6  rgb 1 1 1                  % Wrapper tube steel (T91)\n")
	smr.write(" 14028.06c  -0.5000\n")
	smr.write(" 23000.06c  -0.2000\n")
	smr.write(" 24050.06c  -0.3757\n")
	smr.write(" 24052.06c  -7.5330\n")
	smr.write(" 24053.06c  -0.8706\n")
	smr.write(" 24054.06c  -0.2207\n")
	smr.write(" 25055.06c  -0.6000\n")
	smr.write(" 26054.06c  -5.0380\n")
	smr.write(" 26056.06c -81.2131\n")
	smr.write(" 26057.06c  -1.8926\n")
	smr.write(" 26058.06c  -0.2564\n")
	smr.write(" 28058.06c  -0.1348\n")
	smr.write(" 28060.06c  -0.0534\n")
	smr.write(" 28061.06c  -0.0024\n")
	smr.write(" 28062.06c  -0.0076\n")
	smr.write(" 28064.06c  -0.0018\n")
	smr.write(" 41093.06c  -0.1000\n")
	smr.write(" 42092.06c  -0.1422\n")
	smr.write(" 42094.06c  -0.0905\n")
	smr.write(" 42095.06c  -0.1575\n")
	smr.write(" 42096.06c  -0.1667\n")
	smr.write(" 42097.06c  -0.0965\n")
	smr.write(" 42098.06c  -0.2465\n")
	smr.write(" 42100.06c  -0.1000\n")	
	
	smr.write("mat coolant -10.545 rgb 163 198 239 \n")
	smr.write("82204.06c  -0.0061\n")
	smr.write("82206.06c  -0.1074\n")
	smr.write("82207.06c  -0.0985\n")
	smr.write("82208.06c  -0.2328\n")
	smr.write("set pop 1000 10 10\n")
	smr.write("set acelib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7u_MP.xsdata\"\n")
	smr.write("set declib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.dec\"\n")
	smr.write("set nfylib \"/Users/staqv264/Dropbox/RunSerpent/xs/endf7/sss_endfb7.nfy\"\n")	

	return shname

import shutil
import os

def cleanplota(fname, serpplotpath):

	plotsource      = fname + "_geom1.png"
	plotdestination = serpplotpath + "/fuelassembly.png"

	plotfile = fname
	plotseed = fname + ".seed"
	plotout  = fname + "_serpent_output.txt"

	while os.path.exists(plotfile) == True and os.path.isfile(plotfile) == True:
		os.remove(plotfile)

	while os.path.exists(plotseed) == True and os.path.isfile(plotseed) == True:
		os.remove(plotseed)

	while os.path.exists(plotout) == True and os.path.isfile(plotout) == True:		
		os.remove(plotout)

	while os.path.exists(plotsource) == True and os.path.isfile(plotsource) == True:	
		os.rename(plotsource, plotdestination)

def cleanplotr(radname, serpplotpath):

	plotsource      = radname + "_geom1.png"
	plotdestination = serpplotpath + "/reflectorassembly.png"

	plotfile = radname
	plotseed = radname + ".seed"
	plotout  = radname + "_serpent_output.txt"

	while os.path.exists(plotfile) == True and os.path.isfile(plotfile) == True:
		os.remove(plotfile)

	while os.path.exists(plotseed) == True and os.path.isfile(plotseed) == True:
		os.remove(plotseed)

	while os.path.exists(plotout) == True and os.path.isfile(plotout) == True:		
		os.remove(plotout)

	while os.path.exists(plotsource) == True and os.path.isfile(plotsource) == True:	
		os.rename(plotsource, plotdestination)

def cleanplotsh(shname, serpplotpath):

	plotsource      = shname + "_geom1.png"
	plotdestination = serpplotpath + "/shieldassembly.png"

	plotfile = shname
	plotseed = shname + ".seed"
	plotout  = shname + "_serpent_output.txt"

	while os.path.exists(plotfile) == True and os.path.isfile(plotfile) == True:
		os.remove(plotfile)

	while os.path.exists(plotseed) == True and os.path.isfile(plotseed) == True:
		os.remove(plotseed)

	while os.path.exists(plotout) == True and os.path.isfile(plotout) == True:		
		os.remove(plotout)

	while os.path.exists(plotsource) == True and os.path.isfile(plotsource) == True:	
		os.rename(plotsource, plotdestination)


	