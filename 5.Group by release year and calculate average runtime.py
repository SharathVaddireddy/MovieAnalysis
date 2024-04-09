import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Lenovo/Desktop/big data integration/case studies/cleaned_merged_dataset.csv')

# Group by release year and calculate average runtime
avg_runtime_per_year = df.groupby('release_year')['runtime'].mean()

# Plot the trend
plt.plot(avg_runtime_per_year.index, avg_runtime_per_year.values, marker='o', color='orange')
plt.xlabel('Release Year')
plt.ylabel('Average Runtime (minutes)')
plt.title('Trend in Average Runtime Over the Years')
plt.grid(True)
plt.show()
