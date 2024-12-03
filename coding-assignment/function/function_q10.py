Create a simple URL shortening service using Python dictionaries.
python
url_mapping = {}

def shorten_url(original_url):
    short_url = f"http://short.ly/{len(url_mapping) + 1}"
    url_mapping[short_url] = original_url
    return short_url

print(shorten_url("http://example.com"))
