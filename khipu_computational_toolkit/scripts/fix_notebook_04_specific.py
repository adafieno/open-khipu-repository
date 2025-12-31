"""
Fix remaining linter issues in notebook 04.
"""

import json

with open('notebooks/04_hypothesis_dashboard.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    
    source = cell['source']
    if isinstance(source, list):
        new_source = []
        for line in source:
            # Remove unused chi2_contingency import (not actually used in any cell)
            if 'from scipy.stats import mannwhitneyu, chi2_contingency, pearsonr' in line:
                new_source.append('from scipy.stats import mannwhitneyu, pearsonr\n')
            # Fix f-strings without placeholders
            elif line.strip() in ['print(f"Testing summation hypothesis with tolerance = ±{tolerance}")', 
                                   'print(f"="*80)']:
                # Keep these as they have placeholders or use expressions
                new_source.append(line)
            elif 'print(f"\\n' in line and '{' not in line:
                # Fix f-strings without placeholders
                new_source.append(line.replace('print(f"', 'print("'))
            # Fix unused fig variable - add title
            elif 'fig, ax = plt.subplots(1, 1,' in line:
                new_source.append(line)
            # Fix unused parts variable
            elif 'parts = ax.violinplot' in line:
                new_source.append(line.replace('parts = ax.violinplot', '_ = ax.violinplot'))
            # Fix unused count variable
            elif line.strip().startswith('count = len('):
                # This is actually used in the print statement, so keep it
                new_source.append(line)
            else:
                new_source.append(line)
        cell['source'] = new_source

with open('notebooks/04_hypothesis_dashboard.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("✓ Fixed notebooks/04_hypothesis_dashboard.ipynb")
