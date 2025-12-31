"""
Fix linter issues in Jupyter notebooks by directly editing JSON.
"""

import json

def fix_notebook_01():
    """Fix linter issues in notebook 01."""
    with open('notebooks/01_cluster_explorer.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Find and fix cells by their content
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        
        source = cell['source']
        if isinstance(source, list):
            new_source = []
            for line in source:
                # Fix unused parts variable in violin plot
                if 'parts = ax.violinplot' in line or '_ = ax.violinplot' in line:
                    new_source.append(line.replace('parts = ax.violinplot', '_ = ax.violinplot'))
                # Fix f-strings without placeholders
                elif 'print(f"\\nStructure:")' in line:
                    new_source.append(line.replace('print(f"\\nStructure:")', 'print("\\nStructure:")'))
                elif 'print(f"\\nSummation:")' in line:
                    new_source.append(line.replace('print(f"\\nSummation:")', 'print("\\nSummation:")'))
                elif 'print(f"\\nPCA Coordinates:")' in line:
                    new_source.append(line.replace('print(f"\\nPCA Coordinates:")', 'print("\\nPCA Coordinates:")'))
                else:
                    new_source.append(line)
            cell['source'] = new_source
    
    with open('notebooks/01_cluster_explorer.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("✓ Fixed notebooks/01_cluster_explorer.ipynb")

def fix_notebook_02():
    """Fix linter issues in notebook 02."""
    with open('notebooks/02_geographic_patterns.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Find and fix cells by their content
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        
        source = cell['source']
        if isinstance(source, list):
            new_source = []
            for line in source:
                # Fix f-string without placeholder
                if 'print(f"\\nTop 10 provenances:")' in line:
                    new_source.append(line.replace('print(f"\\nTop 10 provenances:")', 'print("\\nTop 10 provenances:")'))
                # Fix unused parts variable
                elif 'parts = ax.violinplot' in line or '_ = ax.violinplot' in line:
                    new_source.append(line.replace('parts = ax.violinplot', '_ = ax.violinplot'))
                else:
                    new_source.append(line)
            cell['source'] = new_source
    
    with open('notebooks/02_geographic_patterns.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("✓ Fixed notebooks/02_geographic_patterns.ipynb")

def fix_notebook_03():
    """Fix linter issues in notebook 03."""
    with open('notebooks/03_khipu_detail_viewer.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Find and fix cells by their content
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        
        source = cell['source']
        if isinstance(source, list):
            new_source = []
            for line in source:
                # Remove unused HTML import
                if 'from IPython.display import display, HTML' in line:
                    new_source.append('from IPython.display import display\n')
                else:
                    new_source.append(line)
            cell['source'] = new_source
    
    with open('notebooks/03_khipu_detail_viewer.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("✓ Fixed notebooks/03_khipu_detail_viewer.ipynb")

def fix_notebook_04():
    """Fix linter issues in notebook 04."""
    with open('notebooks/04_hypothesis_dashboard.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Find and fix cells by their content
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        
        source = cell['source']
        if isinstance(source, list):
            new_source = []
            for line in source:
                # Remove unused HTML import
                if 'from IPython.display import display, HTML' in line:
                    new_source.append('from IPython.display import display\n')
                else:
                    new_source.append(line)
            cell['source'] = new_source
    
    with open('notebooks/04_hypothesis_dashboard.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("✓ Fixed notebooks/04_hypothesis_dashboard.ipynb")

if __name__ == "__main__":
    print("Fixing notebook linter issues...")
    fix_notebook_01()
    fix_notebook_02()
    fix_notebook_03()
    fix_notebook_04()
    print("\n✅ All notebooks fixed!")
