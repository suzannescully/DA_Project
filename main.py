# import modules here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Import Dataset
Emp_Attrition = pd.read_csv("Dataset/HR-Employee-Attrition.csv")

# 3. Analyse Dataset
# Your project should include sorting, indexing, grouping. [1]
# Replace missing values or dropping duplicates. [1]
# Looping, iterrows [1]
# Merge dataframes [1]
print(Emp_Attrition.size)