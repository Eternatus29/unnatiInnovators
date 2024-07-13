def compare_texts(template_text, actual_text):
    """Compare two texts and provide a summary of deviations."""
    processed_template = preprocess_text(template_text)
    processed_actual = preprocess_text(actual_text)
    diff = ndiff(processed_template.split(), processed_actual.split())
    
    deviations = {
        'template': template_text,
        'actual': actual_text,
        'diff': []
    }
    
    for line in diff:
        if line.startswith('- '):
            deviations['diff'].append(f"Template has '{line[2:]}' which is missing in Actual.")
        elif line.startswith('+ '):
            deviations['diff'].append(f"Actual has '{line[2:]}' which is missing in Template.")
    
    return deviations
