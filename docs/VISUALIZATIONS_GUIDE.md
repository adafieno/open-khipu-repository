# Advanced Visualizations Guide

This guide explains how to use the advanced visualization tools created for the Khipu Analysis project.

## 🌐 Interactive Web Dashboard

**File:** `scripts/dashboard_app.py`

A comprehensive Streamlit web application for exploring khipu data with real-time filtering and interactive visualizations.

### Features:
- **Real-time Filtering:** Select clusters, provenances, size ranges, and summation patterns
- **Multi-tab Interface:**
  - **Overview:** PCA scatter, size vs depth, cluster distribution
  - **Geographic:** Summation rates by provenance, structural features, enrichment heatmap
  - **Clusters:** Detailed cluster analysis with feature distributions
  - **Features:** Correlation analysis and feature relationships
- **Data Export:** Download filtered data and summary statistics as CSV

### Usage:
```bash
streamlit run scripts/dashboard_app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Controls:
- Use the **sidebar** to filter data by cluster, provenance, size, and summation pattern
- Switch between **tabs** to explore different aspects of the data
- **Hover** over plot elements for detailed information
- Use **export buttons** at the bottom to download filtered data

---

## 📐 3D Khipu Structure Viewer

**File:** `scripts/visualize_3d_khipu.py`

Creates interactive 3D visualizations of individual khipu hierarchical structures.

### Features:
- Hierarchical layout showing parent-child cord relationships
- Interactive rotation and zoom (in matplotlib window)
- Three color modes:
  - `value`: Color by numeric value (gradient)
  - `level`: Color by hierarchy level
  - `color`: Uniform coloring
- Multiple viewing angles
- Summation flow visualization (highlights summation relationships in red)

### Usage:

**Basic visualization:**
```bash
python scripts/visualize_3d_khipu.py --khipu-id 1
```

**With specific color mode:**
```bash
python scripts/visualize_3d_khipu.py --khipu-id 1 --color-mode level
```

**Save to file:**
```bash
python scripts/visualize_3d_khipu.py --khipu-id 1 --output outputs/khipu_1.png
```

**Multi-view (4 angles):**
```bash
python scripts/visualize_3d_khipu.py --khipu-id 1 --multi-view
```

**Summation flow (highlight summation edges):**
```bash
python scripts/visualize_3d_khipu.py --khipu-id 1 --summation-flow
```

### Examples:

Try these interesting khipus:
- Khipu 1: Small, simple structure (good starting example)
- Khipu 50: Medium complexity with summation patterns
- Khipu 100: Large structure with multiple levels
- Khipu 200: Complex branching hierarchy

---

## 🗺️ Geographic Heatmap

**File:** `scripts/visualize_geographic_heatmap.py`

Creates interactive maps showing geographic distribution of khipu patterns across archaeological sites in Peru.

### Features:
- **Heatmap overlay:** Intensity based on summation rate
- **Interactive markers:** Click for detailed statistics per provenance
- **Color-coded bubbles:**
  - 🔴 Red: >40% summation rate
  - 🟠 Orange: 25-40% summation rate
  - 🔵 Blue: <25% summation rate
- **Bubble size:** Proportional to number of khipus
- **Two maps:**
  1. Summation heatmap (pattern intensity)
  2. Cluster distribution (dominant archetype per region)

### Usage:
```bash
python scripts/visualize_geographic_heatmap.py
```

**Outputs:**
- `outputs/visualizations/geographic_heatmap.html` - Summation rate heatmap
- `outputs/visualizations/geographic_heatmap_statistics.csv` - Aggregated statistics
- `outputs/visualizations/cluster_geographic_map.html` - Cluster distribution map

### Viewing:
Open the `.html` files in any web browser. The maps are fully interactive:
- **Zoom:** Mouse wheel or +/- buttons
- **Pan:** Click and drag
- **Info:** Click markers for detailed statistics

---

## 🎨 Visualization Workflow

### Recommended Exploration Sequence:

1. **Start with the Dashboard** to get an overview:
   ```bash
   streamlit run scripts/dashboard_app.py
   ```
   - Filter to specific clusters or provenances of interest
   - Export filtered data for focused analysis

2. **Explore Geographic Patterns**:
   ```bash
   python scripts/visualize_geographic_heatmap.py
   ```
   - Identify regional variations in summation patterns
   - Note provenances with high summation rates

3. **Deep Dive into Individual Khipus**:
   ```bash
   python scripts/visualize_3d_khipu.py --khipu-id <ID> --multi-view
   python scripts/visualize_3d_khipu.py --khipu-id <ID> --summation-flow
   ```
   - Choose khipus from interesting clusters/provenances
   - Examine hierarchical structure in 3D
   - Visualize summation relationships

4. **Use Interactive Notebooks** for hypothesis testing:
   - Open `notebooks/03_khipu_detail_viewer.ipynb` for comprehensive khipu analysis
   - Open `notebooks/04_hypothesis_dashboard.ipynb` for custom statistical tests

---

## 📊 Data Sources

All visualizations use processed data from:
- `data/processed/cord_hierarchy.csv` - Hierarchical structure (45,204 cords)
- `data/processed/cord_numeric_values.csv` - Numeric values
- `data/processed/cluster_assignments_kmeans.csv` - 7 archetypes (612 khipus)
- `data/processed/graph_structural_features.csv` - Structural metrics
- `data/processed/summation_test_results.csv` - Summation testing (619 total)
- `data/processed/cluster_pca_coordinates.csv` - PCA projections

---

## 🛠️ Technical Requirements

### Python Packages:
- `streamlit` - Web dashboard framework
- `plotly` - Interactive plotting
- `folium` - Interactive maps
- `matplotlib` - 3D visualization
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `networkx` - Graph analysis

All packages are already installed in your environment.

### System Requirements:
- **RAM:** 2GB minimum (4GB recommended for dashboard)
- **Browser:** Modern browser (Chrome, Firefox, Edge) for HTML maps
- **Display:** 1920×1080 recommended for dashboard

---

## 🎯 Use Cases

### Archaeological Research:
- Compare khipu structures across regions
- Identify regional traditions and variations
- Discover outliers and unique specimens

### Data Quality:
- Visual inspection of complex hierarchies
- Verification of summation patterns
- Identification of potential transcription errors

### Publications:
- High-resolution 3D visualizations (300 DPI)
- Interactive supplements (HTML maps)
- Summary statistics for tables

### Teaching:
- Interactive demonstrations of khipu structure
- Real-time exploration in classroom settings
- Hands-on data analysis exercises

---

## 📝 Notes

- **Dashboard:** First launch may take 10-15 seconds to load data
- **3D Viewer:** Matplotlib 3D is interactive - click and drag to rotate
- **Maps:** Require internet connection for base map tiles
- **Export:** All visualizations can be saved as high-resolution images (PNG, 300 DPI)

---

## 🐛 Troubleshooting

**Dashboard won't start:**
- Ensure port 8501 is available: `netstat -ano | findstr :8501`
- Try alternate port: `streamlit run scripts/dashboard_app.py --server.port 8502`

**3D viewer shows empty plot:**
- Verify khipu ID exists: Check `data/processed/cord_hierarchy.csv`
- Ensure khipu has cord data (not one of the 7 filtered empty records)

**Maps show no data:**
- Check that geographic heatmap script completed successfully
- Verify provenance names match `PROVENANCE_LOCATIONS` dictionary
- Unknown provenances are filtered out by design

**Memory issues:**
- Close other applications
- Filter to smaller subsets in dashboard
- Process khipus individually in 3D viewer

---

## 🚀 Next Steps

After exploring these visualizations, consider:
1. **ML Extensions** (Task 7):
   - Function prediction (accounting vs narrative)
   - Anomaly detection (outliers and errors)
   - Sequence prediction for restoration

2. **Custom Analysis:**
   - Modify dashboard to add new visualizations
   - Create animated sequences in 3D viewer
   - Add temporal dimension if dating data available

3. **Publication:**
   - Export high-resolution figures
   - Create interactive supplements
   - Generate summary tables

---

*For questions or issues, refer to the main project documentation in `README_FORK.md`*
