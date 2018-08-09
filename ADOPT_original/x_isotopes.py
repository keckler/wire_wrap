IsotopeAtomFractionList  = {}
IsotopeMassFractionList  = {}
IsotopeAtomicMassList    = {}
ElementAtomicMassList    = {}
ElementZTranslationList  = {}

####################################################################### //// ######## //// #######
##################### Uranium ######################################### //// ######## //// #######
####################################################################### //// ######## //// #######

U_am = {'92234' : 234.0409456,
		    '92235' : 235.0439231,
		    '92236' : 236.0455619,
		    '92237' : 237.0487240,
	      '92238' : 238.0507826,
		    '92239' : 239.0542878,
		    '92240' : 240.0565857,
	      '92241' : 241.0603300}

U_Z  = {"U" : 92}

IsotopeAtomicMassList.update(U_am)
ElementZTranslationList.update(U_Z)

####################################################################### //// ######## //// #######
##################### Oxygen ########################################## //// ######## //// #######
####################################################################### //// ######## //// #######

O_af  = {'8016' : 1}
O_am  = {'8016' : 15.9949146}    
O_aveam = 15.9949146
O_ama =  {'801' : O_aveam}
O_Z   = {"O" : 801}

IsotopeAtomFractionList.update(O_af)
IsotopeAtomicMassList.update(O_am)
ElementAtomicMassList.update(O_ama)
ElementZTranslationList.update(O_Z)

O_mf = {}

for k,v in O_af.items():

	MassFraction = v * O_am.get(k) / O_aveam
	MFC = {k : MassFraction}
	O_mf.update(MFC)

IsotopeMassFractionList.update(O_mf)


####################################################################### //// ######## //// #######
##################### Nickel ########################################## //// ######## //// #######
####################################################################### //// ######## //// #######

Ni_am  = {'28058' : 57.9353479,
          '28060' : 59.9307906,
          '28061' : 60.9310604,
          '28062' : 61.9283488, 
          '28064' : 63.9279696}            
 
Ni_af  = {'28058' : 68.077/100,
          '28060' : 26.223/100,
          '28061' : 1.1400/100,
          '28062' : 3.6340/100, 
          '28064' : 0.9260/100}    

Ni_aveam = 58.69336129136899

Ni_ama = {'28' : Ni_aveam}

Ni_Z   = {"Ni" : 28}

IsotopeAtomFractionList.update(Ni_af)
IsotopeAtomicMassList.update(Ni_am)
ElementAtomicMassList.update(Ni_ama)
ElementZTranslationList.update(Ni_Z)

Ni_mf = {}

for k,v in Ni_af.items():

	MassFraction = v * Ni_am.get(k) / Ni_aveam
	MFC = {k : MassFraction}
	Ni_mf.update(MFC)

IsotopeMassFractionList.update(Ni_mf)


####################################################################### //// ######## //// #######
##################### Chromium #####  Z = 24  ######################### //// ######## //// #######
####################################################################### //// ######## //// #######

Cr_am  = {'24050' : 49.9460496,
          '24052' : 51.9405119,
          '24053' : 52.9406538,
          '24054' : 53.9388849}            
 
Cr_af  = {'24050' : 4.3450/100,
          '24052' : 83.789/100,
          '24053' : 9.5010/100,
          '24054' : 2.3650/100}    

Cr_aveam = 51.996137516434

Cr_ama = {'24' : Cr_aveam}

Cr_Z   = {"Cr" : 24}

IsotopeAtomFractionList.update(Cr_af)
IsotopeAtomicMassList.update(Cr_am)
ElementAtomicMassList.update(Cr_ama)
ElementZTranslationList.update(Cr_Z)

Cr_mf = {}

for k,v in Cr_af.items():

	MassFraction = v * Cr_am.get(k) / Cr_aveam
	MFC = {k : MassFraction}
	Cr_mf.update(MFC)

IsotopeMassFractionList.update(Cr_mf)

####################################################################### //// ######## //// #######
##################### Manganese ######  Z = 25  ####################### //// ######## //// #######
####################################################################### //// ######## //// #######

Mn_am  = {'25055' : 54.9380496}            
Mn_af  = {'25055' : 1}   
Mn_aveam =  54.9380496
Mn_ama = {'25' : Mn_aveam}
Mn_Z   = {"Mn" : 25}

IsotopeAtomFractionList.update(Mn_af)
IsotopeAtomicMassList.update(Mn_am)
ElementAtomicMassList.update(Mn_ama)
ElementZTranslationList.update(Mn_Z)

