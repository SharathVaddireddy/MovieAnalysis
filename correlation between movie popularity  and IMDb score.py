import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_merged_dataset.csv')

# Plot the scatter plot
plt.scatter(df['tmdb_popularity'], df['imdb_score'], alpha=0.5)
plt.xlabel('TMDb Popularity Score')
plt.ylabel('IMDb Score')
plt.title('Correlation between TMDb Popularity Score and IMDb Score')
plt.show()
