import requests
from pprint import pprint

def main():
    # API URL
    url = "https://aux1-7db214f2-7074-4400-abe0-2a5559030ea9.live.alta3.com/quotes"

    name = input("Enter person who said the quote: ")
    quote = input("Enter quote: ")

    data = {"name": name, "quote": quote}

   
    # Send GET request to retrieve all quotes
    response = requests.post(url, json=data)
    
    quotes = requests.get(url).json().get("quotes", [])
    # Check if the GET request was successful
    if response.status_code == 200 or response.status_code == 201:
        # quotes = response.json().get("quotes", [])
        print("Current quotes in the API:")
        pprint(quotes)

    else:
        print("Failed to retrieve quotes!")

    # TODO: Add code to send a POST request with a new quote

if __name__ == "__main__":
    main()