Mn_mf = {}

for k,v in Mn_af.items():

	MassFraction = v * Mn_am.get(k) / Mn_aveam
	MFC = {k : MassFraction}
	Mn_mf.update(MFC)

IsotopeMassFractionList.update(Mn_mf)

####################################################################### //// ######## //// #######
##################### Molybdenum #####  Z = 42  ####################### //// ######## //// #######
####################################################################### //// ######## //// #######

Mo_am  = {'42092' : 91.9068105,
          '42094' : 93.9050876,
          '42095' : 94.9058415,
          '42096' : 95.9046789,
          '42097' : 96.9060210,
          '42098' : 97.9054078,
          '42100' : 99.9074771}             
 
Mo_af  = {'42092' : 14.84/100,
          '42094' : 9.250/100,
          '42095' : 15.92/100,
          '42096' : 16.68/100,  
          '42097' : 9.550/100,
          '42098' : 24.13/100,
          '42100' : 9.630/100}  

Mo_aveam = 95.93129164089

Mo_ama = {'42' : Mo_aveam}

Mo_Z   = {"Mo" : 42}

IsotopeAtomFractionList.update(Mo_af)
IsotopeAtomicMassList.update(Mo_am)
ElementAtomicMassList.update(Mo_ama)
ElementZTranslationList.update(Mo_Z)

Mo_mf = {}

for k,v in Mo_af.items():

	MassFraction = v * Mo_am.get(k) / Mo_aveam
	MFC = {k : MassFraction}
	Mo_mf.update(MFC)

IsotopeMassFractionList.update(Mo_mf)

####################################################################### //// ######## //// #######
##################### Silicon #####  Z = 14  ########################## //// ######## //// #######
####################################################################### //// ######## //// #######

Si_am  = {'14028' : 27.9769265,
          '14029' : 28.9764947,
          '14030' : 29.9737702}             
 
Si_af  = {'14028' : 92.23/100,
          '14029' : 4.670/100,
          '14030' : 3.100/100}  

Si_aveam = 28.085508489640002

Si_ama = {'14' : Si_aveam}

Si_Z   = {"Si" : 14}

IsotopeAtomFractionList.update(Si_af)
IsotopeAtomicMassList.update(Si_am)
ElementAtomicMassList.update(Si_ama)
ElementZTranslationList.update(Si_Z)

Si_mf = {}

for k,v in Si_af.items():

	MassFraction = v * Si_am.get(k) / Si_aveam
	MFC = {k : MassFraction}
	Si_mf.update(MFC)

IsotopeMassFractionList.update(Si_mf)

####################################################################### //// ######## //// #######
##################### Wolfram/Tungsten #####  Z = 74  ################# //// ######## //// #######
####################################################################### //// ######## //// #######

W_am = {'74000' : 183.84169844142397}    
W_af = {'74000' : 1}
W_aveam = 183.84169844142397
W_ama = {'74' : W_aveam}
W_Z   = {"W" : 74}

IsotopeAtomFractionList.update(W_af)
IsotopeAtomicMassList.update(W_am)
ElementAtomicMassList.update(W_ama)
ElementZTranslationList.update(W_Z)

W_mf = {}

for k,v in W_af.items():

	MassFraction = v * W_am.get(k) / W_aveam
	MFC = {k : MassFraction}
	W_mf.update(MFC)

IsotopeMassFractionList.update(W_mf)

####################################################################### //// ######## //// #######
##################### Vanadium #####  Z = 23  ######################### //// ######## //// #######
####################################################################### //// ######## //// #######

V_am  = {'23000' : 49.922592423750004}             
V_af  = {'23000' : 1}     
V_aveam = 49.922592423750004
V_ama = {'23' : V_aveam}
V_Z   = {"V" : 23}

IsotopeAtomFractionList.update(V_af)
IsotopeAtomicMassList.update(V_am)
ElementAtomicMassList.update(V_ama)
ElementZTranslationList.update(V_Z)

V_mf = {}

for k,v in V_af.items():

	MassFraction = v * V_am.get(k) / V_aveam
	MFC = {k : MassFraction}
	V_mf.update(MFC)

IsotopeMassFractionList.update(V_mf)

####################################################################### //// ######## //// #######
##################### Carbon #####  Z = 6  ############################ //// ######## //// #######
####################################################################### //// ######## //// #######

C_am  = {'6000' : 12.01113723828}             
C_af  = {'6000' : 1}      
C_aveam = 12.01113723828
C_ama = {'600' : C_aveam}
C_Z   = {"C" : 600}

