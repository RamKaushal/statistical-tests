import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import zconfint
data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
#print(data.head(5))
age_df = data[data['Age'].notna()]['Age']
#sns.histplot(age_df)
#plt.show()
survived_data = data[data['Survived'] == 1]
survived_age = survived_data[survived_data['Age'].notna()] 
#print(survived_age.head(5))
empty_list = []
for i in range(60):
    random_data = np.random.choice(survived_age['Age'],60).mean()
    empty_list.append(random_data)
sns.distplot(empty_list)
plt.show()
#h0 - average ageH0: Average age of passengers in Titanic is less than 28:μ0 <=28
#HA : New research claims mean age is greater than 28: μ1 > 28

meanh0 = 28 

ztest_score,pvalue = ztest(empty_list,value=meanh0,alternative = 'larger')
print(pvalue)
#print(ztest_score)

if pvalue<0.5:
    print("reject the null hypothesis with"+str((1-pvalue)*100)+"level of confidence")
else:
    print("failed to reject the h0")

lower,upper = zconfint(x1=empty_list,value=0,alpha=0.05,alternative='two-sided')

print(str(lower)+','+str(upper))
