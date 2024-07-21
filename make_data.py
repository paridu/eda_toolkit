import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker for generating realistic data
fake = Faker()

# Function to create a random dataset
def create_sample_data(num_rows):
    # Create a DataFrame
    df = pd.DataFrame({
        'Date': [fake.date_this_decade() for _ in range(num_rows)],
        'Category': [random.choice(['A', 'B', 'C', 'D']) for _ in range(num_rows)],
        'Item Code': [fake.unique.ean13() for _ in range(num_rows)],
        'Quantity': np.random.randint(1, 100, size=num_rows),
        'Price': np.round(np.random.uniform(10, 500, size=num_rows), 2),
        'Discount': np.round(np.random.uniform(0, 0.5, size=num_rows), 2),
        'Total Sales': lambda x: x['Quantity'] * x['Price'] * (1 - x['Discount']),
    })
    
    # Calculate Total Sales
    df['Total Sales'] = df.apply(lambda row: row['Quantity'] * row['Price'] * (1 - row['Discount']), axis=1)
    
    return df

# Generate a dataset with 500 rows
num_rows = 500
df = create_sample_data(num_rows)

# Save to CSV
df.to_csv('sample_data.csv', index=False)

print("Sample dataset generated and saved as 'sample_data.csv'.")
