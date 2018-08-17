
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.30' ;
COMPILE_DATE              (idx, [1: 20])  = 'Feb 14 2018 11:48:41' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 10])  = 'BnB_stage1' ;
WORKING_DIRECTORY         (idx, [1: 62])  = '/global/home/users/ckeckler/docs/wire_wrap/ADOPT_wire_combined' ;
HOSTNAME                  (idx, [1: 12])  = 'n0033.savio2' ;
CPU_TYPE                  (idx, [1: 41])  = 'Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz' ;
CPU_MHZ                   (idx, 1)        = 45.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Aug 16 14:05:01 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Aug 16 14:06:49 2018' ;

% Run parameters:

POP                       (idx, 1)        = 2000 ;
CYCLES                    (idx, 1)        = 420 ;
SKIP                      (idx, 1)        = 30 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1534453501 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 1 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 20 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  20]) = [  1.00720E+00  1.00609E+00  9.91733E-01  1.00145E+00  9.95217E-01  1.00309E+00  9.95794E-01  9.96615E-01  1.00649E+00  9.89602E-01  9.95061E-01  1.00684E+00  9.92199E-01  1.01162E+00  1.00398E+00  1.00145E+00  1.00261E+00  9.94573E-01  1.00234E+00  9.96038E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 73])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.67961E-03 0.02854  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.98320E-01 4.8E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  7.49600E-01 0.00030  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.49988E-01 0.00029  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.29616E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  5.10739E+01 0.00092  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  5.10720E+01 0.00092  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.70285E+01 0.00157  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  9.81227E-03 0.02925  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 420 ;
SOURCE_POPULATION         (idx, 1)        = 840793 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00189E+03 0.00220 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00189E+03 0.00220 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.73802E+01 ;
RUNNING_TIME              (idx, 1)        =  1.78777E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  9.47517E-01  9.47517E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  3.49500E-02  3.49500E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  8.04817E-01  8.04817E-01  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.78727E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 9.72172 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.98027E+01 0.00141 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  4.57545E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64322.08 ;
ALLOC_MEMSIZE             (idx, 1)        = 11422.48;
MEMSIZE                   (idx, 1)        = 11240.16;
XS_MEMSIZE                (idx, 1)        = 7290.37;
MAT_MEMSIZE               (idx, 1)        = 1329.42;
RES_MEMSIZE               (idx, 1)        = 1.65;
MISC_MEMSIZE              (idx, 1)        = 2618.72;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 182.32;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 140 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-03 ;
NEUTRON_ERG_NE            (idx, 1)        = 157789 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-05 ;
NEUTRON_EMAX              (idx, 1)        =  1.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 444 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 2628 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 646 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1982 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 15990 ;
TOT_TRANSMU_REA           (idx, 1)        = 4042 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  3.55418E+20 ;
TOT_DECAY_HEAT            (idx, 1)        =  2.95033E+07 ;
TOT_SF_RATE               (idx, 1)        =  3.90782E+09 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  2.52853E+20 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  1.77278E+07 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  1.02547E+20 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.17724E+07 ;
INHALATION_TOXICITY       (idx, 1)        =  5.73985E+12 ;
INGESTION_TOXICITY        (idx, 1)        =  3.55873E+11 ;
ACTINIDE_INH_TOX          (idx, 1)        =  5.04320E+12 ;
ACTINIDE_ING_TOX          (idx, 1)        =  1.15049E+11 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  6.96603E+11 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.40809E+11 ;
SR90_ACTIVITY             (idx, 1)        =  2.91059E+17 ;
TE132_ACTIVITY            (idx, 1)        =  4.65166E+18 ;
I131_ACTIVITY             (idx, 1)        =  3.44524E+18 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  5.15811E+17 ;
CS137_ACTIVITY            (idx, 1)        =  7.34685E+17 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  3.80337E+20 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  8.20779E+16 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  8.01385E+20 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.52544E+17 0.00083  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 108 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 0 ;
BURNUP                     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BURN_DAYS                 (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.61362E+00 0.00265 ];
U235_FISS                 (idx, [1:   4]) = [  1.26514E+18 0.01657  1.20254E-02 0.01646 ];
U238_FISS                 (idx, [1:   4]) = [  2.07173E+19 0.00443  1.96890E-01 0.00382 ];
PU239_FISS                (idx, [1:   4]) = [  7.94949E+19 0.00208  7.55773E-01 0.00109 ];
PU240_FISS                (idx, [1:   4]) = [  2.27965E+18 0.01253  2.16789E-02 0.01246 ];
PU241_FISS                (idx, [1:   4]) = [  1.07979E+18 0.01748  1.02591E-02 0.01733 ];
U235_CAPT                 (idx, [1:   4]) = [  3.39509E+17 0.03379  1.69381E-03 0.03380 ];
U238_CAPT                 (idx, [1:   4]) = [  1.53644E+20 0.00134  7.66918E-01 0.00079 ];
PU239_CAPT                (idx, [1:   4]) = [  1.44888E+19 0.00495  7.23450E-02 0.00499 ];
PU240_CAPT                (idx, [1:   4]) = [  2.25764E+18 0.01242  1.12726E-02 0.01247 ];
PU241_CAPT                (idx, [1:   4]) = [  1.55168E+17 0.04721  7.76182E-04 0.04725 ];
SM149_CAPT                (idx, [1:   4]) = [  5.87125E+17 0.02275  2.93179E-03 0.02275 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 840793 8.40000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.76283E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 840793 8.42763E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 550162 5.51613E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 289081 2.89593E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 1550 1.55627E+03 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 840793 8.42763E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.39698E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.50000E+09 0.0E+00  3.50000E+09 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  1.17012E-02 3.4E-09  1.17012E-02 3.4E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  3.05578E+20 3.4E-05  3.05578E+20 3.4E-05  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  1.05189E+20 1.6E-06  1.05189E+20 1.6E-06  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  2.00385E+20 0.00094  1.99355E+20 0.00092  1.03001E+18 0.02308 ];
TOT_ABSRATE               (idx, [1:   6]) = [  3.05574E+20 0.00062  3.04544E+20 0.00060  1.03001E+18 0.02308 ];
TOT_SRCRATE               (idx, [1:   6]) = [  3.05088E+20 0.00083  3.05088E+20 0.00083  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  4.99075E+22 0.00073  4.88405E+22 0.00058  1.06700E+21 0.01967 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  5.65869E+17 0.02811 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.06140E+20 0.00062 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.56311E+22 0.00065 ];
INI_FMASS                 (idx, 1)        =  2.99115E+05 ;
TOT_FMASS                 (idx, 1)        =  2.99115E+05 ;
INI_BURN_FMASS            (idx, 1)        =  2.99115E+05 ;
TOT_BURN_FMASS            (idx, 1)        =  2.99115E+05 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_F                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_P                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.98147E-01 5.2E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.90504E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.07677E+02 1.6E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00107E+00 0.00152  9.97874E-01 0.00153  3.58092E-03 0.03153 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00152E+00 0.00064 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00189E+00 0.00083 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00152E+00 0.00064 ];
ABS_KINF                  (idx, [1:   2]) = [  1.00338E+00 0.00063 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 1.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  3.60583E+00 0.00096 ];
IMP_ALF                   (idx, [1:   2]) = [  3.60323E+00 0.00049 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  2.72338E-01 0.00349 ];
IMP_EALF                  (idx, [1:   2]) = [  2.72538E-01 0.00178 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  9.40640E-01 0.00295 ];
IMP_AFGE                  (idx, [1:   2]) = [  9.38489E-01 0.00134 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  4.74463E-03 0.01665  9.82524E-05 0.10908  8.45488E-04 0.03705  6.85525E-04 0.04312  2.05330E-03 0.02310  8.57531E-04 0.03920  2.04532E-04 0.07844 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  7.99980E-01 0.03869  2.24065E-03 0.10480  2.40041E-02 0.02461  8.16575E-02 0.02988  3.29044E-01 0.00489  1.04525E+00 0.02491  3.26383E+00 0.07012 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  3.59022E-03 0.01940  7.65892E-05 0.13875  6.45364E-04 0.04514  5.15424E-04 0.05504  1.57404E-03 0.02911  6.25375E-04 0.04767  1.53419E-04 0.09479 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.11376E-01 0.04897  1.25516E-02 0.00230  3.00910E-02 0.00033  1.12174E-01 0.00193  3.32074E-01 0.00117  1.31362E+00 0.00263  9.79677E+00 0.01190 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.08759E-07 0.00921  2.08550E-07 0.00921  2.23183E-07 0.07897 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.08681E-07 0.00887  2.08473E-07 0.00887  2.22805E-07 0.07901 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  3.57240E-03 0.03215  6.46610E-05 0.22624  6.59330E-04 0.07393  5.20855E-04 0.08299  1.56987E-03 0.04765  6.10892E-04 0.07598  1.46798E-04 0.15806 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.07263E-01 0.09201  1.26469E-02 0.00702  3.01098E-02 0.00070  1.11946E-01 0.00328  3.30920E-01 0.00201  1.31550E+00 0.00461  9.64902E+00 0.02635 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.97685E-07 0.01275  1.97206E-07 0.01280  9.39395E-08 0.19667 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.97799E-07 0.01272  1.97322E-07 0.01278  9.38837E-08 0.19753 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  3.95644E-03 0.11075  3.53173E-05 0.70637  8.41117E-04 0.24751  4.28580E-04 0.30651  2.12572E-03 0.15750  4.44804E-04 0.28087  8.08945E-05 0.53348 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  6.24691E-01 0.20896  1.24811E-02 0.0E+00  3.01366E-02 0.00161  1.11288E-01 0.00985  3.29659E-01 0.00535  1.30647E+00 0.01535  8.58378E+00 0.16254 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  3.95432E-03 0.10887  3.17521E-05 0.70937  8.48314E-04 0.24286  4.36669E-04 0.30462  2.12116E-03 0.15509  4.29230E-04 0.26614  8.72009E-05 0.48539 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  6.24467E-01 0.20946  1.24811E-02 0.0E+00  3.01366E-02 0.00161  1.11288E-01 0.00985  3.29588E-01 0.00535  1.30647E+00 0.01535  8.58378E+00 0.16254 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.11114E+04 0.11978 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.02364E-07 0.00364 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.02344E-07 0.00314 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  3.44462E-03 0.02473 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.71314E+04 0.02526 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.15932E-09 0.00854 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.97277E+00 0.03884 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  5.10720E+01 0.00092  3.10525E+01 0.00214 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.40280E+04 0.00869  5.67890E+04 0.00348  1.20174E+05 0.00274  1.87329E+05 0.00245  3.13257E+05 0.00178  5.66547E+05 0.00153  8.45239E+05 0.00139  8.78126E+05 0.00142  9.56011E+05 0.00139  7.65335E+05 0.00158  5.89636E+05 0.00200  4.09342E+05 0.00288  4.05759E+05 0.00309  1.95284E+05 0.00424  8.00718E+04 0.00528  4.13655E+04 0.00606  8.81894E+03 0.00564  3.28269E+04 0.00935  2.35590E+04 0.01762  2.06743E+04 0.02919  1.09200E+04 0.03988  5.91352E+03 0.03693  3.16136E+03 0.03968  3.16754E+03 0.04496  2.49078E+03 0.05345  8.83440E+03 0.05757  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.00379E+00 0.00114 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.99167E+22 0.00141  0.00000E+00 0.0E+00 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  3.13215E-01 0.00051  0.00000E+00 0.0E+00 ];
INF_CAPT                  (idx, [1:   4]) = [  4.01550E-03 0.00098  0.00000E+00 0.0E+00 ];
INF_ABS                   (idx, [1:   4]) = [  6.12341E-03 0.00085  0.00000E+00 0.0E+00 ];
INF_FISS                  (idx, [1:   4]) = [  2.10791E-03 0.00141  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  6.12358E-03 0.00142  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.90504E+00 3.4E-05  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.07677E+02 3.2E-06  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  3.16246E-09 0.00928  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.07094E-01 0.00051  0.00000E+00 0.0E+00 ];
INF_SCATT1                (idx, [1:   4]) = [  3.74411E-02 0.00115  0.00000E+00 0.0E+00 ];
INF_SCATT2                (idx, [1:   4]) = [  1.32016E-02 0.00151  0.00000E+00 0.0E+00 ];
INF_SCATT3                (idx, [1:   4]) = [  4.24195E-03 0.00550  0.00000E+00 0.0E+00 ];
INF_SCATT4                (idx, [1:   4]) = [  2.43978E-03 0.00630  0.00000E+00 0.0E+00 ];
INF_SCATT5                (idx, [1:   4]) = [  7.92238E-04 0.01754  0.00000E+00 0.0E+00 ];
INF_SCATT6                (idx, [1:   4]) = [  3.66655E-04 0.03499  0.00000E+00 0.0E+00 ];
INF_SCATT7                (idx, [1:   4]) = [  1.40045E-04 0.09992  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.07114E-01 0.00051  0.00000E+00 0.0E+00 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.74414E-02 0.00115  0.00000E+00 0.0E+00 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.32016E-02 0.00151  0.00000E+00 0.0E+00 ];
INF_SCATTP3               (idx, [1:   4]) = [  4.24175E-03 0.00550  0.00000E+00 0.0E+00 ];
INF_SCATTP4               (idx, [1:   4]) = [  2.43976E-03 0.00632  0.00000E+00 0.0E+00 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.92215E-04 0.01758  0.00000E+00 0.0E+00 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.66574E-04 0.03508  0.00000E+00 0.0E+00 ];
INF_SCATTP7               (idx, [1:   4]) = [  1.40125E-04 0.09993  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.48051E-01 0.00058  0.00000E+00 0.0E+00 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34382E+00 0.00058  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.10331E-03 0.00087  0.00000E+00 0.0E+00 ];
INF_REMXS                 (idx, [1:   4]) = [  6.12065E-03 0.00149  0.00000E+00 0.0E+00 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.07094E-01 0.00051  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S1                    (idx, [1:   8]) = [  3.74411E-02 0.00115  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S2                    (idx, [1:   8]) = [  1.32016E-02 0.00151  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S3                    (idx, [1:   8]) = [  4.24195E-03 0.00550  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S4                    (idx, [1:   8]) = [  2.43978E-03 0.00630  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S5                    (idx, [1:   8]) = [  7.92238E-04 0.01754  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S6                    (idx, [1:   8]) = [  3.66655E-04 0.03499  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S7                    (idx, [1:   8]) = [  1.40045E-04 0.09992  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.07114E-01 0.00051  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP1                   (idx, [1:   8]) = [  3.74414E-02 0.00115  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP2                   (idx, [1:   8]) = [  1.32016E-02 0.00151  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP3                   (idx, [1:   8]) = [  4.24175E-03 0.00550  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP4                   (idx, [1:   8]) = [  2.43976E-03 0.00632  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP5                   (idx, [1:   8]) = [  7.92215E-04 0.01758  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP6                   (idx, [1:   8]) = [  3.66574E-04 0.03508  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP7                   (idx, [1:   8]) = [  1.40125E-04 0.09993  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  2.45832E-01 0.00171  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.42590E-01 0.00325  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.42884E-01 0.00208  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.52311E-01 0.00164  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.35602E+00 0.00171  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.37435E+00 0.00327  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.37252E+00 0.00209  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.32119E+00 0.00164  0.00000E+00 0.0E+00 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  3.59022E-03 0.01940  7.65892E-05 0.13875  6.45364E-04 0.04514  5.15424E-04 0.05504  1.57404E-03 0.02911  6.25375E-04 0.04767  1.53419E-04 0.09479 ];
LAMBDA                    (idx, [1:  14]) = [  8.11376E-01 0.04897  1.25516E-02 0.00230  3.00910E-02 0.00033  1.12174E-01 0.00193  3.32074E-01 0.00117  1.31362E+00 0.00263  9.79677E+00 0.01190 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.30' ;
COMPILE_DATE              (idx, [1: 20])  = 'Feb 14 2018 11:48:41' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 10])  = 'BnB_stage1' ;
WORKING_DIRECTORY         (idx, [1: 62])  = '/global/home/users/ckeckler/docs/wire_wrap/ADOPT_wire_combined' ;
HOSTNAME                  (idx, [1: 12])  = 'n0033.savio2' ;
CPU_TYPE                  (idx, [1: 41])  = 'Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz' ;
CPU_MHZ                   (idx, 1)        = 45.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Aug 16 14:05:01 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Aug 16 14:07:43 2018' ;

% Run parameters:

POP                       (idx, 1)        = 2000 ;
CYCLES                    (idx, 1)        = 420 ;
SKIP                      (idx, 1)        = 30 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1534453501 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 1 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 20 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  20]) = [  1.00700E+00  1.00631E+00  1.01700E+00  1.00001E+00  9.91220E-01  1.00278E+00  9.96345E-01  1.00258E+00  9.86782E-01  9.95857E-01  9.94082E-01  1.00311E+00  9.92107E-01  9.98986E-01  9.96390E-01  9.92418E-01  1.00748E+00  1.00422E+00  9.99874E-01  1.00544E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 73])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.62408E-03 0.02798  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.98376E-01 4.6E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  7.51015E-01 0.00027  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.51386E-01 0.00027  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.29596E+00 0.00042  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  5.08218E+01 0.00099  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  5.08200E+01 0.00099  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.68190E+01 0.00163  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  9.62747E-03 0.02963  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 420 ;
SOURCE_POPULATION         (idx, 1)        = 840876 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00209E+03 0.00218 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00209E+03 0.00218 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.51308E+01 ;
RUNNING_TIME              (idx, 1)        =  2.69717E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  9.47517E-01  9.47517E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  6.78167E-02  3.28667E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.59613E+00  7.91317E-01  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  8.34167E-02  8.34167E-02 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  7.08333E-03  7.66667E-04 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  2.69667E+00  4.53887E+00 ];
CPU_USAGE                 (idx, 1)        = 13.02509 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.98458E+01 0.00106 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  6.33257E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64322.08 ;
ALLOC_MEMSIZE             (idx, 1)        = 11422.48;
MEMSIZE                   (idx, 1)        = 11240.16;
XS_MEMSIZE                (idx, 1)        = 7290.37;
MAT_MEMSIZE               (idx, 1)        = 1329.42;
RES_MEMSIZE               (idx, 1)        = 1.65;
MISC_MEMSIZE              (idx, 1)        = 2618.72;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 182.32;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 140 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-03 ;
NEUTRON_ERG_NE            (idx, 1)        = 157789 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-05 ;
NEUTRON_EMAX              (idx, 1)        =  1.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 444 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 2628 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 646 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1982 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 15990 ;
TOT_TRANSMU_REA           (idx, 1)        = 4042 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  9.21582E+20 ;
TOT_DECAY_HEAT            (idx, 1)        =  2.21241E+08 ;
TOT_SF_RATE               (idx, 1)        =  4.73233E+09 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  3.04684E+20 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  2.13860E+07 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  6.15686E+20 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.99443E+08 ;
INHALATION_TOXICITY       (idx, 1)        =  6.38717E+12 ;
INGESTION_TOXICITY        (idx, 1)        =  4.88436E+11 ;
ACTINIDE_INH_TOX          (idx, 1)        =  5.56717E+12 ;
ACTINIDE_ING_TOX          (idx, 1)        =  1.37502E+11 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  8.19548E+11 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  3.50581E+11 ;
SR90_ACTIVITY             (idx, 1)        =  3.25815E+17 ;
TE132_ACTIVITY            (idx, 1)        =  5.48233E+18 ;
I131_ACTIVITY             (idx, 1)        =  4.05930E+18 ;
I132_ACTIVITY             (idx, 1)        =  5.68856E+18 ;
CS134_ACTIVITY            (idx, 1)        =  6.04402E+17 ;
CS137_ACTIVITY            (idx, 1)        =  8.27254E+17 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  8.46649E+20 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  9.04012E+17 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  9.55740E+16 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  1.44316E+21 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.50258E+17 0.00083  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 108 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 1 ;
BURNUP                     (idx, [1:  2])  = [  2.84729E+00  2.84726E+00 ];
BURN_DAYS                 (idx, 1)        =  2.43333E+02 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.55849E+00 0.00255 ];
U235_FISS                 (idx, [1:   4]) = [  1.16598E+18 0.01806  1.11597E-02 0.01812 ];
U238_FISS                 (idx, [1:   4]) = [  1.99430E+19 0.00444  1.90515E-01 0.00383 ];
PU239_FISS                (idx, [1:   4]) = [  7.95416E+19 0.00209  7.60136E-01 0.00105 ];
PU240_FISS                (idx, [1:   4]) = [  2.44767E+18 0.01323  2.33767E-02 0.01299 ];
PU241_FISS                (idx, [1:   4]) = [  1.15338E+18 0.01879  1.10145E-02 0.01866 ];
U235_CAPT                 (idx, [1:   4]) = [  3.17823E+17 0.03420  1.61957E-03 0.03416 ];
U238_CAPT                 (idx, [1:   4]) = [  1.48347E+20 0.00137  7.55700E-01 0.00078 ];
PU239_CAPT                (idx, [1:   4]) = [  1.45739E+19 0.00491  7.42570E-02 0.00489 ];
PU240_CAPT                (idx, [1:   4]) = [  2.40770E+18 0.01238  1.22657E-02 0.01235 ];
PU241_CAPT                (idx, [1:   4]) = [  1.71176E+17 0.04610  8.71923E-04 0.04608 ];
SM149_CAPT                (idx, [1:   4]) = [  6.17624E+17 0.02399  3.14652E-03 0.02389 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 840876 8.40000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.72436E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 840876 8.42724E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 547267 5.48721E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 292087 2.92482E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 1522 1.52148E+03 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 840876 8.42724E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 3.25963E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.50000E+09 0.0E+00  3.50000E+09 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  1.17012E-02 3.4E-09  1.17012E-02 3.4E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  3.05735E+20 3.9E-05  3.05735E+20 3.9E-05  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  1.05182E+20 1.6E-06  1.05182E+20 1.6E-06  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.96122E+20 0.00100  1.95074E+20 0.00098  1.04829E+18 0.02349 ];
TOT_ABSRATE               (idx, [1:   6]) = [  3.01304E+20 0.00065  3.00256E+20 0.00064  1.04829E+18 0.02349 ];
TOT_SRCRATE               (idx, [1:   6]) = [  3.00516E+20 0.00083  3.00516E+20 0.00083  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  4.88714E+22 0.00078  4.78284E+22 0.00059  1.04309E+21 0.01935 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  5.44738E+17 0.02818 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.01849E+20 0.00066 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.53200E+22 0.00067 ];
INI_FMASS                 (idx, 1)        =  2.99115E+05 ;
TOT_FMASS                 (idx, 1)        =  2.98232E+05 ;
INI_BURN_FMASS            (idx, 1)        =  2.99115E+05 ;
TOT_BURN_FMASS            (idx, 1)        =  2.98232E+05 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_F                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_P                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.98189E-01 5.1E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.90672E+00 3.9E-05 ];
FISSE                     (idx, [1:   2]) = [  2.07690E+02 1.6E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.01170E+00 0.00160  1.00858E+00 0.00157  3.71130E-03 0.03151 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.01633E+00 0.00067 ];
COL_KEFF                  (idx, [1:   2]) = [  1.01766E+00 0.00083 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.01633E+00 0.00067 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01817E+00 0.00067 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 1.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  3.61116E+00 0.00088 ];
IMP_ALF                   (idx, [1:   2]) = [  3.61219E+00 0.00051 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  2.70779E-01 0.00319 ];
IMP_EALF                  (idx, [1:   2]) = [  2.70115E-01 0.00183 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  9.31786E-01 0.00275 ];
IMP_AFGE                  (idx, [1:   2]) = [  9.28602E-01 0.00142 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  4.69639E-03 0.01610  8.99604E-05 0.11848  8.06858E-04 0.03955  7.36528E-04 0.04038  1.95377E-03 0.02507  8.99293E-04 0.03419  2.09981E-04 0.07273 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.84479E-01 0.04598  2.05711E-03 0.11020  2.40052E-02 0.02461  8.71664E-02 0.02611  3.23375E-01 0.00808  1.11976E+00 0.02046  3.48674E+00 0.06674 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  3.72516E-03 0.02018  6.99281E-05 0.15460  6.63044E-04 0.05109  5.52614E-04 0.05380  1.55229E-03 0.03072  7.10902E-04 0.04508  1.76384E-04 0.09458 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  9.14697E-01 0.05567  1.25214E-02 0.00167  3.00906E-02 0.00036  1.11900E-01 0.00186  3.32012E-01 0.00121  1.31400E+00 0.00244  9.82241E+00 0.01119 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.06767E-07 0.00822  2.06427E-07 0.00825  2.74198E-07 0.08823 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.09034E-07 0.00825  2.08691E-07 0.00829  2.76856E-07 0.08855 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  3.65404E-03 0.03163  7.44339E-05 0.22211  6.66262E-04 0.07446  5.89772E-04 0.07832  1.53945E-03 0.04954  6.24666E-04 0.07263  1.59449E-04 0.14598 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.24285E-01 0.08301  1.24855E-02 0.00011  3.00935E-02 0.00043  1.12256E-01 0.00306  3.32228E-01 0.00204  1.30407E+00 0.00605  9.90039E+00 0.01647 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.90686E-07 0.01142  1.90090E-07 0.01141  9.85315E-08 0.16364 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.92831E-07 0.01140  1.92240E-07 0.01140  9.86515E-08 0.16276 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  3.97035E-03 0.11103  9.12672E-05 0.53317  8.06517E-04 0.21458  7.85078E-04 0.27829  1.66865E-03 0.18188  4.79240E-04 0.24791  1.39592E-04 0.43807 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  7.18912E-01 0.22044  1.24811E-02 0.0E+00  3.01191E-02 0.00099  1.11737E-01 0.00837  3.31104E-01 0.00531  1.30647E+00 0.01535  9.97903E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  3.89114E-03 0.11111  7.99370E-05 0.54511  7.88782E-04 0.21664  8.05729E-04 0.27241  1.59852E-03 0.18455  4.66847E-04 0.24050  1.51323E-04 0.44742 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  7.23798E-01 0.21932  1.24811E-02 0.0E+00  3.01191E-02 0.00099  1.11737E-01 0.00837  3.31111E-01 0.00530  1.30647E+00 0.01535  9.97903E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.28444E+04 0.11521 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.98501E-07 0.00296 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.00612E-07 0.00249 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  3.72833E-03 0.01948 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.88766E+04 0.01995 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.12488E-09 0.00856 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.57209E+00 0.03685 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  5.08200E+01 0.00099  3.11092E+01 0.00199 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.41644E+04 0.00594  5.68889E+04 0.00344  1.19857E+05 0.00235  1.87677E+05 0.00166  3.14068E+05 0.00214  5.66779E+05 0.00156  8.43243E+05 0.00173  8.75672E+05 0.00154  9.49854E+05 0.00101  7.62225E+05 0.00147  5.86262E+05 0.00181  4.03779E+05 0.00253  3.98575E+05 0.00335  1.91093E+05 0.00446  7.86798E+04 0.00486  4.08215E+04 0.00526  8.70145E+03 0.00581  3.21803E+04 0.00587  2.32658E+04 0.01105  2.00176E+04 0.02439  1.01573E+04 0.03763  5.53075E+03 0.04669  2.96442E+03 0.04987  2.83823E+03 0.04447  2.28968E+03 0.04593  8.75628E+03 0.05212  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01948E+00 0.00101 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.88810E+22 0.00116  0.00000E+00 0.0E+00 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  3.13491E-01 0.00045  0.00000E+00 0.0E+00 ];
INF_CAPT                  (idx, [1:   4]) = [  4.01357E-03 0.00090  0.00000E+00 0.0E+00 ];
INF_ABS                   (idx, [1:   4]) = [  6.16601E-03 0.00080  0.00000E+00 0.0E+00 ];
INF_FISS                  (idx, [1:   4]) = [  2.15243E-03 0.00116  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  6.25651E-03 0.00117  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.90672E+00 2.1E-05  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.07690E+02 3.0E-06  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  3.12803E-09 0.00911  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.07334E-01 0.00046  0.00000E+00 0.0E+00 ];
INF_SCATT1                (idx, [1:   4]) = [  3.76620E-02 0.00117  0.00000E+00 0.0E+00 ];
INF_SCATT2                (idx, [1:   4]) = [  1.32976E-02 0.00158  0.00000E+00 0.0E+00 ];
INF_SCATT3                (idx, [1:   4]) = [  4.25348E-03 0.00403  0.00000E+00 0.0E+00 ];
INF_SCATT4                (idx, [1:   4]) = [  2.42908E-03 0.00739  0.00000E+00 0.0E+00 ];
INF_SCATT5                (idx, [1:   4]) = [  8.28511E-04 0.02133  0.00000E+00 0.0E+00 ];
INF_SCATT6                (idx, [1:   4]) = [  3.54736E-04 0.03467  0.00000E+00 0.0E+00 ];
INF_SCATT7                (idx, [1:   4]) = [  1.06476E-04 0.12876  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.07354E-01 0.00046  0.00000E+00 0.0E+00 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.76622E-02 0.00117  0.00000E+00 0.0E+00 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.32978E-02 0.00158  0.00000E+00 0.0E+00 ];
INF_SCATTP3               (idx, [1:   4]) = [  4.25341E-03 0.00403  0.00000E+00 0.0E+00 ];
INF_SCATTP4               (idx, [1:   4]) = [  2.42921E-03 0.00740  0.00000E+00 0.0E+00 ];
INF_SCATTP5               (idx, [1:   4]) = [  8.28792E-04 0.02128  0.00000E+00 0.0E+00 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.54600E-04 0.03473  0.00000E+00 0.0E+00 ];
INF_SCATTP7               (idx, [1:   4]) = [  1.06466E-04 0.12899  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.48208E-01 0.00066  0.00000E+00 0.0E+00 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34297E+00 0.00066  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.14607E-03 0.00081  0.00000E+00 0.0E+00 ];
INF_REMXS                 (idx, [1:   4]) = [  6.15698E-03 0.00122  0.00000E+00 0.0E+00 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.07334E-01 0.00046  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S1                    (idx, [1:   8]) = [  3.76620E-02 0.00117  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S2                    (idx, [1:   8]) = [  1.32976E-02 0.00158  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S3                    (idx, [1:   8]) = [  4.25348E-03 0.00403  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S4                    (idx, [1:   8]) = [  2.42908E-03 0.00739  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S5                    (idx, [1:   8]) = [  8.28511E-04 0.02133  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S6                    (idx, [1:   8]) = [  3.54736E-04 0.03467  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S7                    (idx, [1:   8]) = [  1.06476E-04 0.12876  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.07354E-01 0.00046  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP1                   (idx, [1:   8]) = [  3.76622E-02 0.00117  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP2                   (idx, [1:   8]) = [  1.32978E-02 0.00158  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP3                   (idx, [1:   8]) = [  4.25341E-03 0.00403  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP4                   (idx, [1:   8]) = [  2.42921E-03 0.00740  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP5                   (idx, [1:   8]) = [  8.28792E-04 0.02128  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP6                   (idx, [1:   8]) = [  3.54600E-04 0.03473  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP7                   (idx, [1:   8]) = [  1.06466E-04 0.12899  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  2.45697E-01 0.00175  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.42883E-01 0.00219  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.42593E-01 0.00286  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.51902E-01 0.00294  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.35677E+00 0.00175  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.37253E+00 0.00218  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.37427E+00 0.00287  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.32350E+00 0.00297  0.00000E+00 0.0E+00 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  3.72516E-03 0.02018  6.99281E-05 0.15460  6.63044E-04 0.05109  5.52614E-04 0.05380  1.55229E-03 0.03072  7.10902E-04 0.04508  1.76384E-04 0.09458 ];
LAMBDA                    (idx, [1:  14]) = [  9.14697E-01 0.05567  1.25214E-02 0.00167  3.00906E-02 0.00036  1.11900E-01 0.00186  3.32012E-01 0.00121  1.31400E+00 0.00244  9.82241E+00 0.01119 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.30' ;
COMPILE_DATE              (idx, [1: 20])  = 'Feb 14 2018 11:48:41' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 10])  = 'BnB_stage1' ;
WORKING_DIRECTORY         (idx, [1: 62])  = '/global/home/users/ckeckler/docs/wire_wrap/ADOPT_wire_combined' ;
HOSTNAME                  (idx, [1: 12])  = 'n0033.savio2' ;
CPU_TYPE                  (idx, [1: 41])  = 'Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz' ;
CPU_MHZ                   (idx, 1)        = 45.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Aug 16 14:05:01 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Aug 16 14:08:38 2018' ;

% Run parameters:

POP                       (idx, 1)        = 2000 ;
CYCLES                    (idx, 1)        = 420 ;
SKIP                      (idx, 1)        = 30 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1534453501 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 1 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 20 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  20]) = [  1.00673E+00  1.00638E+00  1.01710E+00  1.00048E+00  1.00179E+00  1.00953E+00  9.97258E-01  9.88403E-01  1.01199E+00  1.00054E+00  9.95860E-01  9.96126E-01  1.00152E+00  9.92708E-01  9.89091E-01  9.88225E-01  1.00418E+00  9.92531E-01  9.99721E-01  9.99832E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 73])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.80504E-03 0.02858  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.98195E-01 5.2E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  7.51408E-01 0.00032  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.51819E-01 0.00031  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.29515E+00 0.00043  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  5.05668E+01 0.00095  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  5.05648E+01 0.00095  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.66964E+01 0.00174  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.07183E-02 0.03033  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 420 ;
SOURCE_POPULATION         (idx, 1)        = 840701 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00167E+03 0.00204 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00167E+03 0.00204 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  5.31210E+01 ;
RUNNING_TIME              (idx, 1)        =  3.61913E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  9.47517E-01  9.47517E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.01333E-01  3.35167E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  2.39637E+00  8.00233E-01  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  1.69833E-01  8.64167E-02 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  1.39167E-02  1.23334E-03 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  3.61865E+00  4.52990E+00 ];
CPU_USAGE                 (idx, 1)        = 14.67782 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.98540E+01 0.00086 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.21448E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64322.08 ;
ALLOC_MEMSIZE             (idx, 1)        = 11422.48;
MEMSIZE                   (idx, 1)        = 11240.16;
XS_MEMSIZE                (idx, 1)        = 7290.37;
MAT_MEMSIZE               (idx, 1)        = 1329.42;
RES_MEMSIZE               (idx, 1)        = 1.65;
MISC_MEMSIZE              (idx, 1)        = 2618.72;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 182.32;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 140 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-03 ;
NEUTRON_ERG_NE            (idx, 1)        = 157789 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-05 ;
NEUTRON_EMAX              (idx, 1)        =  1.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 444 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 2628 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 646 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1982 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 15990 ;
TOT_TRANSMU_REA           (idx, 1)        = 4042 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  9.10040E+20 ;
TOT_DECAY_HEAT            (idx, 1)        =  2.19525E+08 ;
TOT_SF_RATE               (idx, 1)        =  5.41432E+09 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  2.93995E+20 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  2.06455E+07 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  6.14724E+20 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.98466E+08 ;
INHALATION_TOXICITY       (idx, 1)        =  6.89048E+12 ;
INGESTION_TOXICITY        (idx, 1)        =  4.90951E+11 ;
ACTINIDE_INH_TOX          (idx, 1)        =  6.03261E+12 ;
ACTINIDE_ING_TOX          (idx, 1)        =  1.34056E+11 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  8.57302E+11 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  3.56480E+11 ;
SR90_ACTIVITY             (idx, 1)        =  3.59759E+17 ;
TE132_ACTIVITY            (idx, 1)        =  5.45769E+18 ;
I131_ACTIVITY             (idx, 1)        =  4.04452E+18 ;
I132_ACTIVITY             (idx, 1)        =  5.66352E+18 ;
CS134_ACTIVITY            (idx, 1)        =  6.86994E+17 ;
CS137_ACTIVITY            (idx, 1)        =  9.18180E+17 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  8.32866E+20 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  8.92307E+17 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  1.06321E+17 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  1.41509E+21 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.49302E+17 0.00082  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 108 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 2 ;
BURNUP                     (idx, [1:  2])  = [  5.69458E+00  5.69452E+00 ];
BURN_DAYS                 (idx, 1)        =  4.86667E+02 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.50678E+00 0.00250 ];
U235_FISS                 (idx, [1:   4]) = [  1.12214E+18 0.01786  1.06510E-02 0.01791 ];
U238_FISS                 (idx, [1:   4]) = [  1.99188E+19 0.00426  1.88910E-01 0.00386 ];
PU239_FISS                (idx, [1:   4]) = [  8.02095E+19 0.00202  7.60780E-01 0.00108 ];
PU240_FISS                (idx, [1:   4]) = [  2.55723E+18 0.01273  2.42437E-02 0.01250 ];
PU241_FISS                (idx, [1:   4]) = [  1.22487E+18 0.01708  1.16265E-02 0.01717 ];
U235_CAPT                 (idx, [1:   4]) = [  3.05888E+17 0.03510  1.57867E-03 0.03484 ];
U238_CAPT                 (idx, [1:   4]) = [  1.44344E+20 0.00140  7.45898E-01 0.00079 ];
PU239_CAPT                (idx, [1:   4]) = [  1.46045E+19 0.00494  7.54850E-02 0.00491 ];
PU240_CAPT                (idx, [1:   4]) = [  2.51162E+18 0.01196  1.29797E-02 0.01192 ];
PU241_CAPT                (idx, [1:   4]) = [  1.82959E+17 0.04533  9.44920E-04 0.04526 ];
SM149_CAPT                (idx, [1:   4]) = [  6.64004E+17 0.02385  3.43655E-03 0.02394 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 840701 8.40000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.68729E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 840701 8.42687E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 542887 5.44378E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 296085 2.96577E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 1729 1.73200E+03 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 840701 8.42687E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -4.65661E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.50000E+09 0.0E+00  3.50000E+09 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  1.17012E-02 3.4E-09  1.17012E-02 3.4E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  3.05830E+20 3.6E-05  3.05830E+20 3.6E-05  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  1.05178E+20 1.6E-06  1.05178E+20 1.6E-06  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.93670E+20 0.00093  1.92580E+20 0.00092  1.08993E+18 0.02013 ];
TOT_ABSRATE               (idx, [1:   6]) = [  2.98848E+20 0.00061  2.97758E+20 0.00060  1.08993E+18 0.02013 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.98603E+20 0.00082  2.98603E+20 0.00082  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  4.83395E+22 0.00078  4.72179E+22 0.00058  1.12152E+21 0.02063 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  6.16033E+17 0.02769 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.99464E+20 0.00061 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.51454E+22 0.00065 ];
INI_FMASS                 (idx, 1)        =  2.99115E+05 ;
TOT_FMASS                 (idx, 1)        =  2.97351E+05 ;
INI_BURN_FMASS            (idx, 1)        =  2.99115E+05 ;
TOT_BURN_FMASS            (idx, 1)        =  2.97351E+05 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_F                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_P                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.97938E-01 5.7E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.90775E+00 3.6E-05 ];
FISSE                     (idx, [1:   2]) = [  2.07699E+02 1.6E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.02643E+00 0.00146  1.02266E+00 0.00147  3.81222E-03 0.02873 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.02469E+00 0.00062 ];
COL_KEFF                  (idx, [1:   2]) = [  1.02449E+00 0.00083 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.02469E+00 0.00062 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02680E+00 0.00062 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 1.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  3.61998E+00 0.00094 ];
IMP_ALF                   (idx, [1:   2]) = [  3.61645E+00 0.00050 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  2.68479E-01 0.00339 ];
IMP_EALF                  (idx, [1:   2]) = [  2.68964E-01 0.00181 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  9.23933E-01 0.00277 ];
IMP_AFGE                  (idx, [1:   2]) = [  9.23428E-01 0.00134 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  4.69624E-03 0.01539  8.18055E-05 0.11629  8.47067E-04 0.03477  6.96004E-04 0.04244  1.97670E-03 0.02390  8.96481E-04 0.03728  1.98177E-04 0.07679 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.39731E-01 0.03911  1.97035E-03 0.11316  2.56582E-02 0.02033  8.31973E-02 0.02862  3.29318E-01 0.00489  1.09388E+00 0.02155  3.21222E+00 0.07096 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  3.67193E-03 0.01951  6.00500E-05 0.16610  6.63442E-04 0.04557  5.36586E-04 0.05357  1.58143E-03 0.03260  6.68166E-04 0.04394  1.62248E-04 0.09821 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.56950E-01 0.05091  1.25386E-02 0.00217  3.01016E-02 0.00032  1.11755E-01 0.00197  3.32577E-01 0.00113  1.30174E+00 0.00357  9.77832E+00 0.01254 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.07287E-07 0.01411  2.07071E-07 0.01419  2.24470E-07 0.06219 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.12547E-07 0.01383  2.12323E-07 0.01391  2.30511E-07 0.06241 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  3.72446E-03 0.02922  5.99812E-05 0.23382  7.13405E-04 0.06581  5.22202E-04 0.07703  1.55821E-03 0.04598  7.16205E-04 0.06847  1.54458E-04 0.15247 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  7.83307E-01 0.08041  1.25311E-02 0.00375  3.00973E-02 0.00052  1.11381E-01 0.00324  3.31199E-01 0.00197  1.28833E+00 0.00693  9.66767E+00 0.02654 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.86492E-07 0.01216  1.86398E-07 0.01221  6.87545E-08 0.12192 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.91273E-07 0.01205  1.91172E-07 0.01209  7.07782E-08 0.12181 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  3.90200E-03 0.10874  2.17902E-04 0.57635  6.77328E-04 0.24441  3.94568E-04 0.28465  1.70346E-03 0.17594  7.25265E-04 0.21821  1.83473E-04 0.60214 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.50370E-01 0.19671  1.24864E-02 0.00026  3.01095E-02 0.00100  1.11793E-01 0.00885  3.30641E-01 0.00497  1.29587E+00 0.01574  9.06656E+00 0.11427 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  3.97938E-03 0.10707  2.18681E-04 0.56514  6.86627E-04 0.23757  4.21366E-04 0.28685  1.71764E-03 0.17104  7.18413E-04 0.21860  2.16650E-04 0.59366 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.48972E-01 0.19707  1.24864E-02 0.00026  3.01095E-02 0.00100  1.11793E-01 0.00885  3.30676E-01 0.00495  1.29591E+00 0.01574  9.06656E+00 0.11427 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.22361E+04 0.11074 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.97433E-07 0.00348 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.02472E-07 0.00314 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  3.78833E-03 0.01812 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.92977E+04 0.01860 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.16769E-09 0.00873 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.05021E+01 0.03993 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  5.05648E+01 0.00095  3.11930E+01 0.00204 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.41962E+04 0.00636  5.70884E+04 0.00397  1.20047E+05 0.00250  1.87353E+05 0.00192  3.14248E+05 0.00169  5.65987E+05 0.00225  8.38372E+05 0.00125  8.70696E+05 0.00130  9.45452E+05 0.00148  7.57334E+05 0.00129  5.80878E+05 0.00186  4.01145E+05 0.00216  3.95253E+05 0.00256  1.90142E+05 0.00324  7.83343E+04 0.00433  4.01936E+04 0.00461  8.49990E+03 0.00452  3.16873E+04 0.00560  2.34433E+04 0.00982  2.09513E+04 0.02514  1.14234E+04 0.03461  6.15016E+03 0.03920  3.16066E+03 0.04030  3.11489E+03 0.04292  2.43636E+03 0.04425  9.14411E+03 0.06103  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02655E+00 0.00084 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.83494E+22 0.00137  0.00000E+00 0.0E+00 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  3.13326E-01 0.00052  0.00000E+00 0.0E+00 ];
INF_CAPT                  (idx, [1:   4]) = [  4.00692E-03 0.00097  0.00000E+00 0.0E+00 ];
INF_ABS                   (idx, [1:   4]) = [  6.18295E-03 0.00097  0.00000E+00 0.0E+00 ];
INF_FISS                  (idx, [1:   4]) = [  2.17603E-03 0.00137  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  6.32735E-03 0.00139  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.90775E+00 3.5E-05  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.07699E+02 2.8E-06  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  3.17136E-09 0.00931  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.07143E-01 0.00052  0.00000E+00 0.0E+00 ];
INF_SCATT1                (idx, [1:   4]) = [  3.78442E-02 0.00113  0.00000E+00 0.0E+00 ];
INF_SCATT2                (idx, [1:   4]) = [  1.33434E-02 0.00200  0.00000E+00 0.0E+00 ];
INF_SCATT3                (idx, [1:   4]) = [  4.25444E-03 0.00486  0.00000E+00 0.0E+00 ];
INF_SCATT4                (idx, [1:   4]) = [  2.44035E-03 0.00617  0.00000E+00 0.0E+00 ];
INF_SCATT5                (idx, [1:   4]) = [  7.93399E-04 0.01658  0.00000E+00 0.0E+00 ];
INF_SCATT6                (idx, [1:   4]) = [  3.61493E-04 0.04332  0.00000E+00 0.0E+00 ];
INF_SCATT7                (idx, [1:   4]) = [  1.16034E-04 0.11111  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.07163E-01 0.00052  0.00000E+00 0.0E+00 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.78441E-02 0.00113  0.00000E+00 0.0E+00 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.33438E-02 0.00200  0.00000E+00 0.0E+00 ];
INF_SCATTP3               (idx, [1:   4]) = [  4.25448E-03 0.00487  0.00000E+00 0.0E+00 ];
INF_SCATTP4               (idx, [1:   4]) = [  2.44025E-03 0.00618  0.00000E+00 0.0E+00 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.93452E-04 0.01659  0.00000E+00 0.0E+00 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.61435E-04 0.04326  0.00000E+00 0.0E+00 ];
INF_SCATTP7               (idx, [1:   4]) = [  1.16234E-04 0.11108  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.48009E-01 0.00063  0.00000E+00 0.0E+00 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34405E+00 0.00063  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.16320E-03 0.00097  0.00000E+00 0.0E+00 ];
INF_REMXS                 (idx, [1:   4]) = [  6.18344E-03 0.00104  0.00000E+00 0.0E+00 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.07143E-01 0.00052  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S1                    (idx, [1:   8]) = [  3.78442E-02 0.00113  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S2                    (idx, [1:   8]) = [  1.33434E-02 0.00200  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S3                    (idx, [1:   8]) = [  4.25444E-03 0.00486  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S4                    (idx, [1:   8]) = [  2.44035E-03 0.00617  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S5                    (idx, [1:   8]) = [  7.93399E-04 0.01658  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S6                    (idx, [1:   8]) = [  3.61493E-04 0.04332  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S7                    (idx, [1:   8]) = [  1.16034E-04 0.11111  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.07163E-01 0.00052  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP1                   (idx, [1:   8]) = [  3.78441E-02 0.00113  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP2                   (idx, [1:   8]) = [  1.33438E-02 0.00200  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP3                   (idx, [1:   8]) = [  4.25448E-03 0.00487  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP4                   (idx, [1:   8]) = [  2.44025E-03 0.00618  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP5                   (idx, [1:   8]) = [  7.93452E-04 0.01659  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP6                   (idx, [1:   8]) = [  3.61435E-04 0.04326  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP7                   (idx, [1:   8]) = [  1.16234E-04 0.11108  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  2.45956E-01 0.00138  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.42446E-01 0.00184  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.42478E-01 0.00263  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.53328E-01 0.00304  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.35531E+00 0.00138  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.37497E+00 0.00183  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.37489E+00 0.00266  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.31606E+00 0.00301  0.00000E+00 0.0E+00 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  3.67193E-03 0.01951  6.00500E-05 0.16610  6.63442E-04 0.04557  5.36586E-04 0.05357  1.58143E-03 0.03260  6.68166E-04 0.04394  1.62248E-04 0.09821 ];
LAMBDA                    (idx, [1:  14]) = [  8.56950E-01 0.05091  1.25386E-02 0.00217  3.01016E-02 0.00032  1.11755E-01 0.00197  3.32577E-01 0.00113  1.30174E+00 0.00357  9.77832E+00 0.01254 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.30' ;
COMPILE_DATE              (idx, [1: 20])  = 'Feb 14 2018 11:48:41' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 10])  = 'BnB_stage1' ;
WORKING_DIRECTORY         (idx, [1: 62])  = '/global/home/users/ckeckler/docs/wire_wrap/ADOPT_wire_combined' ;
HOSTNAME                  (idx, [1: 12])  = 'n0033.savio2' ;
CPU_TYPE                  (idx, [1: 41])  = 'Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz' ;
CPU_MHZ                   (idx, 1)        = 45.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Aug 16 14:05:01 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Aug 16 14:09:33 2018' ;

% Run parameters:

POP                       (idx, 1)        = 2000 ;
CYCLES                    (idx, 1)        = 420 ;
SKIP                      (idx, 1)        = 30 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1534453501 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 1 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 20 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  20]) = [  1.00442E+00  9.93565E-01  9.95030E-01  1.00315E+00  1.00144E+00  1.00262E+00  1.00733E+00  9.93032E-01  9.91723E-01  1.00295E+00  1.00719E+00  9.99602E-01  9.97227E-01  1.00759E+00  9.93676E-01  1.00044E+00  1.00595E+00  1.00204E+00  9.93299E-01  9.97715E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 73])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 69])  = '/global/home/groups/co_nuclear/serpent/xsdata_2/endfb7/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.65940E-03 0.02751  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.98341E-01 4.6E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  7.52741E-01 0.00031  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.53117E-01 0.00030  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.29315E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  5.04439E+01 0.00095  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  5.04420E+01 0.00095  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.65395E+01 0.00167  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  9.85900E-03 0.02945  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 420 ;
SOURCE_POPULATION         (idx, 1)        = 840853 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00203E+03 0.00211 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00203E+03 0.00211 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  7.10460E+01 ;
RUNNING_TIME              (idx, 1)        =  4.53515E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  9.47517E-01  9.47517E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.34533E-01  3.32000E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  3.19427E+00  7.97900E-01  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  2.52950E-01  8.31167E-02 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  2.06833E-02  8.16667E-04 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.53465E+00  4.53465E+00 ];
CPU_USAGE                 (idx, 1)        = 15.66563 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.98564E+01 0.00077 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.73620E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64322.08 ;
ALLOC_MEMSIZE             (idx, 1)        = 11422.48;
MEMSIZE                   (idx, 1)        = 11240.16;
XS_MEMSIZE                (idx, 1)        = 7290.37;
MAT_MEMSIZE               (idx, 1)        = 1329.42;
RES_MEMSIZE               (idx, 1)        = 1.65;
MISC_MEMSIZE              (idx, 1)        = 2618.72;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 182.32;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 140 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-03 ;
NEUTRON_ERG_NE            (idx, 1)        = 157789 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-05 ;
NEUTRON_EMAX              (idx, 1)        =  1.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 444 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 2628 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 646 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1982 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 15990 ;
TOT_TRANSMU_REA           (idx, 1)        = 4042 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  9.02967E+20 ;
TOT_DECAY_HEAT            (idx, 1)        =  2.18522E+08 ;
TOT_SF_RATE               (idx, 1)        =  6.08095E+09 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  2.87214E+20 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  2.01777E+07 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  6.14355E+20 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.97932E+08 ;
INHALATION_TOXICITY       (idx, 1)        =  7.37253E+12 ;
INGESTION_TOXICITY        (idx, 1)        =  4.93954E+11 ;
ACTINIDE_INH_TOX          (idx, 1)        =  6.48820E+12 ;
ACTINIDE_ING_TOX          (idx, 1)        =  1.32195E+11 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  8.83698E+11 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  3.61304E+11 ;
SR90_ACTIVITY             (idx, 1)        =  3.93002E+17 ;
TE132_ACTIVITY            (idx, 1)        =  5.44295E+18 ;
I131_ACTIVITY             (idx, 1)        =  4.03581E+18 ;
I132_ACTIVITY             (idx, 1)        =  5.64848E+18 ;
CS134_ACTIVITY            (idx, 1)        =  7.62350E+17 ;
CS137_ACTIVITY            (idx, 1)        =  1.00756E+18 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  8.24267E+20 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  8.85733E+17 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  1.16437E+17 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  1.39749E+21 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.47966E+17 0.00082  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 108 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 3 ;
BURNUP                     (idx, [1:  2])  = [  8.54187E+00  8.54179E+00 ];
BURN_DAYS                 (idx, 1)        =  7.30000E+02 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.46777E+00 0.00246 ];
U235_FISS                 (idx, [1:   4]) = [  1.04897E+18 0.01766  9.97513E-03 0.01767 ];
U238_FISS                 (idx, [1:   4]) = [  1.94199E+19 0.00442  1.84553E-01 0.00391 ];
PU239_FISS                (idx, [1:   4]) = [  8.04384E+19 0.00197  7.64657E-01 0.00105 ];
PU240_FISS                (idx, [1:   4]) = [  2.63567E+18 0.01166  2.50547E-02 0.01154 ];
PU241_FISS                (idx, [1:   4]) = [  1.26632E+18 0.01667  1.20349E-02 0.01662 ];
U235_CAPT                 (idx, [1:   4]) = [  2.76881E+17 0.03598  1.44821E-03 0.03591 ];
U238_CAPT                 (idx, [1:   4]) = [  1.40784E+20 0.00141  7.36794E-01 0.00082 ];
PU239_CAPT                (idx, [1:   4]) = [  1.46284E+19 0.00461  7.65748E-02 0.00458 ];
PU240_CAPT                (idx, [1:   4]) = [  2.56903E+18 0.01135  1.34443E-02 0.01125 ];
PU241_CAPT                (idx, [1:   4]) = [  1.95707E+17 0.04240  1.02252E-03 0.04231 ];
SM149_CAPT                (idx, [1:   4]) = [  6.78745E+17 0.02198  3.55367E-03 0.02198 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 840853 8.40000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.59690E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 840853 8.42597E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 541079 5.42368E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 298141 2.98595E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 1633 1.63459E+03 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 840853 8.42597E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 2.21189E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.50000E+09 0.0E+00  3.50000E+09 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  1.17012E-02 3.4E-09  1.17012E-02 3.4E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  3.05892E+20 3.5E-05  3.05892E+20 3.5E-05  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  1.05173E+20 1.5E-06  1.05173E+20 1.5E-06  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.91395E+20 0.00101  1.90313E+20 0.00100  1.08140E+18 0.02216 ];
TOT_ABSRATE               (idx, [1:   6]) = [  2.96568E+20 0.00065  2.95486E+20 0.00064  1.08140E+18 0.02216 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.95932E+20 0.00082  2.95932E+20 0.00082  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  4.77018E+22 0.00074  4.66281E+22 0.00056  1.07365E+21 0.01901 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  5.76670E+17 0.02767 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.97145E+20 0.00066 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.49720E+22 0.00065 ];
INI_FMASS                 (idx, 1)        =  2.99115E+05 ;
TOT_FMASS                 (idx, 1)        =  2.96471E+05 ;
INI_BURN_FMASS            (idx, 1)        =  2.99115E+05 ;
TOT_BURN_FMASS            (idx, 1)        =  2.96471E+05 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_F                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_P                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.98054E-01 5.4E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.90846E+00 3.5E-05 ];
FISSE                     (idx, [1:   2]) = [  2.07708E+02 1.5E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03405E+00 0.00146  1.03036E+00 0.00147  3.55869E-03 0.02975 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03287E+00 0.00067 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03395E+00 0.00082 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03287E+00 0.00067 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03488E+00 0.00067 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 1.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  3.62346E+00 0.00100 ];
IMP_ALF                   (idx, [1:   2]) = [  3.62573E+00 0.00050 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  2.67640E-01 0.00365 ];
IMP_EALF                  (idx, [1:   2]) = [  2.66477E-01 0.00179 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  9.15209E-01 0.00302 ];
IMP_AFGE                  (idx, [1:   2]) = [  9.13842E-01 0.00140 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  4.49901E-03 0.01559  8.60765E-05 0.11419  7.92617E-04 0.03790  6.41753E-04 0.04480  1.94825E-03 0.02559  8.27545E-04 0.03799  2.02763E-04 0.07569 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.49437E-01 0.04149  2.08553E-03 0.10925  2.37249E-02 0.02533  8.07875E-02 0.03042  3.25624E-01 0.00689  1.07114E+00 0.02331  3.27848E+00 0.06995 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  3.55032E-03 0.01984  6.99915E-05 0.15938  6.11265E-04 0.04926  5.08745E-04 0.05651  1.54402E-03 0.03218  6.62878E-04 0.04852  1.53422E-04 0.09746 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.41210E-01 0.05014  1.25132E-02 0.00159  3.01064E-02 0.00040  1.11975E-01 0.00200  3.32051E-01 0.00121  1.31052E+00 0.00306  9.77149E+00 0.01319 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.02615E-07 0.00924  2.02445E-07 0.00928  2.15606E-07 0.06987 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.09300E-07 0.00907  2.09122E-07 0.00911  2.23281E-07 0.07015 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  3.45706E-03 0.03034  5.14704E-05 0.25953  5.78796E-04 0.07874  5.15406E-04 0.08369  1.54110E-03 0.04710  6.19074E-04 0.07100  1.51211E-04 0.14791 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  9.12474E-01 0.09901  1.24861E-02 0.00013  3.00932E-02 0.00049  1.12091E-01 0.00330  3.32680E-01 0.00190  1.30062E+00 0.00643  9.48996E+00 0.03444 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.90171E-07 0.01224  1.90210E-07 0.01231  6.00674E-08 0.13888 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.96423E-07 0.01209  1.96463E-07 0.01216  6.22025E-08 0.14113 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  3.72905E-03 0.11330  1.41821E-05 0.83705  6.00519E-04 0.30453  4.89058E-04 0.29874  1.63794E-03 0.16310  6.73117E-04 0.29294  3.14236E-04 0.42503 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  9.71829E-01 0.20043  1.24811E-02 1.5E-08  3.01449E-02 0.00291  1.12702E-01 0.00886  3.34059E-01 0.00436  1.29163E+00 0.01870  9.36214E+00 0.08561 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  3.77311E-03 0.10948  1.28500E-05 0.82346  6.12306E-04 0.29353  4.59131E-04 0.29007  1.68754E-03 0.15736  7.22632E-04 0.28587  2.78656E-04 0.40860 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  9.78079E-01 0.19934  1.24811E-02 0.0E+00  3.01447E-02 0.00291  1.12702E-01 0.00886  3.34059E-01 0.00436  1.29163E+00 0.01870  9.36214E+00 0.08561 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.06051E+04 0.11048 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.96172E-07 0.00389 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.02677E-07 0.00363 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  3.52430E-03 0.01998 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.80226E+04 0.02010 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.09300E-09 0.00815 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04834E+01 0.04151 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  5.04420E+01 0.00095  3.12482E+01 0.00217 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.40816E+04 0.00909  5.69301E+04 0.00414  1.19886E+05 0.00190  1.87951E+05 0.00203  3.12818E+05 0.00207  5.64006E+05 0.00135  8.35195E+05 0.00157  8.67363E+05 0.00104  9.44272E+05 0.00174  7.56118E+05 0.00169  5.80511E+05 0.00185  3.99294E+05 0.00189  3.92013E+05 0.00277  1.87436E+05 0.00366  7.71154E+04 0.00341  3.95800E+04 0.00422  8.47259E+03 0.00536  3.11345E+04 0.00466  2.25551E+04 0.00862  2.00647E+04 0.01825  1.06841E+04 0.02350  5.63123E+03 0.02651  2.92442E+03 0.02190  2.88830E+03 0.03039  2.20058E+03 0.03369  7.87661E+03 0.05870  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.03600E+00 0.00099 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.77113E+22 0.00112  0.00000E+00 0.0E+00 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  3.13878E-01 0.00037  0.00000E+00 0.0E+00 ];
INF_CAPT                  (idx, [1:   4]) = [  4.01273E-03 0.00087  0.00000E+00 0.0E+00 ];
INF_ABS                   (idx, [1:   4]) = [  6.21773E-03 0.00075  0.00000E+00 0.0E+00 ];
INF_FISS                  (idx, [1:   4]) = [  2.20500E-03 0.00112  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  6.41317E-03 0.00113  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.90846E+00 4.2E-05  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.07708E+02 2.8E-06  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  3.09653E-09 0.00669  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.07669E-01 0.00037  0.00000E+00 0.0E+00 ];
INF_SCATT1                (idx, [1:   4]) = [  3.79776E-02 0.00105  0.00000E+00 0.0E+00 ];
INF_SCATT2                (idx, [1:   4]) = [  1.34518E-02 0.00195  0.00000E+00 0.0E+00 ];
INF_SCATT3                (idx, [1:   4]) = [  4.27521E-03 0.00414  0.00000E+00 0.0E+00 ];
INF_SCATT4                (idx, [1:   4]) = [  2.47909E-03 0.00551  0.00000E+00 0.0E+00 ];
INF_SCATT5                (idx, [1:   4]) = [  8.30805E-04 0.01897  0.00000E+00 0.0E+00 ];
INF_SCATT6                (idx, [1:   4]) = [  3.64415E-04 0.03646  0.00000E+00 0.0E+00 ];
INF_SCATT7                (idx, [1:   4]) = [  1.34114E-04 0.08803  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.07688E-01 0.00037  0.00000E+00 0.0E+00 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.79776E-02 0.00105  0.00000E+00 0.0E+00 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.34521E-02 0.00195  0.00000E+00 0.0E+00 ];
INF_SCATTP3               (idx, [1:   4]) = [  4.27522E-03 0.00414  0.00000E+00 0.0E+00 ];
INF_SCATTP4               (idx, [1:   4]) = [  2.47913E-03 0.00553  0.00000E+00 0.0E+00 ];
INF_SCATTP5               (idx, [1:   4]) = [  8.30814E-04 0.01894  0.00000E+00 0.0E+00 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.64399E-04 0.03640  0.00000E+00 0.0E+00 ];
INF_SCATTP7               (idx, [1:   4]) = [  1.34157E-04 0.08786  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.48546E-01 0.00040  0.00000E+00 0.0E+00 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34114E+00 0.00040  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.19856E-03 0.00077  0.00000E+00 0.0E+00 ];
INF_REMXS                 (idx, [1:   4]) = [  6.20956E-03 0.00109  0.00000E+00 0.0E+00 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.07669E-01 0.00037  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S1                    (idx, [1:   8]) = [  3.79776E-02 0.00105  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S2                    (idx, [1:   8]) = [  1.34518E-02 0.00195  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S3                    (idx, [1:   8]) = [  4.27521E-03 0.00414  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S4                    (idx, [1:   8]) = [  2.47909E-03 0.00551  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S5                    (idx, [1:   8]) = [  8.30805E-04 0.01897  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S6                    (idx, [1:   8]) = [  3.64415E-04 0.03646  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_S7                    (idx, [1:   8]) = [  1.34114E-04 0.08803  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.07688E-01 0.00037  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP1                   (idx, [1:   8]) = [  3.79776E-02 0.00105  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP2                   (idx, [1:   8]) = [  1.34521E-02 0.00195  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP3                   (idx, [1:   8]) = [  4.27522E-03 0.00414  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP4                   (idx, [1:   8]) = [  2.47913E-03 0.00553  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP5                   (idx, [1:   8]) = [  8.30814E-04 0.01894  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP6                   (idx, [1:   8]) = [  3.64399E-04 0.03640  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SP7                   (idx, [1:   8]) = [  1.34157E-04 0.08786  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  2.45807E-01 0.00157  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.43108E-01 0.00227  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.42396E-01 0.00233  0.00000E+00 0.0E+00 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.52198E-01 0.00223  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.35614E+00 0.00157  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.37127E+00 0.00226  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.37531E+00 0.00230  0.00000E+00 0.0E+00 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.32185E+00 0.00224  0.00000E+00 0.0E+00 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  3.55032E-03 0.01984  6.99915E-05 0.15938  6.11265E-04 0.04926  5.08745E-04 0.05651  1.54402E-03 0.03218  6.62878E-04 0.04852  1.53422E-04 0.09746 ];
LAMBDA                    (idx, [1:  14]) = [  8.41210E-01 0.05014  1.25132E-02 0.00159  3.01064E-02 0.00040  1.11975E-01 0.00200  3.32051E-01 0.00121  1.31052E+00 0.00306  9.77149E+00 0.01319 ];

