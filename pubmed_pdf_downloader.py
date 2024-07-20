import os
import sys
from Bio import Entrez
import subprocess

#Enter your email_id here
Entrez.email = '#######@gmail.com'

def fetch_pubmed_articles(search_term, retmax=10):
    try:
        handle = Entrez.esearch(db='pubmed', term=search_term, retmax=retmax)
        search_results = Entrez.read(handle)
        handle.close()
        pmid_list = search_results['IdList']
        print("PubMed IDs found:", pmid_list)
        return pmid_list
    except Exception as e:
        print("PubMed search failed:", e)
        return []

def clone_repository(repository_url, repository_name):
    try:
        if not os.path.exists(repository_name):
            git_clone_command = ['git', 'clone', repository_url]
            result = subprocess.run(git_clone_command, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                print("Repository cloned successfully.")
            else:
                print("Failed to clone repository.")
                print("Error message:", result.stderr)
            return result.returncode == 0
        else:
            print(f"Repository '{repository_name}' already exists in the current directory. Skipping cloning.")
            return True
    except subprocess.TimeoutExpired:
        print("Git operation timed out. Check your network connection and try again.")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False

def run_fetch_pdfs(repository_name, pmid_list):
    try:
        original_dir = os.getcwd()
        print(f"Starting directory: {original_dir}")

        repo_path = os.path.join(original_dir, repository_name)
        os.chdir(repo_path)
        print(f"Changed to repository directory: {os.getcwd()}")

        pmids_str = ','.join(pmid_list)
        command = f"{sys.executable} fetch_pdfs.py -pmids {pmids_str}"
        
        print(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        print("Command output:")
        print(result.stdout)
        print("Command errors (if any):")
        print(result.stderr)

        if result.returncode == 0:
            print("fetch_pdfs.py executed successfully.")
        else:
            print("Failed to execute fetch_pdfs.py")

        print("\nContents of the current directory:")
        print(os.listdir('.'))
        
        fetched_pdfs_path = os.path.join(os.getcwd(), 'fetched_pdfs')
        if os.path.exists(fetched_pdfs_path):
            print("\nContents of fetched_pdfs folder:")
            print(os.listdir(fetched_pdfs_path))
            print(f"\nFull path of fetched_pdfs folder: {fetched_pdfs_path}")
        else:
            print(f"\nfetched_pdfs folder not found at {fetched_pdfs_path}")
            print("Searching for fetched_pdfs folder:")
            for root, dirs, files in os.walk(repo_path):
                if 'fetched_pdfs' in dirs:
                    print(f"Found fetched_pdfs at: {os.path.join(root, 'fetched_pdfs')}")
                    break
            else:
                print("Could not find fetched_pdfs folder anywhere in the repository.")

        os.chdir(original_dir)
        print(f"Changed back to original directory: {os.getcwd()}")

    except Exception as e:
        print(f"An error occurred while running fetch_pdfs.py: {e}")

def main():
    search_term = 'Dengue'
    pmid_list = fetch_pubmed_articles(search_term)
    if pmid_list:
        repository_url = 'git@github.com:billgreenwald/Pubmed-Batch-Download.git'
        repository_name = 'Pubmed-Batch-Download'
        if clone_repository(repository_url, repository_name):
            run_fetch_pdfs(repository_name, pmid_list)

if __name__ == "__main__":
    main()