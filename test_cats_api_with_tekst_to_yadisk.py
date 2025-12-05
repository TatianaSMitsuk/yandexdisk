import dotenv
import os

import const_for_cats
import function_cat_api_with_text
import function_work_witn_api_yadisk as f
import const_test_load as cnst
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

@pytest.fixture
def fixt_cat_api_to_yadisk():
    f.direct_create(TOKEN)

    yield

    f.direct_del(TOKEN)


@pytest.mark.parametrize('text',const_for_cats.hardkod)
def test_load_file (fixt_cat_api_to_yadisk,text):

    cat_foto=function_cat_api_with_text.get_random_photo(f'{const_for_cats.cats_url}/says/{const_for_cats.hardkod[0]}?json=true')
    f.loading_file_with_param(cat_foto,TOKEN)
    assert f.get_md5_for_file(cat_foto)==f.get_md5_file_yadisk(cnst.dir_path,cat_foto,TOKEN)
    print(cat_foto)
    os.remove(cat_foto)
