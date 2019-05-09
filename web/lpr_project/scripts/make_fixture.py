import json
import requests
import uuid
import os
from slugify import slugify
from datetime import datetime

def get_file_path(url,timestamp):
    ext = url.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    media_path = '/media/news/images/{}/{}/{}'.format(timestamp.strftime('%Y'), timestamp.strftime('%m'), timestamp.strftime('%d'), filename)
    full_path = os.path.abspath(os.path.join(__file__, "..", media_path))
    t = (media_path, full_path)
    return t

def save_image(url,timestamp_iso):
    r = requests.get(url)
    timestamp = datetime.strptime(timestamp_iso, "%Y-%m-%dT%H:%M:%S%z")
    t = get_file_path(url,timestamp)
    open(t[1], 'wb').write(r.content)
    return t[0]


def main():
    with open('articles_data.json') as file:
        data = json.load(file)
    fixture_data = []
    pk_count = 1
    for article in data:
        entry = {}
        entry['model'] = "news_app.post"
        entry['pk'] = pk_count
        entry['fields'] = {}
        entry['fields']['title'] = article['title']
        entry['fields']['description'] = article['description']
        entry['fields']['image'] = save_image(article['image'],article['datetime'])
        entry['fields']['slug'] = slugify(article['title'])
        entry['fields']['author'] = 1
        entry['fields']['body'] = article['content']
        entry['fields']['publishtime'] = article['datetime']
        entry['fields']['status'] = 'published'
        fixture_data.append(entry)
        pk_count += 1

    with open("articles_fixture.json", "w") as outfile:
        json.dump(fixture_data, outfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
