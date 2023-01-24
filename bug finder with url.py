import requests
from bs4 import BeautifulSoup

def find_bugs(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Search for specific tags or attributes that indicate a bug
    links = soup.find_all('a', href=True)
    forms = soup.find_all('form')
    if not links:
        print("No links found.")
    else:
        print("Links found:")
        for link in links:
            print(link['href'])
    if not forms:
        print("No forms found.")
    else:
        print("Forms found.")

if __name__ == '__main__':
    url = "https://www.example.com"
    find_bugs(url)
