# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:17:16 2022

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
Basel["Datum"] = pd.to_datetime(Basel["date"], format='%Y%m%d')
Basel["Lufttemperatur Tagesmittel"] = pd.to_numeric(Basel["Lufttemperatur Tagesmittel"], errors='coerce')

BaselMonthly = Basel.groupby(pd.Grouper(key='Datum',freq='M')).mean()
BaselMonthly["Datum"] = BaselMonthly.index
BaselYearly = BaselMonthly.groupby(pd.Grouper(key='Datum',freq='Y')).mean()
BaselYearly["Datum"] = BaselYearly.index
BaselYearly.index = pd.to_datetime(BaselYearly.index)
BaselYearly["Jahr"] = pd.DatetimeIndex(BaselYearly["Datum"]).year
BaselYearly["Dekade"] = round(BaselYearly["Jahr"] // 10, 0) * 10
BaselDekade = BaselYearly.groupby("Dekade").mean()
BaselDekade["Dekade"] = BaselDekade.index


# BaselYearly.plot("Datum", "Lufttemperatur Tagesmittel", legend=None)
# plt.title("Jährliche Durchschnittstemperatur in Basel")
# plt.ylabel("Temperatur in Grad Celsius")


# BaselYearly.plot.bar("Jahr", "Lufttemperatur Tagesmittel", legend=None, rot=0)
# plt.title("Jährliche Durchschnittstemperatur in Basel")
# plt.xticks(np.arange(0, len(BaselYearly)+1, 20))
# plt.ylabel("Temperatur in Grad Celsius")

BaselDekade.plot.bar("Dekade", "Lufttemperatur Tagesmittel", legend=None, rot=0)
plt.title("Dekaden - Jährliche Durchschnittstemperatur in Basel")
plt.xticks(np.arange(0, len(BaselDekade)+1, 5))
plt.ylabel("Temperatur in Grad Celsius")

#########################

Jfj = pd.read_csv("DatenJungfraujoch.csv", sep = ";")
Jfj["Datum"] = pd.to_datetime(Jfj["date"], format='%Y%m%d')
Jfj["Lufttemperatur Tagesmittel"] = pd.to_numeric(Jfj["Lufttemperatur Tagesmittel"], errors='coerce')

JfjMonthly = Jfj.groupby(pd.Grouper(key='Datum',freq='M')).mean()
JfjMonthly["Datum"] = JfjMonthly.index
JfjYearly = JfjMonthly.groupby(pd.Grouper(key='Datum',freq='Y')).mean()
JfjYearly["Datum"] = JfjYearly.index
JfjYearly.index = pd.to_datetime(JfjYearly.index)
JfjYearly["Jahr"] = pd.DatetimeIndex(JfjYearly["Datum"]).year
JfjYearly["Dekade"] = round(JfjYearly["Jahr"] // 10, 0) * 10
JfjDekade = JfjYearly.groupby("Dekade").mean()
JfjDekade["Dekade"] = JfjDekade.index

# JfjYearly.plot("Datum", "Lufttemperatur Tagesmittel")
# plt.legend(["Jährliche Durchschnittstemperatur auf dem Jungfraujoch"], prop={'size': 10})

# JfjYearly.plot.bar("Jahr", "Lufttemperatur Tagesmittel", rot=0)
# plt.legend(["Jährliche Durchschnittstemperatur auf dem Jungfraujoch"], prop={'size': 10})
# plt.xticks(np.arange(0, len(JfjYearly)+1, 20))

# JfjDekade.plot.bar("Dekade", "Lufttemperatur Tagesmittel", rot=0)
# plt.legend(["10 - Jährliche Durchschnittstemperatur auf dem Jungfraujoch"], prop={'size': 10})
# plt.xticks(np.arange(0, len(JfjDekade)+1, 5))


#########################

BaselVeränderung = BaselDekade.loc[2010, "Lufttemperatur Tagesmittel"] - BaselDekade.loc[1940, "Lufttemperatur Tagesmittel"]
JfjVeränderung = JfjDekade.loc[2010, "Lufttemperatur Tagesmittel"] - JfjDekade.loc[1940, "Lufttemperatur Tagesmittel"]

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# Ort = ["Basel", "Jungfraujoch"]
# Wert = [BaselVeränderung, JfjVeränderung]
# ax.bar(Ort, Wert)
# plt.title("Zunahme der durchschnittlichen Temperatur der Dekaden 1940 und 2010")
# ax.set_ylabel("Differenz in Grad Celsius")
# plt.show()