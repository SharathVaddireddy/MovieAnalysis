import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Lenovo/Desktop/big data integration/case studies/cleaned_merged_dataset.csv')

# Group by actor/actress and count unique movie
actor_movie_counts = df.groupby('name')['title'].nunique().sort_values(ascending=False)

# Plot the results
plt.figure(figsize=(10, 6))
actor_movie_counts.head(50).plot(kind='bar', color='skyblue')
plt.xlabel('Actor/Actress')
plt.ylabel('Number of Movies')
plt.title('Top 50 Actors/Actresses by Number of Movies')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

