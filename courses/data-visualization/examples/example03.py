import numpy as np
import plotly.express as px

array1 = np.random.normal(10, 0.5, 50) # Normal distribution with mean=10, std=0.5
array2 = np.random.randint(1, 100, 50) # Random integers between 1 and 100

fig = px.scatter(x = array1, y = array2)
fig.show()