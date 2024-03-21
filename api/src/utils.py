import requests

def is_url_image(url):
    if "imgur.com" in url:
        if url.endswith((".gif", ".png", ".jpg", ".jpeg")):
            return True
        else:
            response = requests.head(url)
            content_type = response.headers.get('content-type', '')
            if content_type.startswith('image'):
                return True
            else:
                return False
    else:
        return False