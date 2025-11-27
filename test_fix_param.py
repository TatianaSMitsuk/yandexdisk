
import dotenv
import os
import function_load
import const_test_load
import pytest
import time


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')


@pytest.fixture(params=['example.txt',"1.mp3"])
def fixt_file_load(request):
    const_test_load.file_name=request.param
    code_dir_create = function_load.direct_create(const_test_load.dir_path, TOKEN)
    if code_dir_create[0] == 201:
        print(f'Папка "{const_test_load.dir_path}" успешно создана!')
    else:
        print(f'Ошибка при создании папки: {code_dir_create[0]} - {code_dir_create[1]}')

    function_load.loading_file(const_test_load.file_name, TOKEN)

    yield

    function_load.direct_del(TOKEN, const_test_load.dir_path, const_test_load.const_url)
    time.sleep(2)


def test_load_file (fixt_file_load):
    md5_file_in = function_load.get_md5_for_file(const_test_load.file_name)
    url = f'{const_test_load.const_url}?path={const_test_load.dir_path}'
    assert  str(md5_file_in) == str(function_load.md5_file_yadisk(url, TOKEN))
