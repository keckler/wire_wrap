import os
import shutil

def cleanserpentfiles(Name, serpfilepath):

	serpfile = Name
	serpseed = Name + ".seed"
	serpres  = Name + "_res.m"
	serpdep  = Name + "_dep.m"
	serpout  = Name + "_serpent_output.txt"

	serpfilesave = serpfilepath + "/" + serpfile
	serpseedsave = serpfilepath + "/" + serpseed
	serpressave  = serpfilepath + "/" + serpres
	serpdepsave  = serpfilepath + "/" + serpdep
	serpoutsave  = serpfilepath + "/" + serpout

	while os.path.exists(serpfile) == True and os.path.isfile(serpfile) == True:
		os.rename(serpfile, serpfilesave)	

	while os.path.exists(serpseed) == True and os.path.isfile(serpseed) == True:
		os.rename(serpseed, serpseedsave)	

	while os.path.exists(serpres) == True and os.path.isfile(serpres)   == True:
		os.rename(serpres, serpressave)	

	while os.path.exists(serpdep) == True and os.path.isfile(serpdep)   == True:
		os.rename(serpdep, serpdepsave)	

	while os.path.exists(serpout) == True and os.path.isfile(serpout)   == True:
		os.rename(serpout, serpoutsave)

def cleancylplot(Name, serpfilepath):

	serpfile  = Name + "_inp"
	serpfile2 = Name + "_mburn"	
	serpfile3 = Name + "_nonfuel"
	serpfile4 = Name + "_inp_geom1.png"	
	serpfile5 = Name + "_inp_geom2.png"	
	serpseed  = Name + "_inp.seed"
	serpres   = Name + "_inp_res.m"
	serpdep   = Name + "_inp_dep.m"
	serpout   = Name + "_inp_serpent_output.txt"

	serpfilesave = serpfilepath + "/" + serpfile
	serpfilesave2 = serpfilepath + "/" + serpfile2
	serpfilesave3 = serpfilepath + "/" + serpfile3		
	serpfilesave4 = serpfilepath + "/" + serpfile4
	serpfilesave5 = serpfilepath + "/" + serpfile5	
	serpseedsave = serpfilepath + "/" + serpseed
	serpressave  = serpfilepath + "/" + serpres
	serpdepsave  = serpfilepath + "/" + serpdep
	serpoutsave  = serpfilepath + "/" + serpout

	while os.path.exists(serpfile) == True and os.path.isfile(serpfile) == True:
		os.rename(serpfile, serpfilesave)	

	while os.path.exists(serpfile2) == True and os.path.isfile(serpfile2) == True:
		os.rename(serpfile2, serpfilesave2)	

	while os.path.exists(serpfile3) == True and os.path.isfile(serpfile3) == True:
		os.rename(serpfile3, serpfilesave3)			

	while os.path.exists(serpfile4) == True and os.path.isfile(serpfile4) == True:
		os.rename(serpfile4, serpfilesave4)	

	while os.path.exists(serpfile5) == True and os.path.isfile(serpfile5) == True:
		os.rename(serpfile5, serpfilesave5)			

	while os.path.exists(serpseed) == True and os.path.isfile(serpseed) == True:
		os.rename(serpseed, serpseedsave)	

	while os.path.exists(serpres) == True and os.path.isfile(serpres)   == True:
		os.rename(serpres, serpressave)	

	while os.path.exists(serpdep) == True and os.path.isfile(serpdep)   == True:
		os.rename(serpdep, serpdepsave)	

	while os.path.exists(serpout) == True and os.path.isfile(serpout)   == True:
		os.rename(serpout, serpoutsave)


def copyrunfiles(runfilepath, AverageCoolantVelocity, CoolantOutletTemperature, PinAxialPowerPeaking, RadialPowerPeaking):

	settingsfile = "ADOPT_settings.py"
	settingsfiled = runfilepath + "/" + settingsfile

	shutil.copy(settingsfile, settingsfiled)