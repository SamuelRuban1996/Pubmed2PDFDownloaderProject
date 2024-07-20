# PubMed Article Fetcher and PDF Downloader

This Python script automates the process of searching for PubMed articles, retrieving their PMIDs (PubMed IDs), and downloading the corresponding PDF files. It uses the Entrez API for PubMed searches and a third-party tool (Pubmed-Batch-Download) for PDF downloads.

## Features

- Search PubMed for articles based on a specified search term
- Retrieve PMIDs for matching articles
- Clone the Pubmed-Batch-Download repository for PDF downloading functionality
- Attempt to download PDFs for the retrieved PMIDs
- Provide detailed output about operations and file locations

## Requirements

- Python 3.x
- Biopython library
- Git (for cloning the repository)
- Internet connection

## Installation

1. Clone this repository:
git clone https://github.com/your-username/your-repo-name.git cd your-repo-name


2. Install the required Python library:
pip install biopython


3. Ensure you have Git installed on your system.

## Usage

1. Open the `pubmed_fetch_and_download.py` file.

2. Modify the `Entrez.email` value with your email address:

Entrez.email = 'your-email@example.com'
3.	(Optional) Modify the search_term in the main() function if you want to search for a different topic: 

search_term = 'Your Search Term'
4.	Run the script: 

python pubmed_fetch_and_download.py

5.	The script will output detailed information about its progress, including: 

o	PubMed IDs found
o	Repository cloning status
o	PDF download attempts
o	File locations

6.	Look for the downloaded PDFs in the fetched_pdfs folder within the cloned Pubmed-Batch-Download repository.
Important Notes
•	The success of PDF downloads depends on various factors, including article availability and access rights. Some articles may not be freely available for download.
•	The script uses the Pubmed-Batch-Download tool, which it clones from GitHub. Make sure you have permission to use this tool and comply with its license terms.
•	Respect copyright and usage rights of the articles you download.
Troubleshooting
•	If you don't see the fetched_pdfs folder or downloaded files, check the script output for any error messages or unexpected file locations.
•	Ensure you have the necessary permissions to create folders and files in the script's running directory.
•	If you encounter issues with the Pubmed-Batch-Download tool, refer to its documentation or report issues on its GitHub repository.
Contributing
Contributions to improve the script are welcome. Please feel free to submit pull requests or open issues to discuss potential changes or report bugs.
License
[Specify your license here, e.g., MIT License, GPL, etc.]
Acknowledgements
This script uses the Biopython library and the Pubmed-Batch-Download tool. We acknowledge the creators and maintainers of these resources.


This README provides:

1. An overview of the script's functionality
2. Installation instructions
3. Usage guide
4. Important notes and considerations
5. Troubleshooting tips
6. Information on contributing and licensing

Make sure to customize the following parts:

- Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.
- Choose and specify an appropriate license for your project.
- If you make any changes to the script or its functionality, update the README accordingly.
