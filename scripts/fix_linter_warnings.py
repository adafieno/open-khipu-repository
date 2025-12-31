"""Fix linter false positives in notebooks."""
import json

def fix_notebook_1():
    """Fix notebook 1: stat is unused in compare_clusters."""
    with open('notebooks/01_cluster_explorer.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Find the compare_clusters cell and replace unused stat with _
    for cell in nb['cells']:
        if 'source' in cell and any('def compare_clusters' in line for line in cell['source']):
            source = cell['source']
            new_source = []
            for line in source:
                # stat is NOT used in compare_clusters, only pval is printed
                if 'stat, pval = mannwhitneyu' in line:
                    new_source.append(line.replace('stat, pval', '_, pval'))
                else:
                    new_source.append(line)
            cell['source'] = new_source
            break
    
    with open('notebooks/01_cluster_explorer.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("✓ Fixed notebook 1")

def fix_notebook_2():
    """Fix notebook 2: stat IS used, so keep it; revert the bad change."""
    with open('notebooks/02_geographic_patterns.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Revert the bad change: stat is actually printed, so it should NOT be _
    for cell in nb['cells']:
        if 'source' in cell:
            source = cell['source']
            new_source = []
            modified = False
            
            for line in source:
                # Revert: _, pval = kruskal back to stat, pval = kruskal
                if '_, pval = kruskal' in line:
                    new_source.append(line.replace('_, pval', 'stat, pval'))
                    modified = True
                else:
                    new_source.append(line)
            
            if modified:
                cell['source'] = new_source
    
    with open('notebooks/02_geographic_patterns.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("✓ Fixed notebook 2")

if __name__ == '__main__':
    fix_notebook_1()
    fix_notebook_2()
    print("\n✓ All linter warnings resolved")
