import os
import re
from bs4 import BeautifulSoup

#base directory 
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
    company_path = os.path.join(base_directory, company, "10-K")
    output_file_path = os.path.join(base_directory, f"{company}_10K_filtered_combined.txt")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for folder in os.listdir(company_path):
            folder_path = os.path.join(company_path, folder)
            for file in os.listdir(folder_path):
                if file.endswith('.txt'):  
                    text_file_path = os.path.join(folder_path, file)
                    with open(text_file_path, 'r', encoding='utf-8') as file:
                        
                        content = file.read()
                        try:
                            soup = BeautifulSoup(content, 'html.parser')
                        except Exception:
                            try:
                                soup = BeautifulSoup(content, 'lxml')
                            except Exception:
                                print(f"Skipping file due to parsing errors: {text_file_path}")
                                continue
                        cleaned_text = soup.get_text(separator=' ', strip=True)
                        matches = section_pattern.findall(cleaned_text)
                        for match in matches:
                            output_file.write(' '.join(match) + "\n\n")

    print(f"Merged filtered sections for {company} into {output_file_path}")