IsotopeAtomFractionList.update(C_af)
IsotopeAtomicMassList.update(C_am)
ElementAtomicMassList.update(C_ama)
ElementZTranslationList.update(C_Z)

C_mf = {}

for k,v in C_af.items():

	MassFraction = v * C_am.get(k) / C_aveam
	MFC = {k : MassFraction}
	C_mf.update(MFC)

IsotopeMassFractionList.update(C_mf)

####################################################################### //// ######## //// #######
##################### Iron #####  Z = 26  ############################# //// ######## //// #######
####################################################################### //// ######## //// #######

Fe_am  = {'26054' : 53.9396148,
          '26056' : 55.9349421,
          '26057' : 56.9353987,
          '26058' : 57.9332805}             
 
Fe_af  = {'26054' : 5.8450/100,
          '26056' : 91.754/100,
          '26057' : 2.1190/100,
          '26058' : 0.2820/100}     

Fe_aveam = 55.845150208957

Fe_ama = {'26' : Fe_aveam}

Fe_Z   = {"Fe" : 26}

IsotopeAtomFractionList.update(Fe_af)
IsotopeAtomicMassList.update(Fe_am)
ElementAtomicMassList.update(Fe_ama)
ElementZTranslationList.update(Fe_Z)

Fe_mf = {}

for k,v in Fe_af.items():

	MassFraction = v * Fe_am.get(k) / Fe_aveam
	MFC = {k : MassFraction}
	Fe_mf.update(MFC)

IsotopeMassFractionList.update(Fe_mf)

####################################################################### //// ######## //// #######
##################### Titanium #####  Z = 22  ######################### //// ######## //// #######
####################################################################### //// ######## //// #######

Ti_am  = {'22046' : 45.9526295,
          '22047' : 46.9517638,
          '22048' : 47.9479471,
          '22049' : 48.9478708,
          '22050' : 49.9447921}             
 
Ti_af  = {'22046' : 8.250/100,
          '22047' : 7.440/100,
          '22048' : 73.72/100,
          '22049' : 5.410/100,
          '22050' : 5.180/100}      

Ti_aveam = 47.866749803649995

Ti_ama = {'22' : Ti_aveam}

Ti_Z   = {"Ti" : 22}

IsotopeAtomFractionList.update(Ti_af)
IsotopeAtomicMassList.update(Ti_am)
ElementAtomicMassList.update(Ti_ama)
ElementZTranslationList.update(Ti_Z)

Ti_mf = {}

for k,v in Ti_af.items():

	MassFraction = v * Ti_am.get(k) / Ti_aveam
	MFC = {k : MassFraction}
	Ti_mf.update(MFC)

IsotopeMassFractionList.update(Ti_mf)

####################################################################### //// ######## //// #######
##################### Phosporus #####  Z = 15   ####################### //// ######## //// #######
####################################################################### //// ######## //// #######

P_am  = {'15031' : 30.9737615}            
P_af  = {'15031' : 1}   
P_aveam =  30.9737615
P_ama = {'15' : P_aveam}
P_Z   = {"P" : 15}

IsotopeAtomFractionList.update(P_af)
IsotopeAtomicMassList.update(P_am)
ElementAtomicMassList.update(P_ama)
ElementZTranslationList.update(P_Z)

P_mf = {}

for k,v in P_af.items():

  MassFraction = v * P_am.get(k) / P_aveam
  MFC = {k : MassFraction}
  P_mf.update(MFC)

IsotopeMassFractionList.update(P_mf)

####################################################################### //// ######## //// #######
##################### Sulfur    #####  Z = 16  ######################## //// ######## //// #######
####################################################################### //// ######## //// #######

S_am  = {'16032' : 31.9720707,
         '16033' : 32.9714585,
         '16034' : 33.9678668,
         '16036' : 35.9670809}             
 
S_af  = {'16032' : 95.02/100,
         '16033' : 0.750/100,
         '16034' : 4.210/100,
         '16036' : 0.020/100}      

S_aveam = 32.064388126349996

S_ama = {'16' : S_aveam}

S_Z   = {"S" : 16}

IsotopeAtomFractionList.update(S_af)
IsotopeAtomicMassList.update(S_am)
ElementAtomicMassList.update(S_ama)
ElementZTranslationList.update(S_Z)

S_mf = {}

for k,v in S_af.items():

  MassFraction = v * S_am.get(k) / S_aveam
  MFC = {k : MassFraction}
  S_mf.update(MFC)

