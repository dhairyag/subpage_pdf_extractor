# subpage_pdf_extractor
 Webpage to PDF Converter: The extraction of sub-pages from a main web page and converting them into PDF format.


This script allows you to convert all sub-pages linked from a main page on a website into individual PDF files. It uses `requests` for fetching webpage content, `BeautifulSoup` for parsing HTML to extract URLs, and `wkhtmltopdf` for converting webpages to PDFs.

## Usage
- Ensure wkhtmltopdf is installed and accessible from your command line or terminal.

- Modify the `main_page_url` variable in the script to the main page URL you want to convert sub-pages from.

- Run the script:
```sh
    python extract_subpages_pdf.py
```
The script will extract all sub-page URLs from the specified main page, convert each to a PDF file, and save them in the current working directory with sequentially numbered filenames (1.pdf, 2.pdf, etc.).

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `wkhtmltopdf`

## Installation

### Python Dependencies

Install the required Python packages using pip:

```sh
pip install requests beautifulsoup4
```

### wkhtmltopdf

wkhtmltopdf needs to be installed separately as it is a command-line tool. Follow the instructions provided on [https://wkhtmltopdf.org/](https://wkhtmltopdf.org/) to install appropriate version on local system.

Following commands will help on Ubuntu/Debian:

```sh
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

## Notes
- The script includes a delay of 2 seconds between each conversion to reduce the load on the server hosting the webpages. Adjust the time.sleep(2) call as needed based on your requirements and the website's policy.
- Ensure you have the legal right to download and convert the content of the website you target.
- Help of online search and code GenAI tools have been taken to create this repo.

## Disclaimer

The creator of this repository takes no responsibility for the accuracy, legality, or any other aspect of the content converted or generated using this tool. This software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.


