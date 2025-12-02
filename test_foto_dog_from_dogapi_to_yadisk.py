import dotenv
import os
import function_load as f
import const_test_load as cnst
import random
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
breed, breed_with_subb = f.get_list_of_breed()

@pytest.fixture
def fixt_dog_fromAPI_toYAD():
    f.direct_create(TOKEN)

    yield

    f.direct_del(TOKEN)


def test_load_foto_without_sbb(fixt_dog_fromAPI_toYAD):
    br = random.choice(breed)
    url_foto_list = f.get_three_foto_of_breed(br)

    count=0
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(url_foto_list))}'
    for url in url_foto_list:
        dog_foto_name=f.get_foto(url)
        f.loading_file_with_param(dog_foto_name,TOKEN)
        if f.get_md5_for_file(dog_foto_name) == f.get_md5_file_yadisk(url_md5, dog_foto_name, TOKEN):
            count+=1
        os.remove(dog_foto_name)
    assert count==len(url_foto_list)


def test_load_foto_with_sbb(fixt_dog_fromAPI_toYAD):
    br = random.choice(breed_with_subb)
    sbb_list = f.get_subbread(br)
    url_foto_list = []
    for sbb in sbb_list:
        url = f.get_url_rand_foto_subbread(br, sbb)
        url_foto_list.append(url)

    count=0
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(url_foto_list))}'
    for url in url_foto_list:
        dog_foto_name=f.get_foto(url)
        f.loading_file_with_param(dog_foto_name,TOKEN)
        if f.get_md5_for_file(dog_foto_name) == f.get_md5_file_yadisk(url_md5, dog_foto_name, TOKEN):
            count+=1
        os.remove(dog_foto_name)
    assert count==len(url_foto_list)