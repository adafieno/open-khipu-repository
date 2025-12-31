# Quick Start Guide - Khipu Computational Toolkit

**For reviewers and users of the computational toolkit**

## Repository Structure

After the reorganization, the repository has:

```
open-khipu-repository/
├── khipu.db                        # Original OKR database (unchanged)
├── README.md                       # Original OKR documentation (unchanged)
├── LICENSE                         # Original license (unchanged)
├── contributors                    # Original contributors (unchanged)
│
├── khipu_computational_toolkit/   # ✨ NEW: All computational analysis work
│   ├── scripts/                   # 20+ Python scripts
│   ├── reports/                   # 8 comprehensive phase reports  
│   ├── docs/                      # Methodology & user guides
│   ├── models/                    # Trained ML models
│   ├── requirements.txt           # Python dependencies
│   ├── README.md                  # Toolkit documentation
│   └── OVERVIEW.md               # Detailed project overview
│
├── data/processed/                # ✨ NEW: 40+ processed data files
└── visualizations/                # ✨ NEW: 100+ generated plots
```

## Installation (3 minutes)

### Step 1: Install Python Dependencies

```bash
# From repository root
pip install -r khipu_computational_toolkit/requirements.txt
```

**What this installs:**
- Data analysis: pandas, numpy, scipy
- Machine learning: scikit-learn
- Visualization: matplotlib, seaborn, plotly
- Web apps: streamlit
- Graph analysis: networkx

**Installation time:** ~2-3 minutes

### Step 2: Verify Installation

```bash
# Check Python version
python --version  # Should be 3.11+

# Test import
python -c "import pandas, sklearn, streamlit, networkx; print('✓ All dependencies installed')"
```

## Usage Examples

### Example 1: Launch Interactive Dashboard (Recommended)

```bash
# From repository root
streamlit run khipu_computational_toolkit/scripts/dashboard_app.py
```

**What you get:**
- Opens in browser at `http://localhost:8501`
- 6 interactive tabs: Overview, Clusters, Geographic, Summation, Color, Detailed
- Real-time filtering across 612 khipus
- Export data to CSV

**Use cases:**
- Explore khipus by provenance
- Compare structural clusters
- Visualize geographic distribution
- Analyze summation patterns
- No coding required!

### Example 2: Launch 3D Viewer

```bash
# From repository root (use different port to run simultaneously with dashboard)
streamlit run khipu_computational_toolkit/scripts/interactive_3d_viewer.py --server.port 8502
```

**What you get:**
- Opens in browser at `http://localhost:8502`
- Dropdown selection of all 612 khipus
- Interactive 3D rotation with mouse
- Live statistics panel
- Elevation/azimuth controls

### Example 3: Run Anomaly Detection

```bash
# From repository root
python khipu_computational_toolkit/scripts/detect_anomalies.py
```

**What it does:**
- Analyzes all 612 khipus with 3 methods (Isolation Forest, Statistical, Topology)
- Identifies 13 high-confidence anomalies
- Saves 4 output files to `data/processed/`:
  - `anomaly_detection_results.csv`
  - `high_confidence_anomalies.csv`
  - `anomaly_detection_detailed.csv`
  - `anomaly_detection_summary.json`

**Runtime:** ~3 minutes

### Example 4: Predict Missing Values

```bash
# From repository root
python khipu_computational_toolkit/scripts/predict_missing_values.py
```

**What it does:**
- Predicts 17,321 missing cord values using 3 approaches
- Constraint-based (summation inference): 1,295 predictions
- Sibling patterns (median): 773 predictions
- Random Forest ML: 15,253 predictions
- Saves 4 output files with confidence scores

**Runtime:** ~4 minutes

### Example 5: Generate ML Visualizations

```bash
# From repository root
python khipu_computational_toolkit/scripts/visualize_ml_results.py
```

**What it does:**
- Creates 5 publication-quality plots (300 DPI)
- Anomaly overview, high-confidence details, prediction results, function classification
- Saves to `visualizations/ml_results/`
- Also generates text summary report

**Runtime:** ~1 minute

## Working with Processed Data

All processed data is in `data/processed/` and ready to use:

### Load in Python

```python
import pandas as pd

# Load cluster assignments
clusters = pd.read_csv("data/processed/cluster_assignments_kmeans.csv")
print(f"Found {clusters['cluster'].nunique()} clusters")

# Load anomalies
anomalies = pd.read_csv("data/processed/high_confidence_anomalies.csv")
print(f"Found {len(anomalies)} high-confidence anomalies")

# Load predictions
predictions = pd.read_csv("data/processed/cord_value_predictions.csv")
print(f"Predicted {len(predictions)} missing values")
```

