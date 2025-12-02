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

f.direct_create(TOKEN)
breed,breed_with_subb = f.get_list_of_breed()

br=random.choice(breed_with_subb)
sbb_list=f.get_subbread(br)
print('Порода ',br,' с подпородами ', sbb_list, '\n'*3)
for sbb in sbb_list:
    url=f.get_url_rand_foto_subbread(br,sbb)
    print(url)
    dog_foto_name = f.get_foto(url)
    f.loading_file_with_param(dog_foto_name, TOKEN)
    print('3')
    print(f.get_md5_for_file(dog_foto_name))
    print('4')
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}'
    print(f.get_md5_file_yadisk(url_md5, dog_foto_name, TOKEN))
    print('5')
    os.remove(dog_foto_name)
    print('6')
    print('удаляем', dog_foto_name)
    time.sleep(5)
    print('Проснулись')

input('Тапни')

#print(breed_with_subb)
br=random.choice(breed)
print('Порода ',br,' без подпород ', '\n')
url_foto=f.get_three_foto_of_breed(br)
print(url_foto)
for url in url_foto:
    print(url)
    dog_foto_name=f.get_foto(url)
    f.loading_file_with_param(dog_foto_name,TOKEN)
    print('3')
    print(f.get_md5_for_file(dog_foto_name))
    print('4')
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}'
    print(f.get_md5_file_yadisk(url_md5, dog_foto_name, TOKEN))
    print('5')
    os.remove(dog_foto_name)
    print('6')
    print('удаляем', dog_foto_name)
    time.sleep(5)
    print('Проснулись')

input('Тапни')

f.direct_del(TOKEN)