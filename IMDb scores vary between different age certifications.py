import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_merged_dataset.csv')

# Group data by age certification and calculate the mean IMDb score
age_cert_avg_imdb = df.groupby('age_certification')['imdb_score'].mean().sort_values()

# Create a pyramid graph
fig, ax = plt.subplots(figsize=(8, 6))

# Plot bars for IMDb scores less than 5
ax.barh(age_cert_avg_imdb.index, age_cert_avg_imdb, color='red', label='IMDb Score < 5')

# Plot bars for IMDb scores greater than or equal to 5
ax.barh(age_cert_avg_imdb.index, age_cert_avg_imdb.abs(), color='purple', label='IMDb Score >= 5')

# Add vertical line at IMDb score of 5
ax.axvline(x=5, color='black', linestyle='--')

# Add labels and title
ax.set_xlabel('Average IMDb Score')
ax.set_ylabel('Age Certification')
ax.set_title('Average IMDb Score by Age Certification')
ax.legend()

# Invert y-axis to create a pyramid effect
ax.invert_yaxis()

plt.show()
