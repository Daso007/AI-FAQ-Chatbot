import requests
from bs4 import BeautifulSoup 

URL = "https://aws.amazon.com/s3/faqs/"

def fetch_and_clean_text(url):
    """
    This function takes a URL, fetches its HTML content, 
    and returns the clean, extracted text.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers = headers)

        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        text = soup.get_text()

        lines = (line.strip() for line in text.splitlines())
        clean_text = '\n'.join(line for line in lines if line)

        return clean_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None
    
if __name__ == "__main__":
    scraped_text = fetch_and_clean_text(URL)

    if scraped_text:
        print("--- SUCESSFULLY SCRAPED TEXT ---")
        print(scraped_text)

        with open("scraped_faq.txt", "w", encoding = "utf-8") as f:
            f.write(scraped_text)
        print("\n--- Data also saved to scraped_faq.txt ---")

