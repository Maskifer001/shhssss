import pandas as pd

# Create a DataFrame with some random data
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'age': [25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

# Write the DataFrame to a Parquet file
df.to_parquet('example.parquet')
