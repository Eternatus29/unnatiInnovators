from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from pdfparser import extract_text_from_pdf
from highlightner import highlight_entities
from entityextraction import extract_ner_details
from summerizer import summerized_text
import torch
from transformers import BertTokenizer, BertForSequenceClassification


model_load_path = "bert_model"
model = BertForSequenceClassification.from_pretrained(model_load_path)
tokenizer = BertTokenizer.from_pretrained(model_load_path)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

def predict(text):
    # Tokenize the input text
    inputs = tokenizer(text, truncation=True, max_length=128, return_tensors='pt', padding=True)

    # Move inputs to GPU if available
    inputs = {key:val.to(device) for key, val in inputs.items()}

    # Perform inference 
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1)
        return predicted_class.item()

classes = {
    1: "SERVICES", 
    2: "PAYMENT", 
    3: "TERM OF AGREEMENT", 
    4: "CONFIDENTIALITY", 
    5: "TERMINATION", 
    6: "GOVERNMENT LAW",
    7: "SIGNATURE"
}

    
app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)
pdf_text=''
entity=[]

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        logging.debug("Upload request received")
        uploaded_file = request.files['file']
        logging.debug(f"File received: {uploaded_file.filename}")

        if uploaded_file.filename != '':
            file_content = uploaded_file.read()
            text = extract_text_from_pdf(file_content)
            entities = extract_ner_details(text)
            highlighted_text = highlight_entities(text)
            predicted_text=text_classify(text)
            summerize_text=summerized_text(text)
            logging.debug("PDF text extraction successful")
            return jsonify({'text': text, 'entities': entities, 'highlighted_text': highlighted_text,'predicted_text':predicted_text,'summerized_text':summerize_text}), 200
        else:
            logging.error("No file uploaded")
            return jsonify({'error': 'No file uploaded'}), 400
    except Exception as e:
        logging.error(f"Exception: {e}")  # Print the exception to the console
        return jsonify({'error': str(e)}), 500
    

def text_classify(pdf_text):
    label=''
    arr=[]
    for line in pdf_text.splitlines():
        predicted_class = predict(line)
        if(predicted_class!=7):
          label=f"[{classes[predicted_class]}]"
        else:
          label=''
        arr.append([line, label])
    return arr





if __name__ == '__main__':
    app.run(debug=False)
