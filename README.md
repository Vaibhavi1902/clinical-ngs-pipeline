# clinical-ngs-pipeline
# Clinical NGS Analytics Platform

An educational and research-oriented cloud platform demonstrating an end-to-end
next-generation sequencing (NGS) analytics workflow using AWS, Nextflow,
Docker, Kubernetes, and Streamlit.

> **Important:** This project is for educational/research demonstration only.
> It is not a clinical diagnostic system and must not be used for patient care
> or clinical decision-making.

## Architecture

The platform separates application hosting from bioinformatics computation:

- **Amazon EKS** — hosts the Streamlit dashboard
- **Amazon S3** — stores sequencing data, references, intermediate files,
  results, and reports
- **AWS Batch** — executes computational NGS workloads
- **Nextflow** — orchestrates the bioinformatics workflow
- **Docker** — provides reproducible software environments
- **GitHub** — source-code and workflow management
- **Docker Hub** — container image registry
- **Argo CD** — GitOps deployment to Kubernetes
- **GitHub Actions** — CI/CD automation

## Bioinformatics workflow

The planned workflow is:

FASTQ  
→ FastQC  
→ fastp  
→ BWA-MEM2  
→ SAMtools  
→ BCFtools  
→ VCF  
→ MultiQC

The initial demonstration will use publicly available non-human research data.

## Repository structure

```text
clinical-ngs-pipeline/
├── app/
├── pipeline/
├── scripts/
├── docker/
├── tests/
├── reference/
├── data/
├── config/
├── .gitignore
└── README.md# Clinical NGS Analytics Platform

An educational and research-oriented cloud platform demonstrating an end-to-end
next-generation sequencing (NGS) analytics workflow using AWS, Nextflow,
Docker, Kubernetes, and Streamlit.

> **Important:** This project is for educational/research demonstration only.
> It is not a clinical diagnostic system and must not be used for patient care
> or clinical decision-making.

## Architecture

The platform separates application hosting from bioinformatics computation:

- **Amazon EKS** — hosts the Streamlit dashboard
- **Amazon S3** — stores sequencing data, references, intermediate files,
  results, and reports
- **AWS Batch** — executes computational NGS workloads
- **Nextflow** — orchestrates the bioinformatics workflow
- **Docker** — provides reproducible software environments
- **GitHub** — source-code and workflow management
- **Docker Hub** — container image registry
- **Argo CD** — GitOps deployment to Kubernetes
- **GitHub Actions** — CI/CD automation

## Bioinformatics workflow

The planned workflow is:

FASTQ  
→ FastQC  
→ fastp  
→ BWA-MEM2  
→ SAMtools  
→ BCFtools  
→ VCF  
→ MultiQC

The initial demonstration will use publicly available non-human research data.

## Repository structure

```text
clinical-ngs-pipeline/
├── app/
├── pipeline/
├── scripts/
├── docker/
├── tests/
├── reference/
├── data/
├── config/
├── .gitignore
└── README.md
