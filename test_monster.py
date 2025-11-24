
#from dotenv import load_dotenv
#import os
import function_load
import const_test_load
import pytest
import requests

#load_dotenv()
#TOKEN = os.getenv('TOKEN')
TOKEN='y0__xDqrBQY6LQ7IIOqpoYVuUh3KWnuPCUeTEDZh0X16-4fFxY'


@pytest.fixture(params=['example.txt',"1.mp3"])
def f_file_load(request):
    const_test_load.file_name=request.param
    code_dir_create = function_load.direct_create(const_test_load.url, function_load.head_init(TOKEN, 1))
    if code_dir_create[0] == 201:
        print(f'Папка "{const_test_load.folder_path}" успешно создана!')
    else:
        print(f'Ошибка при создании папки: {code_dir_create[0]} - {code_dir_create[1]}')

    function_load.loading_file(const_test_load.file_name, const_test_load.url_to_file, function_load.head_init(TOKEN, 2))

    yield

    function_load.folder_del(TOKEN, const_test_load.folder_path, const_test_load.const_url, function_load.head_init(TOKEN, 1))


def test_load_file (f_file_load):
    md5_file_in = function_load.get_md5_for_file(const_test_load.file_name)
    assert  str(md5_file_in) == str(function_load.md5_file_yadisk(const_test_load.url, function_load.head_init(TOKEN, 1)))
