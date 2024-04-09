import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/tonyk/Desktop/case stud/case_studies_project/cleaned_merged_dataset.csv')

# Plot a histogram of movie runtimes
plt.figure(figsize=(10, 6))
plt.hist(df['runtime'], bins=20, color='blue', edgecolor='black')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Runtimes')
plt.show()
