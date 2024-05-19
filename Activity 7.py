import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


data=pd.read_csv("C:/Users/Sfundesihle/Downloads/New folder/archive.zip")

sns.set_theme()

sns.set_style("whitegrid")

sns.set_style("whitegrid")



sns.lineplot(x='Games', y='Books', data=data)
plt.show()


sns.set_context("talk")
sns.lineplot(x='Games', y='Books', data=data)
plt.show()

sns.kdeplot(data=data['Wins'],shade=True)

sns.rugplot(data['Games'])


sns.boxplot(x='Games', y='Books', data=data)

sns.violinplot(x='Games', y='Books', data=data)

sns.swarmplot(x='Games', y='Books', data=data)

sns.pairplot(data, hue='Games')

sns.jointplot(x='Games', y='Books', data=data,
kind='scatter')