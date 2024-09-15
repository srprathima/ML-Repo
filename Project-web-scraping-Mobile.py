#!/usr/bin/env python
# coding: utf-8

# In[102]:


# Installing the necessary packages.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import warnings
warnings.filterwarnings("ignore")
import csv

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[103]:


products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
ram = []                #List to store Ram size                
display = []                  #List to store display
camera= []                  #List to store camera info
battery = []               #List to store battery
specifications=[]          #List to store specifications
rams=[]
dis=[]
cam=[]
batt=[]


# In[104]:


for i in range(1,25):
    url='https://www.flipkart.com/search?sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page={}'.format(i)
    page=requests.get(url) # checking if url is loded successfully
    pc=page.text
    soup=BeautifulSoup(pc) #Loading full page into BeautifulSoup 
    for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=data.find('div', attrs={'class':'_3LWZlK'})
        specification = data.find('div', attrs={'class':'fMghEO'})
        if names is None:
            products.append(np.NaN)
        else:
            products.append(names.text)
            
        if price is None:
            prices.append(np.NaN)
        else:
            prices.append(price.text)
            
        if rating is None:
            ratings.append(np.NaN)
        else:
            ratings.append(rating.text)
            
        if specification is None:
            specifications.append(np.NaN)
        else:
            specifications.append(specification.text)
            for each in specification:
                col=each.find_all('li', attrs={'class':'rgWa7D'})
                rams =col[0].text
                dis =col[1].text
                cam = col[2].text
                batt = col[3].text
                ram.append(rams)
                display.append(dis)
                camera.append(cam) 
                battery.append(batt) 

    


# In[105]:


mo_df=pd.DataFrame({'Product Name':products,'Price':prices,'Ratings':ratings,'Camera':camera,"Display":display,'RAM':ram,'Battery':battery})


# In[106]:


mo_df


# In[107]:


import re
RAM_=[]
ROM_=[]
for i in range(0,576):
    AM_=re.findall(r'\d+\s*[A-z]+\s*RAM',mo_df['RAM'][i])
    if AM_ is None:
        RAM_.append(np.NaN)
    else:
        RAM_.append(AM_)    
    OM_=re.findall(r'\d+\s*[A-z]+\s*ROM',mo_df['RAM'][i])
    if OM_ is None:
        ROM_.append(np.NaN)
    else:
        ROM_.append(OM_)
#print(ROM_)


# In[690]:


mo_df2=pd.DataFrame({'RAM_':RAM_,'ROM_':ROM_})


# In[109]:


mo_df['RAM_']=mo_df2['RAM_']


# In[110]:


mo_df['ROM']=mo_df2['ROM_']


# In[111]:


mo_df.drop(['RAM'], axis=1, inplace=True)


# In[112]:


mo_df['Price'].isnull().any()


# In[113]:


mo_df.head()


# In[114]:


mo_df.isna().sum()


# In[117]:


mo_df['Ratings']=mo_df['Ratings'].fillna(4)


# In[118]:



mo_df['Price']=mo_df['Price'].fillna('₹29,798')


# In[715]:


mo_df.to_csv('Mobile_webs.csv')


# In[723]:


Mob_df = pd.read_csv('Mobile_webs.csv')
Mob_df.drop(['Unnamed: 0'], axis=1, inplace=True)
Mob_df.head()


# In[725]:


Mob_df.info()


# In[756]:


# Removing '₹' from Price
Mob_df['Price']=Mob_df['Price'].apply(lambda x:x[1:])
Mob_df['Price'].head()


# In[757]:


# Removing ',' from Price
Mob_df['Price']=Mob_df['Price'].apply(lambda x: x.replace(',',""))
Mob_df['Price'].head()


# 

# In[736]:


for x in range(0,576):
    if Mob_df['RAM_'][x]=='[]':
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace('[]','4'))


# In[737]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['4 GB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['4 GB RAM']",'4'))


# In[738]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['8 GB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['8 GB RAM']",'8'))


