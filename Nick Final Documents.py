#!/usr/bin/env python
# coding: utf-8

# In[80]:


# BEFORE STARTING GO TO .csv file and
# delete all column text e.g timestamp except for Unit and V or will be confusing for datafile to be read
# should only be 2 columns, and Unit , V at top, then all else numbers.

import matplotlib.pyplot as plt
import numpy as np
import tables as tb
import pandas as pd
from scipy.signal import find_peaks
df = pd.read_csv(r"C:\Users\Marcus\Downloads\PT40A_M000_10mVperpC_2Hz_10N.csv")
                #replace this with your data file location in your comp
print(df)



# In[81]:


plt.plot(df.Unit, df.V)
plt.ylabel("V")
plt.xlabel("Unit")
plt.show()
#prints data


# In[82]:


x = df['V']

print(x)

#extract V column


# In[83]:


plt.plot(x)
plt.ylabel("V")
plt.xlabel("Row number")
plt.show()

# plots data file, V only


# In[84]:


flipx = -x
plt.plot(-x)
plt.ylabel("Flipped V")
plt.xlabel("Row number")
plt.show()
# I flip X because it only lets me find peaks not valleys, main thing is we find the row no. of each peak


# In[85]:


peaks, _ = find_peaks(flipx, distance=10e4, height = -0.9, prominence = 0 )
np.diff(peaks)
peakcount = len(peaks)
print ("number of peaks found was", peakcount)
print(peaks)
#identifies peaks and counts them, increase height to increase limit note flipped,so increasing will pick lower peaks,
#if you want to only pick big peaks from the base i.e remove those small ones at start and end, increase prominence


# In[86]:


plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.ylabel("V")
plt.xlabel("Row number")
plt.show()
#shows the peaks highlighted in the original, unflipped version, view this to make sure all orange dots are in areas you like


# In[87]:


rowpick = peaks
finaldata = df.loc[rowpick]
#picks rows and forms new table based on selected data
print(finaldata)


# In[88]:


plt.plot(df.Unit, df.V)
plt.plot(finaldata.Unit, finaldata.V, color= 'red')
plt.ylabel("V")
plt.xlabel("Unit")
plt.show()
#plots the baseline as a new graph for visual check


# In[89]:


finaldata.to_csv(r'C:\Users\Marcus\Downloads\baseline.csv', index = False)

#exports data as csv change the path to where you want to download


# In[ ]:




