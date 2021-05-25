import requests
import bs4
from requests_html import HTMLSession

s= HTMLSession()
original_url = "https://www.trustpilot.com"
url = "https://www.trustpilot.com/review/olacabs.com"

def get_data(url):
    res = s.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup

def scarp(soup):
    #x = []
    h1 = soup.find_all("p", {"class": "review-content__text"})
    for i in h1:
        w = i.text
        return w
      

def url_generator(soup):
     for i in soup.find_all('nav',attrs= {'class':'pagination-container AjaxPager'}):
          h0=i.find('a',attrs = {'class': 'button button--primary next-page'},href= True)['href']
          url = original_url + h0
          return url

while True:
    soup = get_data(url)
    d1 = scarp(soup)
    url = url_generator(soup)
    if not url:
        break
    

