def runserpent_single(Name, SerpentVersion, SerpentPlotting, SerpentSMFRPlotting, SerpentCoreType, Where, zoneSCC, SerpentAxialZones):

	import subprocess

	filename = Name

	if Where == "SMFRiteration":
	
		print(" ")
		print("SERPENT - SMFR core in reference state")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_reference > " + filename + "_run_reference.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_reference > " + filename + "_run_reference.txt"

	elif Where == "SMFR_totalvoid":
	
		print("SERPENT - SMFR core at FULL coolant void")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_totvoid > " + filename + "_totvoid_output.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_totvoid > " + filename + "_totvoid_output.txt"

	elif Where == "SMFR_coolantcoeff":
	
		print("SERPENT - SMFR core w. perturbed coolant")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_coolantreactivity > " + filename + "_run_coolantcoeff.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_coolantreactivity > " + filename + "_run_coolantcoeff.txt"

	elif Where == "SMFR_fuelcoeff":
	
		print("SERPENT - SMFR core w. perturbed fuel")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_fuelreactivity > " + filename + "_run_fuelcoeff_.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_fuelreactivity > " + filename + "_run_fuelcoeff_.txt"

	elif Where == "SMFR_radexp":
	
		print("SERPENT - SMFR core w. perturbed radius")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_radialexpansion > " + filename + "_run_radexp.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_radialexpansion > " + filename + "_run_radexp.txt"

	elif Where == "SMFR_doppler":
	
		print("SERPENT - SMFR core w. perturbed fuel XS")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_fueldoppler > " + filename + "_run_doppler.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_fueldoppler > " + filename + "_run_doppler.txt"

	elif Where == "SMFR_lowseqcool":
	
		print("SERPENT - SMFR core w. perturbed lower coolant")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_lowcoolantreactivity > " + filename + "_run_lowseqcool.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_lowcoolantreactivity > " + filename + "_run_lowseqcool.txt"

	elif Where == "SMFR_upseqcool":
	
		print("SERPENT - SMFR core w. perturbed upper coolant")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  "_geometry_upcoolantreactivity > " + filename + "_run_upseqcool.txt"
		else:
			runline = "sss2 " + filename +  "_geometry_upcoolantreactivity > " + filename + "_run_upseqcool.txt"

	elif Where == "SMFR_seqcool":

		print("SERPENT - SMFR core w. ax. pert. coolant (" + str(zoneSCC+1) + "/" + str(SerpentAxialZones) + ")")

		if SerpentVersion == 1:

			runline = "sss  " + filename +  "_geometry_seqcool_ax" + str(zoneSCC+1) + " > " + filename + "_run_seqc" + str(zoneSCC+1) + ".txt"
		else:
			runline = "sss2 " + filename +  "_geometry_seqcool_ax" + str(zoneSCC+1) + " > " + filename + "_run_seqc" + str(zoneSCC+1) + ".txt"		

	elif Where == "SMFR_seqfuel":

		print("SERPENT - SMFR core w. ax. pert. fuel (" + str(zoneSCC+1) + "/" + str(SerpentAxialZones) + ")")

		if SerpentVersion == 1:

			runline = "sss  " + filename +  "_geometry_seqfuel_ax" + str(zoneSCC+1) + " > " + filename + "_run_seqf" + str(zoneSCC+1) + ".txt"
		else:
			runline = "sss2 " + filename +  "_geometry_seqfuel_ax" + str(zoneSCC+1) + " > " + filename + "_run_seqf" + str(zoneSCC+1) + ".txt"		

	elif Where == "SMFR_seqclad":

		print("SERPENT - SMFR core w. ax. pert. clad (" + str(zoneSCC+1) + "/" + str(SerpentAxialZones) + ")")

		if SerpentVersion == 1:

			runline = "sss  " + filename +  "_geometry_seqclad_ax" + str(zoneSCC+1) + " > " + filename + "_run_seqcl" + str(zoneSCC+1) + ".txt"
		else:
			runline = "sss2 " + filename +  "_geometry_seqclad_ax" + str(zoneSCC+1) + " > " + filename + "_run_seqcl" + str(zoneSCC+1) + ".txt"		

	elif Where == "SMFR_BUC":

		print("SERPENT - SMFR core w. BU-control insertion (" + str(zoneSCC+1) + "/" + str(SerpentAxialZones) + ")")

		if SerpentVersion == 1:

			runline = "sss  " + filename +  "_geometry_BUC_ax" + str(zoneSCC+1) + " > " + filename + "_run_BUC" + str(zoneSCC+1) + ".txt"
		else:
			runline = "sss2 " + filename +  "_geometry_BUC_ax" + str(zoneSCC+1) + " > " + filename + "_run_BUC" + str(zoneSCC+1) + ".txt"		

	elif Where == "SequentialScramRodInsertion":

		print("SERPENT - SMFR core w. SCRAM insertion (" + str(zoneSCC+1) + "/" + str(SerpentAxialZones) + ")")

		if SerpentVersion == 1:

			runline = "sss  " + filename +  "_geometry_SCRAM_ax" + str(zoneSCC+1) + " > " + filename + "_run_SCRAM" + str(zoneSCC+1) + ".txt"
		else:
			runline = "sss2 " + filename +  "_geometry_SCRAM_ax" + str(zoneSCC+1) + " > " + filename + "_run_SCRAM" + str(zoneSCC+1) + ".txt"

	elif Where == "AssemblyPlotting":
	
		if SerpentVersion == 1:
			runline = "sss  " + filename +  " -plot > " + Name + "_serpent_output.txt"
		else:
			runline = "sss2 " + filename +  " -plot > " + Name + "_serpent_output.txt"
	
	elif Where == "CylinderPlot":

		if SerpentVersion == 1:
			runline = "sss  " + filename +  " -plot > " + Name + "_serpent_output.txt"
		else:
			runline = "sss2 " + filename +  " -plot > " + Name + "_serpent_output.txt"

	elif Where == "runcyl":
	
		print(" ")
		print("SERPENT - Running cylindrical core model")

		if SerpentVersion == 1:
			runline = "sss  " + filename +  " > " + Name + "_serpent_output.txt"
		else:
			runline = "sss2 " + filename +  " > " + Name + "_serpent_output.txt"

	try:

		subprocess.check_output([runline, "-l"], shell = True)
	
	except subprocess.CalledProcessError:

		A=1