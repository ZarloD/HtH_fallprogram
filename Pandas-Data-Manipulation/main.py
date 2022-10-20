#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas

# pandas.set_option('display.max_rows', None, 'display.max_columns', None)

# Step 1: Use the appropriate pandas method to read the titanic data into your python file 
titanic_data = pandas.read_csv('titanic.csv')
titanic_data


# In[10]:


# Step 2(a): Use the pandas method that reads the first 25 lines of the dataset
first_25_passengers = titanic_data.head(25)
first_25_passengers


# In[12]:


# Step 2(b): Use the pandas method thats reads the last 25 lines of the dataset
last_25_passengers = titanic_data.tail(25)
last_25_passengers


# In[15]:


# Step 3: Use the pandas method that only tells us the number of rows and columns in our data
titanic_shape = titanic_data.shape
titanic_shape


# In[16]:


# Step 4: Describe the titanic data
titanic_description = titanic_data.describe()
titanic_description


# In[94]:


# Step 5(a): How many passengers were between the ages of 0 to 16? 
age_above_0 = titanic_data['Age'] >= 0
age_below_16 = titanic_data['Age'] <=16

children = titanic_data[age_above_0 & age_below_16]
# children = titanic_data[(titanic_data['Age'] >= 0) & (titanic_data['Age'] <=16)]
children


# In[147]:


# Step 5(b): How many passengers were between the ages of 17 to 25?
age_above_17 = titanic_data['Age'] >= 17
age_below_25 = titanic_data['Age'] <=25

young_adults = titanic_data[age_above_17 & age_below_25]
young_adults


# In[148]:


# Step 5(c): How many passengers were between the ages of 26 to 40?
age_above_26 = titanic_data['Age'] >= 26
age_below_40 = titanic_data['Age'] <=40

adults = titanic_data[age_above_26 & age_below_40]
adults


# In[149]:


# Step 5(d): How many passengers were between the ages of 41 to 59?
age_above_41 = titanic_data['Age'] >= 41
age_below_59 = titanic_data['Age'] <=59

mature_adults = titanic_data[age_above_41 & age_below_59]
mature_adults


# In[87]:


# Step 5(e): How many passengers were 60 or older?
seniors = titanic_data[titanic_data['Age'] >= 60]
seniors


# In[56]:


# Step 6: How many values are missing from the "age" column
missing_ages = titanic_data.shape[0] - titanic_data['Age'].count()
missing_ages


# In[65]:


# Step 7: List out all the available passengers' ages
age_list = titanic_data['Age'].dropna().unique()
age_list


# In[97]:


# Step 8: Filter the DataFrame to find all passengers who boarded the Titanic at Port Cherbourg
cherbourg_passengers = titanic_data[titanic_data['Embarked'] == 'C']
cherbourg_passengers


# In[92]:


# Step 9(a): Find the average age of all female passengers
avg_fem_age = titanic_data[titanic_data['Sex'] == 'female']['Age'].mean()
avg_fem_age


# In[93]:


# Step 9(b): Find the average age of all male passengers
avg_male_age = titanic_data[titanic_data['Sex'] == 'male']['Age'].mean()
avg_male_age


# In[142]:


# Step 10(a): Find the survival percentage of passengers in group "C"
embarked_C = titanic_data['Embarked'] == 'C'
survived_1 = titanic_data['Survived'] == 1
total_embarked_C = len(titanic_data[embarked_C])
total_C_1 = len(titanic_data[embarked_C & survived_1])

cherbourg_survival = (total_C_1 / total_embarked_C) * 100
cherbourg_survival


# In[144]:


# Step 10(b): Find the survival percentage of passengers in group "Q"
embarked_Q = titanic_data['Embarked'] == 'Q'
survived_1 = titanic_data['Survived'] == 1
total_embarked_Q = len(titanic_data[embarked_Q])
total_Q_1 = len(titanic_data[embarked_Q & survived_1])

queenstown_survival = (total_Q_1 / total_embarked_Q) * 100
queenstown_survival


# In[145]:


# Step 10(c): Find the survival percentage of passengers in group "S"
embarked_S = titanic_data['Embarked'] == 'S'
survived_1 = titanic_data['Survived'] == 1
total_embarked_S = len(titanic_data[embarked_S])
total_S_1 = len(titanic_data[embarked_S & survived_1])

south_survival = (total_S_1 / total_embarked_S) * 100
south_survival

