import pandas as pd
import seaborn
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.drop(columns=['id', 'Successes', 'Amount collected', 'Number of investors', 'Per capita investment'], inplace=True)
df_corr = df.corr()
seaborn.clustermap(df_corr, annot=True, fmt=".2f")
plt.show()