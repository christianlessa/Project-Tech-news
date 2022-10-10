from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    new_list = []
    tech_news = search_news({"title": {"$regex": f"{title.lower()}"}})
    for news in tech_news:
        new_list.append((news["title"], news["url"]))
    return new_list


# Requisito 7
def search_by_date(date):
    try:
        new_list = []
        data = {"timestamp": datetime.fromisoformat(date).strftime("%d/%m/%Y")}

        for index in search_news(data):
            new_list.append((index["title"], index["url"]))
        return new_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    tags = []
    for index in search_news({"tags": {"$regex": tag, "$options": "i"}}):
        tags.append((index["title"], index["url"]))
    return tags


# Requisito 9
def search_by_category(category):
    new_list = []
    categories = {"category": {"$regex": category, "$options": "i"}}

    for index in search_news(categories):
        new_list.append((index["title"], index["url"]))
    return new_list
