# Khipu Decipherment Research Project

**A computational research fork of the [Open Khipu Repository](https://github.com/khipulab/open-khipu-repository)**

[![Original DOI](https://zenodo.org/badge/296378423.svg)](https://zenodo.org/badge/latestdoi/296378423)

## About This Fork

This repository is a research fork focused on **AI-assisted khipu decipherment**. It builds upon the excellent foundational work of the Open Khipu Repository (OKR) to develop computational methods for analyzing and potentially decoding Inka khipus.

### Research Goals

1. **Graph-based structural analysis** - Convert khipus into hierarchical graphs to identify patterns
2. **Numeric constraint solving** - Validate and extend positional decimal encoding conventions
3. **Pattern discovery** - Use unsupervised learning to find recurring motifs across cord attributes
4. **Multi-modal analysis** - Integrate numeric, color, spatial, and structural data
5. **Hypothesis testing** - Build frameworks to evaluate competing interpretive models
6. **Provenance analysis** - Correlate patterns with geographic and archaeological context

### Project Status

- ✅ **Phase 0: Reconnaissance** - Database analysis and data model documentation (COMPLETE)
- ⏳ **Phase 1: Infrastructure** - Data extraction pipelines and graph conversion (IN PROGRESS)
- 📋 **Phase 2: Numeric Layer** - Constraint-based numeric interpretation
- 📋 **Phase 3: Pattern Discovery** - Clustering and motif mining
- 📋 **Phase 4: Hypothesis Testing** - Formal evaluation framework

## Repository Structure

```
├── data/              # Processed data and graph representations
├── notebooks/         # Jupyter notebooks for exploration
├── src/               # Python source code
│   ├── extraction/    # Database extraction tools
│   ├── graph/         # Graph construction and analysis
│   ├── numeric/       # Numeric constraint solving
│   ├── patterns/      # Pattern discovery algorithms
│   └── visualization/ # Visualization tools
├── docs/              # Project documentation and findings
├── reports/           # Generated analysis reports
├── scripts/           # Utility scripts
└── khipu.db          # OKR SQLite database (619 khipus)
```

## Original Open Khipu Repository

This research project is built entirely upon the [Open Khipu Repository](https://github.com/khipulab/open-khipu-repository), maintained by:

- **Advisory Board:** Carrie Brezine, Jon Clindaniel, Iván Ghezzi, Sabine Hyland, Manuel Medrano
- **Administration:** Open Khipu Research Laboratory (Jon Clindaniel, jclindaniel@uchicago.edu)
- **Contributors:** Robert and Marcia Ascher, Carrie Brezine, Jon Clindaniel, Hugo Pereyra, Kylie Quave, Gary Urton

### About Khipus

Inka khipus were unique pre-Columbian Andean recording devices using three-dimensional signs—knots, cords, and colors—as symbols functionally similar to early writing systems. Spanish chronicles and contemporary studies indicate khipus recorded everything from accounting to historical narratives. **The khipu recording system remains undeciphered.**

### Data Source

The OKR contains:
- **619 extant khipus** from archaeological sites and museums worldwide
- **54,403 cords** with hierarchical structure and physical attributes
- **110,677 knots** with type, position, and numeric encoding
- **56,306 color records** with detailed multi-color specifications
- Geographic provenance from 53 archaeological sites

## Citation

If you use this research fork, please cite both:

1. **The original OKR:** See their [Zenodo DOI](https://doi.org/10.5281/zenodo.5037551)
2. **This research project:** (Citation details to be added upon publication)

## License

This research fork maintains the **MIT License** of the original OKR.

Copyright (c) 2022 Open Khipu Repository Team (original data)  
Copyright (c) 2025 [Research Project Team] (computational methods)

## Research Methodology

See [docs/methodology/](docs/methodology/) for detailed documentation of:
- Database structure and semantics
- Data quality assessments
- Analysis approaches and algorithms
- Findings and interpretations

## Contact & Contributing

This is an active research project. For questions about:
- **Original OKR data:** Contact okr-team@googlegroups.com
- **This research fork:** [Your contact information]

## Acknowledgments

We gratefully acknowledge:
- The Open Khipu Repository team for curating and sharing this invaluable dataset
- The scholars who meticulously recorded khipu data over decades
- The museums and institutions preserving these artifacts
- The Andean communities whose cultural heritage this represents

---

**Note:** This is a research fork for computational analysis. It does not modify or challenge the original OKR data. All analysis findings will be published through appropriate academic channels with full acknowledgment of the OKR's foundational role.
