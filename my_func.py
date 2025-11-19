import requests

import my_const


#формирует заголовок инициализацииб проверяя наличие файла окружения  с токеном
# 1 тип - только токен
# другой тип - еще тип данных (для загрузки файла)
def head_init(token,type):
    if token:
        if type==1:
            headers = {'Authorization': f'OAuth {token}'}
        else:
            headers = {
                'Authorization': f'OAuth {token}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
    else:
        print('Нет переменной окружения с ключем "TOKEN"')

    return headers

def direct_create (url, headers):
    import requests
    # создание папки
    response = requests.put(url, headers=headers)
    # возвращаем код статуса
    return (response.status_code,response.json().get("message"))

def loading_file(filename, urlToFile, headers):

    # URL для загрузки файла на Яндекс Диск
 #   urlToFile = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={remote_filename}'

#    headers = {
 #      'Authorization': f'OAuth {token}',
 #       'Content-Type': 'application/x-www-form-urlencoded'
#    }
    # Открываем локальный файл для чтения в бинарном режиме
    with open(filename, 'rb') as f:
        # Отправляем PUT-запрос, который создает файл на диске
        responseGET = requests.get(urlToFile, headers=headers)
        if responseGET.status_code == 200:
            dynamicUrl = responseGET.json()["href"]
            response = requests.put(dynamicUrl, f)
            if response.status_code == 201:
                print("Файл успешно загружен!")
            else:
                print(f"Ошибка при загрузке файла: {response.status_code}- {response.json()['message']}")
        else:
            print(f"Ошибка при размещении файла: {responseGET.status_code}- {responseGET.json()['message']} ")
    return responseGET.status_code

def folder_del(token,folder_path,const_url,headers):
    params = {
        'path': folder_path
    }
    response = requests.delete(const_url, headers=headers, params=params)
    if response.status_code in (200, 204):
        print(f'Папка "{folder_path}" успешно удалена.')
    elif response.status_code == 202:
        print(f'Запрос на удаление папки "{folder_path}" успешно принят.')
    else:
        print(f'Ошибка при удалении папки "{folder_path}".')
        print(f'Статус код: {response.status_code}')
        print(f'Ответ: {response.text}')
    return response.status_code

def get_md5_for_file(file_path):
    import hashlib
    """
    Вычисляет MD5-хэш файла.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        str: MD5-хэш файла в виде шестнадцатеричной строки.
    """
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Считываем файл блоками по 4096 байт, чтобы не загружать весь файл в память
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def md5_file_yadisk(file_path,headers):
    response=requests.get(file_path,headers=headers)
 #   print( response.json()['_embedded']['items'][0]['md5'])
    return response.json()['_embedded']['items'][0]['md5']
