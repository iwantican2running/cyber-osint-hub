import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetches and displays HTTP headers from a given URL.

    Args:
        url (str): The URL to fetch headers from.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url)
        # Return the HTTP headers as a dictionary
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes HTTP headers for security-related fields.

    Args:
        headers (dict): The HTTP headers to analyze.

    Returns:
        None: Prints out security-related analyses.
    """
    print("=== HTTP Security Header Analysis ===")
    security_headers = ['Strict-Transport-Security', 'X-Content-Type-Options', 
                        'X-Frame-Options', 'Content-Security-Policy', 
                        'X-XSS-Protection']

    for header in security_headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header}: Not present")

def main():
    # Example usage of the script
    url = input("Enter a URL to analyze (including http:// or https://): ")
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please include http:// or https://")
        return

    # Fetch and analyze HTTP headers
    headers = fetch_http_headers(url)
    if headers:
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```