# IMPORT MODULES HERE
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def filter_by_col_vals(df, colName, colVal, remainingCol):
    '''
    this function filters a dataframe by one columns values and returns one column (remainingCol) of data
    :param df: dataframe
    :param colName: column name
    :param colVal: column value
    :param remainingCol: another column in dataframe to filter
    :return: returns a filtered dataframe
    '''

    filtered_data = df.loc[df[colName] == colVal].filter(items=[remainingCol])
    return filtered_data


# 2. IMPORT DATASET
Emp_Attrition = pd.read_csv("Dataset/HR-Employee-Attrition.csv")

# 3. ANALYSE, PYTHON AND VISUALISE

print(Emp_Attrition.size)
print(Emp_Attrition.columns)
print(Emp_Attrition.columns[0])
print(Emp_Attrition.head)
print(Emp_Attrition.info())

# COUNT NUMBER OF EMPLOYEES IN EACH DEPARTMENT
print(Emp_Attrition['Department'].value_counts())

# SORT AGE OF EMPLOYEES IN ASCENDING ORDER
Emp_Attrition.sort_values('Age', inplace=True)
print(Emp_Attrition)

# CALCULATE MEAN AGE OF EMPLOYEES IN EACH DEPARTMENT
print(Emp_Attrition.groupby('Department')['Age'].mean())

# FILTERED YES/NO FOR ATTRITION BY DEPARTMENT
df1 = Emp_Attrition.filter(items=['Department', 'Attrition'])

# USING FUNCTION ON LINE 18 TO CREATE REUSABLE CODE
sales_att = filter_by_col_vals(df1, 'Department', 'Sales', 'Attrition')
randd_att = filter_by_col_vals(df1, 'Department', 'Research & Development', 'Attrition')
hr_att = filter_by_col_vals(df1, 'Department', 'Human Resources', 'Attrition')

# sales_att = df1.loc[df1['Department'] == 'Sales'].filter(items=['Attrition'])
# randd_att = df1.loc[df1['Department'] == 'Research & Development'].filter(items=['Attrition'])
# hr_att = df1.loc[df1['Department'] == 'Human Resources'].filter(items=['Attrition'])
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

# MERGE DATAFRAMES TO CREATE ATTRITION/DEPARTMENT MATRIX
Dep_Att = pd.DataFrame(data={'No': [hr_att_vals[0], randd_att_vals[0], sales_att_vals[0]],
                             'Yes': [hr_att_vals[1], randd_att_vals[1], sales_att_vals[1]]},
                       index=['HR', 'RD', 'Sales'])
print(Dep_Att)

# CREATE BAR CHART TO SHOW ATTRITION BY DEPARTMENT
ax = Dep_Att.plot.bar(color=['#e17055', '#81ecec'], rot=0, title='Attrition by Department', xlabel='Department')
plt.show()

# TAKE ORIGINAL DATAFRAME AND FILTER FOR AGE AND MONTHLY INCOME COLUMNS
# PLOT USING SEABORN
df2 = Emp_Attrition.filter(items=['YearsInCurrentRole', 'MonthlyIncome'])
print(df2)

# SHOW YEARS IN CURRENT ROLE AND MONTHLY INCOME USING SEABORN BAR PLOT
sns.barplot(data=df2, x='YearsInCurrentRole', y='MonthlyIncome')
plt.show()

# CREATE DATAFRAMES FOR MALE EMPLOYEES AND FEMALE EMPLOYEES
males_df = Emp_Attrition.loc[Emp_Attrition['Gender'] == 'Male']
females_df = Emp_Attrition.loc[Emp_Attrition['Gender'] == 'Female']

# CREATE GRAPHS COMPARING GENDER MONTHLY INCOME FOR EACH JOB ROLE AND YEARS IN CURRENT ROLE

fig, axs = plt.subplots(nrows=2, ncols=2)
axs[0][0].set_title('Males')
axs[0][1].set_title('Females')
axs[1][0].set_title('Males')
axs[1][1].set_title('Females')
axs[1][0].tick_params('x', labelrotation=90)
axs[1][1].tick_params('x', labelrotation=90)
sns.barplot(x='YearsInCurrentRole', y='MonthlyIncome', data=males_df, ax=axs[0][0])
sns.barplot(x='YearsInCurrentRole', y='MonthlyIncome', data=females_df, ax=axs[0][1])
sns.barplot(x='JobRole', y='MonthlyIncome', data=males_df.sort_values('JobRole'), ax=axs[1][0])
sns.barplot(x='JobRole', y='MonthlyIncome', data=females_df.sort_values('JobRole'), ax=axs[1][1])
plt.show()

# FILTER DATAFRAME TO GET MONTHLY INCOME VS YEARS IN CURRENT ROLE
# GROUP BY NUMBER OF YEARS IN THE COMPANY AND CALCULATE MEAN VALUES
monthlyincome_yrsinrole = Emp_Attrition.filter(items=['YearsInCurrentRole', 'MonthlyIncome'])
grouped_monthlyincome_yrsinrole = monthlyincome_yrsinrole.groupby('YearsInCurrentRole')

for year_group in grouped_monthlyincome_yrsinrole:
    year = year_group[0]
    ygDF = year_group[1]  # YEAR GROUP DATAFRAME

    # CALCULATE THE MEAN VALUES FROM THIS GROUP
    income_list = ygDF.filter(items=['MonthlyIncome'])
    mean = np.mean(income_list)  # USING NUMPY TO CALCULATE MEAN MONTHLY INCOME FOR EACH YEAR GROUP

    print('YearsInCurrentRole: {} Avg Salary: {}'.format(year, int(mean)))  # PRINT MEAN AS INTEGER

# LOOK AT DEPARTMENT AND JOB SATISFACTION
age_job_satisfaction = Emp_Attrition.filter(items=['Department', 'JobSatisfaction'])
print(age_job_satisfaction)

# MEAN JOB SATISFACTION RATING FOR EACH DEPARTMENT
print(Emp_Attrition.groupby('Department')['JobSatisfaction'].mean())







