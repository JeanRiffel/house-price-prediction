import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate a fake dataset
num_samples = 5

# Features
num_bedrooms = np.random.randint(1, 5, num_samples)
square_footage = np.random.randint(1000, 3000, num_samples)
location_factor = np.random.uniform(0.8, 1.2, num_samples)  # Random factor for location
available = True

# Linear relationship to generate house prices
house_prices = 50000 + 100 * num_bedrooms + 50 * square_footage * location_factor + np.random.normal(0, 10000, num_samples)

# Create a DataFrame
data = pd.DataFrame({
    'Bedrooms': num_bedrooms,
    #'SquareFootage': square_footage,
    #'LocationFactor': location_factor,
    'Price': house_prices,
    #'Available': available,
})

# Save the dataset to a CSV file
data.to_csv('data/fake_house_prices_dataset.csv', index=False)

# Display the generated dataset
print(data)
