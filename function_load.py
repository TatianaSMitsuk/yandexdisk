import requests
import hashlib
import const_test_load


def direct_create (token):
    url = f'{const_test_load.const_url}?path={const_test_load.dir_path}'
    headers = {'Authorization': f'OAuth {token}'}
    requests.put(url, headers=headers)


def loading_file(token):
    headers = {
                'Authorization': f'OAuth {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
    url_to_file = f'{const_test_load.const_url}/upload?path={const_test_load.dir_path}/{const_test_load.file_name}'
    response_get = requests.get(url_to_file, headers=headers)
    if response_get.status_code == 200:
        dynamic_url = response_get.json()["href"]
        with open(const_test_load.file_name, 'rb') as f:
            requests.put(dynamic_url, f)


def direct_del(token):
    headers = {'Authorization': f'OAuth {token}'}
    params = {
        'path': const_test_load.dir_path
    }
    requests.delete(const_test_load.const_url, headers=headers, params=params)


def get_md5_for_file(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
         for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def md5_file_yadisk(file_path, token):
    headers = {'Authorization': f'OAuth {token}'}
    response=requests.get(file_path,headers=headers)
    return response.json()['_embedded']['items'][0]['md5']
