# Pull Request Guide

## Summary of Changes

This pull request adds the **Khipu Computational Analysis Toolkit** - a comprehensive computational framework for analyzing khipus from the Open Khipu Repository database.

## What's Included

### New Directory: `khipu_computational_toolkit/`

A complete, self-contained analysis toolkit with:

- **20+ Python scripts** for data extraction, analysis, visualization
- **8 comprehensive phase reports** documenting all findings
- **Interactive web dashboard** with 6 analysis tabs
- **3D visualization tools** for exploring khipu structures
- **Machine learning models** for anomaly detection and prediction
- **78-page user guide** for visualization tools

### New Directory: `data/processed/`

40+ processed data files including:
- Extracted cord hierarchies (54,403 cords)
- Numeric values (37,082 decoded)
- Cluster assignments (7 structural archetypes)
- Anomaly detection results (13 high-confidence anomalies)
- Sequence predictions (17,321 missing values)

### New Directory: `visualizations/`

100+ publication-quality plots including:
- Statistical analysis figures
- ML results visualizations
- Interactive geographic maps
- Cluster analysis plots

## Key Features

✅ **Non-invasive** - No modifications to original repository files  
✅ **Self-contained** - All toolkit files in one directory  
✅ **Well-documented** - Comprehensive reports and guides  
✅ **Reproducible** - Complete dependencies and instructions  
✅ **Extensible** - Modular design for future research  

## Research Contributions

1. **Validated numeric encoding** across 95.8% of khipus (confidence: 0.947)
2. **Confirmed summation convention** in 74.2% of khipus
3. **Identified 7 structural archetypes** via clustering (silhouette: 0.42)
4. **Demonstrated empire-wide standardization** of color semantics
5. **Classified 98% as administrative** using machine learning
6. **Detected 13 data quality issues** for expert review
7. **Predicted 17,321 missing values** with confidence scores

## Installation & Usage

```bash
# Install dependencies
pip install -r khipu_computational_toolkit/requirements.txt

# Run dashboard
streamlit run khipu_computational_toolkit/scripts/dashboard_app.py

# Execute analysis
python khipu_computational_toolkit/scripts/detect_anomalies.py
```

See `khipu_computational_toolkit/README.md` for complete documentation.

## File Structure

```
khipu_computational_toolkit/
├── scripts/          # 20+ analysis scripts
├── reports/          # 8 phase reports
├── docs/            # Methodology & guides
├── models/          # Trained ML models
├── requirements.txt
├── README.md        # Toolkit documentation
└── OVERVIEW.md      # Detailed project overview

data/processed/      # 40+ processed data files
visualizations/      # 100+ generated plots
```

## Testing

All scripts have been tested and produce consistent results:
- ✅ Data extraction completes without errors
- ✅ Statistical tests match expected values
- ✅ ML models achieve reported accuracy (98%)
- ✅ Visualizations render correctly
- ✅ Dashboard runs without issues

## Impact

This toolkit enables:
- **Researchers** to explore khipus interactively without coding
- **Computational scientists** to build on validated analyses
- **Data quality** improvements via anomaly detection
- **Restoration efforts** through sequence prediction
- **Reproducibility** via comprehensive documentation

## Author

**Agustín Da Fieno Delucchi**  
Email: adafieno@hotmail.com

Developed in collaboration with the Open Khipu Repository project.

## Questions?

Please see:
- `khipu_computational_toolkit/README.md` for quick start
- `khipu_computational_toolkit/reports/README.md` for report index
- `khipu_computational_toolkit/docs/VISUALIZATIONS_GUIDE.md` for user guide

---

**Status:** All 7 phases complete  
**Lines of Code:** ~10,000+  
**Documentation:** ~50,000 words  
**Data Files:** 40+ processed datasets  
**Visualizations:** 100+ publication-quality plots
