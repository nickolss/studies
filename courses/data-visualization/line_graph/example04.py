import plotly.graph_objs as go
import numpy as np

x = np.arange(10)

fig = go.Figure(
    data=go.Scatter(x = x**3)
)
fig.show()

data = go.Scatter(
    x=  x**3
)

fig2 = go.Figure(data=data)
fig2.show()