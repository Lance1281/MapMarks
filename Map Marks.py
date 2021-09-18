#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd


# my_map = folium.Map()
# my_map

# In[2]:


cities = pd.read_csv('cities.csv')


# In[3]:


def select_marker_color(row):
        if row['status'] == 'active':
            return 'blue'
        elif row['status'] == 'dismissed':
            return 'red'
        


# In[4]:


cities['color'] = cities.apply(select_marker_color, axis=1)


# In[5]:


my_map = folium.Map(
location=[15.0794, 120.6200],
  
)

for _, city in cities.iterrows():
    folium.Marker(
        location=[city['latitude'],city['longitude']],
        popup=city['name'],
        tooltip=city['name'],
        icon=folium.Icon(color=city['color'], prefix='fa', icon='circle')
    ).add_to(my_map)
    
my_map


# In[25]:





# In[ ]:




