**Viral Infection Severity Biomarker Discovery
Overview**

This repository contains scripts and analysis pipelines for identifying severity biomarkers of acute viral infections using three types of blood-based nucleic acid data:

1. Bulk Blood Transcriptome – Meta-analysis and external validation of RNA-seq datasets from whole blood to identify transcriptomic changes in severe infections.
2. Bulk Blood Methylome – Analysis of whole blood methylation data, including global methylation levels, differentially methylated positions (DMPs), and differentially methylated regions (DMRs), with transcriptomic validation.
3. Plasma cf-DNA – Identification of cell-type-specific markers in circulating cell-free DNA (cfDNA) to assess tissue damage and develop prognostic severity markers.

**Repository Structure**

📂 Bulk Blood Transcriptome

Meta-analysis and external validation of multiple whole blood RNA-seq datasets.
Identification of differentially expressed genes (DEGs) associated with disease severity.
Comparison of transcriptomic changes in COVID-19 vs. Influenza and bacterial infections.

📂 Bulk Blood Methylome

Global methylation level analysis in severe, mild, and healthy samples.
Identification of DMPs and DMRs related to disease severity.
Validation of methylation markers with bulk blood transcriptome data.

📂 Plasma cf-DNA

Identification of tissue-specific cfDNA markers for severity assessment.
Estimation of tissue damage extent in severe infections.

**Usage**

Each folder contains scripts and required data preprocessing steps for reproducing the analysis. See individual folders for detailed instructions.