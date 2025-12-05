import requests
import random


def get_random_photo(url):
    cat_photo = requests.get(url)
    print(cat_photo.json())
    type_foto=cat_photo.json()['mimetype'].split('/')[-1]
    cat_photo_name = f'cat{random.randint(0, 1000)}.{type_foto}'
    print(cat_photo_name)
    cat_photo=requests.get(cat_photo.json()['url'])
    print('1')
    with open(cat_photo_name, 'wb') as file:
        file.write(cat_photo.content)
    return cat_photo_name