import requests
import hashlib

import const_test_load




def direct_create (dir_path, token):
    url = f'{const_test_load.const_url}?path={dir_path}'
    headers = {'Authorization': f'OAuth {token}'}
    response = requests.put(url, headers=headers)
    return (response.status_code,response.json().get("message"))

def loading_file(filename, token):
    headers = {
                'Authorization': f'OAuth {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
    url_to_file = f'{const_test_load.const_url}/upload?path={const_test_load.dir_path}/{const_test_load.file_name}'
    responseGET = requests.get(url_to_file, headers=headers)
    if responseGET.status_code == 200:
        dynamic_url = responseGET.json()["href"]
        with open(filename, 'rb') as f:
            response = requests.put(dynamic_url, f)
        if response.status_code == 201:
            print("Файл "+const_test_load.file_name+" успешно загружен!")
        else:
            print(f"Ошибка при загрузке файла: {response.status_code}- {response.json()['message']}")
    else:
        print(f"Ошибка при размещении файла: {responseGET.status_code}- {responseGET.json()['message']} ")
    return responseGET.status_code

def direct_del(token, direct_path, const_url):
    headers = {'Authorization': f'OAuth {token}'}
    params = {
        'path': direct_path
    }
    response = requests.delete(const_url, headers=headers, params=params)
    if response.status_code in (200, 204):
        print(f'Папка "{direct_path}" успешно удалена.')
    elif response.status_code == 202:
        print(f'Запрос на удаление папки "{direct_path}" успешно принят.')
    else:
        print(f'Ошибка при удалении папки "{direct_path}".')
        print(f'Статус код: {response.status_code}')
        print(f'Ответ: {response.text}')
    return response.status_code

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
