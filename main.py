import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches and returns the HTTP headers of a given URL.
    
    Args:
    url (str): The URL to retrieve headers from.
    
    Returns:
    dict: A dictionary of HTTP headers.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes HTTP headers and identifies potential security issues.
    
    Args:
    headers (dict): The HTTP headers to analyze.
    
    Returns:
    None
    """
    security_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security']
    missing_headers = [header for header in security_headers if header not in headers]
    
    if missing_headers:
        print(f"Missing security headers: {', '.join(missing_headers)}")
    else:
        print("All recommended security headers are present.")

def main():
    # Input: URL to analyze
    url = input("Enter the URL to analyze (e.g., https://example.com): ").strip()
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please include the scheme (http/https).")
        return
    
    # Fetch and analyze HTTP headers
    headers = get_http_headers(url)
    if headers:
        print("\nHTTP Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")
        
        print("\nSecurity Analysis:")
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```