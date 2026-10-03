import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')

data.head()

grouped_df = data.groupby('continent').mean(numeric_only=True)
grouped_Df = grouped_df.reset_index()
grouped_df

plots = sns.barplot(x=grouped_df['contient'], y=grouped_df['life_exp'], color='teal')

plots = sns.barplot(x=grouped_df['continent'], y=grouped_df['life_exp'], color='teal')

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                    (bar.get_x() + bar.get_width() / 2,
                     bar.get_height()), ha='center', va='center',
                    size=12, xytext=(0,8),
                    textcoords='offset points')

plt.xlabel("continents", size=14)

plt.ylabel("life expectancy", size=14)

plt.title("this is an annotated barplot")

plt.show()