# In[739]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['6 GB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['6 GB RAM']",'6'))
   


# In[740]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['3 GB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['3 GB RAM']",'3'))


# In[741]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['12 GB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['12 GB RAM']",'8'))


# In[742]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['153 MB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['153 MB RAM']",'2'))


# In[743]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['2 GB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['2 GB RAM']",'2'))


# In[744]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['4 MB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['4 MB RAM']",'1'))
    


# In[745]:


for x in range(0,576):
    if Mob_df['RAM_'][x]== "['8 MB RAM']":
        Mob_df['RAM_']=Mob_df['RAM_'].apply(lambda x: x.replace("['8 MB RAM']",'1'))


# In[746]:


for x in range(0,576):
    if Mob_df['ROM'][x]== "['64 GB ROM']":
        Mob_df['ROM']=Mob_df['ROM'].apply(lambda x: x.replace("['64 GB ROM']",'64'))


# In[730]:


for x in range(0,576):
    if Mob_df['ROM'][x]== "['128 GB ROM']":
        Mob_df['ROM']=Mob_df['ROM'].apply(lambda x: x.replace("['128 GB ROM']",'128'))


# In[731]:


for x in range(0,576):
    if Mob_df['ROM'][x]== "['32 GB ROM']":
        Mob_df['ROM']=Mob_df['ROM'].apply(lambda x: x.replace("['32 GB ROM']",'32'))


# In[732]:


for x in range(0,576):
    if Mob_df['ROM'][x]== "['256 GB ROM']":
        Mob_df['ROM']=Mob_df['ROM'].apply(lambda x: x.replace("['256 GB ROM']",'256'))


# In[733]:


for x in range(0,576):
    if Mob_df['ROM'][x]== "['153 GB ROM']":
        Mob_df['ROM']=Mob_df['ROM'].apply(lambda x: x.replace("['153 GB ROM']",'153'))


# In[748]:


for x in range(0,576):
    if Mob_df['ROM'][x]== "['152 GB ROM']":
        Mob_df['ROM']=Mob_df['ROM'].apply(lambda x: x.replace("['152 GB ROM']",'152'))


# In[749]:


Mob_df 


# In[753]:


Mob_df.drop_duplicates(subset="Product Name",
                     keep=False, inplace=True)


# In[754]:


print(Mob_df['Product Name'].duplicated().any())


# In[758]:


Mob_df['Price'] = Mob_df['Price'].astype(int)


# In[759]:


Mob_df['RAM_'] = Mob_df['RAM_'].astype(int)


# In[764]:


Mob_df['ROM'] = Mob_df['ROM'].astype(str)


# In[691]:


Mob_df.isna().sum()


# In[785]:


price_max=Mob_df[(Mob_df['Price']<30000) & (Mob_df['Ratings']>=3.5)]


# In[773]:


price_max.info()


# In[786]:


price_max


# In[787]:


df=price_max


# In[897]:


df.loc[df['Price'].between(0, 5000, 'both'), 'Price_range'] = '5000'
df.loc[df['Price'].between(5001, 10000, 'both'), 'Price_range'] = '10000'
df.loc[df['Price'].between(10001, 15000, 'both'), 'Price_range'] = '15000'
df.loc[df['Price'].between(15001, 20000, 'both'), 'Price_range'] = '20000'
df.loc[df['Price'].between(20001, 25000, 'both'), 'Price_range'] = '25000'
df.loc[df['Price'].between(25001, 30000, 'both'), 'Price_range'] = '30000'


# In[898]:


df['Price_range'] = df['Price_range'].astype(int)


# In[791]:


Display_=[]
for i in range(0,172):
    dis=re.findall(r'\d+.\d+',df['Display'][i])[0]
    Display_.append(dis)


# In[793]:


df2=pd.DataFrame({'Display_cm':Display_})
df['Display']=df2['Display_cm']


# In[794]:


df['Display'] = df['Display'].astype(float)


# In[795]:


df = df.reset_index()


# In[900]:


sort_df = df.sort_values(by = 'Price_range')


