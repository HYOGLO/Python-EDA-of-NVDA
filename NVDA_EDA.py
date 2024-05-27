import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already fetched the data into a DataFrame named 'nvidia_data'
# The DataFrame should have columns like 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'

# Load data into DataFrame
nvidia_data = pd.read_csv("NVDA.csv")

# Display first few rows of the data
print(nvidia_data.head())

# Summary statistics
print(nvidia_data.describe())

# Check for missing values
print(nvidia_data.isnull().sum())

# Plotting
plt.figure(figsize=(12, 6))

# Plotting closing price over time
plt.subplot(2, 1, 1)
plt.plot(nvidia_data['Date'], nvidia_data['Close'], color='blue')
plt.title('NVIDIA Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')

# Plotting volume over time
plt.subplot(2, 1, 2)
plt.plot(nvidia_data['Date'], nvidia_data['Volume'], color='green')
plt.title('NVIDIA Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.tight_layout()
plt.show()
