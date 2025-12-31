# Reports Index

This directory contains comprehensive reports for each phase of the Khipu Computational Analysis Toolkit project.

## Project Overview

**[PROJECT_PROGRESS_SUMMARY.md](PROJECT_PROGRESS_SUMMARY.md)** - Complete project summary including all completed phases, key findings, statistics, and next steps.

## Phase Reports

### Phase 0: Reconnaissance ✅ COMPLETE
**[phase0_reconnaissance_report.md](phase0_reconnaissance_report.md)**

Database analysis and data model documentation for the Open Khipu Repository.

**Key Contents:**
- 24 tables analyzed
- 280,000+ records
- Data quality assessment
- Viability rating: 8.5/10
- Recommendations for Phase 1

**Generated:** December 30, 2025

---

### Phase 1: Baseline Validation ✅ COMPLETE
**[phase1_baseline_validation_report.md](phase1_baseline_validation_report.md)**

Numeric decoding pipeline and arithmetic validation across all 619 khipus.

**Key Statistics:**
- 54,403 cords decoded
- 95.8% of khipus have numeric data
- Average confidence: 0.947
- 110,151 knots processed

**Generated:** December 31, 2025

---

### Phase 2: Extraction Infrastructure ✅ COMPLETE
**[phase2_extraction_infrastructure_report.md](phase2_extraction_infrastructure_report.md)**

Comprehensive extraction tools for cords, knots, colors, and graph representations.

**Components:**
- Cord hierarchy extractor (54,403 cords)
- Knot data extractor (110,151 knots)
- Color extractor (56,306 records)
- Graph builder (619 NetworkX graphs)

**Key Finding:** White is the most common color (26.8%), validating boundary marker hypothesis.

**Generated:** December 31, 2025

---

### Phase 3: Summation Hypothesis Testing ✅ COMPLETE
**[phase3_summation_testing_report.md](phase3_summation_testing_report.md)**

Testing pendant-to-parent summation patterns across the entire dataset.

**Key Results:**
- 74.2% of khipus exhibit summation relationships
- 30.2% have high match rates (>80%)
- White cords show +9.1% higher summation match rates
- Hypothesis validated (Medrano & Khosla 2024)

**Generated:** December 31, 2025

---

### Phase 4: Pattern Discovery � IN PROGRESS
**[phase4_pattern_discovery_progress.md](phase4_pattern_discovery_progress.md)**

Graph-based pattern mining, clustering, and motif discovery.

**Completed Analyses:**
- High-match khipu analysis: 9 khipus with ≥80% summation match rate
- Hierarchical summation testing: Multi-level recursive patterns across 619 khipus
- Key finding: White cords negatively correlate with summation consistency

**Remaining Analyses:**
- Graph similarity metrics
- Structural clustering
- Subgraph motif mining
- Geographic correlation

**Generated:** December 31, 2025

---

### Phase 5: Multi-Model Framework 📋 PENDING

Hypothesis evaluation with uncertainty quantification and expert validation.

**Planned Framework:**
- Hypothesis parameterization
- Multi-model comparison
- Uncertainty quantification
- Expert-in-the-loop validation
- Academic publication

---

## Quick Reference

### Output Data Files

All processed data is in `data/processed/`:

| File | Records | Phase |
|------|---------|-------|
| `validation_results_full.json` | 619 khipus | Phase 1 |
| `cord_numeric_values.csv` | 54,403 | Phase 1 |
| `cord_hierarchy.csv` | 54,403 | Phase 2 |
| `knot_data.csv` | 110,151 | Phase 2 |
| `color_data.csv` | 56,306 | Phase 2 |
| `white_cords.csv` | 15,125 | Phase 2 |
| `summation_test_results.csv` | 619 | Phase 3 |

### Graph Data Files

Graph representations in `data/graphs/`:

| File | Content | Phase |
|------|---------|-------|
| `khipu_graphs.pkl` | 619 NetworkX graphs | Phase 2 |
| `khipu_graphs_metadata.json` | Graph statistics | Phase 2 |

### Key Findings Summary

1. **Numeric encoding validated** - 95.8% khipus have decodable numeric data (avg confidence 0.947)
2. **White cord hypothesis confirmed** - Most common color (26.8%), +9.1% higher summation rates
3. **Summation patterns widespread** - 74.2% of khipus exhibit pendant-to-parent summation
4. **Multi-level hierarchical summation** - 34.7% of high-match khipus show recursive patterns
5. **Encoding diversity** - 25.8% low-match khipus suggest narrative/categorical encoding

---

## Contact

**Lead Researcher:** Agustín Da Fieno Delucchi  
**Email:** adafieno@hotmail.com

**Original Data:** [Open Khipu Repository](https://github.com/khipulab/open-khipu-repository)

---

**Last Updated:** December 31, 2025  
**Status:** Phases 0-3 Complete
