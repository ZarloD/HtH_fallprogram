import pandas
import seaborn
import matplotlib.pyplot as plt

''' 
The best way to complete this activity is to copy the code in this file into a jupyter notebook file you create. This will also you to see your visualizations easier. Once you have finished creating your visuals copy your code back into this file and submit it to Replit. Don't forget to also upload your new code to Github! 
'''

# Step 1: Create a heatmap showing the correlation between the following features: survival, pclass, sex, age, and fare 
corr_heatmap = sns.heatmap(df.corr(), annot = True, cmap = 'viridis')

# Step 2: Create a bar graph that illustrates how many passengers fell into each of these age ranges: 0 - 16, 17 - 25, 26 -40, 41 - 59, 60 or older
age_group_chart = 

# Step 3: Create a line graph showing the average survival percentage of each of the previous age groups
survival_age_pers = 

# Step 4: Create a pie chart that shows the percentage of survivors that were male and the percentage of survivors that were female
survivors = 

# Step 5: Create a histogram that shows the distribution of passengers between the three embarking locations: C (Cherbourg), Q (Queenstown), S (Southampton)
titanic_description = 