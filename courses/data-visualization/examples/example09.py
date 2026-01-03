import pandas as pd

df = pd.read_csv('../sample_data/train.csv')

print(
    df.query(
        '(Sex == "female") & (Survived == 1)'
    ) 
)

