import pandas as pd

# Load the dataset
df = pd.read_csv('data.csv')

# Define a dictionary mapping incorrect values to correct values
corrections = {
    'Malee': 'Male',
    'Femalle': 'Female',
    'M': 'Male',
    'F': 'Female'
}

# Apply corrections to the 'gender' column
df['gender'] = df['gender'].map(corrections).fillna(df['gender'])  # Fill missing values back

# Save the corrected dataset
df.to_csv('corrected_data.csv', index=False)

print("Data correction complete. Corrected data saved to 'corrected_data.csv'.")