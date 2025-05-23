#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('mymoviedb.csv',lineterminator='\n')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


#change dtype of release date from object to date,eliminate white space from Action, Adventure etc.
df['Genre'].head()


# In[6]:


df['Genre']


# In[7]:


df.duplicated()


# In[8]:


df.duplicated().sum()


# In[9]:


df.describe()


# In[10]:


df['Release_Date'] = pd.to_datetime(df['Release_Date'])

print(df['Release_Date'].dtypes)


# In[11]:


df['Release_Date'] = df['Release_Date'].dt.year

df['Release_Date'].dtypes 


# In[12]:


df.head()


# In[13]:


#Dropping the columns 
colms = ['Overview', 'Original_Language', 'Poster_Url']


# In[14]:


df.drop(colms, axis=1, inplace=True)


# In[15]:


df.columns


# In[16]:


df.head()


# categorizing Vote_Average column 
# 
# we would cut the column values and make 4 categories popular,average,below_average,not_popular to describe it more using categorize_col() function provided above

# In[17]:


def categorize_col(df, colms, labels):
    
    edges = [df[colms].describe()['min'],
             df[colms].describe()['25%'],
             df[colms].describe()['50%'],
             df[colms].describe()['75%'],
             df[colms].describe()['max']]
            
    df[colms] = pd.cut(df[colms], edges, labels = labels,duplicates='drop')
    return df


# In[18]:


labels = ['not_popular', 'below_average', 'average', 'popular']

categorize_col(df, 'Vote_Average', labels)

df['Vote_Average'].unique()


# In[19]:


df.head()


# In[20]:


df['Vote_Average'].value_counts()


# In[21]:


df.dropna(inplace=True)

df.isna().sum()


# In[22]:


df.head()


# Split genres into list and explode our df per row for each movie

# In[23]:


df['Genre'] = df['Genre'].str.split(', ')

df = df.explode('Genre').reset_index(drop = True)

df.head()


# In[24]:


#casting column into category

df['Genre'] = df['Genre'].astype('category')

df['Genre'].dtypes


# In[25]:


df.info()


# In[26]:


df.nunique()


# In[27]:


df.head()


# Data Visualization

# In[28]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_style('whitegrid')


# In[29]:


#what's the most frequent genre of movies released on netflix?

df['Genre'].describe()


# In[30]:


sns.catplot(y='Genre',data=df,kind='count',
           order=df['Genre'].value_counts().index,
           color = 'Red')

plt.title('Genre column distribution')

plt.show()


# In[31]:


#which has highest votes in the vote_average column?

df.head()


# In[32]:


sns.catplot(y='Vote_Average' ,data=df, kind='count',
           order=df['Vote_Average'].value_counts().index,
           color='Pink')
plt.title('Vote Distribution')
plt.show()


# In[35]:


#what movie got highest popularity? what's its genre?
df.head(2)


# In[40]:


df[df['Popularity'] == df['Popularity'].max()]


# In[41]:


#what movie got lowest popularity? what's its genre?

df[df['Popularity'] == df['Popularity'].min()]


# In[42]:


#which year has most filmmed movies?

df['Release_Date'].hist()

plt.title('Release data column distribution')

plt.show()


# In[ ]:


#summary

