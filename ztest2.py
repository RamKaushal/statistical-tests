import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import zconfint
#h0: No difference in age of two genders who survived
#h1: There is difference in genders
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
survied = df[df['Survived']==1] 
final_survied = survied[survied['Age'].notna()]
#print(final_survied.head(5))
#checking the distribution of male

final_survied_male = final_survied[final_survied['Sex']=='male']
final_survied_male_age = final_survied_male[final_survied_male['Age'].notna()]['Age']
sns.distplot(final_survied_male_age)
plt.show()
#checking the distribution of female
final_survied_female = final_survied[final_survied['Sex']=='female']
final_survied_female_age = final_survied_female[final_survied_female['Age'].notna()]['Age']
sns.distplot(final_survied_female_age)
plt.show()

samples_list = []
for i in range(60):
    final_survied_male_age_samples = np.random.choice(final_survied_male_age,60).mean()
    samples_list.append(final_survied_male_age_samples)

sns.distplot(samples_list)
plt.show()