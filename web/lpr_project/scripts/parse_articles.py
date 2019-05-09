import requests
import json
from bs4 import BeautifulSoup

URL = 'https://libertarian-party.ru'

def get_soup(url):
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup

def get_all_articles(soup):
    articles = soup.find_all('article')
    return articles

def parse_one_article(article):
    article_data = {}
    article_data['title'] = article.find('h3', class_='card-title').a.get_text()
    article_data['description'] = article.find('p', class_='card-content').get_text().strip()
    article_data['image'] = URL + article.img.get('src')
    article_data['datetime'] = article.find('time').get('datetime')
    article_data['content'] = parse_one_article_inner(article)
    return article_data

def clearify(content, exclude_attrs):
    for tag in content:
        for attr in dict(tag.attrs):
            if attr not in exclude_attrs:
                del tag.attrs[attr]
    return "".join(str(tag) for tag in content).strip()


def parse_one_article_inner(article):
    exclude_attrs = ['href','src']
    article_url = article.a.get('href')
    article_full_url = URL + article_url
    print("parsing article: "+article_full_url)
    soup = get_soup(article_full_url)
    content = soup.find('div', class_ = 'Post-Content').contents
    clear_content = clearify(content, exclude_attrs)
    return clear_content

def get_count(soup):
    count = soup.find('ul', class_='pager-next').find_all('li')[0].get_text()
    return count


def main():
    soup = get_soup(URL+'/posts')
    count = int(get_count(soup))
    articles_data = []
    for n in range(1, count+1):
        print("parsing page: "+URL+'/posts?page={}'.format(n))
        soup = get_soup(URL+'/posts?page={}'.format(n))
        articles = get_all_articles(soup)

        for article in articles:
            articles_data.append(parse_one_article(article))

    with open("articles_data.json", "w") as outfile:
        json.dump(articles_data, outfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
