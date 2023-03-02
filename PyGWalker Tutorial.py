#!/usr/bin/env python
# coding: utf-8

# ![Pygwalker.png](attachment:Pygwalker.png)

# ## <<<    PyGWalker: A Python Library for Exploratory Data Analysis with Visualization   >>>

# > PyGWalker can simplify your Jupyter Notebook data analysis and data visualization workflow, by turning your pandas dataframe into a Tableau-style User Interface for visual exploration.
# 
# > PyGWalker (pronounced like "Pig Walker", just for fun) is named as an abbreviation of "Python binding of Graphic Walker". It integrates Jupyter Notebook (or other jupyter-based notebooks) with Graphic Walker, a different type of open-source alternative to Tableau. It allows data scientists to analyze data and visualize patterns with simple drag-and-drop operations.

# # <span style='color:Blue'>  Install PyGWalker

# In[ ]:


pip install pygwalker


# # <span style='color:Blue'> Importing libraries

# In[2]:


import pandas as pd
import pygwalker as pyg


# # <span style='color:Blue'> Checking directories

# In[3]:


dir(pyg)


# # <span style='color:Blue'> Loading data

# In[4]:


df = pd.read_csv(r'Superstore_USA.csv')
df.head()


# # <span style='color:Blue'> Now take DataFrame into PyGWalker 

# In[5]:


pyg.walk(df, vegaTheme = 'vega') #You can view the dataframe in a table and configure the analytic types and semantic types.
# Or you can store dataframe into another variable as per below
# new_df = pyg.walk(df, vegaTheme = 'vega')


# # <span style='color:Blue'> Now visualize as per requirements

# In[15]:


pyg.walk(df, vegaTheme = 'vega')


# In[7]:


pyg.walk(df, vegaTheme = 'vega')


# In[8]:


pyg.walk(df, vegaTheme = 'vega')


# # <span style='color:Blue'> Upload another datasets

# In[19]:


df_df = pd.read_csv(r'vix-daily_csv.csv')
pyg.walk(df_df, vegaTheme = 'vega')


# # <span style='color:Blue'> Upload another datasets

# In[11]:


import xlrd
df2 = pd.read_excel(r'Data_Train.xlsx')
pyg.walk(df2, vegaTheme = 'vega')


# In[12]:


df2 = pd.read_excel(r'Data_Train.xlsx')
pyg.walk(df2, vegaTheme = 'vega')


# # <span style='color:Blue'> Upload another datasets

# In[13]:


df3 = pd.read_csv(r'AgentLogingReport.csv')
pyg.walk(df3, vegaTheme = 'vega')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




