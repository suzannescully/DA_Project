# import modules here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 2. Import Dataset
Emp_Attrition = pd.read_csv("Dataset/HR-Employee-Attrition.csv")

# 3. Analyse Dataset
# Your project should include sorting, indexing, grouping. [1]
# Replace missing values or dropping duplicates. [1]
# Looping, iterrows [1]
# Merge dataframes [1]
# 4) Python
# • Use functions to create reusable code. [1]
# • Numpy. [1]
# • Dictionary or Lists. [1]
# 5) Visualize
# • Seaborn, Matplotlib [2]

print(Emp_Attrition.size)
print(Emp_Attrition.columns)
print(Emp_Attrition.columns[0])
print(Emp_Attrition.head)
print(Emp_Attrition.info())

# how many employees in each department
print(Emp_Attrition['Department'].value_counts())

# sort age in ascending order
Emp_Attrition.sort_values('Age', inplace=True)
print(Emp_Attrition)

# mean age of employees in each department
print(Emp_Attrition.groupby('Department')['Age'].mean())

# yes/no for attrition in each department
print(Emp_Attrition[['Department','Attrition']])

# average job satisfaction bar plot per department

# group by ?

# merge or concat dataframes

# numpy
array = np.array(Emp_Attrition)
array_size = array.size
array_shape = array.shape
print('size of array -', array_shape)

print('Number of Total Columns -', len(Emp_Attrition))

# grouping

# drop duplicates

# graph to show gender/job role and average hourly rate
















