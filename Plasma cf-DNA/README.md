****Plasma cf-DNA Analysis****

**Overview**

This folder contains scripts for analyzing circulating cell-free DNA (cfDNA) methylation to identify tissue-specific markers associated with COVID-19 severity.

The analysis is based on whole-genome bisulfite sequencing (WGBS) cfDNA data from two datasets:
UCSF & McGill University cfDNA datasets from the study:
"Cell-free DNA tissues of origin by methylation profiling reveals significant cell, tissue, and organ-specific injury related to COVID-19 severity"
 📌 Data accessible at this GitHub Repository: https://github.com/alexpcheng/cfDNAme

Additionally, to identify tissue-specific differentially methylated regions (DMRs), we use:
"A DNA Methylation Atlas of Normal Human Cell Types" as a reference for cell-type-specific methylation patterns.
A CSV file (atlas.csv) in this folder contains pre-extracted tissue-specific DMRs from the atlas.

**Analysis Pipeline**

1. Scenario Designing

2. Data Preprocessing

3. Differential Analysis

4. Tissue-Specific Methylation Analysis

5. Annotations and Marker Selection


**Usage**

Scripts for each analysis step are available in this folder.
The atlas.csv file provides precomputed tissue-specific DMRs for reference.