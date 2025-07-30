import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("all_1.v_1_ClpS.xlsx")
df.columns = df.columns.str.strip()
print("Columns:", df.columns.tolist())

# Determine method type from 'version' column
df['method'] = df['version'].apply(lambda x: 'dist' if 'dist' in x.lower() else 'mpnn')

# Assign color based on method
color_map = {'dist': 'lightblue', 'mpnn': 'steelblue'}
df['color'] = df['method'].map(color_map)

# Plot setup
plt.figure(figsize=(8, 6))

label_map = {
    'dist': 'Redesign non-motif residues',
    'mpnn': 'Redesign entire sequence'
}

# Scatter points by method
for method in ['dist', 'mpnn']:
    subset = df[df['method'] == method]
    plt.scatter(
        subset['ipTM'], subset['plDDT A'],
        color=color_map[method],
        label=label_map[method],
        edgecolor='k'
    )

# Axes and title
plt.xlabel('YAA + Binder ipTM', fontsize = 24)
plt.ylabel('plDDT Binder', fontsize = 24)
plt.title('AF3 Confidence Initial Run', fontsize=28)

#Add rectangles
plt.gca().add_patch(
    plt.Rectangle(
        (0.7, 80), 
        width=1 - 0.7, 
        height=100 - 80, 
        linewidth=2, 
        edgecolor='gold', 
        facecolor='none'
    )
)
plt.gca().add_patch(
    plt.Rectangle(
        (0.8, 90), 
        width=1 - 0.8, 
        height=100 - 90, 
        linewidth=2, 
        edgecolor='red', 
        facecolor='none'
    )
)

plt.grid(True)
plt.ylim(50, 100)
plt.xlim(0, 1)
# Add legend
plt.legend(title='Method',fontsize=13, title_fontsize = 16, loc='lower right')

plt.tight_layout()
plt.savefig("all_v1.pdf", format='pdf')
plt.show()