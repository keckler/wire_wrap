# coding=utf-8
from x_prop import *
import sys

####################################################################### //// ######## //// #######
##################### FUEL ############################################ //// ######## //// #######
####################################################################### //// ######## //// #######

def fuelinfo(FissileFraction, Fissile, Fertile, Fuel, ElementAtomicMassList, IsotopeAtomFractionList, IsotopeAtomicMassList, Batches,
		     MetallicFuelNonActinideMassFraction, TotalFuelMaterials):

	FuelAtomicMass            = []
	ActinideMassFraction      = []
	ActinideAtomicMass        = []
	ActinideAtomFraction      = []
	NonActinideMassFraction   = []
	NonActinideAtomFraction   = []

	FuelIsotopeMassFractions = {}
	FuelIsotopeAtomFractions = {}

	NonActinideIsotopeMassFractions = {}
	NonActinideIsotopeAtomFractions = {}

	FissileIsotopeMassFractions = {}
	FissileIsotopeAtomFractions = {}

	FertileIsotopeMassFractions = {}
	FertileIsotopeAtomFractions = {}

	FissileVector = {}
	FertileVector = {}

	FissileAtomicMass = []
	FertileAtomicMass = []

	TRU_A = {'93237' : 237.0481673,
		     '94238' : 238.0495534,
		     '94239' : 239.0521565,
		     '94240' : 240.0538075,
		     '94241' : 241.0568453,
		     '94242' : 242.0587368,
		     '95241' : 241.0568229,
		     '95342' : 242.0595430,
		     '95243' : 243.0613727,
		     '96242' : 242.0588293,
		     '96243' : 243.0613822,
		     '96244' : 244.0627463,
		     '96245' : 245.0654856,
		     '96246' : 246.0672176,
		     '96247' : 247.0703460,
		     '96248' : 248.0723422,
		     '98249' : 249.0748468,
		     '98250' : 250.0764000,
		     '98251' : 251.0795801,
		     '98252' : 252.0816196}

	if Fuel == "UO2":

		NonActinide                 = "801"
		NonActinideAtomsPerMolecule = 2
		FuelType                    = "Ceramic"

	elif Fuel == "Carbide":

		NonActinide                 = "601"
		NonActinideAtomsPerMolecule = 1
		FuelType                    = "Ceramic"

	elif Fuel == "Nitride":

		NonActinide                 = "701"
		NonActinideAtomsPerMolecule = 1
		FuelType                    = "Ceramic"

	elif Fuel == "MetallicZr":
	
		NonActinide                 = "40"
		FuelType                    = "AlloyedMetallic"		

	elif Fuel == "MetallicTh":
	
		NonActinide                 = "None"
		FuelType                    = "PureMetallic"	

	elif Fuel == "MetallicU":
	
		NonActinide                 = "None"
		FuelType                    = "PureMetallic"	

	NonActinide_af    = {}

	if NonActinide == "None":
		MetallicFuelNonActinideMassFraction = 0
	else:
		NonActinideNumber = int(NonActinide)	

	for batch in range(TotalFuelMaterials):

		if Fissile[batch] == "U235":
	
			FissileAtomicMass.append(235.0439231)

			FissileV1 = {'92235' : 1}
			FissileV2 = {batch : FissileV1}
			FissileVector.update(FissileV2)

		elif Fissile[batch] == "U233":
	
			FissileAtomicMass.append(233.0396282)

			FissileV1 = {'92233' : 1}
			FissileV2 = {batch : FissileV1}
			FissileVector.update(FissileV2)

		# Chang, Y. I., LoPinto, P., Konomura, M., Cahalan, J., Dunn, F., Farmer, M., et al. (2005). 
		# Small Modular Fast Reactor design description.

		elif Fissile[batch] == "TRU-SMFR":

			FissileV1 = {'93237' : 6.730/100,
					     '94238' : 2.780/100,
					     '94239' : 48.92/100,
					     '94240' : 23.01/100,
					     '94241' : 6.910/100,
					     '94242' : 5.000/100,
					     '95241' : 4.640/100,
					     '95342' : 0.020/100,
					     '95243' : 1.460/100,
					     '96243' : 0.010/100,
					     '96244' : 0.490/100,
					     '96245' : 0.040/100,
					     '96246' : 0.010/100}

			TRU_am = 0

			for k,v in FissileV1.items():

				TRU_am += v * TRU_A.get(k)

			FissileAtomicMass.append(TRU_am)			  

		# Ferrer, R. M., Asgari, M., Bays, S., & Forget, B. (2007). 
		# Fast Reactor Alternative Studies: 
		# Effects of Transuranic Groupings on Metal and Oxide Sodium Fast Reactor Designs.
		# Idaho National Laboratory.
	
		# LWR, 51 MWd/kg - 5 year decay

		elif Fissile[batch] == "TRU-51-5":

			FissileV1 = {'93237' : 5.3038e-2,
					     '94238' : 2.6160e-2,
					     '94239' : 4.8048e-1,
					     '94240' : 2.1616e-1,
					     '94241' : 1.0428e-1,
					     '94242' : 6.1756e-2,
					     '95241' : 3.3425e-2,
					     '95342' : 1.1307e-4,
					     '95243' : 1.7275e-2,
					     '96242' : 1.1037e-6,
					     '96243' : 5.3366e-5,
					     '96244' : 6.6230e-3,
					     '96245' : 5.7519e-4,
					     '96246' : 6.7242e-5,
					     '96247' : 1.1858e-6,
					     '96248' : 9.0107e-8,
					     '98249' : 1.4706e-9,
					     '98250' : 4.2611e-10,
					     '98251' : 2.4317e-10,
					     '98252' : 4.0293e-11}

			TRU_am = 0

			for k,v in FissileV1.items():

				TRU_am += v * TRU_A.get(k)

			FissileAtomicMass.append(TRU_am)	

		# LWR, 51 MWd/kg - 10 year decay

		elif Fissile[batch] == "TRU-51-10":

			FissileV1 = {'93237' : 5.3450e-2,
					     '94238' : 2.5184e-2,
					     '94239' : 4.8098e-1,
					     '94240' : 2.1746e-1,
					     '94241' : 8.2038e-2,
					     '94242' : 6.1829e-2,
					     '95241' : 5.5491e-2,
					     '95342' : 1.1048e-4,
					     '95243' : 1.7288e-2,
					     '96242' : 3.7083e-7,
					     '96243' : 4.7315e-5,
					     '96244' : 5.4757e-3,
					     '96245' : 5.7559e-4,
					     '96246' : 6.7273e-5,
					     '96247' : 1.1872e-6,
					     '96248' : 9.0214e-8,
					     '98249' : 1.4821e-9,
					     '98250' : 3.2738e-10,
					     '98251' : 2.4255e-10,
					     '98252' : 1.0894e-11}

			TRU_am = 0
			
			for k,v in FissileV1.items():

				TRU_am += v * TRU_A.get(k)

			FissileAtomicMass.append(TRU_am)			

		# LWR, 33 MWd/kg - 30 year decay

		elif Fissile[batch] == "TRU-33-30":

			FissileV1 = {'93237' : 4.2508e-2,
					     '94238' : 1.2376e-2,
					     '94239' : 5.4395e-1,
					     '94240' : 2.1930e-1,
					     '94241' : 2.9062e-2,
					     '94242' : 4.4895e-2,
					     '95241' : 9.7175e-2,
					     '95342' : 9.9897e-5,
					     '95243' : 9.5270e-3,
					     '96242' : 2.6202e-7,
					     '96243' : 1.6023e-5,
					     '96244' : 9.2911e-4,
					     '96245' : 1.1562e-4,
					     '96246' : 1.2412e-5,
					     '96247' : 1.4336e-7,
					     '96248' : 7.1153e-9,
					     '98249' : 8.1270e-11,
					     '98250' : 5.7606e-12,
					     '98251' : 9.9988e-12,
					     '98252' : 1.7475e-15}

			TRU_am = 0

			for k,v in FissileV1.items():

				TRU_am += v * TRU_A.get(k)

			FissileAtomicMass.append(TRU_am)	
	
		if Fertile[batch] == "U238":
	
			FertileAtomicMass.append(238.0507826)
			FertileV1 = {'92238' : 1}

		elif Fertile[batch] == "DU":
		
			DU_A      = {'92235' : 235.0439231,
					     '92238' : 238.0507826}

			FertileV1 = {'92235' : 0.20/100,
					     '92238' : 99.8/100}

			DU_am = 0

			for k,v in DU_A.items():

				DU_am += v * FertileV1.get(k)

			FertileAtomicMass.append(DU_am)				     

		elif Fertile[batch] == "NU":
		
			NU_A      = {'92235' : 235.0439231,
					     '92238' : 238.0507826}

			FertileV1 = {'92235' : 0.710/100,
					     '92238' : 99.29/100}

			NU_am = 0

			for k,v in NU_A.items():

				NU_am += v * FertileV1.get(k)

			FertileAtomicMass.append(NU_am)	

		elif Fertile[batch] == "Th":
		
			NU_A      = {'90232' : 232.0380504}
			FertileV1 = {'90232' : 100/100}
			FertileAtomicMass.append(232.0380504)	

		FissileV2 = {batch : FissileV1}
		FissileVector.update(FissileV2) 

		FertileV2 = {batch : FertileV1}
		FertileVector.update(FertileV2)	

		ActinideAtomicMass.append(FissileAtomicMass[batch] * FissileFraction[batch] + (1-FissileFraction[batch]) * FertileAtomicMass[batch])

		if NonActinide != "None":

			for k,v in IsotopeAtomFractionList.items():
		
				if NonActinideNumber < 10:
		
					CheckActinide = k[0]
			
				elif NonActinideNumber >= 10 and NonActinideNumber < 100:
			
					CheckActinide = k[0:2]
			
				else:
			
					CheckActinide = k[0:3]
		
				if CheckActinide == NonActinide:
		
					X = {k : v}
					NonActinide_af.update(X)
		
			NonActinide_am    = {}
		
			for k,v in IsotopeAtomicMassList.items():
		
				if NonActinideNumber < 10:
		
					CheckActinide = k[0]
			
				elif NonActinideNumber >= 10 and NonActinideNumber < 100:
			
					CheckActinide = k[0:2]
			
				else:
			
					CheckActinide = k[0:3]
		
				if CheckActinide == NonActinide:
		
					X = {k : v}
					NonActinide_am.update(X)
		
			NonActinide_ama  = ElementAtomicMassList.get(NonActinide)

	for batch in range(TotalFuelMaterials):

		if FuelType == "Ceramic":
	
			####################################################################### //// ######## //// #######
			##################### Define non-actinide component ################### //// ######## //// #######
			####################################################################### //// ######## //// #######	
		
			FuelAtomicMass.append(ActinideAtomicMass[batch] + NonActinideAtomsPerMolecule*NonActinide_ama)
			ActinideMassFraction.append(ActinideAtomicMass[batch] / FuelAtomicMass[batch])
			NonActinideMassFraction.append(1-ActinideMassFraction[batch])
			ActinideAtomFraction.append(1/(NonActinideAtomsPerMolecule + 1))
			NonActinideAtomFraction.append(1-ActinideAtomFraction[batch])
		
			NonActinideIsotopeAtomFractionCC = {}
			NonActinideIsotopeMassFractionCC = {}
		
			for k,v in NonActinide_af.items():
		
				NonActinideIsotopeAtomFraction = v * NonActinideAtomFraction[batch]
		
				NonActinideIsotopeAtomFractionC = {k : NonActinideIsotopeAtomFraction}
				NonActinideIsotopeAtomFractionCC.update(NonActinideIsotopeAtomFractionC)
				NonActinideIsotopeAtomFractionCCC = {batch : NonActinideIsotopeAtomFractionCC}
				NonActinideIsotopeAtomFractions.update(NonActinideIsotopeAtomFractionCCC)
		
				AtomFractionToMassFractionTranslator = NonActinide_am.get(k) / NonActinide_ama
				NonActinideIsotopeMassFraction = v * AtomFractionToMassFractionTranslator * NonActinideMassFraction[batch]
		
				NonActinideIsotopeMassFractionC = {k : NonActinideIsotopeMassFraction}
				NonActinideIsotopeMassFractionCC.update(NonActinideIsotopeMassFractionC)
				NonActinideIsotopeMassFractionCCC = {batch : NonActinideIsotopeMassFractionCC}
				NonActinideIsotopeMassFractions.update(NonActinideIsotopeMassFractionCCC)
	
		elif FuelType == "AlloyedMetallic":
	
			####################################################################### //// ######## //// #######
			##################### Define non-actinide component ################### //// ######## //// #######
			####################################################################### //// ######## //// #######	
		
			ActinideMassFraction.append(1-MetallicFuelNonActinideMassFraction)
			NonActinideMassFraction.append(MetallicFuelNonActinideMassFraction)
	
			NonActinideIsotopeMassFractionCC = {}
		
			for k,v in NonActinide_af.items():
		
				AtomFractionToMassFractionTranslator = NonActinide_am.get(k) / NonActinide_ama
				NonActinideIsotopeMassFraction = v * AtomFractionToMassFractionTranslator * NonActinideMassFraction[batch]
		
				NonActinideIsotopeMassFractionC = {k : NonActinideIsotopeMassFraction}
				NonActinideIsotopeMassFractionCC.update(NonActinideIsotopeMassFractionC)
				NonActinideIsotopeMassFractionCCC = {batch : NonActinideIsotopeMassFractionCC}
				NonActinideIsotopeMassFractions.update(NonActinideIsotopeMassFractionCCC)

		elif FuelType == "PureMetallic":

			####################################################################### //// ######## //// #######
			##################### Define non-actinide component ################### //// ######## //// #######
			####################################################################### //// ######## //// #######	
		
			ActinideMassFraction.append(1-MetallicFuelNonActinideMassFraction)
			NonActinideMassFraction.append(MetallicFuelNonActinideMassFraction)
			NonActinideIsotopeMassFractionCC = {}

	####################################################################### //// ######## //// #######
	##################### Define fissile component      ################### //// ######## //// #######
	####################################################################### //// ######## //// #######	

		FissileIsotopeAtomFractionCC = {}
		FissileIsotopeMassFractionCC = {}

		for k,v in FissileVector.items():

			if k == batch:

				for x,y in v.items():
	
					FissileIsotopeMassFraction  = y * FissileFraction[batch] * ActinideMassFraction[batch]
					FissileIsotopeMassFractionC = {x : FissileIsotopeMassFraction}
					FissileIsotopeMassFractionCC.update(FissileIsotopeMassFractionC)
	
			FissileIsotopeMassFractionCCC = {batch : FissileIsotopeMassFractionCC}
			FissileIsotopeMassFractions.update(FissileIsotopeMassFractionCCC)

	####################################################################### //// ######## //// #######
	##################### Define fertile component      ################### //// ######## //// #######
	####################################################################### //// ######## //// #######	

		FertileIsotopeAtomFractionCC = {}
		FertileIsotopeMassFractionCC = {}

		for k,v in FertileVector.items():

			if k == batch:

				for x,y in v.items():
	
					FertileIsotopeMassFraction  = y * (1- FissileFraction[batch]) * ActinideMassFraction[batch]
					FertileIsotopeMassFractionC = {x : FertileIsotopeMassFraction}
					FertileIsotopeMassFractionCC.update(FertileIsotopeMassFractionC)

			FertileIsotopeMassFractionCCC = {batch : FertileIsotopeMassFractionCC}
			FertileIsotopeMassFractions.update(FertileIsotopeMassFractionCCC)	

	# Check mass fraction normalization
	A = 0

	if NonActinide != "None":

		# Add the mass fractions of non-actinide components
		for k,v in NonActinideIsotopeMassFractions.items():
		
				if k == batch:
		
					for x,y in v.items():
			
						A += y

	# Add the mass fractions of fissile fuel components
	for k,v in FissileIsotopeMassFractions.items():

		if k == batch:
	
			for x,y in v.items():
	
				A += y

	# Add the mass fractions of fertile fuel components
	for k,v in FertileIsotopeMassFractions.items():
	
		if k == batch:

			for x,y in v.items():
	
				A += y
	
	# If the mass fractions are not normalized, cancel the run
	if round(A, 3) != 1:

		sys.exit("Fuel mass fractions are not normalized!")

	return(NonActinideIsotopeAtomFractions, FissileIsotopeAtomFractions, FertileIsotopeAtomFractions, NonActinideIsotopeMassFractions, \
		   FissileIsotopeMassFractions, FertileIsotopeMassFractions, ActinideMassFraction)


