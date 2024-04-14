import requests

def query_wikipedia(search_term):
    # URL for the Wikipedia API
    api_url = "https://en.wikipedia.org/w/api.php"
    
    # Parameters for the API request
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_term
    }
    
    # Perform the request
    response = requests.get(api_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Extract search results
        search_results = data.get("query", {}).get("search", [])
        
        # Print the titles of the search results
        for result in search_results:
            print(result['title'])
            
        return(search_results[0]["title"])
    else:
        print(f"Error: {response.status_code}")

# Example usage
# query_wikipedia("What can you tell me about the Python Programming Language")

def get_wikipedia_page_details(page_title):
    # URL for the Wikipedia API
    api_url = "https://en.wikipedia.org/w/api.php"
    
    # Parameters for the API request
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
        "titles": page_title
    }
    
    # Perform the request
    response = requests.get(api_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Extract page details
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            revisions = page_info.get('revisions', [])
            if revisions:
                content = revisions[0].get('*', 'N/A')
                # Create a link to the Wikipedia page
                page_link = f"https://en.wikipedia.org/?curid={page_id}"
                return content, page_link
    else:
        print(f"Error: {response.status_code}")
        return None, None
# Example usage
# get_wikipedia_page_details("History of Python")
