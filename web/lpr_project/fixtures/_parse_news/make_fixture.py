import json
import requests
import uuid
from slugify import slugify
from datetime import datetime
import os
import random



def get_file_path(url,timestamp):
    ext = url.split('.')[-1].lower()
    filename = '{}-{}-{}_{}.{}'.format(timestamp.strftime('%Y'),timestamp.strftime('%m'), timestamp.strftime('%d'), uuid.uuid4(), ext)
    media_path = 'news/'+filename
    return media_path


def save_image(url,timestamp_iso):
    r = requests.get(url)
    timestamp = datetime.strptime(timestamp_iso, "%Y-%m-%dT%H:%M:%S%z")
    media_path = get_file_path(url,timestamp)
    full_path = "/lpr_project/media/"+media_path
    with open(full_path, "wb+") as outfile:
        outfile.write(r.content)
        print("image saved: "+full_path)
    return media_path


def main():
    os.makedirs("/lpr_project/media/news/", exist_ok=True)
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
        entry['fields']['author'] = random.randint(1,4)
        entry['fields']['body'] = article['content']
        entry['fields']['publishtime'] = article['datetime']
        entry['fields']['createtime'] = article['datetime']
        entry['fields']['updated'] = False
        entry['fields']['status'] = 'published'
        fixture_data.append(entry)
        pk_count += 1

    with open("/lpr_project/fixtures/news.json", "w") as outfile:
        json.dump(fixture_data, outfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
