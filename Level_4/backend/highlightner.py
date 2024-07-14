import spacy
nlp = spacy.load("en_core_web_sm")



def highlight_entities(text):
    doc = nlp(text)
    highlighted_text = text
    for ent in reversed(doc.ents):  # reverse to not mess up the offsets
        start = ent.start_char
        end = ent.end_char
        label = ent.label_
        highlighted_text = highlighted_text[:start] + f'<mark>{ent.text}</mark>' + highlighted_text[end:]
    return highlighted_text