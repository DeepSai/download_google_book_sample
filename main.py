import requests
import json
import os
import time

base_path = 'the_analects'
if not os.path.exists(base_path):
    os.makedirs(base_path)

def get_urls(num):
    """
    Get every page's url of certain book
    This instance is about <The Analects>
    """
    url = "https://books.google.at/books?id=77cdBQAAQBAJ&lpg=PP1&dq=%E5%82%85%E4%BD%A9%E6%A6%AE&pg=PA{}&jscmd=click3&vq=%E5%82%85%E4%BD%A9%E6%A6%AE".format(num)
    res = requests.get(url)
    res_text = json.loads(res.text)
    pages = res_text["page"]

    result = {}
    for p in pages:
        if 'src' in p:
            page_num = p['pid']
            page_src = p['src'] 
            result[page_num] = page_src
    return result

def dl_image(img_name, img_url):
    """
    Download image to local
    """
    path = os.path.join(base_path, img_name)
    res = requests.get(img_url)
    with open(path, 'wb') as fout:
        fout.write(res.content)

# Get the first 50 pages
for i in range(1,50,4):
    data = get_urls(i)
    time.sleep(3)
    for img_name, img_url in data.items():
        dl_image(img_name, img_url)
        time.sleep(3)

