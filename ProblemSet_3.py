#!/usr/bin/env python
# coding: utf-8

# # Question 1

# Introduction: Special thanks to: https://github.com/justmarkham for sharing the dataset and materials. Occupations Step 1. Import the necessary libraries Step 2. Import the dataset from this address. Step 3. Assign it to a variable called users Step 4. Discover what is the mean age per occupation Step 5. Discover the Male ratio per occupation and sort it from the most to the least Step 6. For each occupation, calculate the minimum and maximum ages Step 7. For each combination of occupation and sex, calculate the mean age Step 8. For each occupation present the percentage of women and men
# 
# Step 1. Import the necessary libraries

# In[1]:


#Step 1. Import the necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt


# Step 2. Import the dataset from this address. Step 3. Assign it to a variable called users

# In[2]:


# 2. Importing dataset from the github link:
# 3. Assigning dataset to a variable called 'users':

link = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(link, delimiter = '|')
users.head(13)


# Step 4. Discover what is the mean age per occupation

# In[4]:


# 4. Mean age per occupation:

meanAge = users.groupby(['occupation']).agg({'age':'mean'})
print("---- Average age occupation-wise ----")
print(meanAge)


# Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# In[5]:


# 5. Finding male ratio per occupation and sort from most to least:

df = users[['gender','occupation']]
male = df.loc[df['gender'] == 'M']
total = df.groupby('occupation').count()
male = male.groupby('occupation').count()
maleRatio = male / total
maleRatio.sort_values(by = 'gender', ascending = False)


# Step 6. For each occupation, calculate the minimum and maximum ages

# In[7]:


# 6. Finding minimum and maximum ages for each occupation:

minAge = users.groupby(['occupation']).agg({'age':'min'})
maxAge = users.groupby(['occupation']).agg({'age':'max'})
print("---- Minimum age - occupation-wise ----")
print(minAge)
print(' ')
print("---- Maximum age - occupation wise ----")
print(maxAge)


# Step 7. For each combination of occupation and sex, calculate the mean age

# In[8]:


# 7. Finding mean age for each combination of occupation and sex:

meanAge = users.groupby(['occupation','gender']).agg({'age':'mean'})
print("---- Mean age by occupation and gender ----")
print(meanAge)


# Step 8. For each occupation present the percentage of women and men

# In[11]:


# 8. Percentage of men and women for each occupation:

percentM_F = (users.groupby(['occupation', 'gender'])['gender'].count().groupby(level = 0).transform(lambda x: x/x.sum()*100))
print("---- Percentage of men and women in each occupation ----")
print(percentM_F)


# # Question 2

# Step 1. Import the necessary libraries

# In[10]:


# 1. Importing necessary libraries:

import pandas as pd
import numpy as np


# Step 2. Import the dataset from this address
# 
# Step 3. Assign it to a variable called euro12

# In[12]:


# 2. Import dataset from github link provided
# 3. Assigning dataset to variable called euro12 and showing top 10 rows

githubLink = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(githubLink, delimiter = ',')
euro12.head(10)


# Step 4. Select only the Goal column

# In[13]:


# 4. Only selecting 'Goals' column

goalsC = euro12['Goals']
goalsC.head(5)


# Step 5. How many team participated in the Euro2012?

# In[14]:


# 5. Finding the number of teams that participated in Euro2012

teamSum = len(euro12['Team'].unique())
print("Total number of teams that participated in Euro 2012 are",teamSum)


# Step 6. What is the number of columns in the dataset?

# In[15]:


# 6. Finding total number of columns in dataset

euro12.shape
print(" Total number of columns in the dataset are", euro12.shape[1])


# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[16]:


# 7. Only select Team, Yellow Cards and Red Cards columns and, assign them to dataframe called discipline

discipline = euro12[['Team','Yellow Cards','Red Cards']]
discipline.head(10)


# Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[17]:


# 8. Sort teams by red card to yellow cards

discipline.sort_values(by = ['Yellow Cards', 'Red Cards'], ascending = False)


# Step 9. Calculate the mean Yellow Cards given per Team

# In[18]:


# 9. Mean number of yellow cards given per team

yellowCard_M = euro12.groupby(['Team']).agg({'Yellow Cards':'mean'})
print("--- The average yellow cards received per team are ---")
print(yellowCard_M)


# Step 10. Filter teams that scored more than 6 goals

# In[19]:


# 10. Filtering teams scoring more than 6 goals

teamGoal6 = euro12[euro12['Goals'] > 6]
teamGoal6


# Step 11. Select the teams that start with G

# In[20]:


# 11. Displaying team names starting with letter 'G'

Team_G = euro12[euro12["Team"].str.startswith("G")]
Team_G


# Step 12. Select the first 7 columns

# In[21]:


# 12. Selecting first 7 columns only

teams7= euro12.iloc[:, :7]
teams7


# Step 13. Select all columns except the last 3

# In[22]:


# 13. Selecting all columns except last 3

teamsNoLast3 = euro12.iloc[:, :-3]
teamsNoLast3


# Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[23]:


euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]


# # Question 3

# Step 1. Import the necessary libraries

# In[24]:


# 1. Importing necessary libraries

import pandas as pd
import numpy as np


# Step 2. Create

# In[25]:


# 2. Create 3 differents Series, each of length 100, as follows:
    # • The first a random number from 1 to 4
    # • The second a random number from 1 to 3
    # • The third a random number from 10,000 to 30,000

series1 = pd.Series(np.random.randint(1,5,100))
series2 = pd.Series(np.random.randint(1,4,100))
series3 = pd.Series(np.random.randint(10000,30000,100))


# Step 3. Create a DataFrame by joinning the Series by column

# In[27]:


# 3. Creating a DataFrame by joining the Series by column

joinedSeries = {"Series1": series1,"Series2": series2,"Series3": series3}
joinedDF = pd.concat(joinedSeries, axis = 1)
joinedDF.head(13)


# Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter

# In[28]:


# 4. Changing the name of the columns to bedrs, bathrs, price_sqr_meter respectively

joinedDF.rename(columns = {'Series1' : 'bedrs', 'Series2' : 'bathrs', 'Series3' : 'price_sqr_meter'}, inplace = True)
joinedDF.head(13)


# Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

# In[29]:


# 5. Creating a column DataFrame with the values of the 3 Series and assigning it to 'bigcolumn'

bigcolumn = pd.DataFrame(joinedDF['bedrs'].astype(str) + joinedDF['bathrs'].astype(str) + joinedDF['price_sqr_meter'].astype(str))
bigcolumn


# Step 6. Ops it seems it is going only until index 99. Is it true? Soution: True

# In[30]:


# 6. Ops it seems it is going only until index 99. Is it true?
# Answer: Yes, it is true.


# Step 7. Reindex the DataFrame so it goes from 0 to 299

# In[31]:


# 7. Reindexing the DataFrame so it goes from 0 to 299

bigcolumn.reindex(range(0, 300))


# # Question 5

# Step 1. Import the necessary libraries

# In[36]:


# 1. Importing necessary libraries 

import pandas as pd
import numpy as np


# Step 2. Import the dataset from this address.
# 
# Step 3. Assign it to a variable called chipo.

# In[37]:


# 2. Importing dataset from git-hub address
# 3. Assigning it a variable called chipo 

githubLink = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_table(githubLink)


# Step 4. See the first 10 entries

# In[38]:


# 4. See the first 10 entries

chipo.head(10)


# Step 5. What is the number of observations in the dataset?
# 
# Step 6. What is the number of columns in the dataset?

# In[39]:


# 5. What is the number of observations in the dataset?
# 6. What is the number of columns in the dataset?

print( "No. of observations in the dataset are {}".format(chipo.shape[0]))
print( "No. of columns in the dataset are {}".format(chipo.shape[1]))


# Step 7. Print the name of all the columns.

# In[40]:


# 7. Print the name of all the columns.

chipo.columns


# Step 8. How is the dataset indexed?

# In[41]:


# 8. How is the dataset indexed?

# Python uses a default 0-based indexing and hence indexing always starts from 0 to total number -1, 
# which in our dataset is 4621.


# Step 9. Which was the most-ordered item?
# 
# Step 10. For the most-ordered item, how many items were ordered?

# In[44]:


# 9. Which was the most-ordered item? 
# 10. For the most-ordered item, how many items were ordered?

most_ordered =  chipo.groupby(['item_name']).agg({'quantity':'sum'}).sort_values(by = 'quantity', ascending = False)
print("---- Most ordered item is "+ str(most_ordered.iloc[0].name)+" with an order quantity of "+ str(most_ordered.iloc[0].quantity) +" units" )


# Step 11. What was the most ordered item in the choice_description column?

# In[46]:


# 11. What was the most ordered item in the choice_description column?

most_ordered =  chipo.groupby(['choice_description']).agg({'quantity':'sum'}).sort_values(by='quantity', ascending = False)
print("---- Most ordered item is "+ str(most_ordered.iloc[0].name) + " with an order quantity of " + str(most_ordered.iloc[0].quantity)+" units")


# Step 12. How many items were orderd in total?

# In[47]:


# 12. How many items were orderd in total?

print("Total orders are", chipo['quantity'].sum())


# Step 13. • Turn the item price into a float • Check the item price type • Create a lambda function and change the type of item price • Check the item price type

# In[48]:


# 13.
# • Turn the item price into a float
# • Check the item price type
# • Create a lambda function and change the type of item price
# • Check the item price type

chipo['item_price'] = chipo['item_price'].apply(lambda x: x.replace('$', '')).astype(float)
chipo.head(10)


# Step 14. How much was the revenue for the period in the dataset?

# In[49]:


# 14. How much was the revenue for the period in the dataset?

print("Total revenue $", chipo['item_price'].sum())


