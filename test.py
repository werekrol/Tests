import requests

def add_folder(token, file_path):
    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": f'{file_path}'},
        headers={"Authorization": f"OAuth {token}"}
    )
    return response

if __name__ == '__main__':
    add_folder(' ', 'new-folder_5')