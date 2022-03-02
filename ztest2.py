import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import zconfint
#h0: No difference in age of two genders who survived
#h1: There is difference in genders
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
survied = df[df['Survived']==1] 
final_survied = df[df['Age'].notna()]
print(final_survied.head(5))