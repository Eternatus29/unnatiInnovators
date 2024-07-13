import streamlit as st
from pdfparser import extract_text_from_pdf
from highlightner import highlight_entities
from entityextraction import extract_ner_details
from summerizer import summerized_text
import torch
from transformers import BertTokenizer, BertForSequenceClassification

model_load_path = "./bert_model"
model = BertForSequenceClassification.from_pretrained(model_load_path)
tokenizer = BertTokenizer.from_pretrained(model_load_path)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

classes = {
    1: "SERVICES", 
    2: "PAYMENT", 
    3: "TERM OF AGREEMENT", 
    4: "CONFIDENTIALITY", 
    5: "TERMINATION", 
    6: "GOVERNMENT LAW",
    7: "SIGNATURE"
}

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

def text_classify(pdf_text):
    arr = []
    for line in pdf_text.splitlines():
        predicted_class = predict(line)
        if predicted_class != 7:
            label = f"[{classes[predicted_class]}]"
        else:
            label = ''
        arr.append([line, label])
    return arr

def main():
    st.title('PDF Analysis and Classification')

    uploaded_file = st.file_uploader("Upload a PDF", type=['pdf'])

    if uploaded_file is not None:
        file_content = uploaded_file.read()
        text = extract_text_from_pdf(file_content)
        entities = extract_ner_details(text)
        highlighted_text = highlight_entities(text)
        predicted_text = text_classify(text)
        summerize_text = summerized_text(text)

        st.subheader('Uploaded PDF Text')
        st.text(text)

        st.subheader('Entities Detected')
        st.json(entities)

        st.subheader('Highlighted Text')
        st.text(highlighted_text)

        st.subheader('Predicted Text Classification')
        st.json(predicted_text)

        st.subheader('Summarized Text')
        st.text(summerize_text)

if __name__ == '__main__':
    main()
