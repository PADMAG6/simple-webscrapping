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
      with open('sample1', 'a',encoding='utf-8') as f:
          h1 = soup.find_all('p', {"class": "review-content__text"})
          for i in h1:
             w = i.text
             f.write(w)


def url_generator(soup):
     for i in soup.find_all('nav',attrs= {'class':'pagination-container AjaxPager'}):
         if i.find('a',attrs = {'class': 'button button--primary next-page'},href= True):
             url = original_url + i.find('a',attrs = {'class': 'button button--primary next-page'},href= True)['href']
             return url
         else:
             print("No pages to check")


while True:
    soup = get_data(url)
    d1 = scarp(soup)
    url = url_generator(soup)
    #print(url)
    if not url:
        break


