import spacy

# Load spaCy's pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Function to perform NER
def perform_ner(text):
    #param text: The text on which to perform NER.

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities    # Return List of named entities.

# Perform NER on the extracted text
entities = perform_ner(extracted_text)

# Print the entities
for entity in entities:
    print(entity)
