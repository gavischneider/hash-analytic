import pandas as pd
import seaborn as sns

df = pd.read_csv("gapminder-FiveYearData.csv")
print(df.head())

heatmap_data = pd.pivot_table(df, values='lifeExp', index=['continent'], columns='year')
heatmap = sns.heatmap(heatmap_data, cmap="YlGnBu")

figure = heatmap.get_figure()
figure.savefig('output.png', dpi=400)
