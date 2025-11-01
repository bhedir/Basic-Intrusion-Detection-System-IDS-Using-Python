import requests
import time

domains = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://google.com",
    "https://github.com",
    "https://wikipedia.org"
]

# Infinite loop to keep making requests
while True:
    for url in domains:
        response = requests.get(url, headers={"Connection": "close"})
        print(f"{url} -> {response.status_code}")
    
    # Add a short delay between each full cycle (optional)
    time.sleep(2)

