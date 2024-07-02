import fitz  # PyMuPDF
from textblob import TextBlob

# Function to extract text from a PDF
def extract_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)  
    for page in doc:
        text += page.get_text()
    return text

# Function to compare PDFs and highlight differing words in red
def compare_and_highlight(pdf_path1, pdf_path2, output_path):
    text1 = extract_text(pdf_path1)
    text2 = extract_text(pdf_path2)

    # Create TextBlob objects for both texts
    blob1 = TextBlob(text1)
    blob2 = TextBlob(text2)
    
    # Find the words that are different between the two TextBlob objects
    differing_words = set(blob2.words) - set(blob1.words)

    print(f"Differing words: {differing_words}")
    
    doc = fitz.open(pdf_path2)
    
    # Track highlighted words to avoid duplicates
    highlighted_words = set()
    
    for page in doc:
        for word in differing_words:
            if word not in highlighted_words:
                for inst in page.search_for(word):
                    # Highlight the differing word with a yellow background
                    highlight = page.add_highlight_annot(inst)
                    highlight.set_colors(stroke=None, fill=(1, 0, 0))  # Set highlight color to yellow
                    highlighted_words.add(word)  # Mark the word as highlighted
    
    # Save the modified PDF with highlighted differing words
    doc.save(output_path)
    doc.close()

pdf_path1 = 'document_1.pdf'
pdf_path2 = 'document_2.pdf'

# Output PDF file path with differing words highlighted in yellow
output_path = 'highlightedDocument.pdf'

# Compare PDFs and highlight differing words in yellow
compare_and_highlight(pdf_path1, pdf_path2, output_path)