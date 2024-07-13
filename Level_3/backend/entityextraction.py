import spacy
nlp = spacy.load("en_core_web_sm")

def extract_ner_details(pdf_text):
    entities=[]
    for line in pdf_text.splitlines():
        doc = nlp(line)
        for ent in doc.ents:
            entities.append(f"{ent.text} [{ent.label_}]\n")

    
    return entities