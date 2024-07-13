
from transformers import BartForConditionalGeneration, BartTokenizer

# Load the BART tokenizer and model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')


def split_text(text, chunk_size=1000):
    if not text:
        raise ValueError("Input text is None or empty.")
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_text(text, max_length=60, min_length=30):
    if not text:
        raise ValueError("Input text is None or empty.")
    inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs['input_ids'], 
        max_length=max_length, 
        min_length=min_length, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summerized_text(text):
    if text:
        try:
            chunks = split_text(text)
            summaries = [summarize_text(chunk) for chunk in chunks]
            combined_summary = ' '.join(summaries)
            return combined_summary
        except Exception as e:
            print(f"Error processing text: {e}")
    else:
        print("No text extracted from the PDF.")
