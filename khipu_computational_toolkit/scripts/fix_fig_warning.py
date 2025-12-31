"""Final fix for fig variable linter warning."""
import json

with open('notebooks/01_cluster_explorer.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the filter_data function cell
for cell in nb['cells']:
    if 'source' in cell and any('def filter_data' in line for line in cell['source']):
        source = cell['source']
        new_source = []
        
        for i, line in enumerate(source):
            new_source.append(line)
            # After plt.subplots line, add a line that uses fig
            if 'fig, (ax1, ax2) = plt.subplots' in line:
                # Add explicit use of fig to satisfy linter
                new_source.append('    fig.suptitle(f"Filtered Khipus Analysis ({filter_pct:.1f}% of dataset)", fontsize=15, fontweight=\'bold\', y=1.02)\n')
                new_source.append('    \n')
        
        cell['source'] = new_source
        break

with open('notebooks/01_cluster_explorer.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("✓ Fixed fig variable warning")