def cladding(Cladding, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList):

	## Cladding material
	CladdingChoice = eval(Cladding)

	CladdingIsotopeMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in CladdingChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v
				CMFC = {k : CMF}
				CladdingIsotopeMassFractions.update(CMFC)

				OneCheck += CMF

	if round(OneCheck, 3) != 1:

			sys.exit("Cladding mass fractions are not normalized!")

	## ATOM FRACTIONS	
	
	CladdingAverageAtomicMassFunction = 0

	for Element,MassFraction in CladdingChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CladdingAverageAtomicMassFunction += MassFraction / v

	CladdingComponentMassFunction = {}
	TotCCMF = 0

	for Element,MassFraction in CladdingChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CCMF = MassFraction * (CladdingAverageAtomicMassFunction / v)

				TotCCMF += CCMF
				CCMF2 = {Element : CCMF}
				CladdingComponentMassFunction.update(CCMF2)

	CladdingElementAtomFractions = {}

	for k,v in CladdingComponentMassFunction.items():

		CEAF = v / TotCCMF
		CEAF2 = {k : CEAF}
		CladdingElementAtomFractions.update(CEAF2)

	CladdingIsotopeAtomFractions = {}
	OneCheck = 0

	CladdingAverageAtomicMass = 0

	for Element,AtomFraction in CladdingElementAtomFractions.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in IsotopeAtomFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = AtomFraction * v
				CMFC = {k : CMF}
				CladdingIsotopeAtomFractions.update(CMFC)

				OneCheck += CMF

		CladdingAverageAtomicMass += AtomFraction * ElementAtomicMassList.get(str(ElementNumber))

	if round(OneCheck, 3) != 1:

			sys.exit("Cladding mass fractions are not normalized!")

	return(CladdingIsotopeMassFractions, CladdingIsotopeAtomFractions, CladdingAverageAtomicMass)