IsotopeMassFractionList.update(S_mf)

####################################################################### //// ######## //// #######
##################### Niobium    #####  Z = 41   ###################### //// ######## //// #######
####################################################################### //// ######## //// #######

Nb_am    = {'41093' : 92.9063775}            
Nb_af    = {'41093' : 1}   
Nb_aveam =  92.9063775
Nb_ama   = {'41' : Nb_aveam}
Nb_Z     = {"Nb" : 41}

IsotopeAtomFractionList.update(Nb_af)
IsotopeAtomicMassList.update(Nb_am)
ElementAtomicMassList.update(Nb_ama)
ElementZTranslationList.update(Nb_Z)

Nb_mf = {}

for k,v in Nb_af.items():

  MassFraction = v * Nb_am.get(k) / Nb_aveam
  MFC = {k : MassFraction}
  Nb_mf.update(MFC)

IsotopeMassFractionList.update(Nb_mf)

####################################################################### //// ######## //// #######
##################### Copper     #####  Z = 29   ###################### //// ######## //// #######
####################################################################### //// ######## //// #######

Cu_am  = {'29063' : 62.9296011,
          '29065' : 64.9277937}             
 
Cu_af  = {'29063' : 69.17/100,
          '29065' : 30.83/100}      

Cu_aveam = 63.545643878579995

Cu_ama = {'29' : Cu_aveam}

Cu_Z   = {"Cu" : 29}

IsotopeAtomFractionList.update(Cu_af)
IsotopeAtomicMassList.update(Cu_am)
ElementAtomicMassList.update(Cu_ama)
ElementZTranslationList.update(Cu_Z)

Cu_mf = {}

for k,v in Cu_af.items():

  MassFraction = v * Cu_am.get(k) / Cu_aveam
  MFC = {k : MassFraction}
  Cu_mf.update(MFC)

IsotopeMassFractionList.update(Cu_mf)

####################################################################### //// ######## //// #######
##################### Sodium     #####  Z = 11  ####################### //// ######## //// #######
####################################################################### //// ######## //// #######

Na_am  = {'11023' : 22.9897697}            
Na_af  = {'11023' : 1}   
Na_aveam =  22.9897697
Na_ama = {'11' : Na_aveam}
Na_Z   = {"Na" : 11}

IsotopeAtomFractionList.update(Na_af)
IsotopeAtomicMassList.update(Na_am)
ElementAtomicMassList.update(Na_ama)
ElementZTranslationList.update(Na_Z)

Na_mf = {}

for k,v in Na_af.items():

  MassFraction = v * Na_am.get(k) / Na_aveam
  MFC = {k : MassFraction}
  Na_mf.update(MFC)

IsotopeMassFractionList.update(Na_mf)

####################################################################### //// ######## //// #######
##################### Lead       #####  Z = 82  ####################### //// ######## //// #######
####################################################################### //// ######## //// #######

Pb_am  = {'82204' : 203.9730288,
          '82206' : 205.9744490,
          '82207' : 206.9758806,
          '82208' : 207.9766359}             
 
Pb_af  = {'82204' : 1.40/100,
          '82206' : 24.1/100,
          '82207' : 22.1/100,
          '82208' : 52.4/100}      

Pb_aveam = 207.2168914364

Pb_ama = {'82' : Pb_aveam}

Pb_Z   = {"Pb" : 82}

IsotopeAtomFractionList.update(Pb_af)
IsotopeAtomicMassList.update(Pb_am)
ElementAtomicMassList.update(Pb_ama)
ElementZTranslationList.update(Pb_Z)

Pb_mf = {}

for k,v in Pb_af.items():

  MassFraction = v * Pb_am.get(k) / Pb_aveam
  MFC = {k : MassFraction}
  Pb_mf.update(MFC)

IsotopeMassFractionList.update(Pb_mf)

####################################################################### //// ######## //// #######
##################### Bismuth       #####  Z = 83  #################### //// ######## //// #######
####################################################################### //// ######## //// #######

Bi_am    = {'83209' : 208.9803832}            
Bi_af    = {'83209' : 1}   
Bi_aveam = 208.9803832
Bi_ama   = {'83' : Bi_aveam}
Bi_Z     = {"Bi" : 83}

IsotopeAtomFractionList.update(Bi_af)
IsotopeAtomicMassList.update(Bi_am)
ElementAtomicMassList.update(Bi_ama)
ElementZTranslationList.update(Bi_Z)

