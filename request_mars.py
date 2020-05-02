import requests
from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor
import threading

def scrape_craigslist(endpoint):
    response = requests.get(endpoint)
    soup =  BeautifulSoup(response.text, 'html.parser')
    print(f'done scraping {endpoint}')

def get_urls(domain):
    response = requests.get(domain)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_href = [link.get('href') for link in soup.findAll('a', attrs={'href'})]
    return all_href

if __name__ == "__main__":
    for url in get_urls('https://houston.craigslist.org/'):
        t = threading.Thread(target=scrape_craigslist, args=(url,))
        print(f'scraping {url}')
        t.start()