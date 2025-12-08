import dotenv
import os
from api import const_test_load,  yandex_disk
import time
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')


@pytest.fixture
def fixt_file_load():
    yandex_disk.direct_create(TOKEN)

    yield

    yandex_disk.direct_del(TOKEN)
    time.sleep(2)

@pytest.mark.parametrize('file_name', [const_test_load.file_name, const_test_load.file_name_second])
def test_load_file (fixt_file_load, file_name):
    yandex_disk.loading_file_with_param(file_name, TOKEN)
    md5_file_in = yandex_disk.get_md5_for_file(file_name)
    url = f'{const_test_load.const_url}?path={const_test_load.dir_path}'
    assert  md5_file_in == yandex_disk.get_md5_file_yadisk(url, file_name.split('/')[-1],TOKEN)
