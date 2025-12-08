import dotenv
import os
import yandex_disk
import const_test_load
import time
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')


@pytest.fixture
def fixt_file_load():
    function_work_witn_api_yadisk.direct_create(TOKEN)

    yield

    function_work_witn_api_yadisk.direct_del(TOKEN)
    time.sleep(2)

@pytest.mark.parametrize('file_name',[const_test_load.file_name,const_test_load.file_name_second])
def test_load_file (fixt_file_load, file_name):
    function_load.loading_file_with_param(file_name, TOKEN)
    md5_file_in = function_load.get_md5_for_file(file_name)
    url = f'{const_test_load.const_url}?path={const_test_load.dir_path}'
    assert  str(md5_file_in) == str(function_load.get_md5_file_yadisk(url, TOKEN))
