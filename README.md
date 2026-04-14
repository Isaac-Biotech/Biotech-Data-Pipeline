# Biotech Data Pipeline 🧬💻

**A suite of automated Python and Biopython scripts for genomic data parsing, FASTA processing, and global database querying.**

## Overview
This repository contains a collection of computational biology tools designed to bridge the gap between "wet lab" genetic data and "dry lab" bioinformatics automation. It progresses from foundational Python data pipelines to advanced, industry-standard library implementations using **Biopython**.

## Technical Stack
* **Language:** Python (3.14)
* **Libraries:** Biopython (1.87), `os`
* **Databases:** NCBI Entrez (National Center for Biotechnology Information)
* **Formats Handled:** `.txt` (Raw data), `.fasta` (Genomic sequences)

## The Toolkit

### 1. The Biopython Suite (Advanced)
Industry-standard automation scripts utilizing the Biopython library for high-speed analysis and global data fetching.
* **`ncbi_database_fetcher.py`**: Connects directly to the US Government's NCBI database via `Bio.Entrez` to query and download live human mRNA transcripts (e.g., Human HBB/Sickle Cell). Includes custom error-handling to bypass local OS version conflicts.
* **`fasta_parser.py`**: Automates the reading and parsing of standard `.fasta` files output by modern DNA sequencing machines using `Bio.SeqIO`.
* **`biopython_translator.py`**: Instantly translates raw DNA sequences into protein chains, automatically identifying and handling stop codons.
* **`biopython_gc_analyzer.py`**: Calculates the precise GC-Content percentage of genetic sequences using native library algorithms.

### 2. Foundational Data Pipelines (Core Python)
Custom-built foundational scripts demonstrating core programming logic, dictionary mapping, and batch processing without relying on external libraries.
* **`batch_file_processor.py`**: A directory-scanning automation tool that opens, reads, and processes multiple biological data files simultaneously.
* **`dna_to_protein_translator.py`**: A manually engineered dictionary mapping algorithm that slices DNA strings into 3-letter codons and translates them into amino acids.
* **`manual_gc_calculator.py`**: A logical parsing script that calculates the GC-content of a DNA string using foundational math and string iteration.

## Installation & Usage
To run the advanced tools in this pipeline, ensure Biopython is installed in your local environment:
```bash
pip install biopython