### Load in R

```r
library(readr)

# Load cluster assignments
clusters <- read_csv("data/processed/cluster_assignments_kmeans.csv")
cat(sprintf("Found %d clusters\n", length(unique(clusters$cluster))))

# Load anomalies
anomalies <- read_csv("data/processed/high_confidence_anomalies.csv")
cat(sprintf("Found %d high-confidence anomalies\n", nrow(anomalies)))
```

### Open in Excel/Spreadsheet

All CSV files can be opened directly in Excel, LibreOffice, or Google Sheets:
- `data/processed/cord_numeric_values.csv` - 54,403 decoded cord values
- `data/processed/cluster_assignments_kmeans.csv` - 612 khipu clusters
- `data/processed/anomaly_detection_results.csv` - Anomaly scores for all khipus
- And 37 more processed files...

## Documentation

### For Quick Start
- **This file** - Basic usage examples
- `khipu_computational_toolkit/README.md` - Toolkit overview

### For Detailed Understanding
- `khipu_computational_toolkit/reports/README.md` - Index of all phase reports
- `khipu_computational_toolkit/reports/QUICK_START.md` - Quick reference guide
- `khipu_computational_toolkit/reports/PROJECT_PROGRESS_SUMMARY.md` - Complete summary

### For Visualization Tools
- `khipu_computational_toolkit/docs/VISUALIZATIONS_GUIDE.md` - 78-page comprehensive guide

### For Methodology
- `khipu_computational_toolkit/reports/phase0_reconnaissance_report.md` - Database analysis
- `khipu_computational_toolkit/reports/phase1_baseline_validation_report.md` - Numeric validation
- ... through phase7 (all 8 phase reports available)

## Common Tasks

### Task 1: Find All Khipus from a Provenance

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('khipu.db')
df = pd.read_sql_query("""
    SELECT KHIPU_ID, ASCHER_CORD_COUNT, PROVENANCE
    FROM khipu_main
    WHERE PROVENANCE LIKE '%Pachacamac%'
    ORDER BY ASCHER_CORD_COUNT DESC
""", conn)
print(df)
```

### Task 2: Get All Khipus in a Cluster

```python
import pandas as pd

clusters = pd.read_csv("data/processed/cluster_assignments_kmeans.csv")
cluster_3 = clusters[clusters['cluster'] == 3]
print(f"Cluster 3 has {len(cluster_3)} khipus")
print(cluster_3['khipu_id'].tolist())
```

### Task 3: Find Anomalous Khipus

```python
import pandas as pd

anomalies = pd.read_csv("data/processed/high_confidence_anomalies.csv")
print(f"High-confidence anomalies: {len(anomalies)}")
print(anomalies[['khipu_id', 'num_methods_flagged', 'isolation_forest_score']])
```

### Task 4: Export Filtered Data

```python
import pandas as pd

# Load and filter
clusters = pd.read_csv("data/processed/cluster_assignments_kmeans.csv")
large_khipus = clusters[clusters['num_nodes'] > 200]

# Export
large_khipus.to_csv("my_filtered_data.csv", index=False)
print(f"Exported {len(large_khipus)} large khipus")
```

## Troubleshooting

### Issue: "Module not found" error

**Solution:** Install dependencies
```bash
pip install -r khipu_computational_toolkit/requirements.txt
```

### Issue: "File not found" error

**Solution:** Make sure you're running from repository root
```bash
# Check current directory
pwd  # or cd on Windows

# Should show: .../open-khipu-repository
# If not, navigate to repository root first
```

### Issue: Dashboard won't start

**Solution 1:** Check if port is already in use
```bash
# Use a different port
streamlit run khipu_computational_toolkit/scripts/dashboard_app.py --server.port 8503
```

**Solution 2:** Check Streamlit installation
```bash
streamlit --version
# Should show: Streamlit, version 1.28.0+
```

### Issue: Scripts run but produce no output

**Solution:** Check that `data/processed/` directory exists
```bash
# Create if missing
mkdir -p data/processed
mkdir -p visualizations
```

## Support

**Questions about the toolkit?**  
Contact: Agustín Da Fieno Delucchi (adafieno@hotmail.com)

**Questions about the original data?**  
Contact: Open Khipu Repository team (okr-team@googlegroups.com)

**Bug reports or feature requests?**  
Open an issue on GitHub

---

**Last Updated:** December 31, 2025  
**Toolkit Version:** 1.0.0  
**Tested on:** Python 3.11, Windows/Linux/macOS
