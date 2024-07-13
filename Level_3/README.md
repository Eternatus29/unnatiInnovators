Business Contract Validation
This project provides a tool for validating business contracts using natural language processing (NLP) techniques. It extracts text from PDF files, performs entity extraction, highlights key entities, classifies text into predefined categories, and generates a summary of the contract content.

Features
PDF Text Extraction: Utilizes PyMuPDF to extract text from uploaded PDF files.
Entity Extraction: Identifies named entities (NER) such as persons, organizations, and dates using SpaCy.
Entity Highlighting: Highlights identified entities within the contract text.
Text Classification: Classifies clauses into predefined categories (Services Provided, Payment, Term, Confidentiality, Termination, Governing Law, Signature) using a fine-tuned BERT model.
Text Summarization: Summarizes contract content using Facebook's BART model.
User Interface: React frontend for file upload, data display, and navigation through extracted, highlighted, classified, and summarized text sections.

Installation:
Backend (Flask API)

Clone the repository:
git clone [https://github.com/Manikandan2025/repository.git](https://github.com/Manikandan2025/intel_project.git)
cd repository

Install Python dependencies using pip:
pip install -r requirements.txt

Downloading spacy model
python -m spacy download en_core_web_sm

Download the bert-model zip file from this link:
[https://drive.google.com/drive/folders/1lazhsDO7kTB6r5b4iUyyqEJsYa16Bnje?usp=sharing](https://drive.google.com/file/d/18dkfHr5QH73nK4A4J9EQXnw-LhZ-B7jC/view?usp=sharing)

Unzip the downloaded bert-model and place the bert_model folder inside the backend folder

Run the backend and front-end seperately
Run the Flask API:
locate the backend folder "cd backend" and run:
python app.py

Frontend (React)
Install npm packages:
npm install

Start the React development server:
npm start

Usage
Upload Contract: Drag and drop a PDF file or click to select files.
Generate Analysis: Click "Generate" to extract, analyze, classify, and summarize the contract.
Navigate Sections: Use the navigation bar to switch between extracted text, highlighted entities, text classification, and summary sections.

API Endpoints
POST /upload: Uploads a PDF file for processing. Returns extracted text, identified entities, highlighted text with entities, classified clauses, and a summary.

Backend: Python, Flask, PyMuPDF, SpaCy, Transformers (Hugging Face), Torch
Frontend: React.js



