import re

def remove_specified_items(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to find and remove specified items
    items_to_remove = ['1', '1A', '2', '3', '4', '10', '11', '12', '13', '14', '15', '16', '9', '9A', '9B', '9C']
    # Constructing regex pattern to match "Item X." and consider potential subsections like 9A, 9B, etc.
    pattern = r'Item\s(' + '|'.join(items_to_remove) + r')\..*?(?=Item\s\d+\.|$)'

    item_pattern = re.compile(pattern, re.DOTALL)

    # Remove specified items from the content
    cleaned_content = re.sub(item_pattern, '', content)

    # Write the cleaned content to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_content)

# List of input files and corresponding output files
input_files = [r'C:\Users\archishman vb\OneDrive\Desktop\Georgia_Tech\sec-edgar-filings\AAPL_10K_filtered_combined.txt', r'C:\Users\archishman vb\OneDrive\Desktop\Georgia_Tech\sec-edgar-filings\AMZN_10K_filtered_combined.txt', r'C:\Users\archishman vb\OneDrive\Desktop\Georgia_Tech\sec-edgar-filings\NVDA_10K_filtered_combined.txt']
output_files = ['aapl.txt', 'amzn.txt', 'nvda.txt']

# Loop over all files and apply the function
for input_file, output_file in zip(input_files, output_files):
    remove_specified_items(input_file, output_file)
