# Pull Request Strategy

## Database Handling

### Problem
The OKR database (`data/khipu.db`) contains the source data and should **not** be modified or included in pull requests.

### Solution Implemented

✅ **`.gitignore` updated** to exclude:
- `khipu.db` (root level)
- `data/khipu.db` (proper location)
- `*.pyc`, `__pycache__/` (Python cache)
- `.venv/` (virtual environment)
- `*.pkl` (saved models)

✅ **Scripts work with database at `data/khipu.db`**:
- All scripts expect database at repository root: `../data/khipu.db`
- Scripts should be run from repository root
- No database modifications are committed

✅ **Only processed outputs are included**:
- `khipu_computational_toolkit/data/processed/` - 40+ CSV files
- `khipu_computational_toolkit/data/graphs/` - Pickled NetworkX graphs
- `khipu_computational_toolkit/visualizations/` - PNG plots

## Pull Request Checklist

### What to Include

```bash
git add khipu_computational_toolkit/
```

This includes:
- ✅ `scripts/` - All analysis scripts
- ✅ `reports/` - All phase reports
- ✅ `docs/` - Documentation and guides
- ✅ `models/` - Trained ML models
- ✅ `data/processed/` - Processed CSV files
- ✅ `data/graphs/` - Graph structures
- ✅ `visualizations/` - Generated plots
- ✅ `notebooks/` - Jupyter notebooks
- ✅ `src/` - Python modules
- ✅ `README.md`, `OVERVIEW.md`, `requirements.txt`

### What to Exclude (Automatically via `.gitignore`)

- ❌ `data/khipu.db` - Original database (not modified)
- ❌ `.venv/` - Virtual environment
- ❌ `*.pyc`, `__pycache__/` - Python cache
- ❌ `*.pkl` files at root - Model checkpoints
- ❌ `.DS_Store` - Mac system files

### Commit Command

```bash
git add khipu_computational_toolkit/
git add .gitignore

git commit -m "Add Khipu Computational Analysis Toolkit

Complete computational framework with:
- 20+ Python scripts for data extraction and ML
- 8 comprehensive phase reports (0-7)
- Interactive dashboard and 3D visualization tools
- 40+ processed data files
- 100+ publication-quality visualizations
- Jupyter notebooks for interactive analysis
- Complete documentation and user guides

All analysis uses existing data/khipu.db without modifications.
See khipu_computational_toolkit/README.md for usage."
```

## Syncing with Upstream

### If OKR Updates Their Database

```bash
# Your work is isolated in khipu_computational_toolkit/
# Upstream changes to data/khipu.db won't conflict

# Update from upstream
git fetch upstream
git merge upstream/master

# Database updates automatically
# Your processed data remains intact
```

### If You Want to Re-run Analysis

```bash
# Your scripts always use the current data/khipu.db
# Re-run any script to update processed outputs

python khipu_computational_toolkit/scripts/detect_anomalies.py
python khipu_computational_toolkit/scripts/predict_missing_values.py
```

## Repository Structure

```
open-khipu-repository/
├── data/
│   ├── khipu.db              # ❌ NOT in PR (upstream maintains)
│   └── raw/                  # ❌ NOT in PR (upstream maintains)
│
├── khipu_computational_toolkit/  # ✅ ENTIRE FOLDER in PR
│   ├── data/
│   │   ├── processed/        # ✅ Your processed data
│   │   └── graphs/           # ✅ Your graph structures
│   ├── visualizations/       # ✅ Your plots
│   ├── scripts/              # ✅ Your analysis code
│   ├── reports/              # ✅ Your documentation
│   ├── docs/                 # ✅ Your guides
│   ├── models/               # ✅ Your ML models
│   ├── notebooks/            # ✅ Your Jupyter notebooks
│   ├── src/                  # ✅ Your Python modules
│   └── README.md             # ✅ Your toolkit guide
│
├── README.md                 # ❌ NOT modified (upstream's)
├── LICENSE                   # ❌ NOT modified (upstream's)
├── contributors              # ❌ NOT modified (upstream's)
└── .gitignore                # ✅ UPDATED (excludes database)
```

## Key Points

1. **Database is never committed** - `.gitignore` prevents this
2. **Your work is isolated** - Everything in `khipu_computational_toolkit/`
3. **No conflicts with upstream** - Original OKR files untouched
4. **Easy to sync** - Pull upstream changes without conflicts
5. **Reproducible** - Anyone can run your scripts with their `data/khipu.db`

## Testing Before PR

```bash
# Verify database is ignored
git status  # Should NOT show data/khipu.db

# Verify toolkit is staged
git add khipu_computational_toolkit/
git status  # Should show toolkit files

# Test that scripts still work
streamlit run khipu_computational_toolkit/scripts/dashboard_app.py
```

---

**Status:** ✅ Ready for Pull Request  
**Database:** ✅ Protected via .gitignore  
**Conflicts:** ✅ None expected
