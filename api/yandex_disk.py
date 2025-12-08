import time

import requests
import hashlib
from api import const_test_load, constant_picture


def directory_create (directory_name, token):
    url = f'{const_test_load.const_url}?path={directory_name}'
    headers = {'Authorization': f'OAuth {token}'}
    requests.put(url, headers=headers)

def direct_create (token):
    directory_create(const_test_load.dir_path,token)


def loading_file_with_param(file_name, token):
    headers = {
                'Authorization': f'OAuth {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
    url_to_file = f'{const_test_load.const_url}/upload?path={const_test_load.dir_path}/{file_name.split("/")[-1]}'
    response_get = requests.get(url_to_file, headers=headers)
    if response_get.status_code == 200:
        dynamic_url = response_get.json()["href"]
        with open(file_name, 'rb') as f:
            requests.put(dynamic_url, f)

def directory_delete(directory_name, token):
    headers = {'Authorization': f'OAuth {token}'}
    params = {
        'path': directory_name
    }
    requests.delete(const_test_load.const_url, headers=headers, params=params)
    time.sleep(2)


def direct_del(token):
    directory_delete(const_test_load.dir_path, token)


def get_md5_for_file(file_name):
    md5_hash = hashlib.md5()
    with open(file_name, "rb") as f:
         for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def get_md5_file_yadisk(direct_name, file_name, token):
    headers = {'Authorization': f'OAuth {token}'}
    response=requests.get(direct_name,headers=headers)
    md_five=''
    for file_on_yadisk in response.json()['_embedded']['items']:
        if file_on_yadisk['name']==file_name:
            md_five=file_on_yadisk['md5']
    return md_five


def loading_file_from_url(from_url, token):
    headers = {
                'Authorization': f'OAuth {token}',
            }
    file_name = from_url.split('/')[-1]
    url_to_file = f'{const_test_load.const_url}/upload?url={from_url}&path={constant_picture.directory_path}/{file_name}'
    file_post=requests.post(url_to_file, headers=headers)
    i=0
    while requests.get(file_post.json()['href'],headers=headers).json()['status'] =='success' or i==10:
        i+=1
        time.sleep(2)

    return file_name



