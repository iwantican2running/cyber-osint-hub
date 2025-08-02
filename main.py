import requests

def get_http_headers(url):
    """
    Fetch HTTP headers from a given URL.

    Parameters:
        url (str): The URL from which to fetch headers.

    Returns:
        dict: A dictionary of HTTP headers if the request is successful, None otherwise.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyze and print key HTTP header information.

    Parameters:
        headers (dict): A dictionary of HTTP headers.

    Returns:
        None
    """
    if not headers:
        print("No headers to analyze.")
        return

    print(f"Analyzing headers for {headers.get('Host', 'Unknown Host')}:")
    print(f"Status Code: {headers.get('Status', 'N/A')}")
    print(f"Content-Type: {headers.get('Content-Type', 'N/A')}")
    print(f"Server: {headers.get('Server', 'N/A')}")
    
    # Check for security-related headers
    security_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'Content-Security-Policy', 'Strict-Transport-Security']
    for header in security_headers:
        value = headers.get(header)
        if value:
            print(f"{header}: {value}")
        else:
            print(f"{header}: Not present, consider adding for improved security.")

def main():
    """
    Main function to execute the script functionality.
    
    Collects HTTP headers from a user-provided URL and analyzes them.
    
    Returns:
        None
    """
    url = input("Enter a URL (e.g., https://example.com): ")
    headers = get_http_headers(url)
    analyze_headers(headers)

if __name__ == "__main__":
    main()
```