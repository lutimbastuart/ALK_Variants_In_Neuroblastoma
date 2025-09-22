import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re

# Function to parse interaction_summary.txt
def parse_interaction_file(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Match lines starting with "Contact:"
            match = re.match(r'Contact:\s*(\d+\s+\w+)\s+(\d+\s+\w+),\s*Frequency:\s*"([\d.]+)"', line.strip())
            if match:
                res1, res2, freq = match.groups()
                data.append({
                    'res1': res1,
                    'res2': res2,
                    'freq': float(freq)
                })
    return data

# Read and parse the input file
filename = 'interaction_summary.txt'
data = parse_interaction_file(filename)

# Create DataFrame
df = pd.DataFrame(data)

# Extract residue numbers and names
df['res1_num'] = df['res1'].str.split().str[0].astype(int)
df['res2_num'] = df['res2'].str.split().str[0].astype(int)
df['res1_name'] = df['res1'].str.split().str[1]
df['res2_name'] = df['res2'].str.split().str[1]
df['pair'] = df['res1'] + ' - ' + df['res2']

# --- Bar Plot: Top 10 Frequent Contacts ---
top_n = 20
df_top = df.nlargest(top_n, 'freq').sort_values('freq', ascending=True)

plt.figure(figsize=(10, 6))
bars = plt.barh(df_top['pair'], df_top['freq'], color=plt.cm.viridis(df_top['freq'] / df['freq'].max()))
plt.xlabel('Frequency (%)', fontsize=12)
plt.ylabel('Residue Pairs', fontsize=12)
plt.title('Top 20 Protein-Protein Hbond Interaction Frequencies', fontsize=14, pad=20)
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Add frequency labels on bars
for bar, freq in zip(bars, df_top['freq']):
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f'{freq:.2f}%', 
             va='center', ha='left', fontsize=10)

plt.tight_layout()
plt.savefig('top_interactions_barplot.png', dpi=300)
plt.close()

# --- Heatmap: All Interactions ---
# Assume residues < 1000 are from chain A, > 1000 from chain B
pivot_data = df.pivot_table(values='freq', index='res2_num', columns='res1_num', fill_value=0)
plt.figure(figsize=(12, 10))
sns.heatmap(pivot_data, cmap='YlOrRd', annot=True, fmt='.1f', cbar_kws={'label': 'Frequency (%)'})
plt.title('Residue-Residue Interaction Frequency Heatmap', fontsize=14, pad=20)
plt.xlabel('Residue Number (Chain B)', fontsize=12)
plt.ylabel('Residue Number (Chain A)', fontsize=12)
plt.tight_layout()
plt.savefig('interaction_heatmap.png', dpi=300)
plt.close()

# --- Summary Statistics ---
print(f"Total Interactions: {len(df)}")
print(f"Max Frequency: {df['freq'].max():.2f}%")
print(f"Min Frequency: {df['freq'].min():.2f}%")
print(f"Average Frequency: {df['freq'].mean():.2f}%")
