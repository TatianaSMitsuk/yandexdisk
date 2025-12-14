
import dotenv
import os
from api import constant_picture, const_test_load as constant, yandex_disk as f
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

@pytest.fixture
def fixt_picture_to_yadisk():
    f.directory_create(constant_picture.directory_path, TOKEN)

    yield

    f.directory_delete(constant_picture.directory_path, TOKEN)

@pytest.mark.parametrize('picture', constant_picture.three_picture)
def test_load_file (fixt_picture_to_yadisk,picture):
    file_name=f.loading_file_from_url(picture,TOKEN)
    url_md5 = f'{constant.const_url}?path={constant_picture.directory_path}&limit={str(len(constant_picture.three_picture))}'
    md5=f.get_md5_file_yadisk(url_md5,file_name,TOKEN)
    assert md5



