import dotenv
import os
import yandex_disk as f
import dog_api as fd
import const_test_load as cnst
import random
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
breed, breed_with_subb = fd.get_list_of_breed()

@pytest.fixture
def fixt_dog_fromAPI_toYAD():
    f.direct_create(TOKEN)

    yield

    f.direct_del(TOKEN)


def test_load_photo_without_sbb(fixt_dog_fromAPI_toYAD):
    br = random.choice(breed)
    url_photo_list = fd.get_three_photo_of_breed(br)

    count=0
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(url_photo_list))}'
    for url in url_photo_list:
        dog_photo_name=fd.get_photo(url)
        f.loading_file_with_param(dog_photo_name,TOKEN)
        if f.get_md5_for_file(dog_photo_name) == f.get_md5_file_yadisk(url_md5, dog_photo_name, TOKEN):
            count+=1
        os.remove(dog_photo_name)
    assert count==len(url_photo_list)


def test_load_photo_with_sbb(fixt_dog_fromAPI_toYAD):
    br = random.choice(breed_with_subb)
    sbb_list = fd.get_subbread(br)
    url_photo_list = []
    for sbb in sbb_list:
        url = fd.get_url_rand_photo_subbread(br, sbb)
        url_photo_list.append(url)

    count=0
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(url_photo_list))}'
    for url in url_photo_list:
        dog_photo_name=fd.get_photo(url)
        f.loading_file_with_param(dog_photo_name,TOKEN)
        if f.get_md5_for_file(dog_photo_name) == f.get_md5_file_yadisk(url_md5, dog_photo_name, TOKEN):
            count+=1
        os.remove(dog_photo_name)
    assert count==len(url_photo_list)