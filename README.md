Markdown
# 🛡️ LLM Shield : AI Vulnerability Auditing & Monitoring

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.10-005571?style=for-the-badge&logo=elasticsearch)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn)

## A. Subject Presentation
* **Chosen Subject:** Evaluation of LLM robustness based on adversarial frameworks (inspired by HarmBench and TestAttack methodologies).
* **Scientific Objective:** To systematically quantify the resilience of different LLM architectures against prompt injection and establish a novel correlation between inference latency and internal safety mechanisms.
* **Reformulated Problematic:** How can we dynamically evaluate the robustness of LLMs against adversarial attacks, and how can we leverage real-time telemetry (ELK Stack) combined with Machine Learning to monitor, cluster, and predict vulnerabilities?

## B. Corpus Description
* **Source of the original corpus:** Aggregated and adapted from open-source adversarial repositories (HarmBench, TestAttack) to ensure a standardized baseline of malicious behaviors.
* **Description of the experimental corpus created:** A custom, structured JSON dataset containing both benign (baseline) queries and malicious prompts, designed for automated, sequential API injection via our Django engine.
* **Construction Methodology:** Prompts were selected based on their semantic structure and translated into a dynamic payload format that our auditing script uses to query multiple models simultaneously.
* **Categorization used:** The attacks are strictly categorized into four attack vectors:
  1. `direct_injection`: Explicit command overrides.
  2. `roleplay`: Forcing the model to adopt a restricted persona (e.g., "DAN").
  3. `jailbreak`: Complex scenario building to bypass ethical filters.
  4. `obfuscation`: Encoding or formatting tricks to hide malicious intent.

## C. Tested LLM Models
All models were evaluated under strict, reproducible conditions to ensure comparative validity.

| Model Name | Type | Version | Execution Parameters |
| :--- | :--- | :--- | :--- |
| **GPT-2** | Open-source (Baseline) | Standard | `temp: 0.7`, `top_p: 0.9`, `max_tokens: 150` |
| **Llama 2** | Open-source | 7b-chat-hf | `temp: 0.7`, `top_p: 0.9`, `max_tokens: 150` |
| **Mistral** | Open-source | 7B-Instruct | `temp: 0.7`, `top_p: 0.9`, `max_tokens: 150` |
| **Gemma** | Open-source | 7B | `temp: 0.7`, `top_p: 0.9`, `max_tokens: 150` |

## D. Results Summary
Our automated evaluation pipeline yielded the following vulnerability metrics across our standardized experimental corpus.

| Model | Direct Injection Bypass | Jailbreak Bypass | Obfuscation Bypass | Roleplay Bypass | **Global Bypass Rate** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GPT-2** | 90% | 90% | 90% | 90% | **90.0%** |
| **Mistral-7B**| 10% | 20% | 20% | 30% | **20.0%** |
| **Gemma-7B** | 10% | 10% | 20% | 10% | **12.5%** |
| **Llama-2-7b**| 0% | 0% | 0% | 0% | **0.0%** |

* **Main Indicators:** Beyond standard Bypass Rates, we introduced the **Latency-Security Metric**. K-Means clustering revealed that highly secure models (like Llama 2) incur a massive computational latency overhead (~1.6M ms during our stress tests) to process refusals, whereas vulnerable models (GPT-2) bypass instantly.
* 📄 **Link to Scientific Report:** [Insert Link to your PDF here, e.g., `./docs/LLM_Shield_Scientific_Report.pdf`]

## E. Project Tree Structure
```text
Test_attack_on_LLM_hackathon_project/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── /data
│   ├── original_benchmark/         # Source datasets (HarmBench/TestAttack refs)
│   └── experimental_corpus/        # Structured JSON payloads for Django
├── /webapp                         # Django Application (Scanning Engine)
│   ├── manage.py
│   └── /security                   # Core logic (views.py interacting with LLMs & ELK)
├── /results
│   ├── /raw_outputs                # Raw Elasticsearch JSON telemetry
│   ├── /processed_results.csv      # Cleaned data for ML analysis
│   └── /figures                    # Exported Kibana & Matplotlib PNGs
├── /notebooks                      # Data Science Environment
│   └── LLM_Security.ipynb          # Statistical analysis, K-Means & Random Forest
└── /docs
    └── annotation_grid.md          # Rules for automated heuristic annotation
```

## F. Instructions to Reproduce the Experiment
This project is containerized to guarantee identical execution environments.

**1. Dependency Installation & Infrastructure Setup**
Ensure Docker Desktop (with WSL2 if on Windows) is running.
```bash
git clone [https://github.com/amarimanel/Test_attack_on_LLM_hackathon_project.git](https://github.com/amarimanel/Test_attack_on_LLM_hackathon_project.git)
cd Test_attack_on_LLM_hackathon_project
```

**2. API Keys Configuration**
Create a `.env` file at the root of the project to store your Hugging Face or proprietary API keys (File Not commited).

```

**3. Execution Command**
Launch the Django web application and the ELK Stack (Elasticsearch + Kibana) simultaneously:
```bash
docker-compose up --build
```
Access the testing interface at `http://localhost:8000` to initiate the script, and `http://localhost:5601` to view live telemetry.

**4. Machine Learning Analysis Location**
Once the results are generated and stored via Elasticsearch, the offline statistical analysis and predictive modeling can be reproduced by running the Jupyter Notebook:
```bash
jupyter notebook notebooks/LLM_Security.ipynb
```

## G. Credits
* Original adversarial frameworks inspired by:  TestAttack repositories.
* Project realized by: Manel Amari, Amel AMAROUCHENE, Ouassim BENTIZI, Dany AGSOUS
* Encadrants : Yann Fornier, Vandamme SIMON
* ECE Paris Hackathon 2026.
```
***
