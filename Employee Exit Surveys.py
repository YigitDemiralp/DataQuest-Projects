#!/usr/bin/env python
# coding: utf-8

# # Employee Exit Surveys

# In this project, we'll play the role of data analyst and pretend our stakeholders want to know the following:
# 
# - Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?
# - Are younger employees resigning due to some kind of dissatisfaction? What about older employees?

# In[2]:


import numpy as np
import pandas as pd
from IPython.display import display

dete_survey = pd.read_csv('dete_survey.csv')
tafe_survey = pd.read_csv('tafe_survey.csv')

pd.options.display.max_columns = None



# In[3]:


dete_survey.info()
dete_survey.head()


# In[3]:


tafe_survey.info()
tafe_survey.head()


# We can make the following observations based on the work above:
# 
# - The dete_survey dataframe contains 'Not Stated' values that indicate values are missing, but they aren't represented as  NaN.
# - Both the dete_survey and tafe_survey contain many columns that we don't need to complete our analysis.
# - Each dataframe contains many of the same columns, but the column names are different.
# - There are multiple columns/answers that indicate an employee resigned because they were dissatisfied.

# # Read the 'Not Stated' as NaN & Drop Unnecessary Columns

# In[4]:


# Read in the data again, but this time read `Not Stated` values as `NaN`
dete_survey = pd.read_csv('dete_survey.csv', na_values='Not Stated')

#Drop Unnecessary Columns
dete_survey_updated = dete_survey.drop(dete_survey.columns[28:49], axis=1)

tafe_survey_updated = tafe_survey.drop(tafe_survey.columns[17:66], axis = 1)


# # Standardize The Column Names

# Because we eventually want to combine them, we'll have to standardize the column names
# 

# In[5]:


dete_survey_updated.columns = dete_survey_updated.columns.str.replace(' ', '_').str.lower().str.strip()

tafe_survey_updated = tafe_survey.rename(columns = {'Record ID': 'id', 
'CESSATION YEAR': 'cease_date',
'Reason for ceasing employment': 'separationtype',
'Gender. What is your Gender?': 'gender',
'CurrentAge. Current Age': 'age',
'Employment Type. Employment Type': 'employment_status',
'Classification. Classification': 'position',
'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service'})

#Checking if the column rename worked
print(dete_survey_updated.columns)
print('\n')
print(tafe_survey_updated.columns)


# In[6]:


print(dete_survey_updated['separationtype'].value_counts())
print(tafe_survey_updated['separationtype'].value_counts())



# In[7]:


# Update all separation types containing the word "resignation" to 'Resignation'
dete_survey_updated['separationtype'] = dete_survey_updated['separationtype'].str.split('-').str[0]

dete_resignations = dete_survey_updated[dete_survey_updated['separationtype'] == 'Resignation'].copy()
tafe_resignations = tafe_survey_updated[tafe_survey_updated['separationtype'] == 'Resignation'].copy()





# In[8]:


get_ipython().magic('matplotlib inline')
dete_resignations['cease_date'].value_counts()
dete_resignations['cease_date'] = dete_resignations['cease_date'].str.extract(r'([1-2][0-9][0-9][0-9].0)')

print(dete_resignations['cease_date'].value_counts().sort_index(ascending = False))
print(dete_resignations['dete_start_date'].value_counts().sort_index(ascending = False))
print('\n')
print(tafe_resignations['cease_date'].value_counts().sort_index(ascending = False))

dete_resignations.boxplot(column=['dete_start_date'])



# In[9]:


dete_resignations['institute_service'] = dete_resignations['cease_date'] - dete_resignations['dete_start_date']


# In[ ]:




