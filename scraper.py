import requests
from bs4 import BeautifulSoup

def scrape_body_text(url):
    """
    Scrapes the text content from the body of a webpage.
    
    Args:
        url (str): The URL of the webpage to scrape.
        
    Returns:
        str: The text content from the body without any HTML tags.
        
    Raises:
        requests.exceptions.RequestException: If there's an error with the HTTP request.
    """
    try:
        # Send HTTP request to the URL
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the body tag
        body = soup.body
        
        if body:
            # Get all text from body, stripping HTML tags
            body_text = body.get_text(separator=' ', strip=True)
            return body_text
        else:
            return "No body tag found in the HTML content."
            
    except requests.exceptions.RequestException as e:
        return ""

# Example usage
if __name__ == "__main__":
    url = "https://example.com"
    content = scrape_body_text(url)
    print(content)