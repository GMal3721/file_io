#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[19]:



    df = pd.read_csv("INFO-450-Assingment-6/workout_data.csv")


# In[20]:


import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, r="frequency", theta="direction")
fig.show()


# In[16]:


import plotly.express as px
data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig = px.funnel(data, x='number', y='stage')
fig.show()


# In[17]:


import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill")
fig.show()


# In[ ]:




