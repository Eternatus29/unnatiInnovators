import difflib

def compare_texts(text1, text2):
    # Split the texts into lines for comparison
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    # Use difflib to generate the unified diff
    diff = difflib.unified_diff(lines1, lines2, lineterm='')

    return list(diff)

# Example texts
text1 = """This is a sample contract.
The terms and conditions are as follows:
1. Payment will be made in 30 days.
2. Delivery will be within 45 days."""

text2 = """This is a sample contract.
1. Payment will be made in 30 days.
2. Delivery will be within 60 days."""

# Compare and print differences
differences = compare_texts(text1, text2)

# Print the differences in a readable format
print("Comparison Result:")
print("------------------")
for line in differences:
    if line.startswith('---') or line.startswith('+++') or line.startswith('@@'):
        continue  # Skip lines that indicate file names or chunk headers
    elif line.startswith('-'):
        print(f"Removed: {line[1:].strip()}")
    elif line.startswith('+'):
        print(f"Added: {line[1:].strip()}")
    else:
        print(f"Unchanged: {line.strip()}")
