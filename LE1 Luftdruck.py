# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 07:36:08 2022

@author: schue
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates     

Basel = pd.read_csv("DatenBasel.csv", sep = ";")
Basel["Niederschlag"] = pd.to_numeric(Basel["Niederschlag"], errors='coerce')
Basel["Luftdruck"] = pd.to_numeric(Basel["Luftdruck"], errors='coerce')
Basel["Gesamtbewölkung"] = pd.to_numeric(Basel["Gesamtbewölkung"], errors='coerce')


# Basel.hist(column = "Luftdruck", bins = 30)
# plt.title("Verteilung des Luftdruck in Basel seit 1864")

Basel["Luftdruck"].plot.density()
plt.title("Verteilung des Luftdruck in Basel seit 1864")
