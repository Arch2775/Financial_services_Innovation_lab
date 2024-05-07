import os
import re
from bs4 import BeautifulSoup

# Define the base directory where the SEC filings are stored
base_directory = r"C:\Users\archishman vb\OneDrive\Desktop\Georgia_Tech\sec-edgar-filings"

# List of company tickers
companies = ["AAPL", "NVDA", "AMZN"]

# Regular expression to match the sections
section_pattern = re.compile(r'(Item\s+7[^A].*?)(?=Item\s+\d+)|'
                             r'(Item\s+7A.*?)(?=Item\s+\d+)|'
                             r'(Item\s+8[^A].*?)(?=Item\s+\d+)',
                             re.DOTALL | re.IGNORECASE)
                             

# Iterate over each company
for company in companies:
    # Create a path for the company's 10-K filings
    company_path = os.path.join(base_directory, company, "10-K")
    # Create a new file to store the merged documents
    output_file_path = os.path.join(base_directory, f"{company}_10K_filtered_combined.txt")

    # Open the output file in write mode
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Iterate over each folder in the company's 10-K directory
        for folder in os.listdir(company_path):
            # Construct the path to the folder
            folder_path = os.path.join(company_path, folder)
            # Search for text files within the folder
            for file in os.listdir(folder_path):
                if file.endswith('.txt'):  # Check if the file is a text file
                    text_file_path = os.path.join(folder_path, file)
                    # Open the text file in read mode
                    with open(text_file_path, 'r', encoding='utf-8') as file:
                        # Read the content of the file
                        content = file.read()
                        try:
                            # Attempt to parse with html.parser
                            soup = BeautifulSoup(content, 'html.parser')
                        except Exception:
                            # If parsing fails, try with lxml
                            try:
                                soup = BeautifulSoup(content, 'lxml')
                            except Exception:
                                # If both parsers fail, skip this file
                                print(f"Skipping file due to parsing errors: {text_file_path}")
                                continue
                        # Extract text from the parsed content
                        cleaned_text = soup.get_text(separator=' ', strip=True)
                        # Find all matches of the specified items in the cleaned text
                        matches = section_pattern.findall(cleaned_text)
                        # Write each match to the output file
                        for match in matches:
                            output_file.write(' '.join(match) + "\n\n")

    print(f"Merged filtered sections for {company} into {output_file_path}")


