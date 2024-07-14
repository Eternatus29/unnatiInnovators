# Business Contract Validation -To Classify Content within the Contract 
Clauses and Determine Deviations from Templates and highlight them.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Intel AI Workbench](https://img.shields.io/badge/Powered%20by-Intel%20AI%20Workbench-orange.svg)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/ai-analytics-toolkit.html#gs.v40l3v)

![Intel Logo](https://logos-world.net/wp-content/uploads/2021/09/Intel-Logo-2006-2020-700x394.png)


*Empowering Legal Teams with AI-Driven Contract Analysis*

This project, developed as part of the Intel Unnati program, leverages machine learning and generative AI to streamline the validation of business contracts, identifying deviations from standard templates and highlighting critical differences.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Usage](#installation--usage)
- [Team](#team)
- [License](#license)

## Project Overview

Business contracts are the backbone of commercial relationships, but their complexity and length often make manual review tedious and error-prone. This solution automates the process, extracting key information, classifying clauses, and pinpointing discrepancies, allowing legal teams to focus on high-level analysis and decision-making.

## Key Features

- *PDF Parsing:* Extracts text content from PDF contracts.
- *Named Entity Recognition (NER):* Identifies key entities (e.g., parties, dates, amounts) within contract text.
- *Clause Classification:* Categorizes contract text into predefined clauses (e.g., confidentiality, termination, indemnification).
- *Template Deviation Detection:* Compares contract text to standard templates and highlights deviations.
- *PDF Highlighting:* Visually marks up PDF contracts to show classified clauses and identified deviations.
- *Summarization:* Generates concise summaries of identified deviations.

## Technology Stack

- *Machine Learning:*  
    - spaCy (for NER)
    - Scikit-learn (for classification)
- *Generative AI:* 
    - Transformers (for summarization)
- *Backend:* 
    - Python (3.9+), Flask
- *Frontend:* 
    - ReactJS (18+), Node.js, npm 
- *Database:* 
    - MongoDB (5.0+)
- *Infrastructure:* 
    - Docker
- *Intel AI Workbench Components:*
    - PDF-Parser, Text-Classifier, PDF-Highlighter, OCR, NER, Text-Compare, Summarizer

## Installation & Usage

-  *Prerequisites:*
   - Python 3.9+
   - Node.js and npm
   - Docker
   - MongoDB

- *Clone:* git clone https://github.com/Eternatus29/unnatiInnovators.git
- *Backend Setup:*
   - cd backend
   - pip install -r requirements.txt
   - streamlit run app.py (for StreamLit)
   - python app.py (for Flask)
   - (Optional) Set up environment variables for Flask app
- *Frontend Setup:*
   - cd frontend
   - npm install
   - npm run start
- *Run with Docker:*
   - docker-compose up --build (This will build and start containers for the backend, frontend, and MongoDB)
- *Access the App:* 
   - Open your browser and navigate to http://localhost:3000


## Team

- Luvkush Sharma
- Anik Roy
- Dheeraj Sharma
- Uday Pratap Singh
- Muskan Garg


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.