import dotenv
import os
import yandex_disk as f
import dog_api as fd
import const_test_load as cnst
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

url_photo, url_photo_sbb = fd.form_list_breed_and_sbb_photo()

@pytest.fixture
def fixt_dog_fromAPI_toYAD():
    f.direct_create(TOKEN)

    yield

    f.direct_del(TOKEN)

@pytest.mark.parametrize('url_photo_list',[url_photo,url_photo_sbb])
def test_load_all_file(fixt_dog_fromAPI_toYAD, url_photo_list):
    count=0
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(url_photo_list))}'
    for url in url_photo_list:
        dog_photo_name=fd.get_photo(url)
        f.loading_file_with_param(dog_photo_name,TOKEN)
        if f.get_md5_for_file(dog_photo_name) == f.get_md5_file_yadisk(url_md5, dog_photo_name, TOKEN):
            count+=1
        os.remove(dog_photo_name)
    assert count==len(url_photo_list)