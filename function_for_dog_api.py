import requests
import const_test_load
import random


def get_list_of_breed():
    response=requests.get(const_test_load.url_breed+'s/list/all')
    breed=[]
    breed_with_subb=[]
    for key,value in response.json()['message'].items():
        if len(value)==0:
            breed.append(key)
        else:
            breed_with_subb.append(key)
    return breed, breed_with_subb


def get_three_photo_of_breed(breed):
    url_3_photo=const_test_load.url_breed+'/'+breed+'/images/random/3'
    response = requests.get(url_3_photo)
    list_photo_name=response.json()['message']
    return list_photo_name

def get_photo(url):
    dog_photo_name = url.split('/')[-1]
    dog_photo = requests.get(url)
    with open(dog_photo_name, 'wb') as file:
        file.write(dog_photo.content)
    return dog_photo_name


def get_subbread(breed):
    url_sbb=const_test_load.url_breed+'/'+breed+'/list'
    sbb = requests.get(url_sbb)
    return sbb.json()['message']


def get_url_rand_photo_subbread(breed, sbb):
    url=const_test_load.url_breed+'/'+breed+'/'+sbb+'/images/random'
    url_file=requests.get(url)
    return url_file.json()['message']


def form_list_breed_and_sbb_photo():
    breed, breed_with_subb = get_list_of_breed()

    br = random.choice(breed_with_subb)
    sbb_list = get_subbread(br)
    url_photo_sbb = []
    for sbb in sbb_list:
        url = get_url_rand_photo_subbread(br, sbb)
        url_photo_sbb.append(url)

    br = random.choice(breed)
    url_photo = get_three_photo_of_breed(br)
    return url_photo, url_photo_sbb