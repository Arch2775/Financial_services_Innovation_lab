# Financial_services_Innovation_lab


I. Task 1.1 : 

1. **sec_10-k_data** :- code to download the 10-K forms from the EDGAR database from 1995 till 2023. It then stores the filings in a directory called "sec-edgar-filings"
2. **merge.py** :- code to filter the 10-k forms for the specific sections in the form, namely :-
   
   a. Item 7 -  Management’s Discussion and Analysis of Financial Condition and Results of Operations
   
   b. Item 7A - Quantitative and Qualitative Disclosures About Market Risk
   
   c. Item 8 - Financial Statements and Supplementary Data 

   and stores them in text files names "{company}_10K_filtered_combined.txt"
4. **clean.py** :- code to further clean the text files from any residual text/html tags or gibberish content.


II. Task 1.2 : 


