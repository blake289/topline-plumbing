import os
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.images.append(attr[1])

url = "https://toplineplumbing530.com/"
output_dir = "public/images/original_site"

os.makedirs(output_dir, exist_ok=True)

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
    
    parser = ImageParser()
    parser.feed(html)
    
    downloaded = 0
    for src in parser.images:
        if not src: continue
        
        img_url = urljoin(url, src)
        parsed_url = urlparse(img_url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename: continue
        filename = filename.split('?')[0] # remove query params
        
        filepath = os.path.join(output_dir, filename)
        
        try:
            print(f"Downloading {img_url} to {filepath}")
            img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(img_req, timeout=10) as img_response:
                with open(filepath, "wb") as f:
                    f.write(img_response.read())
            downloaded += 1
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            
    print(f"Done downloading {downloaded} images.")
except Exception as e:
    print(f"Error fetching website: {e}")
