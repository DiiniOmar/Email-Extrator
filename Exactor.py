import requests
import re
from bs4 import BeautifulSoup

# List of websites to scrape for email addresses
websites = [
    "http://www.example.co.uk/",
    "https://example.co.uk/",
   

]

# Regular expression pattern to match email addresses
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'


# Function to extract emails from a given website
def extract_emails_from_website(url):
    try:
        print(f"Scraping {url}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)  # Fetch the website content with a 10-second timeout
        response.raise_for_status()  # Raise an exception if the request failed

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all email addresses from the page content
        emails = re.findall(email_pattern, soup.get_text())

        # Remove duplicates by converting to a set, then back to a list
        unique_emails = list(set(emails))
        print(f"Found {len(unique_emails)} email(s) on {url}: {unique_emails}\n")
        return unique_emails
    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape {url}: {e}\n")
        return []


# Dictionary to store emails found on each website
all_emails = {}

# Loop through each website and extract emails
for website in websites:
    emails = extract_emails_from_website(website)
    all_emails[website] = emails

# Display the extracted emails from all websites
print("Summary of extracted emails:")
for website, emails in all_emails.items():
    print(f"{website}: {emails}")
