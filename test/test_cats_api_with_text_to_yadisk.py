import dotenv
import os

from api import cat_api, const_for_cats, const_test_load as cnst, yandex_disk as f
import pytest


dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

@pytest.fixture
def fixt_cat_api_to_yadisk():
    f.direct_create(TOKEN)

    yield

    f.direct_del(TOKEN)


@pytest.mark.parametrize('text', const_for_cats.title)
def test_load_file (fixt_cat_api_to_yadisk,text):

    cat_photo= cat_api.get_random_photo(f'{const_for_cats.cats_url}/says/{text}?json=true')
    f.loading_file_with_param(cat_photo,TOKEN)
    url_md5 = f'{cnst.const_url}?path={cnst.dir_path}&limit={str(len(const_for_cats.title))}'
    assert f.get_md5_for_file(cat_photo)==f.get_md5_file_yadisk(url_md5,cat_photo,TOKEN)
    os.remove(cat_photo)
