import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:\Users\nutha\PycharmProjects\pythonProject5\merged_dataset.csv', dtype={'runtime': str})

# Replace empty cells with 'NA'
df.fillna('NA', inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('cleaned_file.csv', index=False)
