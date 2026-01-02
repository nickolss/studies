import pandas as pd
import numpy as np

data = {
    'Name': ['Andre', 'Beatriz', 'Carla'],
    'Age': [18, 21, 19],
    'City': ['São Paulo', 'São Paulo', 'Rio de Janeiro']
}

df = pd.DataFrame(data) # Looks like an Excel

print(df)

print(df['Name']) # Prints only the names

df['State'] = [
    'SP',
    'SP',
    'RJ'
]

print(df)