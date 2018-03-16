import vk
import sys
import getpass
import requests


APP_ID = 6411046
API_VERSION = 5.73


def get_user_login():
    return input('Enter your vk.com login: ')


def get_user_password():
    return getpass.getpass(prompt='Input your vk.com password: ')


def get_friends_list(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    return api.friends.get(v=API_VERSION, fields='nickname')['items']


def output_friends_online_to_console(friends_list):
    for friend in friends_list:
        if friend['online']:
            print('{} {} is online now'.format(
                friend['first_name'],
                friend['last_name'],
            ))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_list = get_friends_list(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit('Authorization failed')
    except requests.exceptions.RequestException as error:
        sys.exit('{}\n{}'.format(
            'Cannot connect to vk.com api service',
            error,
        ))
    output_friends_online_to_console(friends_list)
