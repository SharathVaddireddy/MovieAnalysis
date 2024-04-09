import pandas as pd

# Load the credits dataset
credits_dataset = pd.read_csv(r"C:\Users\nutha\Downloads\archive (3)\credits.csv")

# Load the titles dataset
titles_dataset = pd.read_csv(r"C:\Users\nutha\Downloads\archive (3)\titles.csv")

# Perform the merge operation
merged_dataset = pd.merge(credits_dataset, titles_dataset, on='id', how='inner')

# Save the merged dataset to a new CSV file
merged_dataset.to_csv('merged_dataset.csv', index=False)

import pandas as pd

# Load the merged dataset
merged_dataset = pd.read_csv(r"C:\Users\nutha\PycharmProjects\pythonProject5\merged_dataset.csv")

# Drop duplicate rows
merged_dataset.drop_duplicates(inplace=True)

# Replace any empty values with NaN
merged_dataset.replace('', pd.NA, inplace=True)

# Drop rows with missing values in specific columns
merged_dataset.dropna(subset=['id', 'name', 'title'], inplace=True)

# Convert columns to appropriate data types if needed
merged_dataset['release_year'] = pd.to_numeric(merged_dataset['release_year'], errors='coerce')
merged_dataset['runtime'] = pd.to_numeric(merged_dataset['runtime'], errors='coerce')

# Remove leading and trailing whitespaces from string columns
merged_dataset['name'] = merged_dataset['name'].str.strip()
merged_dataset['title'] = merged_dataset['title'].str.strip()

# Perform any other cleaning or preprocessing steps as needed

# Save the cleaned dataset to a new CSV file
merged_dataset.to_csv('cleaned_merged_dataset.csv', index=False)
