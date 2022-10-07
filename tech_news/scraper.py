import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    fakeHeader = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(headers=fakeHeader, timeout=1, url=url)
        sleep(1)
        return response.text or None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("div.cs-overlay a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".next::attr(href)").get()
    return urls or None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
