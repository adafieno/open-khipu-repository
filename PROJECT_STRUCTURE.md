# Khipu Decipherment Project Structure

This document describes the folder organization for the khipu decipherment project.

## Directory Structure

```
open-khipu-repository/
├── data/                   # Data storage
│   ├── raw/               # Original data exports from khipu.db
│   ├── processed/         # Cleaned and transformed data
│   └── graphs/            # Graph representations of khipus
│
├── notebooks/             # Jupyter notebooks for exploration and analysis
│
├── src/                   # Source code
│   ├── extraction/        # Data extraction from OKR database
│   ├── graph/             # Graph construction and manipulation
│   ├── numeric/           # Numeric constraint solving
│   ├── patterns/          # Pattern discovery algorithms
│   ├── hypothesis/        # Hypothesis testing framework
│   ├── visualization/     # Visualization tools
│   └── utils/             # Shared utilities
│
├── docs/                  # Documentation
│   ├── literature/        # Literature review and notes
│   ├── methodology/       # Methodology documentation
│   └── findings/          # Analysis findings and reports
│
├── tests/                 # Unit and integration tests
│
├── reports/               # Generated reports (data quality, analysis)
│
├── models/                # Trained models (if applicable)
│
├── config/                # Configuration files
│
├── scripts/               # Utility scripts
│
├── khipu.db               # OKR SQLite database (ground truth)
├── contributors           # List of OKR contributors
├── LICENSE                # MIT License
└── README.md              # Project README

```

## Usage Guidelines

### Phase 0: Reconnaissance
- Database exploration scripts → `notebooks/`
- Data quality reports → `reports/`
- Initial documentation → `docs/methodology/`

### Phase 1: Infrastructure
- Data extraction → `src/extraction/`
- Graph conversion → `src/graph/`
- Visualization → `src/visualization/`

### Phase 2: Numeric Layer
- Constraint rules → `src/numeric/`
- Validated data → `data/processed/`

### Phase 3: Pattern Discovery
- Discovery algorithms → `src/patterns/`
- Pattern library → `data/processed/`

### Phase 4: Hypothesis Testing
- Testing framework → `src/hypothesis/`
- Results → `docs/findings/`
