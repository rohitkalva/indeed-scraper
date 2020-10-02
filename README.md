# Indeed.de Job Scraper

This is a simple program that extracts the following information from job listings on https://de.indeed.com/:

- Posted (When the job listing was posted - translated from German)
- Job Title
- Company
- Location
- Job Description
- Translated Description to English
- E-mail address if available
- Job URL

Two columns are also generated and prepended to the extracted data:

- Date (The date the search was performed)
- Time (The time the search was performed)

## How to use

To use the program, follow the steps below:

- Ensure both indeed_job_info.py and indeed_scraper.py are in the same directory

- Change the `NUMBER_OF_SEARCH_PAGES` variable inside of indeed_scraper.py to the number of pages you would like to extract (each page currently contains 15 job listings)
- Run indeed_scraper.py
-A file will be CSV file will be created in the same directory
-Remember this is only for jobs in Germany
-While running the above file it will ask to input 3 thing 
-1. The city you want job to be searched.
-2. Your job title.
-3. The number of pages to be searched in the website.

---
**NOTE**

This program has been modified to search for jobs with title backend developer in the Berlin area which are then sorted by date posted. However, the `location`, `sort_type`, and `query` variables within indeed_scraper.py can be changed to generate different search results.
If no need of changing the above `sort_type`.Directly run the file . As it will ask you for location , job title and no of pages to be searched in the indeed website
---
