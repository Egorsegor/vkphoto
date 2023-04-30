import vk_api
from datetime import datetime
list = []

def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)
    upload.photo('img1.jpg', album_id, group_id)
    upload.photo('img2.jpg', album_id, group_id)
    upload.photo('img3.jpg', album_id, group_id)
    upload.photo('img4.jpg', album_id, group_id)


if __name__ == '__main__':
    main()
