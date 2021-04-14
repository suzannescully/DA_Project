# import modules here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 2. Import Dataset
Emp_Attrition = pd.read_csv("Dataset/HR-Employee-Attrition.csv")

# 3. Analyse Dataset
# Your project should include sorting, indexing, grouping. [1] done
# Replace missing values or dropping duplicates. [1]
# Looping, iterrows [1]
# Merge dataframes [1] done
# 4) Python
# • Use functions to create reusable code. [1]
# • Numpy. [1]
# • Dictionary or Lists. [1] done
# 5) Visualize
# • Seaborn, Matplotlib [2] bar chart with matplotlib done, scatter plot with seaborn

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
# print(Emp_Attrition[['Department','Attrition']])
df1 = Emp_Attrition.filter(items=['Department', 'Attrition'])

sales_att = df1.loc[df1['Department'] == 'Sales'].filter(items=['Attrition'])
randd_att = df1.loc[df1['Department'] == 'Research & Development'].filter(items=['Attrition'])
hr_att = df1.loc[df1['Department'] == 'Human Resources'].filter(items=['Attrition'])
print(hr_att)

print(sales_att.value_counts())
print(sales_att.value_counts().values)
sales_att_vals = sales_att.value_counts().values

print(hr_att.value_counts())
print(hr_att.value_counts().values)
hr_att_vals = hr_att.value_counts().values

print(randd_att.value_counts())
print(randd_att.value_counts().values)
randd_att_vals = randd_att.value_counts().values

# merge dataframes to create attrition-department matrix
Dep_Att = pd.DataFrame(data={'No': [hr_att_vals[0], randd_att_vals[0], sales_att_vals[0]], 'Yes': [hr_att_vals[1], randd_att_vals[1], sales_att_vals[1]]}, index=['HR', 'RD', 'Sales'])
print(Dep_Att)

# create bar chart showing attrition yes/no per department
ax = Dep_Att.plot.bar(color=['#e17055', '#81ecec'], rot=0, title='Attrition by Department', xlabel='Department')
plt.show()


# scatter plot age and monthly rate
# first take the original dataframe and filter for age and monthly rate columns
# then plot
df2 = Emp_Attrition.filter(items=['Age', 'MonthlyRate'])
print(df2)
sns.scatterplot(data=df2, x='Age', y='MonthlyRate')
plt.show()

# numpy
# array = np.array(Emp_Attrition)
# array_size = array.size
# array_shape = array.shape
# print('size of array -', array_shape)
#
# print('Number of Total Columns -', len(Emp_Attrition))

# drop duplicates

# graph to show gender/job role and average hourly rate
















