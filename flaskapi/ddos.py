import requests
import time

def hit_url(url, repetitions):
    for count in range(1, repetitions + 1):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Request {count}: Success")
            else:
                print(f"Request {count}: Failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request {count}: Error - {e}")
        
        # Wait for 1 second before the next request
        time.sleep(1)

if __name__ == "__main__":
    url = "http://0.0.0.0:2224/fast"
    repetitions = int(input("Enter the number of times to hit the URL: "))
    hit_url(url, repetitions)
