# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:17:16 2022

@author: schue
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    

#########################
# Prepare Data Basel

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

def PlotBaselLinienChart():
    BaselYearly.plot("Datum", "Lufttemperatur Tagesmittel", legend=None)
    plt.title("Jährliche Durchschnittstemperatur in Basel")
    plt.ylabel("Temperatur in Grad Celsius")

# PlotBaselLinienChart()

def PlotBaselBarYearly():
    BaselYearly.plot.bar("Jahr", "Lufttemperatur Tagesmittel", legend=None, rot=0)
    plt.title("Jährliche Durchschnittstemperatur in Basel")
    plt.xticks(np.arange(0, len(BaselYearly)+1, 20))
    plt.ylabel("Temperatur in Grad Celsius")

# PlotBaselBarYearly()

def PlotBaselBarDekade():
    BaselDekade.plot.bar("Dekade", "Lufttemperatur Tagesmittel", legend=None, rot=0)
    plt.title("Dekaden - Jährliche Durchschnittstemperatur in Basel")
    plt.xticks(np.arange(0, len(BaselDekade)+1, 5))
    plt.ylabel("Temperatur in Grad Celsius")

# PlotBaselBarDekade()

#########################
# Prepare Data Bern

Bern = pd.read_csv("DatenBern.csv", sep = ";")
Bern["Datum"] = pd.to_datetime(Bern["date"], format='%Y%m%d')
Bern["Lufttemperatur Tagesmittel"] = pd.to_numeric(Bern["Lufttemperatur Tagesmittel"], errors='coerce')

BernMonthly = Bern.groupby(pd.Grouper(key='Datum',freq='M')).mean()
BernMonthly["Datum"] = BernMonthly.index
BernYearly = BernMonthly.groupby(pd.Grouper(key='Datum',freq='Y')).mean()
BernYearly["Datum"] = BernYearly.index
BernYearly.index = pd.to_datetime(BernYearly.index)
BernYearly["Jahr"] = pd.DatetimeIndex(BernYearly["Datum"]).year
BernYearly["Dekade"] = round(BernYearly["Jahr"] // 10, 0) * 10
BernDekade = BernYearly.groupby("Dekade").mean()
BernDekade["Dekade"] = BernDekade.index


#########################
# Prepare Data Lugano

Lugano = pd.read_csv("DatenLugano.csv", sep = ";")
Lugano["Datum"] = pd.to_datetime(Lugano["date"], format='%Y%m%d')
Lugano["Lufttemperatur Tagesmittel"] = pd.to_numeric(Lugano["Lufttemperatur Tagesmittel"], errors='coerce')

LuganoMonthly = Lugano.groupby(pd.Grouper(key='Datum',freq='M')).mean()
LuganoMonthly["Datum"] = LuganoMonthly.index
LuganoYearly = LuganoMonthly.groupby(pd.Grouper(key='Datum',freq='Y')).mean()
LuganoYearly["Datum"] = LuganoYearly.index
LuganoYearly.index = pd.to_datetime(LuganoYearly.index)
LuganoYearly["Jahr"] = pd.DatetimeIndex(LuganoYearly["Datum"]).year
LuganoYearly["Dekade"] = round(LuganoYearly["Jahr"] // 10, 0) * 10
LuganoDekade = LuganoYearly.groupby("Dekade").mean()
LuganoDekade["Dekade"] = LuganoDekade.index


#########################
# Linechart of the three

ÜbersichtTemperaturBasel = BaselYearly[["Lufttemperatur Tagesmittel"]]
ÜbersichtTemperaturBasel = ÜbersichtTemperaturBasel.rename(columns={"Lufttemperatur Tagesmittel": "Basel", })
ÜbersichtTemperaturBern = BernYearly[["Lufttemperatur Tagesmittel"]]
ÜbersichtTemperaturBern = ÜbersichtTemperaturBern.rename(columns={"Lufttemperatur Tagesmittel": "Bern", })
ÜbersichtTemperaturLugano = LuganoYearly[["Lufttemperatur Tagesmittel"]]
ÜbersichtTemperaturLugano = ÜbersichtTemperaturLugano.rename(columns={"Lufttemperatur Tagesmittel": "Lugano", })

def Linechart():
    Übersicht = ÜbersichtTemperaturBasel.join(ÜbersichtTemperaturBern)
    Übersicht = Übersicht.join(ÜbersichtTemperaturLugano)
    Übersicht.plot()
    plt.ylabel("Temperatur in Grad Celsius")
    plt.ylim(ymin=0)
    
# Linechart()


#########################
# Barchart differences Dekaden


BaselVeränderung = BaselDekade.loc[2010, "Lufttemperatur Tagesmittel"] - BaselDekade.loc[1940, "Lufttemperatur Tagesmittel"]
BernVeränderung = BernDekade.loc[2010, "Lufttemperatur Tagesmittel"] - BernDekade.loc[1940, "Lufttemperatur Tagesmittel"]
LuganoVeränderung = LuganoDekade.loc[2010, "Lufttemperatur Tagesmittel"] - LuganoDekade.loc[1940, "Lufttemperatur Tagesmittel"]

def BarchartDekaden():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    Ort = ["Basel", "Bern", "Lugano"]
    Wert = [BaselVeränderung, BernVeränderung, LuganoVeränderung]
    ax.bar(Ort, Wert)
    plt.title("Zunahme der durchschnittlichen Temperatur der Dekaden 1940 und 2010")
    ax.set_ylabel("Differenz in Grad Celsius")
    plt.show()
    
BarchartDekaden()