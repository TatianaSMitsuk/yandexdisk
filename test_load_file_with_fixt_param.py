import dotenv
import os
import function_load
import const_test_load
import time
import pytest



dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')


@pytest.fixture(params=["1.mp3",'example.txt'])
def fixt_file_load(request):
    const_test_load.file_name=request.param
    function_load.direct_create(TOKEN)
    function_load.loading_file(TOKEN)

    yield

    function_load.direct_del(TOKEN)
    time.sleep(2)


def test_load_file (fixt_file_load):
    md5_file_in = function_load.get_md5_for_file(const_test_load.file_name)
    url = f'{const_test_load.const_url}?path={const_test_load.dir_path}'
    assert  str(md5_file_in) == str(function_load.get_md5_file_yadisk(url, TOKEN))
