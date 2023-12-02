import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Function to generate synthetic data
def generate_data(num_samples=1000, random_seed=42):
    np.random.seed(random_seed)

    # Generate random circles
    circle_data = np.random.rand(num_samples, 2)
    circle_labels = np.ones((num_samples, 1))

    # Generate random squares
    square_data = np.random.rand(num_samples, 2)
    square_data[:, 0] += 0.5  # Shift squares to the right
    square_labels = np.zeros((num_samples, 1))

    # Concatenate circles and squares
    data = np.concatenate([circle_data, square_data], axis=0)
    labels = np.concatenate([circle_labels, square_labels], axis=0)

    # Shuffle the data
    indices = np.arange(2 * num_samples)
    np.random.shuffle(indices)
    data = data[indices]
    labels = labels[indices]

    return data, labels

# Generate synthetic data
num_samples = 10000
data, labels = generate_data(num_samples)

# Split the data into training and validation sets using scikit-learn
train_data, val_data, train_labels, val_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

# Create pandas DataFrames
train_df = pd.DataFrame(np.hstack([train_data, train_labels]), columns=['Feature 1', 'Feature 2', 'Label'])
val_df = pd.DataFrame(np.hstack([val_data, val_labels]), columns=['Feature 1', 'Feature 2', 'Label'])

# Save DataFrames to CSV files
train_df.to_csv('train_data.csv', index=False)
val_df.to_csv('val_data.csv', index=False)

# Display the first few rows of the generated training data
print("Generated Training Data:")
print(train_df.head())