Bi_mf = {}

for k,v in Bi_af.items():

  MassFraction = v * Bi_am.get(k) / Bi_aveam
  MFC = {k : MassFraction}
  Bi_mf.update(MFC)

IsotopeMassFractionList.update(Bi_mf)

####################################################################### //// ######## //// #######
##################### Helium        #####  Z = 2   #################### //// ######## //// #######
####################################################################### //// ######## //// #######

He_am    = {'2004' : 4.0026032}            
He_af    = {'2004' : 1}   
He_aveam = 4.0026032
He_ama   = {'200' : He_aveam}
He_Z     = {"He" : 200}

IsotopeAtomFractionList.update(He_af)
IsotopeAtomicMassList.update(He_am)
ElementAtomicMassList.update(He_ama)
ElementZTranslationList.update(He_Z)

He_mf = {}

for k,v in He_af.items():

  MassFraction = v * He_am.get(k) / He_aveam
  MFC = {k : MassFraction}
  He_mf.update(MFC)

IsotopeMassFractionList.update(He_mf)

####################################################################### //// ######## //// #######
##################### Nitrogen       #####  Z = 7   ################### //// ######## //// #######
####################################################################### //// ######## //// #######

N_am    = {'7014' : 14.0030740,
           '7015' : 15.0001089}            
N_af    = {'7014' : 99.634/100,
           '7015' : 0.3660/100}   
N_aveam = 14.006723147734
N_ama   = {'701' : N_aveam}
N_Z     = {"N" : 701}

IsotopeAtomFractionList.update(N_af)
IsotopeAtomicMassList.update(N_am)
ElementAtomicMassList.update(N_ama)
ElementZTranslationList.update(N_Z)

N_mf = {}
for k,v in N_af.items():

  MassFraction = v * N_am.get(k) / N_aveam
  MFC = {k : MassFraction}
  N_mf.update(MFC)

IsotopeMassFractionList.update(N_mf)

####################################################################### //// ######## //// #######
##################### Zirconium       #####  Z = 40  ################## //// ######## //// #######
####################################################################### //// ######## //// #######

Zr_am  = {'40090' : 89.9047037,
          '40091' : 90.9056450,
          '40092' : 91.9050401,
          '40094' : 93.9063158,             
          '40096' : 95.9082757} 

Zr_af  = {'40090' : 51.45/100,
          '40091' : 11.22/100,
          '40092' : 17.15/100,
          '40094' : 17.38/100,             
          '40096' : 2.800/100}      

Zr_aveam = 91.22364720544

Zr_ama = {'40' : Zr_aveam}

Zr_Z   = {"Zr" : 40}

IsotopeAtomFractionList.update(Zr_af)
IsotopeAtomicMassList.update(Zr_am)
ElementAtomicMassList.update(Zr_ama)
ElementZTranslationList.update(Zr_Z)

Zr_mf = {}
for k,v in Zr_af.items():

  MassFraction = v * Zr_am.get(k) / Zr_aveam
  MFC = {k : MassFraction}
  Zr_mf.update(MFC)

IsotopeMassFractionList.update(Zr_mf)

def boron(B10Fraction, IsotopeMassFractionList, IsotopeAtomicMassList, IsotopeAtomFractionList, ElementZTranslationList, ElementAtomicMassList):

  ####################################################################### //// ######## //// #######
  ##################### Boron      #####  Z = 5    ###################### //// ######## //// #######
  ####################################################################### //// ######## //// #######
  
  B_am  = {'5010' : 10.0129370,
           '5011' : 11.0093055}             
   
  B_af  = {'5010' : B10Fraction,
           '5011' : 1-B10Fraction}      
  
  B_aveam = 0

  for k,v in B_af.items():
  
    B_aveam += v * B_am.get(k)
  
  B_ama = {'501' : B_aveam}
  
  B_Z   = {"B" : 501}
  
  IsotopeAtomFractionList.update(B_af)
  IsotopeAtomicMassList.update(B_am)
  ElementAtomicMassList.update(B_ama)
  ElementZTranslationList.update(B_Z)
  
  B_mf = {}
  
  for k,v in B_af.items():
  
    MassFraction = v * B_am.get(k) / B_aveam
    MFC = {k : MassFraction}
    B_mf.update(MFC)
  
  IsotopeMassFractionList.update(B_mf) 

  return(IsotopeMassFractionList, IsotopeAtomicMassList, IsotopeAtomFractionList, ElementZTranslationList, ElementAtomicMassList)