# In[797]:


sort_df1 = df.sort_values(by = 'Display')


# In[902]:


sort_df['Company'],sort_df['Model']=sort_df['Product Name'].str.split(" ",1).str


# In[903]:


sort_df.drop(['Product Name'], axis=1, inplace=True)


# In[904]:


sort_df.drop(['Camera'], axis=1, inplace=True)


# In[905]:


sort_df['Company'] = sort_df['Company'].astype(str)


# In[826]:


for x in range(0,172):
    if sort_df['ROM'][x]== "['0 GB ROM']":
        sort_df['ROM']=df['ROM'].apply(lambda x: x.replace("['0 GB ROM']",'0'))


# In[827]:


for x in range(0,172):
    if sort_df['ROM'][x]== "['153 MB ROM']":
        sort_df['ROM']=df['ROM'].apply(lambda x: x.replace("['153 MB ROM']",'0'))


# In[906]:


sort_df = sort_df[['Company', 'Model', 'Price','RAM_','Ratings','Price_range','Display','ROM']]


# In[907]:


gk = sort_df.groupby(['Company','Price_range'])


# In[833]:


sort_df.describe()


# In[834]:


sort_df.info()


# In[908]:


gk.first()


# In[ ]:


###Plotting


# In[ ]:





# In[919]:


#PIE PLOT TO SHOW THE MAJOR COMPANIES THE PROVIDE MOBILE PHONES IN GIVEN PRICE RANGE
sort_df['Company'].value_counts().plot(kind='pie').set(title="Companies")

#can conclude from here that companies the provide more phones for given price range  are SAMSUNG and REALME.


# In[877]:


sns.boxplot(x = sort_df['Company'], y = sort_df['Price_range']).set(title="Price range for each Company")


# In[878]:


# create grouped boxplot 

sns.boxplot(x = sort_df['Company'],y = sort_df['Ratings'], color='skyblue').set(title="Ratings for each company")


# In[872]:


#BAR PLOT- TO SHOW THE EFFECT OF DISPLAY ON PRICE OF THE MOBILE PHONE

sns.barplot(x=sort_df['Display'],y=sort_df['Price_range']).set(title="Effect of Display size on Prices")

plt.xticks(rotation='vertical')

plt.show()

#We can conclude from here that products with higher Display have higher Price to some extent.


# In[871]:


# LMP PLOT TO SHOW THE EFFECT OF RAM SIZE ON PRICE OF MOBILE PHONES
sns.lmplot(x='RAM_', y='Price_range', data=sort_df, line_kws={'color': 'purple'})

plt.title('Effect of RAM on Prices')
plt.show()
#We can conclude from here that products with higher RAM size have higher Prices.


# In[914]:


sns.distplot(sort_df['Price'],kde=True).set(title=" Density of product Prices")
plt.show()


# In[915]:


#BOX PLOT
sns.boxplot(x=sort_df['Price_range']).set(title="Products available in Price range")


# In[916]:


# HEAT PLOT TO SHOW CORRELATION BETWEEN VARIOUS FACTORES.
#represents different shades of a colour to distinguish the values in the graph.
#The higher values are represented in the lighter shades and the lesser values are represented in darker shades.

cor=sort_df.corr()
sns.heatmap(cor,annot=True).set(title="Correlation of all factors")


# In[918]:


#PAIR PLOT- lets you understand the pairwise relationship between different variables in a dataset. 
sns.pairplot(sort_df)
plt.show()


# In[655]:


"""We Concluded these above points,

From the above visualization, my analysis is to provide customers with some valuble information
about best products available with good ratings and with Price constraint of below 30,000.

Here my aim is, by using Web scraping with Python to find out 

1.The best mobile company available in market to provide products in given price range.
2.Company with most satisfied customers with ratings
3.Factors like 'RAM' and 'Display' effecting the prices
4.Price range in which most of the mobile phones available
5.Corelation between all the factors to consider before buying a mobile phone

Above is the information which customers can consider."""


# In[ ]:




