# Khipu Computational Analysis Toolkit

**A comprehensive computational framework for analyzing Inka khipus from the Open Khipu Repository**

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

## Overview

This toolkit provides a complete computational analysis pipeline for studying khipu structure, numeric encoding, color semantics, and hierarchical patterns. Built on the [Open Khipu Repository](https://github.com/khipulab/open-khipu-repository) database, it includes data extraction, statistical analysis, machine learning, and interactive visualization tools.

**Key Statistics:**
- 612 khipus analyzed
- 54,403 cords decoded
- 110,151 knots processed
- 7 structural archetypes identified
- 98% administrative function confirmed
- 17,321 missing values predicted

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/khipulab/open-khipu-repository.git
cd open-khipu-repository

# Install dependencies
pip install -r khipu_computational_toolkit/requirements.txt
```

### Run the Dashboard

```bash
# Launch interactive web dashboard
streamlit run khipu_computational_toolkit/scripts/dashboard_app.py

# Launch 3D viewer (on port 8502)
streamlit run khipu_computational_toolkit/scripts/interactive_3d_viewer.py --server.port 8502
```

### Execute Analysis Pipeline

```bash
# Phase 1: Extract and validate numeric data
python khipu_computational_toolkit/scripts/validate_numeric_decoding.py

# Phase 3: Test summation patterns
python khipu_computational_toolkit/scripts/test_summation_patterns.py

# Phase 4: Cluster analysis
python khipu_computational_toolkit/scripts/cluster_khipus.py

# Phase 5: Test color hypotheses
python khipu_computational_toolkit/scripts/test_summation_hypotheses.py

# Phase 7: Anomaly detection and prediction
python khipu_computational_toolkit/scripts/detect_anomalies.py
python khipu_computational_toolkit/scripts/predict_missing_values.py
python khipu_computational_toolkit/scripts/visualize_ml_results.py
```

## Project Structure

```
khipu_computational_toolkit/
├── scripts/                    # Analysis and visualization scripts (20+ files)
│   ├── dashboard_app.py       # Interactive web dashboard (6 tabs)
│   ├── interactive_3d_viewer.py  # 3D khipu structure viewer
│   ├── detect_anomalies.py    # Multi-method anomaly detection
│   ├── predict_missing_values.py # ML-based value prediction
│   └── ...
├── reports/                    # Comprehensive phase reports
│   ├── README.md              # Reports index
│   ├── phase0_reconnaissance_report.md
│   ├── phase1_baseline_validation_report.md
│   ├── phase2_extraction_infrastructure_report.md
│   ├── phase3_summation_testing_report.md
│   ├── phase4_pattern_discovery_progress.md
│   ├── phase5_multi_model_framework_report.md
│   ├── phase6_advanced_visualizations_report.md
│   ├── phase7_ml_extensions_report.md
│   ├── PROJECT_PROGRESS_SUMMARY.md
│   └── QUICK_START.md
├── docs/                      # Methodology and guides
│   ├── VISUALIZATIONS_GUIDE.md  # 78-page user guide
│   ├── methodology/           # Research methodology docs
│   └── literature/            # Literature review
├── models/                    # Trained ML models
│   └── function_classifier.pkl  # Random Forest (98% accuracy)
├── requirements.txt           # Python dependencies
├── OVERVIEW.md               # Detailed project overview
└── README.md                 # This file
```

**Output Directories** (created at repository root):
```
data/processed/                # Extracted and processed data (40+ CSV files)
visualizations/                # Generated plots and figures
└── ml_results/               # ML analysis visualizations
```

## Features

### 🔍 Data Extraction & Validation
- Numeric value decoder (95.8% khipus have numeric data, avg confidence 0.947)
- Cord hierarchy extractor (54,403 cords)
- Knot data extractor (110,151 knots)
- Color data extraction (56,306 records)
- Graph structure builder (612 NetworkX graphs)

### 📊 Statistical Analysis
- Pendant-to-parent summation testing (74.2% exhibit summation)
- Multi-hypothesis testing framework (4 color semantics hypotheses)
- Cluster analysis (7 structural archetypes, silhouette=0.42)
- PCA dimensionality reduction (3 dominant patterns)
- Geographic correlation analysis

### 🤖 Machine Learning
- **Anomaly Detection:** 13 high-confidence anomalies (3 methods: Isolation Forest, Statistical, Topology)
- **Sequence Prediction:** 17,321 missing values predicted (Constraint-based, Sibling patterns, Random Forest)
- **Function Classification:** 98% accounting vs 2% narrative (Random Forest, 98% accuracy)
- **Feature Importance:** numeric_coverage (39.9%), color_diversity (26.8%), branching (17.9%)

### 📈 Interactive Visualizations
- **Web Dashboard:** 6 tabs with real-time filtering (overview, clusters, geographic, summation, color, detailed)
- **3D Viewer:** Dropdown selection of all 612 khipus with rotation controls
- **Geographic Map:** Andes region visualization with 15+ archaeological sites (400+ khipus plotted)
- **ML Results:** 5 publication-quality plots (anomaly overview, predictions, function classification)

## Key Findings

1. **Numeric Encoding Validated:** 95.8% of khipus have decodable numeric data with high confidence (0.947)

2. **Summation Convention Widespread:** 74.2% of khipus exhibit pendant-to-parent summation relationships

3. **White Cord Hypothesis:** White cords improve summation detection by +10.7 percentage points (p<0.001)

4. **Administrative Function Dominates:** 98% of khipus are accounting records (validated across multiple analyses)

5. **Empire-Wide Standardization:** Color semantics uniform across all provenances (p=1.00)

6. **Color as Function Marker:** Accounting khipus use 57% more colors than narrative (p<0.001, Cohen's d=0.68)

7. **Structural Archetypes:** 7 distinct clusters represent different recording styles
   - Cluster 3: Large, complex khipus (mean 235 cords)
   - Cluster 5: Anomalous structures (66.7% flagged, data quality concern)

8. **Data Quality Targets:** 13 high-confidence anomalies identified for expert review
   - Khipus 1000020 and 1000279 flagged by all 3 detection methods

9. **Restoration Potential:** 17,321 missing cord values predicted with confidence scores
   - 1,295 high-confidence (constraint-based)
   - 773 medium-confidence (sibling patterns)

10. **Multi-Level Hierarchies:** 34.7% of high-match khipus show recursive summation patterns

## Methodology

The toolkit implements a 7-phase computational pipeline:

**Phase 0: Reconnaissance** - Database analysis and data model documentation (24 tables, 280,000+ records)

**Phase 1: Baseline Validation** - Numeric decoding and arithmetic validation (619 khipus)

**Phase 2: Extraction Infrastructure** - Data extraction tools for cords, knots, colors, graphs

**Phase 3: Summation Testing** - Statistical testing of pendant-to-parent summation hypothesis

**Phase 4: Pattern Discovery** - Graph-based clustering and PCA analysis (7 archetypes)

**Phase 5: Multi-Model Framework** - Hypothesis testing for color semantics (4 hypotheses, 98% function classification)

**Phase 6: Advanced Visualizations** - Interactive web tools (dashboard, 3D viewer, geographic map)

**Phase 7: ML Extensions** - Anomaly detection, sequence prediction, validation

See [reports/](reports/) for detailed phase reports.

## Requirements

- Python 3.11+
- pandas, numpy, scipy
- scikit-learn (ML models)
- matplotlib, seaborn, plotly (visualization)
- networkx (graph analysis)
- streamlit (web dashboard)
- sqlite3 (database access)

Full dependencies in [requirements.txt](requirements.txt)

## Documentation

- **[OVERVIEW.md](OVERVIEW.md)** - Detailed project overview with full context
- **[reports/README.md](reports/README.md)** - Index of all phase reports
- **[reports/PROJECT_PROGRESS_SUMMARY.md](reports/PROJECT_PROGRESS_SUMMARY.md)** - Complete project summary
- **[reports/QUICK_START.md](reports/QUICK_START.md)** - Quick start guide
- **[docs/VISUALIZATIONS_GUIDE.md](docs/VISUALIZATIONS_GUIDE.md)** - Comprehensive visualization user guide (78 pages)

## Usage Examples

### Example 1: Query Database and Extract Data

```python
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('../khipu.db')

# Query khipu metadata
df = pd.read_sql_query("""
    SELECT KHIPU_ID, PROVENANCE, ASCHER_CORD_COUNT 
    FROM khipu_main 
    WHERE PROVENANCE IS NOT NULL
    ORDER BY ASCHER_CORD_COUNT DESC
    LIMIT 10
""", conn)

print(df)
conn.close()
```

### Example 2: Load Processed Data

```python
import pandas as pd

# Load cluster assignments
clusters = pd.read_csv('../data/processed/cluster_assignments_kmeans.csv')

# Load anomaly detection results
anomalies = pd.read_csv('../data/processed/anomaly_detection_results.csv')

# Load sequence predictions
predictions = pd.read_csv('../data/processed/cord_value_predictions.csv')

# Filter high-confidence anomalies
high_conf = anomalies[anomalies['high_confidence_anomaly'] == 1]
print(f"Found {len(high_conf)} high-confidence anomalies")
```

### Example 3: Visualize Khipu Structure

```python
import networkx as nx
import matplotlib.pyplot as plt
import sqlite3

# Load cord hierarchy
conn = sqlite3.connect('../khipu.db')
hierarchy = pd.read_sql_query("""
    SELECT CORD_ID, PENDANT_FROM, CORD_LEVEL
    FROM cord_hierarchy
    WHERE KHIPU_ID = 1000279
""", conn)

# Build graph
G = nx.DiGraph()
for _, row in hierarchy.iterrows():
    G.add_node(row['CORD_ID'], level=row['CORD_LEVEL'])
    if pd.notna(row['PENDANT_FROM']):
        G.add_edge(row['PENDANT_FROM'], row['CORD_ID'])

# Visualize
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=500, font_size=8, arrows=True)
plt.title("Khipu 1000279 Hierarchy")
plt.show()
```

## Contributing

This toolkit was developed as an extension to the Open Khipu Repository. For questions or contributions:

**Toolkit Author:** Agustín Da Fieno Delucchi  
**Email:** adafieno@hotmail.com

**Original Repository:** [Open Khipu Repository](https://github.com/khipulab/open-khipu-repository)  
**Contact:** okr-team@googlegroups.com

## Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{dafieno2025khipu,
  author = {Da Fieno Delucchi, Agustín},
  title = {Khipu Computational Analysis Toolkit},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/khipulab/open-khipu-repository}
}
```

And cite the underlying data:

```bibtex
@dataset{open_khipu_repository,
  author = {Clindaniel, Jon and Brezine, Carrie and Medrano, Manuel},
  title = {The Open Khipu Repository},
  year = {2021},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.5037551},
  url = {https://doi.org/10.5281/zenodo.5037551}
}
```

## License

This toolkit is provided under the MIT License. See [LICENSE](../LICENSE) for details.

The underlying khipu data is provided by the Open Khipu Repository under their terms of use.

## Acknowledgments

- **Open Khipu Repository Advisory Board:** Carrie Brezine, Jon Clindaniel, Iván Ghezzi, Sabine Hyland, Manuel Medrano
- **Data Contributors:** All scholars who have recorded khipu data (see [contributors](../contributors))
- **Research:** Built on foundational work by Gary Urton, Carrie Brezine, Manuel Medrano, Jon Clindaniel, and many others

---

**Last Updated:** December 31, 2025  
**Status:** All Phases (0-7) Complete  
**Version:** 1.0.0
