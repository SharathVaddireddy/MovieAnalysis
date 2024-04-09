import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_merged_dataset.csv')

# Group by production country and calculate average IMDb score
country_avg_imdb = df.groupby('production_countries')['imdb_score'].mean().sort_values(ascending=False)

# Plot the results
plt.figure(figsize=(12, 6))
country_avg_imdb.plot(kind='bar')
plt.xlabel('Production Country')
plt.ylabel('Average IMDb Score')
plt.title('Average IMDb Score by Production Country')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