def duct(Duct, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList):

	## Duct material
	DuctChoice = eval(Duct)

	DuctIsotopeMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in DuctChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v
				CMFC = {k : CMF}
				DuctIsotopeMassFractions.update(CMFC)

				OneCheck += CMF

	if round(OneCheck, 3) != 1:

			sys.exit("Duct mass fractions are not normalized!")


	## ATOM FRACTIONS	
	
	DuctAverageAtomicMassFunction = 0

	for Element,MassFraction in DuctChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				DuctAverageAtomicMassFunction += MassFraction / v

	DuctComponentMassFunction = {}
	TotCCMF = 0

	for Element,MassFraction in DuctChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CCMF = MassFraction * (DuctAverageAtomicMassFunction / v)

				TotCCMF += CCMF
				CCMF2 = {Element : CCMF}
				DuctComponentMassFunction.update(CCMF2)

	DuctElementAtomFractions = {}

	for k,v in DuctComponentMassFunction.items():

		CEAF = v / TotCCMF
		CEAF2 = {k : CEAF}
		DuctElementAtomFractions.update(CEAF2)

	DuctIsotopeAtomFractions = {}
	OneCheck = 0
	DuctAverageAtomicMass = 0

	for Element,AtomFraction in DuctElementAtomFractions.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in IsotopeAtomFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = AtomFraction * v
				CMFC = {k : CMF}
				DuctIsotopeAtomFractions.update(CMFC)

				OneCheck += CMF

		DuctAverageAtomicMass += AtomFraction * ElementAtomicMassList.get(str(ElementNumber))

	if round(OneCheck, 3) != 1:

			sys.exit("Duct mass fractions are not normalized!")

	return(DuctIsotopeMassFractions, DuctIsotopeAtomFractions, DuctAverageAtomicMass)

