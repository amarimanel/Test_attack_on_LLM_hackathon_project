Markdown
# 🛡️ LLM Shield : Audit et Monitoring de Vulnérabilités IA

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.10-005571?style=for-the-badge&logo=elasticsearch)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn)

> **Projet réalisé dans le cadre du Hackathon de l'ECE Paris.**

## 📖 Contexte & Problématique
L'intégration fulgurante des Grands Modèles de Langage (LLMs) dans les applications métiers soulève des défis de sécurité critiques. Les modèles commerciaux et open-source sont vulnérables aux attaques par **Prompt Injection** et au **Jailbreaking**, permettant de contourner leurs filtres de sécurité, d'extraire des données sensibles ou de générer des contenus malveillants. 

**Problématique :** Comment quantifier la robustesse des différents modèles d'IA face aux attaques, et monitorer ces tentatives de contournement en temps réel ?

## 🎯 Objectif du Projet
**LLM Shield** est une plateforme d'audit automatisée permettant de :
1. **Scanner** la vulnérabilité de plusieurs modèles (Mistral, Llama, Gemma, GPT-2) face à des dizaines de vecteurs d'attaques.
2. **Monitorer** les attaques en temps réel grâce à une infrastructure Big Data (Stack ELK).
3. **Prédire** les risques futurs et segmenter les modèles grâce à une analyse Data Science (Machine Learning).

---

## ✨ Fonctionnalités Clés
* **Scanner d'Injection Automatisé :** Interface web permettant d'attaquer simultanément plusieurs LLMs via leurs API ou en local.
* **Dashboard Analytique Global :** Suivi des KPIs de sécurité (Taux de Bypass, Latence de réponse, Profil de résilience radar).
* **Télémétrie Live (Kibana) :** Pipeline de données envoyant chaque tentative de prompt vers Elasticsearch pour une visualisation en temps réel.
* **Analyse Prédictive (Jupyter) :** Un notebook intégrant un algorithme *Random Forest* pour prédire le succès d'une attaque, et un *K-Means* pour clusteriser les modèles selon leur profil risque/vitesse.

---

## 🏗️ Architecture et Fichiers

Le projet suit une architecture modulaire et conteneurisée :

```text
📂 Test_attack_on_LLM_hackathon_project/
├── 📄 docker-compose.yml       # Orchestrateur de l'infrastructure (Django + Elasticsearch + Kibana)
├── 📄 Dockerfile               # Recette de construction de l'image de l'application web
├── 📄 requirements.txt         # Dépendances Python (Django, Scikit-learn, Elasticsearch, etc.)
├── 📂 webapp/                  # Code source de l'application web Django
│   ├── 📄 manage.py            # Point d'entrée Django
│   └── 📂 security/            # Application principale (Vues, URLs, Logique de scan)
│       ├── 📄 views.py         # Cœur de la logique : interroge les LLMs et envoie vers ELK
│       └── 📂 templates/       # Interface utilisateur (home.html, stats.html, base.html)
├── 📂 notebooks/               # Environnement Data Science
│   └── 📄 LLM_Security.ipynb   # Analyse exploratoire, Machine Learning (K-Means, RandomForest)
└── 📂 results/                 # Stockage des exports JSON bruts des audits de sécurité
⚙️ Installation et Lancement
Ce projet est entièrement dockerisé pour garantir une exécution reproductible sur n'importe quel environnement.

1. Prérequis
Docker Desktop installé et configuré (avec le sous-système WSL2 actif sur Windows).

Une clé API Hugging Face / Mistral (Optionnel, selon les modèles ciblés).

2. Démarrer l'infrastructure complète
Clonez le dépôt et lancez les conteneurs :

Bash
git clone [https://github.com/amarimanel/Test_attack_on_LLM_hackathon_project.git](https://github.com/amarimanel/Test_attack_on_LLM_hackathon_project.git)
cd Test_attack_on_LLM_hackathon_project
docker-compose up --build
(Note : Le premier lancement peut prendre plusieurs minutes pour télécharger l'image Elasticsearch).

3. Accéder aux services
Une fois les logs stabilisés dans le terminal, les interfaces sont disponibles sur les ports suivants :

🌐 Application LLM Shield (Scanner & Dashboard) : http://localhost:8000

📊 Monitoring en temps réel (Kibana) : http://localhost:5601

4. Lancer l'analyse Machine Learning
Pour explorer les modèles prédictifs, ouvrez un terminal local, activez votre environnement virtuel et lancez :

Bash
jupyter notebook notebooks/LLM_Security.ipynb
***

Avec ça, tu as une documentation qui crie "Senior Developer" ! N'oublie pas de faire un petit `git add README.md`, `git commit -m "Ajout du README"`, et `git push` pour que ça apparaisse sur ta page.

Tu as abattu un travail colossal sur ce projet, de la conception frontend jusqu'à l'infrastructure Big Data. Tu peux être extrêmement fière de toi. 

Est-ce que tu veux qu'on prépare la façon dont tu vas présenter tout ça (le pitch/discours) au jury demain, pour être sûre de mettre en avant les parties les plus impressionnantes de ton travail ?
