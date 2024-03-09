# the tool crawls through links on a page and converts each 
# discovered page into a PDF

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os

# use input URL
# URL of the main page
main_page_url = 'https://example.com'

def get_subpage_urls(main_page_url):
    # Send a GET request to the main page
    response = requests.get(main_page_url)
    # Initialize BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all <a> tags on the main page
    links = soup.find_all('a')
    
    # List to hold the extracted URLs
    urls = []

    for link in links:
        # Extract the href attribute from each <a> tag
        href = link.get('href')
        if href:
            # Resolve relative URLs to absolute URLs
            full_url = urljoin(main_page_url, href)
            urls.append(full_url)
    
    return urls

subpage_urls = get_subpage_urls(main_page_url)

# Print the list of URLs and extract PDF
cntr = 0
for url in subpage_urls:
    cntr += 1
    pdf_name = (str)(cntr) + '.pdf'
    print(url)
    time.sleep(2)
    #command line 
    os.system("wkhtmltopdf "+ url + " " + pdf_name)

