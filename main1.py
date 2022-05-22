import requests
from os import path

class YaUploader:

    host = 'https://cloud-api.yandex.net'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files/'
        headers = self.get_headers()
        params = {"media_type": "image"}
        response = requests.get(url, headers=headers, params=params)
        print(response.json())

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href')

    def upload_file(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    token = "AQAAAAAFcqkgAADLW-wnk0Q3c0RFlECxHtb9Q1U"
    full_name = path.basename(r'C:\Users\MSI Ovelyan\Desktop\Homework_8\my_file.txt')
    uploader = YaUploader(token)
    uploader.upload_file(full_name, full_name)