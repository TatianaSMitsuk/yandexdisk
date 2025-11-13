import tkinter as tk
from tkinter import filedialog
import requests
from dotenv import load_dotenv
import os
import MyFunc
import MyConst

load_dotenv()
TOKEN = os.getenv('TOKEN')

# создание папки
kod=MyFunc.direct_create(MyConst.url,MyFunc.head_init(TOKEN,1))

#  Проверьте результат
if kod[0] == 201:
    print(f'Папка "{MyConst.folder_path}" успешно создана!')
else:
    print(f'Ошибка при создании папки: {kod[0]} - {kod[1]}')
#грузим файл
kod=MyFunc.loading_file(MyConst.file_name,MyConst.urlToFile,MyFunc.head_init(TOKEN,2))

# удаляем
print("Убрать за собой?")
input()
MyFunc.folder_del(TOKEN,MyConst.folder_path,MyConst.const_url,MyFunc.head_init(TOKEN,1))
