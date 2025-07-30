import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("barchart.xlsx")  # Replace with actual filename

# Extract version type and group
df['group'] = df['version'].str.extract(r'(v\d+)')
df['method'] = df['version'].str.extract(r'_(mpnn|dist)')

# Calculate percentage
df['percent_hits'] = (df['#hits'] / df['Total']) * 100

# Pivot data to have one row per group (v1, v2, etc.), with mpnn and dist as columns
pivot = df.pivot(index='group', columns='method', values='percent_hits').fillna(0)

# Plot
plt.figure(figsize=(10, 6))

# Plot stacked bars with custom legend labels
bar1 = plt.bar(
    pivot.index,
    pivot['mpnn'],
    label='Redesign entire sequence',
    color='steelblue',
    edgecolor='k'
)
bar2 = plt.bar(
    pivot.index,
    pivot['dist'],
    bottom=pivot['mpnn'],
    label='Redesign non-motif residues',
    color='lightblue',
    edgecolor='k'
)

# Labels and styling
plt.xlabel('ClpS Diffusion Version', fontsize = 20)
plt.ylabel('% Hits', fontsize = 20)
plt.title('% Hits by ClpS Diff. Version Design Method', fontsize=24)
plt.ylim(0, 20)
plt.legend(title='Design Method', title_fontsize=20, fontsize=18)
plt.xticks(rotation=45, fontsize=18)

plt.tight_layout()
plt.savefig("stacked_hits_by_version.pdf", format='pdf')
plt.show()