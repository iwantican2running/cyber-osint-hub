import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetch the HTTP headers from a given URL.

    Args:
        url (str): The URL to fetch headers from.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        # Return the headers in a dictionary format
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return {}

def analyze_headers(headers):
    """
    Analyze and extract key information from HTTP headers.

    Args:
        headers (dict): The HTTP headers to analyze.

    Returns:
        dict: A dictionary containing interesting header information.
    """
    analysis = {
        "Content-Type": headers.get("Content-Type"),
        "Server": headers.get("Server"),
        "X-Powered-By": headers.get("X-Powered-By"),
        "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
    }
    return {k: v for k, v in analysis.items() if v}  # Filter out None values

def main():
    """
    Main function to run the OSINT header analysis.
    """
    # Example URL for analysis
    url = input("Enter a URL to analyze (e.g., https://example.com): ")
    parsed_url = urlparse(url)

    # Ensure the URL is valid
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please include the scheme (http/https).")
        return

    print(f"Fetching HTTP headers for: {url}")
    headers = get_http_headers(url)
    
    if headers:
        print("HTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("\nAnalyzed Key Information:")
        analyzed_info = analyze_headers(headers)
        for key, value in analyzed_info.items():
            print(f"{key}: {value}")
    else:
        print("No headers retrieved.")

if __name__ == "__main__":
    main()