import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Load the dataset
df = pd.read_csv('cleaned_merged_dataset.csv')

# Get a list of unique countries in the dataset
unique_countries = df['production_countries'].unique()

# Prompt the user to choose a country
print("Select a country from the following options:")
for i, country in enumerate(unique_countries):
    print(f"{i + 1}. {country}")

country_choice = int(input("Enter the number corresponding to your choice: ")) - 1

if 0 <= country_choice < len(unique_countries):
    chosen_country = unique_countries[country_choice]

    # Filter the data for the chosen country
    df_country = df[df['production_countries'] == chosen_country]

    # Count the occurrences of each genre in the chosen country
    genre_counts_country = df_country['genres'].str.split(',').explode().str.strip().value_counts()

    # Plot a treemap for the genre counts in the chosen country
    plt.figure(figsize=(12, 8))
    squarify.plot(sizes=genre_counts_country.values, label=genre_counts_country.index, alpha=0.8)
    plt.axis('off')
    plt.title(f'Distribution of Movie Genres in {chosen_country} (Treemap)')
    plt.show()
else:
    print("Invalid choice. Please enter a valid number.")
