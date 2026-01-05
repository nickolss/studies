import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

y = np.random.randint(low=100, high=5000, size=50) # Generate 50 random integers between 100 and 5000
x = pd.date_range(start='2025-1-1', freq='D', periods=50) # Generate 50 dates starting from Jan 1, 2025

plt.figure(figsize=(8,5))
plt.plot(x, y)
plt.title('Line Graph Example')
# plt.show()


fig = px.line(x=x, y=y, title='Line Graph Example with Plotly', labels={'x':'Date', 'y':'Value'})
fig.show()