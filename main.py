import tkinter as tk
from tkinter import filedialog
import requests

TOKEN = 'y0__xDqrBQY6LQ7IIOqpoYVuUh3KWnuPCUeTEDZh0X16-4fFxY'
folder_path = '/MyCreateDirectory4'

# URL-запроса
url = f'https://cloud-api.yandex.net/v1/disk/resources?path={folder_path}'

# заголовки авторизации
headers = {'Authorization': f'OAuth {TOKEN}'}

# создание папки
response = requests.put(url, headers=headers)

#  Проверьте результат
if response.status_code == 201:
    print(f'Папка "{folder_path}" успешно создана!')
else:
    print(f'Ошибка при создании папки: {response.status_code} - {response.json()["message"]}')


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

remote_filename = folder_path + '/' + file_path.split('/')[-1]

# URL для загрузки файла на Яндекс Диск
urlToFile = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={remote_filename}'

headers = {
    'Authorization': f'OAuth {TOKEN}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
# Открываем локальный файл для чтения в бинарном режиме

with open(file_path, 'rb') as f:
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


