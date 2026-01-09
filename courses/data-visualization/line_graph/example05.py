import plotly.graph_objs as go
import numpy as np

N = 50
x = np.linspace(0, 1, N)
random_y = np.random.normal(30, 2.5, N)

line = [
    go.Scatter(
        x = x,
        y = random_y,
        mode='lines',
        name='Line 1'
    )
]

layout = go.Layout(
    title='Minha Figura',
    xaxis=dict(title='Eixo X'),
    yaxis=dict(title='Eixo Y')
)

fig = go.Figure(
    data = line, 
    layout=layout
)

fig.show()