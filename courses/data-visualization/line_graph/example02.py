import plotly.express as px
import pandas as pd

df = px.data.gapminder()
print(df.head())

print(df['continent'].unique()) # Show unique continents
print(df['country'].unique())   # Show unique countries


df = df.query('country == "Brazil"')
print(df.head())


title = 'Life Expectancy in Brazil Over the Years'
fig = px.line(df, x='year', y='lifeExp', title=title)
fig.show()