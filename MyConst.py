folder_path = '/MyCreateDirectory'
file_name='example.txt'
const_url='https://cloud-api.yandex.net/v1/disk/resources'
#url для создания папки
url = f'{const_url}?path={folder_path}'
remote_filename = folder_path + '/' + file_name
#url для запроса на загрузку
urlToFile = f'{const_url}/upload?path={remote_filename}'