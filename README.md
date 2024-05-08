# Financial_services_Innovation_lab


# I. Task 1.1 : 

1. **sec_10-k_data** :- code to download the 10-K forms from the EDGAR database from 1995 till 2023. It then stores the filings in a directory called "sec-edgar-filings"
2. **merge.py** :- code to filter the 10-k forms for the specific sections in the form, namely :-
   
   a. Item 7 -  Management’s Discussion and Analysis of Financial Condition and Results of Operations
   
   b. Item 7A - Quantitative and Qualitative Disclosures About Market Risk
   
   c. Item 8 - Financial Statements and Supplementary Data 

   and stores them in text files named

     "{company}_10K_filtered_combined.txt"
4. **clean.py** :- code to further clean the text files from any residual text/html tags or gibberish content.


# II. Task 1.2 : 

1. The cleaned text files are then fed to the Google Gemini 1.5 pro LLM model in the Google AI Studio to summarize the content, make inferences and present financial data in tables.

   The model summarizes the content in Items 7,7A,8 to help users understand the company's fundamentals

   The model is prompted to make inferences of the given company's 10-K on the basis of
   
      a. Gross Margin of the company for the past 3 years.

      - **Gross margins** help investors assess a company’s profitability. 
      - We can see how well each company converts sales to profits using this margin.
      - It provides a benchmark for comparing a company’s performance with competitors.
      

      b. Table for net sales, operating expenses, cash flow from operations.

      - **Net Sales**: Helps investors assess a company's growth potential and market position.
      - **Operating Expenses**: Enables investors to gauge the efficiency and cost-effectiveness of a company's operations.
      - **Cash Flow from Operations**: Provides insight into the company's ability to generate cash to sustain and grow its operations.

      c. the company's assets and liabilities for the last 4 years.

      - **Assets**: By examining the assets, investors can evaluate a company's ability to generate future profits and its capacity for growth and sustainability.
      - **Liabilities**: The liabilities helps investors assess the company's financial risk and its ability to manage and fulfill financial obligations without compromising operational stability.

      d. "what are the potential risk factors associated with this company?" 

      - Evaluates the risks associated with the company w.r.t it's sector, competitors, geopolitical scenarios, supply-demand, economy and regulations.
      -  Investors assess these risks to make informed decisions about the potential rewards and downsides of investing in a company.

      the code for the above prompts and inferences is stored in "LLM_inferences" file.

2. The tables obtained from the LLM_inferences is then plotted using mathplotlib. the code for which is present in "plots.ipynb"

3. The frontend is created and deployed using streamlit, as it is simple to implement and deploy. (**app.py**)


## Demo

https://financialservicesinnovationlab-u77mafyjsfwuwehggdu8lg.streamlit.app/

## Tech Stack 

1. Frontend : Streamlit for UI and deployment as it is python-compatible and is easy to deploy.
2. Backend : python is used for both the tasks, .ipynb notebook for plots.
3. sec_edgar_downloader : package used to extract 10-k files from EDGAR database.


## References

1. https://www.youtube.com/watch?v=srOs3xH1sG4
2. https://www.youtube.com/watch?v=SU1L6f0N6iw&t=536s
3. https://www.youtube.com/watch?v=YL6KGYuEaSg&t=593s
4. https://www.investopedia.com/terms/l/liability.asp
5. https://einvestingforbeginners.com/gross-margins-daah/
6. https://www.netsuite.com/portal/resource/articles/financial-management/gross-profit-margin.shtml
7. https://sec-api.io/resources/extract-textual-data-from-edgar-10-k-filings-using-python
8. https://www.investopedia.com/articles/fundamental-analysis/09/form-10k.asp
9. https://www.investopedia.com/terms/1/10-k.asp
10. https://sec-edgar-downloader.readthedocs.io/en/latest/#supported-sec-filing-types

    


