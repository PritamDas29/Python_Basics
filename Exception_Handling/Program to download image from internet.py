import urllib.request
import urllib.error
import time

# Using a more stable image source
url = "https://www.python.org/static/community_logos/python-logo.png"
filename = "python_logo.png"

try:
    # Create a request with a proper User-Agent header
    request = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    
    # Download the image
    print(f"Downloading image from: {url}")
    urllib.request.urlretrieve(url, filename)
    print(f"Image downloaded successfully as '{filename}'!")
    
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")