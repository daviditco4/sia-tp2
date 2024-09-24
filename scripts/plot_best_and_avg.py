import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Construct the relative path to the CSV file
csv_path = 'D:/siatp2v2/sia-tp2/outputs/best_array_timeout.csv'

# Step 1: Read the CSV file
df = pd.read_csv(csv_path)

# Remove the "Generation" prefix and keep only the number
df.columns = [col.replace('Generation', '') for col in df.columns]

# Step 2: Define the chunk size (25 rows in this case)
chunk_size = 25

legend_labels = ["Timeout 10", "Timeout 50", "Timeout 120", "Timeout 1800"] 

# Step 3: Iterate through the dataframe in chunks of 25 rows
# Initialize a figure for plotting
plt.figure(figsize=(10, 6))

# Loop through the data in chunks
for i, label in zip(range(0, len(df), chunk_size), legend_labels):
    chunk = df.iloc[i:i + chunk_size]
    
    # Step 4: Calculate the mean and standard deviation for the chunk
    chunk_mean = chunk.mean()
    chunk_std = chunk.std()
    
    # Step 5: Plot the mean with error bars representing the standard deviation
    plt.errorbar(x=chunk.columns, y=chunk_mean, yerr=chunk_std, label=label)
    
# Step 6: Customize the plot
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Best Fitness per Generation for Timeout')
plt.xticks(np.arange(0, len(df.columns), 10), labels=df.columns[::10])
plt.legend(loc='lower right')
plt.grid(False)

# Step 8: Save the plot as an image
plt.savefig('output_graph_best_timeout.png', format='png', dpi=450)  # Save as PNG with 300 dpi

# Step 7: Show the plot
plt.show()
