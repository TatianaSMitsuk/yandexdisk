import requests
import hashlib
import const_test_load


def direct_create (token):
    url = f'{const_test_load.const_url}?path={const_test_load.dir_path}'
    headers = {'Authorization': f'OAuth {token}'}
    requests.put(url, headers=headers)


def loading_file_with_param(file_name, token):
    headers = {
                'Authorization': f'OAuth {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
    url_to_file = f'{const_test_load.const_url}/upload?path={const_test_load.dir_path}/{file_name}'
    response_get = requests.get(url_to_file, headers=headers)
    if response_get.status_code == 200:
        dynamic_url = response_get.json()["href"]
        with open(file_name, 'rb') as f:
            requests.put(dynamic_url, f)
            f.close()


def direct_del(token):
    headers = {'Authorization': f'OAuth {token}'}
    params = {
        'path': const_test_load.dir_path
    }
    requests.delete(const_test_load.const_url, headers=headers, params=params)
    print('Убрали за собой')


def get_md5_for_file(file_name):
    md5_hash = hashlib.md5()
    with open(file_name, "rb") as f:
         for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def get_md5_file_yadisk(direct_name, file_name, token):
    headers = {'Authorization': f'OAuth {token}'}
    response=requests.get(direct_name,headers=headers)
    for file_on_ydisk in response.json()['_embedded']['items']:
        if file_on_ydisk['name']==file_name:
            md_five=file_on_ydisk['md5']
    return md_five


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


def get_three_foto_of_breed(breed):
    url_3_foto=const_test_load.url_breed+'/'+breed+'/images/random/3'
    response = requests.get(url_3_foto)
    list_foto_name=response.json()['message']
    return list_foto_name

def get_foto(url):
    dog_foto_name = url.split('/')[-1]
    print(url)
    print('Зашел', dog_foto_name)
    dog_foto = requests.get('https://images.dog.ceo/breeds/husky/blue-car-travel.jpg')
    print(dog_foto)
    print('1')
    with open(dog_foto_name, 'wb') as file:
        file.write(dog_foto.content)
        print('2')
    return dog_foto_name


def get_subbread(breed):
    url_sbb=const_test_load.url_breed+'/'+breed+'/list'
    sbb = requests.get(url_sbb)
    return sbb.json()['message']


def get_url_rand_foto_subbread(breed, sbb):
    url=const_test_load.url_breed+'/'+breed+'/'+sbb+'/images/random'
    url_file=requests.get(url)
    return url_file.json()['message']