def coolantisotopes(Coolant, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	                Na, Pb, LBE):

	## Coolant material
	CoolantChoice = eval(Coolant)

	CoolantIsotopeMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in CoolantChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v
				CMFC = {k : CMF}
				CoolantIsotopeMassFractions.update(CMFC)

				OneCheck += CMF

	if round(OneCheck, 3) != 1:

			sys.exit("Coolant mass fractions are not normalized!")

	## ATOM FRACTIONS	
	
	CoolantAverageAtomicMassFunction = 0

	for Element,MassFraction in CoolantChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CoolantAverageAtomicMassFunction += MassFraction / v

	CoolantComponentMassFunction = {}
	TotCCMF = 0

	for Element,MassFraction in CoolantChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CCMF = MassFraction * (CoolantAverageAtomicMassFunction / v)

				TotCCMF += CCMF
				CCMF2 = {Element : CCMF}
				CoolantComponentMassFunction.update(CCMF2)

	CoolantElementAtomFractions = {}

	for k,v in CoolantComponentMassFunction.items():

		CEAF = v / TotCCMF
		CEAF2 = {k : CEAF}
		CoolantElementAtomFractions.update(CEAF2)

	CoolantIsotopeAtomFractions = {}
	OneCheck = 0
	CoolantAverageAtomicMass = 0

	for Element,AtomFraction in CoolantElementAtomFractions.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in IsotopeAtomFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = AtomFraction * v
				CMFC = {k : CMF}
				CoolantIsotopeAtomFractions.update(CMFC)

				OneCheck += CMF

		CoolantAverageAtomicMass += AtomFraction * ElementAtomicMassList.get(str(ElementNumber))

	if round(OneCheck, 3) != 1:

			sys.exit("Coolant mass fractions are not normalized!")

	return(CoolantIsotopeMassFractions, CoolantIsotopeAtomFractions, CoolantAverageAtomicMass)

def bondisotopes(Bond, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	             Na, Pb, LBE, He):

	## Bond material
	BondChoice = eval(Bond)

	BondIsotopeMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in BondChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v
				CMFC = {k : CMF}
				BondIsotopeMassFractions.update(CMFC)

				OneCheck += CMF

	if round(OneCheck, 3) != 1:

			sys.exit("Bond mass fractions are not normalized!")

	## ATOM FRACTIONS	
	
	BondAverageAtomicMassFunction = 0

	for Element,MassFraction in BondChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				BondAverageAtomicMassFunction += MassFraction / v

	BondComponentMassFunction = {}
	TotCCMF = 0

	for Element,MassFraction in BondChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CCMF = MassFraction * (BondAverageAtomicMassFunction / v)

				TotCCMF += CCMF
				CCMF2 = {Element : CCMF}
				BondComponentMassFunction.update(CCMF2)

	BondElementAtomFractions = {}

	for k,v in BondComponentMassFunction.items():

		CEAF = v / TotCCMF
		CEAF2 = {k : CEAF}
		BondElementAtomFractions.update(CEAF2)

	BondIsotopeAtomFractions = {}
	OneCheck = 0
	BondAverageAtomicMass = 0

	for Element,AtomFraction in BondElementAtomFractions.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in IsotopeAtomFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = AtomFraction * v
				CMFC = {k : CMF}
				BondIsotopeAtomFractions.update(CMFC)

				OneCheck += CMF

		BondAverageAtomicMass += AtomFraction * ElementAtomicMassList.get(str(ElementNumber))

	if round(OneCheck, 3) != 1:

			sys.exit("Bond mass fractions are not normalized!")

	return(BondIsotopeMassFractions, BondIsotopeAtomFractions,BondAverageAtomicMass)

def reflectorisotopes(ReflectorPinMaterial, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList):

	## Reflector material
	ReflectorChoice = eval(ReflectorPinMaterial)

	ReflectorIsotopeMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in ReflectorChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v
				CMFC = {k : CMF}
				ReflectorIsotopeMassFractions.update(CMFC)

				OneCheck += CMF

	if round(OneCheck, 3) != 1:

			sys.exit("Reflector mass fractions are not normalized!")


	## ATOM FRACTIONS	
	
	ReflectorAverageAtomicMassFunction = 0

	for Element,MassFraction in ReflectorChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				ReflectorAverageAtomicMassFunction += MassFraction / v

	ReflectorComponentMassFunction = {}
	TotCCMF = 0

	for Element,MassFraction in ReflectorChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CCMF = MassFraction * (ReflectorAverageAtomicMassFunction / v)

				TotCCMF += CCMF
				CCMF2 = {Element : CCMF}
				ReflectorComponentMassFunction.update(CCMF2)

	ReflectorElementAtomFractions = {}

	for k,v in ReflectorComponentMassFunction.items():

		CEAF = v / TotCCMF
		CEAF2 = {k : CEAF}
		ReflectorElementAtomFractions.update(CEAF2)

	ReflectorIsotopeAtomFractions = {}
	OneCheck = 0
	ReflectorAverageAtomicMass = 0

	for Element,AtomFraction in ReflectorElementAtomFractions.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in IsotopeAtomFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = AtomFraction * v
				CMFC = {k : CMF}
				ReflectorIsotopeAtomFractions.update(CMFC)

				OneCheck += CMF

		ReflectorAverageAtomicMass += AtomFraction * ElementAtomicMassList.get(str(ElementNumber))

	if round(OneCheck, 3) != 1:

			sys.exit("Reflector mass fractions are not normalized!")

	return(ReflectorIsotopeMassFractions, ReflectorIsotopeAtomFractions, ReflectorAverageAtomicMass)

