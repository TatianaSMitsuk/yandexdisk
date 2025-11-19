import my_func
import my_const
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TOKEN')

def test_dir_create():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    assert MyFunc.direct_create(MyConst.url,MyFunc.head_init(TOKEN,1))==201

def test_file_load():
    from dotenv import load_dotenv
    import os
    import my_func
    import my_const

    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    # создание папки
    kod = my_func.direct_create(my_const.url, my_func.head_init(TOKEN, 1))

    #  Проверьте результат
    if kod[0] == 201:
        print(f'Папка "{my_const.folder_path}" успешно создана!')
    else:
        print(f'Ошибка при создании папки: {kod[0]} - {kod[1]}')
    # грузим файл
    kod = my_func.loading_file(my_const.file_name, my_const.url_to_file, my_func.head_init(TOKEN, 2))
    md5_file_in = my_func.get_md5_for_file(my_const.file_name)


    assert  md5_file_in==my_func.md5_file_yadisk(my_const.url, my_func.head_init(TOKEN, 1))
    # удаляем

    my_func.folder_del(TOKEN, my_const.folder_path, my_const.const_url, my_func.head_init(TOKEN, 1))
