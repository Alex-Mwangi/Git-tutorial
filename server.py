import urllib.request

try:
    with urllib.request.urlopen("https://www.yahoo.com") as response:
        html = response.read()
        print(html.decode('utf-8'))  # Decode the content to UTF-8

except urllib.error.URLError as e:
    print(f"Error fetching data: {e}")a