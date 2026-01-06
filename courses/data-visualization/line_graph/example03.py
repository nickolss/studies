import plotly.express as px
import pandas as pd

df = px.data.gapminder().query("continent == 'Americas'")
title = 'Life Expectancy in the Americas Over the Years'
fig = px.line(df, x='year', y='lifeExp', title=title, color='country')
fig.show()
