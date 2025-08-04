import requests

def fetch_http_headers(url):
    """
    Fetches HTTP headers from the specified URL.
    
    Args:
        url (str): The URL to fetch headers from.
        
    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes HTTP headers to extract useful information.
    
    Args:
        headers (dict): The HTTP headers to analyze.
        
    Returns:
        None
    """
    print("\n--- HTTP Header Analysis ---")
    print(f"Status Code: {headers.get('Status', 'N/A')}")
    print(f"Server: {headers.get('Server', 'N/A')}")
    print(f"Content-Type: {headers.get('Content-Type', 'N/A')}")
    print(f"Content-Length: {headers.get('Content-Length', 'N/A')}")
    print(f"Cache-Control: {headers.get('Cache-Control', 'N/A')}")
    print(f"X-Frame-Options: {headers.get('X-Frame-Options', 'N/A')}")
    print(f"X-XSS-Protection: {headers.get('X-XSS-Protection', 'N/A')}")
    print(f"Strict-Transport-Security: {headers.get('Strict-Transport-Security', 'N/A')}")
    print("------------------------------")

def main():
    """
    Main function to execute the script.
    Prompts user for a URL and fetches HTTP headers for analysis.
    
    Returns:
        None
    """
    url = input("Enter a URL (including http:// or https://): ")
    headers = fetch_http_headers(url)
    
    if headers:
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```