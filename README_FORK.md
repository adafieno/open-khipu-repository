# Khipu Computational Analysis Toolkit

**AI-Assisted Hypothesis Testing for Inka Khipu Research**

*A computational research fork of the [Open Khipu Repository](https://github.com/khipulab/open-khipu-repository)*

[![Original DOI](https://zenodo.org/badge/296378423.svg)](https://zenodo.org/badge/latestdoi/296378423)

## About This Fork

This repository is a research fork focused on **computational hypothesis-testing tools for khipu analysis**. It builds upon the excellent foundational work of the Open Khipu Repository (OKR) to develop rigorous, falsifiable methods for testing interpretive models of Inka khipus.

**This is not a "decipherment" project.** Rather, it provides computational infrastructure to help scholars test hypotheses transparently, quantify uncertainty, and surface structural patterns that may inform future interpretive work.

### Research Goals

1. **Arithmetic validation framework** - Test summation consistency and internal numeric logic (following Medrano & Khosla 2024)
2. **Graph-based structural analysis** - Convert khipus into hierarchical graphs to identify recurring patterns
3. **Hypothesis parameterization** - Represent multiple interpretations explicitly (e.g., color semantics as configurable assumptions)
4. **Pattern discovery with constraints** - Use unsupervised learning while requiring patterns across multiple provenances
5. **Multi-modal feature extraction** - Integrate numeric, color, spatial, and structural data with uncertainty tracking
6. **Expert-in-the-loop validation** - Build checkpoints for domain expert review at each analytical stage

### Project Status

- ✅ **Phase 0: Reconnaissance** - Database analysis and data model documentation (COMPLETE)
- ✅ **Phase 1: Baseline Validation** - Arithmetic validation and numeric decoding pipeline (COMPLETE)
  - Decoded 54,403 cords with numeric values (68.2% coverage)
  - Validated all 619 khipus for arithmetic consistency (95.8% have numeric data, avg confidence 0.947)
  - Exported processed datasets: cord_numeric_values.csv, validation_results_full.json
- ✅ **Phase 2: Extraction Infrastructure** - Cord/knot extractors with validation hooks (COMPLETE)
  - Cord hierarchy extractor: 54,403 cords, 16.9% missing attachments, avg confidence 0.949
  - Knot data extractor: 110,151 knots, 95.2% with numeric values, avg confidence 0.896
  - Exported: cord_hierarchy.csv, knot_data.csv with metadata
- ✅ **Phase 3: Summation Hypothesis Testing** - Test white cord boundaries, pendant sum patterns (COMPLETE)
  - Tested all 619 khipus for pendant-to-parent summation patterns
  - Identified white cord boundary markers across dataset
  - Exported: summation_test_results.csv with detailed analysis
- 📋 **Phase 4: Pattern Discovery** - Clustering and motif mining with provenance-aware constraints
- 📋 **Phase 5: Multi-Model Framework** - Hypothesis evaluation with uncertainty quantification

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

Inka khipus were unique pre-Columbian Andean recording devices using three-dimensional signs—knots, cords, and colors—as symbols functionally similar to early writing systems. Spanish chronicles and contemporary studies indicate khipus recorded everything from accounting to historical narratives.

**Status:** The numeric encoding system is well-understood (decimal positional notation established by Locke 1912, refined by Ascher & Ascher). Recent work (Medrano & Khosla 2024) found ~74% of khipus contain internally consistent arithmetic summations. However, semantic meaning beyond accounting remains debated, with no consensus on whether khipus encoded narrative, categorical, or linguistic information.

### Prior Computational Work

This project builds on:
- **Medrano & Khosla (2024):** Algorithmic analysis of 650 khipus, arithmetic consistency testing, white cord boundary detection
- **Clindaniel (2024):** Transformer-based clustering of cord attributes, latent categorical structure discovery
- **Ascher & Ascher:** Foundational comparative datasets and arithmetic structure documentation

Our contribution focuses on **validation infrastructure** and **hypothesis testing frameworks** rather than new interpretive claims.

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
Copyright (c) 2025 Agustín Da Fieno Delucchi (computational methods)

## Research Methodology

See [docs/methodology/](docs/methodology/) for detailed documentation of:
- Database structure and semantics
- Data quality assessments and uncertainty quantification
- Validation strategies and expert-in-the-loop checkpoints
- Hypothesis parameterization and multi-interpretation support
- Overfitting prevention (provenance-aware splitting, cross-validation, perturbation testing)
- Analysis approaches with falsifiable claims
- Findings with confidence intervals and limitations

**Key Principle:** AI surfaces structure and quantifies uncertainty; domain experts provide interpretation and validation.

## Contact & Contributing

This is an active research project. For questions about:
- **Original OKR data:** Contact okr-team@googlegroups.com
- **This research fork:** Agustín Da Fieno Delucchi (adafieno@hotmail.com)

## Acknowledgments

We gratefully acknowledge:
- The Open Khipu Repository team for curating and sharing this invaluable dataset
- The scholars who meticulously recorded khipu data over decades
- The museums and institutions preserving these artifacts
- The Andean communities whose cultural heritage this represents

---

**Note:** This is a research fork for computational analysis. It does not modify or challenge the original OKR data. This project builds **tools for hypothesis testing**, not semantic decipherment. We surface patterns, test falsifiable claims, and quantify uncertainty—interpretation remains the domain of archaeologists, anthropologists, and historians. All findings will be published through appropriate academic channels with full acknowledgment of the OKR's foundational role and prior computational work.
