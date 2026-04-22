**MedLit AI** <br>
**AI Powered Biomedical Literature Mining Pipeline** <br>
Automated extraction of genes,drugs, and clinical insights from PubMed research papers using LLM powered NLP.

**Overview** <br>
**Problem Statement** <br>
Biomedical researchers and students face an overwhelming volume of scientific literature. Manually reading, parsing, and summarizing dozens of PubMed papers for a single disease — just to identify relevant genes, drug targets, and key findings — is time-consuming, inconsistent, and does not scale.

**Solution** <br>
**MedLit AI** is an end-to-end pipeline that takes disease name as input and automatically:
* Fetched the most relevant papers from PubMed(NCBI).
* Uses an LLM to extract genes,drugs, and summaries from each paper.
* Scores and ranks papers by scientific richness and recency.
* Outputs a structured, human-readble research report.

This tool is designed to accelerate literatur reviews for researchers, bioinformaticians, and students, reducing hours of manual work to seconds.

**Key Features** <br>
* PubMed Integration -- Queries NCBI's Entrez API with biomedically enriched search  terms (gene, protein, mutation, pathway, drug, therapy)
* LLM-Powered Entity Extraction -- Extracts gene symbols, drug/compound names, and concise paper summaries using a structured JSON prompt
* Hallucination-Resistant Prompting -- Strict prompt engineering with explicit rules against fabrication: returns empty lists when data is absent.
* Relevance Scoring - Ranks papers using a composite score based on entity density and publiation recency.
* Report Generation - Produces a clean, readable .txt report for top5 papers, saved locally
* Configurable and Extensible - Easy to swap LLM providers, adjust paper limits, or expand entity types

**Tech Stack**
Language: Python
Database: NCBI PubMed via Entrez(BioPython)
LLM Provider: Groq API
LLM Model: qwen/qwen3-32b

**Pipeline Architecture**
User Input (Disease Name)
        │
        ▼
┌───────────────────┐
│  PubMed Fetch     │  ← NCBI Entrez API (BioPython)
│  (Top 10 papers)  │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  LLM Extraction   │  ← Groq API / qwen3-32b
│  Genes, Drugs,    │     Structured JSON prompt
│  Summary          │     per paper
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Relevance Scorer │  ← Entity count + recency weighting
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Report Generator │  ← Top 5 papers, saved as .txt
└───────────────────┘

**How it works**
1. Fetch Papers
The pipeline queries PubMed using a compound search term that combines the disease name with biomedical keywords (gene, protein, mutation, drug, therapy, etc.). It retrieves up to 10 papers sorted by relevance and parses their titles, abstracts, and publication years from the XML response.
2. Extract Entities (LLM)
Each paper's title and abstract (up to 1000 characters) are passed to the qwen/qwen3-32b model via Groq. The model is prompted to return a strict JSON object containing:

genes — list of real biological gene symbols (e.g., APP, PSEN1, APOE)
drugs — list of drug or compound names (e.g., Donepezil, Memantine)
summary — a 1–2 sentence plain-language summary

A regex parser safely extracts the JSON block from the LLM response to handle any extraneous output.
3. Rank Papers
Each paper receives a composite relevance score:

+2 points per gene identified
+2 points per drug identified
+3 points if published within the last 2 years
+1 point if published within the last 5 years

4. Generate Report
The top 5 papers are formatted into a structured report and saved as a .txt file named after the disease (e.g., Alzheimer_disease.txt).

**Author**
**Sanmati** — Bioinformatics & AI

📧 sanmti.bioinfo@gmail.com
GitHub: @your-username

**License**
This project is licensed under the MIT License.
