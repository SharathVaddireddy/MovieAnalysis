import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Lenovo/Desktop/big data integration/case studies/cleaned_merged_dataset.csv')

# Visualization : Histogram of IMDb Scores
plt.hist(df['imdb_score'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.title('Distribution of IMDb Scores')
plt.grid(True)
plt.show()
