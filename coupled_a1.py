import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd
import openpyxl
from scipy import integrate
#import MyTicToc as mt

#ET - evapotranspiration
#Lt - uotflow
ba = 28355      #base area
ta = 9100       #top area
sw = 38         #slope width
h = 12          #slope height
hc = 1.5        #clay layer height
ww = 281083000  #total wet weight
ecw = 0.4       #clay layer porosity
ewb = 0.5       #waste body porosity
kcw = 0.000001  #clay layer filtration coefficient
kwb = 0.00001   #waste body filtration coefficient
Jrt = pd.read_excel (r'meteo.xlsx', sheet_name='1', usecols='C') #precipitation
pev = pd.read_excel (r'meteo.xlsx', sheet_name='1', usecols='D') #evaporation
Qdr = pd.read_excel (r'leak.xlsx', sheet_name='1', usecols='B') #leakage
