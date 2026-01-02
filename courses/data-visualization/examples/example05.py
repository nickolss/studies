import pandas as pd

data = {
    'Name': ['Andre', 'Beatriz', 'Carla'],
    'Age': [18, 21, 19],
    'City': ['São Paulo', 'São Paulo', 'Rio de Janeiro']
}

df = pd.DataFrame(data)

# Select row using index
print(df.loc[0, :])

# Select just name using index
print(df.loc[0, 'Name'])

# Select Age and City
print(df.loc[0, 'Age':])

# Select more rows
print(df.loc[1:2, :])

# Select specific rows
print(df.loc[[0,2], :])


print(df['Age'].describe())