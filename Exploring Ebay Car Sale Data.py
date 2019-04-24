#!/usr/bin/env python
# coding: utf-8

# # German Ebay Car Sales Data Exploration
# 
# In this project, I am going to analyze car sales on Ebay in the German website.
# 
# The data dictionary provided with data is as follows:
# 
# -  dateCrawled - When this ad was first crawled. All field-values are taken from this date.
# -  name - Name of the car.
# 
# -  seller - Whether the seller is private or a dealer.
# -  offerType - The type of listing
# - price - The price on the ad to sell the car.
# - abtest - Whether the listing is included in an A/B test.
# - vehicleType - The vehicle Type.
# - yearOfRegistration - The year in which which year the car was first registered.
# - gearbox - The transmission type.
# - powerPS - The power of the car in PS.
# - model - The car model name.
# - kilometer - How many kilometers the car has driven.
# - monthOfRegistration - The month in which which year the car was first -registered.
# - fuelType - What type of fuel the car uses.
# - brand - The brand of the car.
# - notRepairedDamage - If the car has a damage which is not yet repaired.
# - dateCreated - The date on which the eBay listing was created.
# - nrOfPictures - The number of pictures in the ad.
# - postalCode - The postal code for the location of the vehicle.
# - lastSeenOnline - When the crawler saw this ad last online.
# 
# The aim of this project is to clean the data and analyze the included used car listings.

# In[1]:


import numpy as np
import pandas as pd

autos = pd.read_csv("autos.csv", encoding = "Latin-1")


# In[2]:


autos


# In[3]:


autos.info()
autos.head()


# In[4]:


autos.columns


# 
# We'll make a few changes here:
# 
# - Columnn names from camelcase to snakecase.
# - Change a few wordings to more accurately describe the columns.

# In[5]:


autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'nr_of_pictures', 'postal_code',
       'last_seen']


# In[6]:


autos.head()


# # Exploring Data for Cleaning
# 

# In[7]:


autos.describe(include='all')


# Our initial observations:
# 
# There are a number of text columns where all (or nearly all) of the values are the same:
# - seller
# - offer_type
# 
# The num_photos column looks odd, we'll need to investigate this further.

# We make the odometer and price columns numeric by
# 
# - Removing any-non numeric characters
# - Converting the column to int/float

# In[8]:


autos["price"] = autos["price"].str.replace("$","").str.replace(",","").astype(int)


# In[9]:


autos["odometer"] = autos["odometer"].str.replace(",","").str.replace("km","").astype(int)


# In[10]:


autos.rename({"odometer": "odometer_km"}, axis=1, inplace=True)


# We are going to now analyze the odometer and price columns to determine any anomalies

# In[11]:


print(min(autos["price"]))
print(max(autos["price"]))
print(autos["price"].unique().shape)
print(autos["price"].describe())


# In[12]:


autos["price"].value_counts().sort_index(ascending=False).head(20)


# Given that eBay is an auction site, there could legitimately be items where the opening bid is \$1. We will keep the \$1 items, but remove anything above \$350,000, since it seems that prices increase steadily to that number and then jump up to less realistic numbers.

# In[13]:


autos = autos[autos["price"].between(1,350000)]


# In[14]:


(autos["date_crawled"]
 .str[:10]
.value_counts(normalize=True, dropna=False)
.sort_values())


# In[15]:


(autos["ad_created"]
 .str[:10]
.value_counts(normalize=True, dropna=False)
.sort_index())


# In[16]:


(autos["last_seen"]
 .str[:10]
.value_counts(normalize=True, dropna=False)
.sort_index())


# In[17]:


autos["registration_year"].describe()


# The year that the car was first registered will likely indicate the age of the car. Looking at this column, we note some odd values. The minimum value is 1000, long before cars were invented and the maximum is 9999, many years into the future.
# 
# We will delete anything outside of 1900 to 2016

# In[18]:


autos = autos[autos["registration_year"].between(1900,2016)]


# In[21]:


autos["registration_year"].value_counts(normalize=True).head(10)


# # Analyzing Brands

# We identify car brands and their percentages

# In[24]:


autos["brand"].value_counts(normalize=True)


# In[32]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
common_brands


# In[33]:


brand_mean_prices = {}
    
for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)
    
brand_mean_prices


# - Audi, BMW and Mercedes Benz are more expensive
# - Ford and Opel are less expensive
# - Volkswagen is in between - this may explain its popularity, it may be a 'best of 'both worlds' option.

# In[34]:


brand_mean_mileage = {}

for brand in common_brands:
    brand_only = autos[autos["brand"]==brand]
    mean_mileage = brand_only['odometer_km'].mean()
    brand_mean_mileage[brand] = int(mean_mileage)


# In[39]:


bmp_price = pd.Series(brand_mean_prices)
bmp_mileage = pd.Series(brand_mean_mileage).so

df = pd.DataFrame(bmp_mileage, columns=['mean_mileage'])
df