def shieldisotopes(ShieldPinMaterial, T91, HT9, D9, ElementZTranslationList, IsotopeAtomFractionList, 
	               IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, B4C):

	## Shield material
	ShieldChoice = eval(ShieldPinMaterial)

	ShieldIsotopeMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in ShieldChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v
				CMFC = {k : CMF}
				ShieldIsotopeMassFractions.update(CMFC)

				OneCheck += CMF

	if round(OneCheck, 3) != 1:

			sys.exit("Shield mass fractions are not normalized!")


	## ATOM FRACTIONS	
	
	ShieldAverageAtomicMassFunction = 0

	for Element,MassFraction in ShieldChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				ShieldAverageAtomicMassFunction += MassFraction / v

	ShieldComponentMassFunction = {}
	TotCCMF = 0

	for Element,MassFraction in ShieldChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in ElementAtomicMassList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CCMF = MassFraction * (ShieldAverageAtomicMassFunction / v)

				TotCCMF += CCMF
				CCMF2 = {Element : CCMF}
				ShieldComponentMassFunction.update(CCMF2)

	ShieldElementAtomFractions = {}

	for k,v in ShieldComponentMassFunction.items():

		CEAF = v / TotCCMF
		CEAF2 = {k : CEAF}
		ShieldElementAtomFractions.update(CEAF2)

	ShieldIsotopeAtomFractions = {}
	OneCheck = 0
	ShieldAverageAtomicMass = 0

	for Element,AtomFraction in ShieldElementAtomFractions.items():

		ElementNumber = ElementZTranslationList.get(Element)	

		for k,v in IsotopeAtomFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = AtomFraction * v
				CMFC = {k : CMF}
				ShieldIsotopeAtomFractions.update(CMFC)

				OneCheck += CMF

		ShieldAverageAtomicMass += AtomFraction * ElementAtomicMassList.get(str(ElementNumber))

	if round(OneCheck, 3) != 1:

			sys.exit("Shield mass fractions are not normalized!")

	return(ShieldIsotopeMassFractions, ShieldIsotopeAtomFractions, ShieldAverageAtomicMass)

def gridplate(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	          IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	          LowerGridPlateSteel, LowerGridPlateSteelFraction, CoolantInletTemperature, CoolantInletDensity,
	          Pb, LBE, Na, Coolant):

	CoolantDensity = CoolantInletDensity / 1000

	PlateProperties = nonfuelsolidproperties(material=LowerGridPlateSteel, temperature=CoolantInletTemperature, fastflux=1, stress=1, dpa=1, porosity=1)
	SteelDensity = PlateProperties.density

	CoolantVolumeFraction = 1 - LowerGridPlateSteelFraction

	SteelMassFraction   = SteelDensity * LowerGridPlateSteelFraction / (SteelDensity * LowerGridPlateSteelFraction + CoolantDensity * CoolantVolumeFraction)
	CoolantMassFraction = 1 - SteelMassFraction
	GridPlateCellDensity = SteelDensity * LowerGridPlateSteelFraction + CoolantDensity * CoolantVolumeFraction

	PlateSteelChoice = eval(LowerGridPlateSteel)

	GridPlateMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in PlateSteelChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v * SteelMassFraction

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				GridPlateMassFractions.update(CMFC)

				OneCheck += CMF

	CoolantChoice   = eval(Coolant)

	for Element,MassFraction in CoolantChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v * CoolantMassFraction

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				GridPlateMassFractions.update(CMFC)

				OneCheck += CMF

	return(GridPlateCellDensity, GridPlateMassFractions)

def gridplate_perturbed(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	          IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	          LowerGridPlateSteel, LowerGridPlateSteelFraction, CoolantInletTemperature, CoolantInletDensity,
	          Pb, LBE, Na, Coolant, CoolantTemperaturePerturbation):

	if CoolantTemperaturePerturbation == "void" or CoolantTemperaturePerturbation == "Void" or CoolantTemperaturePerturbation == "VOID":

		CoolantDensity = 1e-30

	else:

		CoolantProperties = nonsolids(material=Coolant, temperature=(CoolantInletTemperature+CoolantTemperaturePerturbation), pressure=0)
		CoolantDensity = CoolantProperties.density

	PlateProperties = nonfuelsolidproperties(material=LowerGridPlateSteel, temperature=CoolantInletTemperature, fastflux=1, stress=1, dpa=1, porosity=1)
	SteelDensity = PlateProperties.density

	CoolantVolumeFraction = 1 - LowerGridPlateSteelFraction

	SteelMassFraction   = SteelDensity * LowerGridPlateSteelFraction / (SteelDensity * LowerGridPlateSteelFraction + CoolantDensity * CoolantVolumeFraction)
	CoolantMassFraction = 1 - SteelMassFraction
	GridPlateCellDensity = SteelDensity * LowerGridPlateSteelFraction + CoolantDensity * CoolantVolumeFraction

	PlateSteelChoice = eval(LowerGridPlateSteel)

	GridPlateMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in PlateSteelChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v * SteelMassFraction

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				GridPlateMassFractions.update(CMFC)

				OneCheck += CMF

	CoolantChoice   = eval(Coolant)

	for Element,MassFraction in CoolantChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v * CoolantMassFraction

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				GridPlateMassFractions.update(CMFC)

				OneCheck += CMF

	return(GridPlateCellDensity, GridPlateMassFractions)

def barrel(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	          IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	          CoreBarrelSteel, CoolantAverageTemperature):

	# Calculate the density of the steel in the grid plate
	if CoreBarrelSteel   == "T91":

		SteelDensity = 7.7425 - 0.0003289 * CoolantAverageTemperature

	elif CoreBarrelSteel == "HT9":
	
		SteelDensity = 7.874 - 3.23 * 1e-4 * CoolantAverageTemperature

	elif CoreBarrelSteel == "D9":
	
		## TAKEN FROM SS316 ##
		SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantAverageTemperature - 3.894 * 1e-8 * CoolantAverageTemperature ** 2

	elif CoreBarrelSteel == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantAverageTemperature - 3.894 * 1e-8 * CoolantAverageTemperature ** 2

	elif CoreBarrelSteel == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 7.984 - 2.651 * 1e-4 * CoolantAverageTemperature - 1.158*1e-7 * CoolantAverageTemperature ** 2

	BarrelDensity = SteelDensity

	BarrelSteelChoice = eval(CoreBarrelSteel)

	BarrelMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in BarrelSteelChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				BarrelMassFractions.update(CMFC)

				OneCheck += CMF

	return(BarrelMassFractions, BarrelDensity)	

def insulator(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	          IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	          InsulatorMaterial, CoolantAverageTemperature, ZrO2):

	# Calculate the density of the steel in the grid plate
	if InsulatorMaterial   == "T91":

		LowerInsulatorDensity = 7.7425 - 0.0003289 * (CoolantInletTemperature + 15)

	elif InsulatorMaterial == "ZrO2":
	
		LowerInsulatorDensity = 6.0

	elif InsulatorMaterial == "HT9":
	
		LowerInsulatorDensity = 7.874 - 3.23 * 1e-4 * (CoolantInletTemperature + 15)

	elif InsulatorMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		LowerInsulatorDensity = 8.804 - 4.209 * 1e-4 * (CoolantInletTemperature + 15) - 3.894 * 1e-8 * (CoolantInletTemperature + 15) ** 2

	elif InsulatorMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		LowerInsulatorDensity = 8.804 - 4.209 * 1e-4 * (CoolantInletTemperature + 15) - 3.894 * 1e-8 * (CoolantInletTemperature + 15) ** 2

	elif InsulatorMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		LowerInsulatorDensity = 7.984 - 2.651 * 1e-4 * (CoolantInletTemperature + 15) - 1.158*1e-7 * (CoolantInletTemperature + 15) ** 2

	# Calculate the density of the steel in the grid plate
	if InsulatorMaterial   == "T91":

		UpperInsulatorDensity = 7.7425 - 0.0003289 * (CoolantOutletTemperature + 15)

	elif InsulatorMaterial == "ZrO2":
	
		UpperInsulatorDensity = 6.0

	elif InsulatorMaterial == "HT9":
	
		UpperInsulatorDensity = 7.874 - 3.23 * 1e-4 * (CoolantOutletTemperature + 15)

	elif InsulatorMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		UpperInsulatorDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 15) - 3.894 * 1e-8 * (CoolantOutletTemperature + 15) ** 2

	elif InsulatorMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		UpperInsulatorDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 15) - 3.894 * 1e-8 * (CoolantOutletTemperature + 15) ** 2

	elif InsulatorMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		UpperInsulatorDensity = 7.984 - 2.651 * 1e-4 * (CoolantOutletTemperature + 15) - 1.158*1e-7 * (CoolantOutletTemperature + 15) ** 2
	
	InsulatorChoice = eval(InsulatorMaterial)

	InsulatorMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in InsulatorChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				InsulatorMassFractions.update(CMFC)

				OneCheck += CMF

	return(InsulatorMassFractions, LowerInsulatorDensity, UpperInsulatorDensity)

def lowerendcap(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	            IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	            EndCapMaterial, CoolantInletTemperature, CoolantOutletTemperature):

	# Calculate the density of the steel in the grid plate
	if EndCapMaterial   == "T91":

		LowerEndCapDensity = 7.7425 - 0.0003289 * CoolantInletTemperature

	elif EndCapMaterial == "ZrO2":
	
		LowerEndCapDensity = 6.0

	elif EndCapMaterial == "HT9":
	
		LowerEndCapDensity = 7.874 - 3.23 * 1e-4 * CoolantInletTemperature

	elif EndCapMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		LowerEndCapDensity = 8.804 - 4.209 * 1e-4 * CoolantInletTemperature - 3.894 * 1e-8 * CoolantInletTemperature ** 2

	elif EndCapMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		LowerEndCapDensity = 8.804 - 4.209 * 1e-4 * CoolantInletTemperature - 3.894 * 1e-8 * CoolantInletTemperature ** 2

	elif EndCapMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		LowerEndCapDensity = 7.984 - 2.651 * 1e-4 * CoolantInletTemperature - 1.158*1e-7 * CoolantInletTemperature ** 2

	if EndCapMaterial   == "T91":

		UpperEndCapDensity = 7.7425 - 0.0003289 * (CoolantOutletTemperature + 20)

	elif EndCapMaterial == "ZrO2":
	
		UpperEndCapDensity = 6.0

	elif EndCapMaterial == "HT9":
	
		UpperEndCapDensity = 7.874 - 3.23 * 1e-4 * (CoolantOutletTemperature + 20)

	elif EndCapMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		UpperEndCapDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 20) - 3.894 * 1e-8 * (CoolantOutletTemperature + 20) ** 2

	elif EndCapMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		UpperEndCapDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 20) - 3.894 * 1e-8 * (CoolantOutletTemperature + 20) ** 2

	elif EndCapMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		UpperEndCapDensity = 7.984 - 2.651 * 1e-4 * (CoolantOutletTemperature + 20) - 1.158*1e-7 * (CoolantOutletTemperature + 20) ** 2
	
	EndCapChoice = eval(EndCapMaterial)

	EndCapMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in EndCapChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				EndCapMassFractions.update(CMFC)

				OneCheck += CMF

	return(EndCapMassFractions, LowerEndCapDensity, UpperEndCapDensity)

def insidereflector(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	                IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	                AxialReflectorPinMaterial, CoolantAverageTemperature, CoolantOutletTemperature):

	# Calculate the density of the steel in the grid plate
	if AxialReflectorPinMaterial   == "T91":

		SteelDensity = 7.7425 - 0.0003289 * CoolantAverageTemperature

	elif AxialReflectorPinMaterial == "HT9":
	
		SteelDensity = 7.874 - 3.23 * 1e-4 * CoolantAverageTemperature

	elif AxialReflectorPinMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantAverageTemperature - 3.894 * 1e-8 * CoolantAverageTemperature ** 2

	elif AxialReflectorPinMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantAverageTemperature - 3.894 * 1e-8 * CoolantAverageTemperature ** 2

	elif AxialReflectorPinMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 7.984 - 2.651 * 1e-4 * CoolantAverageTemperature - 1.158*1e-7 * CoolantAverageTemperature ** 2

	LowerInnerAxialReflectorDensity = SteelDensity

	# Calculate the density of the steel in the grid plate
	if AxialReflectorPinMaterial   == "T91":

		SteelDensity = 7.7425 - 0.0003289 * (CoolantOutletTemperature + 25)

	elif AxialReflectorPinMaterial == "HT9":
	
		SteelDensity = 7.874 - 3.23 * 1e-4 * (CoolantOutletTemperature + 25)

	elif AxialReflectorPinMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		SteelDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 25) - 3.894 * 1e-8 * (CoolantOutletTemperature + 25) ** 2

	elif AxialReflectorPinMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 25) - 3.894 * 1e-8 * (CoolantOutletTemperature + 25) ** 2

	elif AxialReflectorPinMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 7.984 - 2.651 * 1e-4 * (CoolantOutletTemperature + 25) - 1.158*1e-7 * (CoolantOutletTemperature + 25) ** 2

	UpperInnerAxialReflectorDensity = SteelDensity

	InnerReflectorChoice = eval(AxialReflectorPinMaterial)

	InnerReflectorMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in InnerReflectorChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				InnerReflectorMassFractions.update(CMFC)

				OneCheck += CMF

	return(LowerInnerAxialReflectorDensity, UpperInnerAxialReflectorDensity, InnerReflectorMassFractions)

def insideshield(T91, D9, HT9, B4C, ElementZTranslationList, IsotopeAtomFractionList, 
	             IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	             AxialShieldPinMaterial, CoolantAverageTemperature, CoolantOutletTemperature):

	# Calculate the density of the steel in the grid plate
	if AxialShieldPinMaterial   == "T91":

		SteelDensity = 7.7425 - 0.0003289 * (CoolantAverageTemperature - 5)

	elif AxialShieldPinMaterial == "HT9":
	
		SteelDensity = 7.874 - 3.23 * 1e-4 * (CoolantAverageTemperature - 5)

	elif AxialShieldPinMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		SteelDensity = 8.804 - 4.209 * 1e-4 * (CoolantAverageTemperature - 5) - 3.894 * 1e-8 * (CoolantAverageTemperature - 5) ** 2

	elif AxialShieldPinMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 8.804 - 4.209 * 1e-4 * (CoolantAverageTemperature - 5) - 3.894 * 1e-8 * (CoolantAverageTemperature - 5) ** 2

	elif AxialShieldPinMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 7.984 - 2.651 * 1e-4 * (CoolantAverageTemperature - 5) - 1.158*1e-7 * (CoolantAverageTemperature - 5) ** 2

	elif AxialShieldPinMaterial == "B4C":

		SteelDensity = 2.52 / (0.9948748015e0 + 0.1719000000e-4 * (CoolantAverageTemperature - 5))

	LowerInnerAxialShieldDensity = SteelDensity

	# Calculate the density of the steel in the grid plate
	if AxialShieldPinMaterial   == "T91":

		SteelDensity = 7.7425 - 0.0003289 * (CoolantOutletTemperature + 10)

	elif AxialShieldPinMaterial == "HT9":
	
		SteelDensity = 7.874 - 3.23 * 1e-4 * (CoolantOutletTemperature + 10)

	elif AxialShieldPinMaterial == "D9":
	
		## TAKEN FROM SS316 ##
		SteelDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 10) - 3.894 * 1e-8 * (CoolantOutletTemperature + 10) ** 2

	elif AxialShieldPinMaterial == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 8.804 - 4.209 * 1e-4 * (CoolantOutletTemperature + 10) - 3.894 * 1e-8 * (CoolantOutletTemperature + 10) ** 2

	elif AxialShieldPinMaterial == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 7.984 - 2.651 * 1e-4 * (CoolantOutletTemperature + 10) - 1.158*1e-7 * (CoolantOutletTemperature + 10) ** 2

	elif AxialShieldPinMaterial == "B4C":

		SteelDensity = 2.52 / (0.9948748015e0 + 0.1719000000e-4 * (CoolantOutletTemperature + 25))

	UpperInnerAxialShieldDensity = SteelDensity

	InnerShieldChoice = eval(AxialShieldPinMaterial)

	InnerShieldMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in InnerShieldChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				InnerShieldMassFractions.update(CMFC)

				OneCheck += CMF

	return(LowerInnerAxialShieldDensity, UpperInnerAxialShieldDensity, InnerShieldMassFractions)

def bottomplate(T91, D9, HT9, ElementZTranslationList, IsotopeAtomFractionList, 
	            IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	            BottomPlateSteel, CoolantInletTemperature):

	# Calculate the density of the steel in the grid plate
	if BottomPlateSteel   == "T91":

		SteelDensity = 7.7425 - 0.0003289 * CoolantInletTemperature

	elif BottomPlateSteel == "HT9":
	
		SteelDensity = 7.874 - 3.23 * 1e-4 * CoolantInletTemperature

	elif BottomPlateSteel == "D9":
	
		## TAKEN FROM SS316 ##
		SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantInletTemperature - 3.894 * 1e-8 * CoolantInletTemperature ** 2

	elif BottomPlateSteel == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 8.804 - 4.209 * 1e-4 * CoolantInletTemperature - 3.894 * 1e-8 * CoolantInletTemperature ** 2

	elif BottomPlateSteel == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		SteelDensity = 7.984 - 2.651 * 1e-4 * CoolantInletTemperature - 1.158*1e-7 * CoolantInletTemperature ** 2

	BottomPlateCellDensity = SteelDensity

	BottomPlateSteelChoice = eval(BottomPlateSteel)

	BottomPlateMassFractions = {}

	OneCheck = 0

	## MASS FRACTIONS
	for Element,MassFraction in BottomPlateSteelChoice.items():

		ElementNumber = ElementZTranslationList.get(Element)

		for k,v in IsotopeMassFractionList.items():

			if ElementNumber < 10:
	
				CheckElement = int(k[0])
		
			elif ElementNumber >= 10 and ElementNumber < 100:
		
				CheckElement = int(k[0:2])
		
			else:
	
				CheckElement = int(k[0:3])

			if ElementNumber == CheckElement:

				CMF = MassFraction * v

				if CMF == 0:

					CMF = 1e-30

				CMFC = {k : CMF}
				BottomPlateMassFractions.update(CMFC)

				OneCheck += CMF

	return(BottomPlateMassFractions, BottomPlateCellDensity)	

