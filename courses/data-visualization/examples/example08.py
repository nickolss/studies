import pandas as pd

df = pd.read_csv("../sample_data/train.csv")

# print(df.head())

# print(df.describe())

# df['Sex'].value_counts()

# Select only man
print(
    df[
        df['Sex']=='male' # Select where Sex equals male
    ]
)

#or

print(
    df.loc[
        df['Sex']=='male'
    ]
)


# Select only women names
print(
    df[
        df['Sex']=='female'
    ]
    ['Name']
)


# Select using query
print(
    df.query(
        'Name == "Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)"'
    )
)

# Selection using multi conditions
print(
    df[
        (df['Sex']=='female') &
        (df['Survived'] == 1)
    ]
)