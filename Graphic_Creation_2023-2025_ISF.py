# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 15:01:07 2025
x0

@author: Isaac Bradford, ibradfo@purdue.edu
"""

# import required modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import matplotlib.dates as mdates
import numpy as np
import scipy as sp

df25 = pd.read_csv('2025_Data_set_M.csv') #open a csv within GH folder for data process.
df24 = pd.read_csv('2024_Data_set_M.csv') #open a csv within GH folder for data process.
df23 = pd.read_csv('2023_Data_set_M.csv') #open a csv within GH folder for data process.

#https://www.statology.org/seaborn-font-size/ set font size
sns.set(font_scale = 2.0)
#https://stackoverflow.com/questions/26868304/how-to-get-rid-of-grid-lines-when-plotting-with-seaborn-pandas-with-secondary
sns.set_style("whitegrid", {'axes.grid' : False})

#2023 CHLA
plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance from Dam', y='Chla (ug/L)', data=df23, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Mississinewa: Chl-a Recorded Distance from the Dam over Summer 2023")
adgb.set_ylim(0,90)
plt.savefig('ChlaMISS23.png', bbox_inches = 'tight', pad_inches=1,  dpi = 400)
plt.show()

#2024 CHLA
plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance from Dam', y='Chla (ug/L)', data=df24, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Mississinewa: Chl-a Recorded Distance from the Dam over Summer 2024")
adgb.set_ylim(0,90)
plt.savefig('ChlaMISS24.png', bbox_inches = 'tight', pad_inches=1, dpi = 400)
plt.show()

#2025 CHLA
plt.figure(figsize=(12,6)) #space out recording
adgb = sns.boxplot(x='Distance from Dam', y='Chla (ug/L)', data=df25, showmeans=True, meanprops={'marker':'o','markerfacecolor':'black', 'markeredgecolor':'black', 'markersize':'5'}) 
#https://www.geeksforgeeks.org/python/how-to-set-x-axis-values-in-matplotlib-in-python/
plt.xticks(x='Distance from Dam', rotation=45)
adgb.set_xlabel('Distance from Dam (m)')
adgb.set_ylabel('Chl-a Concentration (ug/L)')
adgb.set_title("Mississinewa: Chl-a Recorded Distance from the Dam over Summer 2025")
adgb.set_ylim(0,90)
plt.savefig('ChlaMISS25.png', bbox_inches = 'tight', pad_inches=1, dpi = 400)
plt.show()


#2025 Secchi Disk Coorilation
df25_sd = df25.dropna(subset='Secchi Depth (m)')

plt.figure(figsize=(12,10)) #space out recording
gz = sns.jointplot(x='Secchi Depth (m)', y='Chla (ug/L)', data=df25_sd, kind='reg')
gz.set_axis_labels(xlabel='Secchi Depth (m)', ylabel='Chla (ug/L)')
plt.suptitle("Secchi Depth vs. Chla, 2025 Mississinewa")
r, p = sp.stats.pearsonr(df25_sd['Secchi Depth (m)'], df25_sd['Chla (ug/L)'])
ax = plt.gca()
ax.text(.05, .8, 'r={:.2f}'.format(r), transform=ax.transAxes)
#plt.savefig(outFileName) # saves the graph into the github folder
plt.savefig('Secchi.png', bbox_inches = 'tight', pad_inches=1, dpi = 400)
plt.show()

"""WORK HERE"""
plt.figure(figsize=(12,6)) #space out recording
# https://stackoverflow.com/questions/68881330/seaborn-plot-with-two-y-axis
ax1 = plt.subplot()
ax2 = ax1.twinx()


adgb = sns.scatterplot(x='Date', y='Chla (ug/L)', data=df25, ax=ax1, label = 'Chla') 
adgb = sns.scatterplot(x='Date', y='TP BDL', data=df25, color='red', ax=ax2, markers='s', label='TP')
adgb = sns.scatterplot(x='Date', y='Nox BDL', data=df25, color= 'orange', ax=ax2, markers='s', label ='NOx')
ax2.tick_params(axis='y', colors='red')
#https://stackoverflow.com/questions/5484922/secondary-axis-with-twinx-how-to-add-to-legend
#legend creation
ax.legend(loc = 0)
ax2.legend(loc=3)
sns.move_legend(ax2, "upper left", bbox_to_anchor=(0.785,0.86))

adgb.set_xlabel('Date')
#https://stackoverflow.com/questions/31632637/label-axes-on-seaborn-barplot
ax2.set(ylabel='TP, NOx (ppm)')
adgb.set_title("Average Chl-a Recorded Distance from the Dam over Summer 2024")

plt.savefig('WIP_TP_NOx_CHLA.png', bbox_inches = 'tight', pad_inches=1, dpi = 400)
plt.show()

"""
gz = sns.jointplot(x='Secchi Depth (m)', y='Chla (ug/L)', data=df25_sd, kind='reg')
gz.set_axis_labels(xlabel='Secchi Depth (m)', ylabel='Chla (ug/L)')
plt.suptitle("Secchi Depth vs. Chla, 2025 Mississinewa")
r, p = sp.stats.pearsonr(df25_sd['Secchi Depth (m)'], df25_sd['Chla (ug/L)'])
ax = plt.gca()
ax.text(.05, .8, 'r={:.2f}'.format(r), transform=ax.transAxes)
#plt.savefig(outFileName) # saves the graph into the github folder
plt.savefig('Secchi.png', dpi = 400)
plt.show()
"""

