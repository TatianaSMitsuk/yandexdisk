import dotenv
import os
import function_load as f
import const_test_load as cnst
import requests
import time
import random
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

breed, breed_with_subb = f.get_list_of_breed()

br = random.choice(breed_with_subb)
sbb_list = f.get_subbread(br)
print('Порода ', br, ' с подпородами ', sbb_list, '\n' * 3)
url_foto_sbb = []
for sbb in sbb_list:
    url = f.get_url_rand_foto_subbread(br, sbb)
    url_foto_sbb.append(url)

br = random.choice(breed)
print('Порода ', br, ' без подпород ', '\n')
url_foto = f.get_three_foto_of_breed(br)


@pytest.fixture
def fixt_dog_fromAPI_toYAD():
    f.direct_create(TOKEN)


    yield

    f.direct_del(TOKEN)

@pytest.mark.parametrize('url_foto_list',[url_foto,url_foto_sbb])
def test_load_all_file(fixt_dog_fromAPI_toYAD, url_foto_list):
    count=0
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(url_foto_list))}'
    for url in url_foto_list:
        dog_foto_name=f.get_foto(url)
        f.loading_file_with_param(dog_foto_name,TOKEN)
        if f.get_md5_for_file(dog_foto_name) == f.get_md5_file_yadisk(url_md5, dog_foto_name, TOKEN):
            count+=1
        os.remove(dog_foto_name)
    assert count==len(url_foto_list)