# Step 15. How many orders were made in the period?

# In[50]:


# 15. How many orders were made in the period?

print("Total unique order ids are", chipo['order_id'].nunique())


# Step 16. What is the average revenue amount per order?

# In[51]:


# 16. What is the average revenue amount per order?

print('---- Average amount per order ----')
print(chipo.groupby(['order_id']).agg({'item_price':'mean'}))


# Step 17. How many different items are sold?

# In[52]:


# 17. How many different items are sold?

print("Total unique items sold are",chipo['item_name'].nunique())


# # Question 6

# In[56]:


# Importing required libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[59]:


# Reading csv file
marriage_data = pd.read_csv('us-marriages-divorces-1867-2014.csv')
marriage_data.head(10)


# In[60]:


plt.plot(marriage_data['Year'], marriage_data['Marriages_per_1000'], label = "Marriages per capita")
plt.xlabel("Year")  #  x - axis label
plt.ylabel("Relationship")  #  y - axis label
plt.plot(marriage_data['Year'], marriage_data['Divorces_per_1000'], label = "Divorces per capita")
plt.legend(loc = "upper right")
plt.title("Marriages vs. Divorces per capita in the US between the years 1867 - 2014")  # title
plt.rcParams ["figure.figsize"] = (20,10)
plt.show()


# # Question 7

# In[61]:


marriage1900 = marriage_data[marriage_data['Year'] == 1900]
marriage1950 = marriage_data[marriage_data['Year'] == 1950]
marriage2000 = marriage_data[marriage_data['Year'] == 2000]
plt.bar(marriage1900['Year'], marriage1900['Marriages_per_1000'], width = 15, label = 'Marriages per 1000 in 1900')
plt.bar(marriage1900['Year'], marriage1900['Divorces_per_1000'], width = 15, label = 'Divorces per 1000 in 1900')
plt.bar(marriage1950['Year'], marriage1950['Marriages_per_1000'], width = 15, label = 'Marriages per 1000 in 1950')
plt.bar(marriage1950['Year'], marriage1950['Divorces_per_1000'], width = 15, label = 'Divorces per 1000 in 1950')
plt.bar(marriage2000['Year'], marriage1950['Marriages_per_1000'], width = 15, label = 'Marriages per 1000 in 2000')
plt.bar(marriage2000['Year'], marriage1950['Divorces_per_1000'], width = 15, label = 'Divorces per 1000 in 2000')
plt.xlabel("Year") # x - axis label 
plt.ylabel("Count") # y - axis label  
plt.legend(loc = "upper left")
plt.title(" Vertical bar chart showing marriages and divorce rates in the US per capita for the years 1900, 1950 and 2000 respectively ")
plt.rcParams ["figure.figsize"] = (15,10)
plt.show()


# # Question 8

# In[62]:


actors = pd.read_csv('actor_kill_counts.csv')
actors.head(10)


# In[63]:


# Sorting actor names by their kill count

kill_count = actors.sort_values(by = 'Count', ascending = True)
kill_count.head(10)


# In[64]:


# Plotting a horizontal bar graph

plt.barh(kill_count['Actor'], kill_count['Count'])
plt.ylabel("Actor Name") # y - axis label
plt.xlabel("Kill Count") # x - axis label
plt.title("Horizontal bar graph showing actor name and their kill count sorted from highest to lowest")
plt.rcParams ["figure.figsize"] = (20,10)
plt.show()


# # Question 9

# In[65]:


# Top 10 rows details of dataset

romans = pd.read_csv('roman-emperor-reigns.csv')
romans.head(10)


# In[66]:


# Percentage of deaths grouped by cause of death

percent_assasin = romans.groupby(['Cause_of_Death'])['Cause_of_Death'].count().transform( lambda x: x/x.sum()*100)
percent_death = pd.DataFrame(percent_assasin)
percent_death.rename(columns={'Cause_of_Death' : "Percent_Cause_of_death" }, inplace = True)
display(percent_death.head(10))
percent_death['Cause_of_Death'] = percent_death.index


# In[67]:


# Pie graph showing fractions of deaths based on cause of death

data = percent_death['Percent_Cause_of_death']
keys = percent_death['Cause_of_Death']
palette_color = sns.color_palette('dark')
plt.pie(data, labels = keys, colors = palette_color, autopct='%.0f%%') # plotting data on chart
plt.show()
plt.rcParams ["figure.figsize"] = (15,10)


# # Question 10

# Create a scatter plot showing the relationship between the total revenue earned by arcades and the number of Computer Science PhDs awarded in the U.S. between 2000 and 2009.

# In[70]:


# Reading and displaying the top 10 rows in dataset

revenue = pd.read_csv('arcade-revenue-vs-cs-doctorates.csv')
revenue.head(10)


# In[76]:


sns.scatterplot(x = revenue['Total Arcade Revenue (billions)'], y = revenue['Computer Science Doctorates Awarded (US)'], data = revenue, style = None)


# In[ ]:




