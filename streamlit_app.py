#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np
import plotly as plt
import seaborn as sns
import streamlit as st



os.chdir(r'C:\Users\idehi\Desktop\Data Science map')

alcohol = pd.read_csv (r'alcoholSubstanceAbuse.csv')
suicide = pd.read_csv (r'crudeSuicideRates.csv')
traffic = pd.read_csv (r'roadTrafficDeaths.csv')


print (alcohol.head())
print (suicide.head())
print (traffic.head())

Continents=pd.read_csv("Continents.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)


# In[ ]:





# In[2]:


Continents=Continents.rename(columns={"name":"Location"})
Continents=Continents[["Location","Continent"]]

ac_con = alcohol.merge(Continents,on="Location")
print(ac_con)


# In[3]:


ac_su = alcohol.merge(suicide, on=["Location", 'Period', 'Dim1'], suffixes=('_ac', '_su'), how='inner')
ac_su = ac_su.rename(columns={'First Tooltip_ac': 'Alcohol abuse', 'First Tooltip_su': 'Suicide rate'
                             , 'Dim1': 'Sex'})
ac_su=ac_su.sort_values(["Location","Period"])
ac_su.head(10000)


# In[15]:

sex_list = ['Both sexes', 'Male', 'Female']
agree_1 = st.checkbox("Show scatterplot.")
if agree_1:
    st.selectbox('Which category do you want to see?', sex_list)
    sns.scatterplot(x=ac_su['Alcohol abuse'], y=ac_su['Suicide rate'], hue=ac_su['Sex'])
    st.pyplot()


# In[ ]:





# In[9]:





# In[12]:


alcohol_1 = alcohol[alcohol.Dim1 == 'Both sexes']
ac_su = ac_su.rename(columns={'First Tooltip': 'Alcohol abuse', 'Dim1': 'Sex'})


# In[11]:





# In[ ]:





# In[13]:


agree_2 = st.checkbox("Show boxplot.")
if agree_2:
    sns.boxplot(x=alcohol['Alcohol Abuse'], y=alcohol['Sex'])
st.pyplot()


# In[ ]:





# In[ ]:
