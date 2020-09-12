'''
HTTP - hyper text transfer protocol

GET - простой запрос, который возвращает информацию по заданному адресу
        (информацию из ресурса)

POST - это запрос на добавление информации на ресурс

PUT - запрос на изменение информации на ресурсе

DELETE - запрос на удаление информации на ресурсе
'''

'''
pip3 install requests
'''
'''
import requests

resp = requests.get('https://www.citrus.ua/printer_13')
print(type(resp))
'''

'''
 Чтоб сделать запрос с помощью requests:
 resp = requests.get(url, data={}, headers={})
    resp - это переменная, куда запишутся данные после запроса 
    по url.
    data={sth:smth} - это данные, которые мы передаем ресурсу
    ЭТО НЕ ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР
    headers={head1:value} - это заголовки НЕ ОБЯЗ ПАРАМЕТР

resp.text - отдаст тело ответа(response) в виде строки(текста) 
resp.json() - отдаст в виде словаря(json на самом деле)
resp.status_code - показывает статус код 

'''

import requests

resp = requests.get('https://random-word-api.herokuapp.com/word?number=2')
print(resp.json())
