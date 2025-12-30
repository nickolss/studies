import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../sample_data/salaries.csv')
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()