"""
Scrapes English-speaking, Berlin-based, job information from Indeed
Germany including Job Title, Company, Location, Job Description
and Job URL and then outputs data to a CSV file. Outputted data
also includes date and time when scrape was performed.
"""

from datetime import datetime

import indeed_job_info as indeed

#input for location and job search
location = str(input("Enter the Metropolitan City:\t"))
#sort_type = str(input("Enter you sort_type (date/salary)\t"))
search_query = str(input("Enter the (Job_Tiltle/Company/keyword):\t"))

# Change number_of_search_pages to specify how many pages to be scraped
number_of_search_pages = int(input("Enter the number of pages to be:\t"))


# Constant variables
PAGE_RESULTS_NUMBERS = list(range(0, 300, 10))
URL_SUFFIX_NUMBERS = PAGE_RESULTS_NUMBERS[:number_of_search_pages]

# Location, sorting and language
# location = "Berlin"                this is sample 
sort_type = "date"
language = "en"
# search_query = "backend developer"             this is sample
query = search_query.replace(" ", "+")

# Time and date variables
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")
date_time_list = [current_date, current_time]

def main():
    
    # Create empty dictionary to store job listing information for each job
    
    job_dict = {}
    
    # Creating a running count that will act as a unique ID for each job listing
    
    count = 1
    
    # Loop through each page of job adverts
    for search_page in URL_SUFFIX_NUMBERS:
    
        # Create soup object for current main jobs listing page
    
        soup = indeed.main_page_setup(search_page, location, sort_type, query)
    
        # Extract job links from page
    
        job_links = indeed.prepare_job_links(soup)
    
        # Extract the times each job was posted from the main jobs page
    
        posted_times = indeed.capture_time_posted(soup)
    
        # Loop through each link, extract all data from job listing into list and add to dict
    
        for i, job_link in enumerate(job_links):
    
            # Create soup object for individual job listing page
    
            soup = indeed.single_page_setup(job_link)
    
            # Scrape individual job data from page
    
            job_data = indeed.scrape_page_data(soup)
    
            # Insert current date and time
    
            job_data = date_time_list + posted_times[i] + job_data + [job_links[i]]
    
            # Add job data to dict
    
            job_dict[count] = job_data
    
            # Increment count
    
            count += 1
    
    indeed.export_data(job_dict)

# Run program
if __name__ == '__main__':
    main()



