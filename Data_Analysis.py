#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


movies=pd.read_csv("Movie-Ratings.csv")


# In[3]:


len(movies)


# In[4]:


movies.head()


# In[5]:


movies.columns


# In[6]:


movies.columns=['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']


# In[7]:


movies.head()


# In[8]:


movies.info()


# In[9]:


movies.describe()


# In[10]:


movies.Film=movies.Film.astype('category')


# In[11]:


movies.Year=movies.Year.astype('category')


# In[12]:


movies.Genre=movies.Genre.astype('category')


# In[13]:


movies.info()


# In[14]:


movies.Genre.cat.categories


# In[15]:


movies.describe()


# ----

# In[16]:


from matplotlib import pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[17]:


sns.set_style("darkgrid")


# In[18]:


#Jointplots


# In[19]:


j=sns.jointplot(data=movies,x='CriticRating', y='AudienceRating')


# In[20]:


j=sns.jointplot(data=movies,x='CriticRating', y='AudienceRating', kind='hex')


# In[21]:


#histogram
n1=plt.hist(movies.AudienceRating, bins=15)


# In[22]:


n1=plt.hist(movies.CriticRating, bins=15)


# In[23]:


#Stacked Histogram

list1=list()
mylabels=list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)

h=plt.hist(list1,bins=30,stacked=True,rwidth=1, label=mylabels)
plt.legend()
plt.show()


# In[24]:


#KDE Plot

k1=sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False,cmap='Reds')
k1b=sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='Reds')


# In[25]:


#subplots
f,axes=plt.subplots(1,2,figsize=(12,6),sharex=True,sharey=True)
k1=sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0])
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[1])
k1.set(xlim=(-20,160))


# In[26]:


#boxplot
w=sns.boxplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating')


# In[27]:


#violinplot
w=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating')


# In[28]:


#histograms subplots
sns.set_style("darkgrid")
g=sns.FacetGrid(movies, row='Genre',col='Year',hue='Genre')
g=g.map(plt.hist,'BudgetMillions')


# In[29]:


#Scatter subplots 
g=sns.FacetGrid(movies, row='Genre',col='Year',hue='Genre')
kws=dict(s=50,linewidth=0.5,edgecolor='black')
g=g.map(plt.scatter,'CriticRating','AudienceRating',**kws)


# In[30]:


#Scatter subplots 
g=sns.FacetGrid(movies, row='Genre',col='Year',hue='Genre')
kws=dict(s=50,linewidth=0.5,edgecolor='black')
g=g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
for ax in g.axes.flat:
    ax.plot((0,100),(0,100),c="gray",ls="--")
g.add_legend()
plt.show()


# In[31]:


#dashboard
f,axes=plt.subplots(2,2,figsize=(15,15))
k1=sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0,0])
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,1])
w=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating',ax=axes[1,0])
k4=sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False,cmap='Reds',ax=axes[1,1])
k4b=sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='Reds',ax=axes[1,1])
                 
k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
plt.show()


# In[32]:


#thematic dashboard
sns.set_style("dark",{"axes.facecolor":"black"})

f,axes=plt.subplots(2,2,figsize=(15,15))

k1=sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,               shade=True, shade_lowest=True,cmap='inferno',               ax=axes[0,0])
k1b=sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,                cmap='cool',ax=axes[0,0])

k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,               shade=True, shade_lowest=True,cmap='inferno',               ax=axes[0,1])
k2b=sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,                cmap='cool',ax=axes[0,1])

w=sns.violinplot(data=movies,                 x='Year',y='BudgetMillions',ax=axes[1,0],                paletter='YlOrRd')

k4=sns.kdeplot(movies.CriticRating,movies.AudienceRating,               shade=True,shade_lowest=False,cmap='Blues_r',               ax=axes[1,1])
k4b=sns.kdeplot(movies.CriticRating,movies.AudienceRating,                cmap='gist_gray_r',ax=axes[1,1])
                 
k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
plt.show()

