**MedLit AI** <br>
**AI Powered Biomedical Literature Mining Pipeline** <br>
Automated extraction of genes,drugs, and clinical insights from PubMed research papers using LLM powered NLP.

**Overview** <br>
Biomedical researchers face an overwhelming volume of scientific literature. Manually reading and summarizing dozens of PubMed papers just to identify relevant genes, drug targets, and key findings is time-consuming and does not scale.
**MedLit AI** solves this by taking a disease name as input and automatically fetching the most relevant PubMed papers, extracting biological entities using an LLM, scoring papers by scientific richness and recency, and delivering a structured research report — reducing hours of manual review to seconds.

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

**Pipeline Architecture** <br>
User Input (Disease Name) <br>
        │<br>
        ▼<br>
┌───────────────────┐                                <br>
│  PubMed Fetch     │  ← NCBI Entrez API (BioPython) <br>
│  (Top 10 papers)  │                                <br>
└────────┬──────────┘                                <br>
         │<br>
         ▼<br>
┌───────────────────┐                         <br>
│  LLM Extraction   │  ← Groq API / qwen3-32b <br>
│  Genes, Drugs,    │     Structured JSON prompt <br>
│  Summary          │     per paper              <br>
└────────┬──────────┘                            <br>
         │<br>
         ▼<br>
┌───────────────────┐                                     <br>
│  Relevance Scorer │  ← Entity count + recency weighting <br>
└────────┬──────────┘                                     <br>
         │<br>
         ▼<br>
┌───────────────────┐                                <br>
│  Report Generator │  ← Top 5 papers, saved as .txt <br>
└───────────────────┘                                <br>

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
