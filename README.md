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
- Create a new directory inside the directory that contains the above files and name it 'output_data'
- Change the `NUMBER_OF_SEARCH_PAGES` variable inside of indeed_scraper.py to the number of pages you would like to extract (each page currently contains 15 job listings)
- Run indeed_scraper.py

Once the program has finished running, a CSV titled with the current date and time will be saved into the 'output_data' folder. From here, you can open the CSV file and sort through the job listing data.

---
**NOTE**

This program has been modified to search for jobs with title backend developer in the Berlin area which are then sorted by date posted. However, the `location`, `sort_type`, and `query` variables within indeed_scraper.py can be changed to generate different search results.
---
