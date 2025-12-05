import dotenv
import os

import const_for_cats
import cat_api
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


@pytest.mark.parametrize('text',const_for_cats.title)
def test_load_file (fixt_cat_api_to_yadisk,text):

    cat_foto=cat_api.get_random_photo(f'{const_for_cats.cats_url}/says/{text}?json=true')
    f.loading_file_with_param(cat_foto,TOKEN)
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(const_for_cats.title))}'

    assert f.get_md5_for_file(cat_foto)==f.get_md5_file_yadisk(url_md5,cat_foto,TOKEN)
    os.remove(cat_foto)
