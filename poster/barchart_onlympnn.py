import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("barchart.xlsx")
df.columns = df.columns.str.strip()  # Clean up column names

# Extract version type
df['group'] = df['version'].str.extract(r'(v\d+)')

# Calculate percentage
df['percent_hits'] = (df['#hits'] / df['Total']) * 100

# Group by version (if multiple entries per version exist)
pivot = df.groupby('group')['percent_hits'].mean()

# Plot
plt.figure(figsize=(10, 6))

# Single bars, all in steelblue
plt.bar(pivot.index, pivot.values, color='steelblue', edgecolor='k', label='Redesign entire sequence')

# Labels and styling
plt.xlabel('ClpS Diffusion Version', fontsize=20)
plt.ylabel('% Hits', fontsize=20)
plt.title('% Hits by ClpS Diff. Version', fontsize=24)
plt.xticks(rotation=45, fontsize=18)
plt.yticks(fontsize=14)
plt.ylim(0, 20)

# Optional legend if you still want it
# plt.legend(title='Design Strategy', title_fontsize=14, fontsize=12)

plt.tight_layout()
plt.savefig("single_method_hits_by_version.pdf", format='pdf')
plt.show()