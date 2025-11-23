
from dotenv import load_dotenv
import os
import function_test_load
import const_test_load

load_dotenv()
TOKEN = os.getenv('TOKEN')

# создание папки
code_dir_create=function_test_load.direct_create(const_test_load.url, function_test_load.head_init(TOKEN,1))

#  Проверьте результат
if code_dir_create[0] == 201:
    print(f'Папка "{const_test_load.folder_path}" успешно создана!')
else:
    print(f'Ошибка при создании папки: {code_dir_create[0]} - {code_dir_create[1]}')
#грузим файл
function_test_load.loading_file(const_test_load.file_name,const_test_load.url_to_file,function_test_load.head_init(TOKEN,2))
md5_file_in=function_test_load.get_md5_for_file(const_test_load.file_name)
print(md5_file_in)
print(function_test_load.md5_file_yadisk(const_test_load.url , function_test_load.head_init(TOKEN,1)))


print("Убрать за собой?")
input()
function_test_load.folder_del(TOKEN,const_test_load.folder_path,const_test_load.const_url,function_test_load.head_init(TOKEN,1))
