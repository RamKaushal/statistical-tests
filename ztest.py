import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
#print(data.head(5))
age_df = data[data['Age'].notna()]['Age']
sns.histplot(age_df)
plt.show()
survived_data = data[data['Survived'] == 1]
survived_age = survived_data[survived_data['Age'].notna()] 
print(survived_age.head(5))