def bucontrolabs(T91, D9, HT9, B4C, ElementZTranslationList, IsotopeAtomFractionList, 
	             IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	             BUControlAbsorber, CoolantAverageTemperature, CoolantOutletTemperature,
	             BUControlB10Fraction):

	# Calculate the density of the steel in the grid plate
	if BUControlAbsorber   == "T91":

		BUControlDensity = 7.7425 - 0.0003289 * (CoolantAverageTemperature - 5)

	elif BUControlAbsorber == "HT9":
	
		BUControlDensity = 7.874 - 3.23 * 1e-4 * (CoolantAverageTemperature - 5)

	elif BUControlAbsorber == "D9":
	
		## TAKEN FROM SS316 ##
		BUControlDensity = 8.804 - 4.209 * 1e-4 * (CoolantAverageTemperature - 5) - 3.894 * 1e-8 * (CoolantAverageTemperature - 5) ** 2

	elif BUControlAbsorber == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		BUControlDensity = 8.804 - 4.209 * 1e-4 * (CoolantAverageTemperature - 5) - 3.894 * 1e-8 * (CoolantAverageTemperature - 5) ** 2

	elif BUControlAbsorber == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		BUControlDensity = 7.984 - 2.651 * 1e-4 * (CoolantAverageTemperature - 5) - 1.158*1e-7 * (CoolantAverageTemperature - 5) ** 2

	elif BUControlAbsorber == "B4C":

		BUControlDensity = 2.52 / (0.9948748015e0 + 0.1719000000e-4 * (CoolantAverageTemperature - 5))

	BUControlMassFractions = {}

	if BUControlAbsorber == "B4C":

		BMassFrac = 21.737/100
		CMassFrac = 1 - BMassFrac

		BC_am  = {'5010' : 10.0129370,
		          '5011' : 11.0093055}             
		 
		BUControlMassFractions  = {'5010' : BMassFrac * BUControlB10Fraction,
		          				   '5011' : BMassFrac * (1-BUControlB10Fraction),
		          				   '6000' : CMassFrac}      

	else:

		for Element,MassFraction in BuControlChoice.items():
		
			ElementNumber = ElementZTranslationList.get(Element)
		
			for k,v in IsotopeMassFractionList.items():
		
				if ElementNumber < 10:
		
					CheckElement = int(k[0])
			
				elif ElementNumber >= 10 and ElementNumber < 100:
			
					CheckElement = int(k[0:2])
			
				else:
		
					CheckElement = int(k[0:3])
		
				if ElementNumber == CheckElement:
		
					CMF = MassFraction * v
		
					if CMF == 0:
		
						CMF = 1e-30
		
					CMFC = {k : CMF}
					InnerShieldMassFractions.update(CMFC)
		
					OneCheck += CMF

	return(BUControlMassFractions, BUControlDensity)

def scramabs(T91, D9, HT9, B4C, ElementZTranslationList, IsotopeAtomFractionList, 
	         IsotopeAtomicMassList, IsotopeMassFractionList, ElementAtomicMassList, 
	         ScramAbsorber, CoolantAverageTemperature, CoolantOutletTemperature,
	         ScramB10Fraction):

	# Calculate the density of the steel in the grid plate
	if ScramAbsorber   == "T91":

		ScramDensity = 7.7425 - 0.0003289 * (CoolantAverageTemperature - 5)

	elif ScramAbsorber == "HT9":
	
		ScramDensity = 7.874 - 3.23 * 1e-4 * (CoolantAverageTemperature - 5)

	elif ScramAbsorber == "D9":
	
		## TAKEN FROM SS316 ##
		ScramDensity = 8.804 - 4.209 * 1e-4 * (CoolantAverageTemperature - 5) - 3.894 * 1e-8 * (CoolantAverageTemperature - 5) ** 2

	elif ScramAbsorber == "SS316":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		ScramDensity = 8.804 - 4.209 * 1e-4 * (CoolantAverageTemperature - 5) - 3.894 * 1e-8 * (CoolantAverageTemperature - 5) ** 2

	elif ScramAbsorber == "SS304":
	
		# PROPERTIES FOR LMFBR SAFETY ANALYSIS, ANL-CEN-RSD-76-1, 1976
		ScramDensity = 7.984 - 2.651 * 1e-4 * (CoolantAverageTemperature - 5) - 1.158*1e-7 * (CoolantAverageTemperature - 5) ** 2

	elif ScramAbsorber == "B4C":

		ScramDensity = 2.52 / (0.9948748015e0 + 0.1719000000e-4 * (CoolantAverageTemperature - 5))

	ScramMassFractions = {}

	if ScramAbsorber == "B4C":

		BMassFrac = 21.737/100
		CMassFrac = 1 - BMassFrac

		BC_am  = {'5010' : 10.0129370,
		          '5011' : 11.0093055}             
		 
		ScramMassFractions  = {'5010' : BMassFrac * ScramB10Fraction,
		          			   '5011' : BMassFrac * (1-ScramB10Fraction),
		          			   '6000' : CMassFrac}      

	else:

		for Element,MassFraction in BuControlChoice.items():
		
			ElementNumber = ElementZTranslationList.get(Element)
		
			for k,v in IsotopeMassFractionList.items():
		
				if ElementNumber < 10:
		
					CheckElement = int(k[0])
			
				elif ElementNumber >= 10 and ElementNumber < 100:
			
					CheckElement = int(k[0:2])
			
				else:
		
					CheckElement = int(k[0:3])
		
				if ElementNumber == CheckElement:
		
					CMF = MassFraction * v
		
					if CMF == 0:
		
						CMF = 1e-30
		
					CMFC = {k : CMF}
					InnerShieldMassFractions.update(CMFC)
		
					OneCheck += CMF

	return(ScramMassFractions, ScramDensity)

