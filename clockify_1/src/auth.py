import requests
21
session = requests.Session()
session.post('https://clockify.me/login', {
     'username': 'pbobchinsky@yandex.ru',
     'password': 'AlexVlad_clockify',
     'remember': 1,
})

