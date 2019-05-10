import requests
import json
from bs4 import BeautifulSoup

URL = 'https://archive.libertarian-party.ru'

def get_soup(url):
    html_doc = requests.get(url)
    html_doc.encoding = 'utf-8'
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    return soup

def get_all_reforms(soup):
    reforms_soup = []
    for ankor in soup.select("h3 a"):
        link = URL + ankor.get("href")
        print("making soup from: " + link)
        reform  = get_soup(link)
        reforms_soup.append(reform)
    return reforms_soup

def parse_one_reform(reform):
    reform_data = {}
    reform_data['subheader'] = reform.find(id="body_content_title").get_text().split(".")[-1].strip()
    reform_data['content'] = str(reform.find(id="main-content"))
    print("reform parsed: "+reform_data['subheader'])
    return reform_data


def main():
    reforms_data = []
    soup = get_soup(URL+'/nashi-printsipy/programma')
    reforms_soup = get_all_reforms(soup)

    for reform in reforms_soup:
        reforms_data.append(parse_one_reform(reform))

    fixture_data = []
    pk_count = 1
    for reform in reforms_data:
        entry = {}
        entry['model'] = "principles_app.reform"
        entry['pk'] = pk_count
        entry['fields'] = {}
        entry['fields']['header'] = ""
        entry['fields']['subheader'] = reform['subheader']
        entry['fields']['content'] = reform['content']
        fixture_data.append(entry)
        pk_count += 1

    with open("reforms.json", "w") as outfile:
        json.dump(fixture_data, outfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
