from sqlite3 import Timestamp
from unicodedata import category
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
    selector = Selector(text=html_content)

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("a.fn::text").get(),
        "comments_count": len(selector.css("ol.comment-list li").getall()),
        "summary": ''.join(selector.css(
            '.entry-content > p:nth-of-type(1) *::text').getall()).strip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css(".meta-category .label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
