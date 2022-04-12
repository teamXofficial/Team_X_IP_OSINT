"""
2022 by _Team_X_Official_
Скрипт написан на основе ipapi.co

"""
import random, requests
from requests import get
from banner import *
print(banner)
colors = random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
target = input(colors + "Введите IP-адрес вашей цели: ")
print(colors + 'Цель: ' + get('https://ipapi.co/' +target+'/ip').text)
print(colors + 'Город: ' + get('https://ipapi.co/'+target+'/city').text)
print(colors + 'Регион: ' + get('https://ipapi.co/'+target+'/region').text)
print(colors + 'Код региона: ' + get('https://ipapi.co/'+target+'/region_code').text)
print(colors + 'Страна: ' + get('https://ipapi.co/'+target+'/country').text)
print(colors + 'Столица страны: ' + get('https://ipapi.co/'+target+'/country_capital').text)
print(colors + 'Площядь страны: ' + get('https://ipapi.co/'+target+'/country_area').text)
print(colors + 'Население страны: ' + get('https://ipapi.co/'+target+'/country_population').text)
print(colors + 'Код контингента: ' + get('https://ipapi.co/'+target+'/continent_code').text)
print(colors + 'Принадлежние IP адреса стране ЕС: ' + get('https://ipapi.co/'+target+'/in_eu').text)
print(colors + 'Почтовый индекс: ' + get('https://ipapi.co/'+target+'/postal').text)
print(colors + 'Широта: ' + get('https://ipapi.co/'+target+'/latitude').text)
print(colors + 'Долгота: ' + get('https://ipapi.co/'+target+'/longitude').text)
print(colors + 'Часовой пояс: ' + get('https://ipapi.co/'+target+'/timezone').text)
print(colors + 'Смещение UTC: ' + get('https://ipapi.co/'+target+'/utc_offset/').text)
print(colors + 'Телефонный код страны: ' + get('https://ipapi.co/'+target+'/country_calling_code').text)
print(colors + 'Код валюты: ' + get('https://ipapi.co/'+target+'/currency').text)
print(colors + 'Название валюты: ' + get('https://ipapi.co/'+target+'/currency_name').text)
print(colors + 'Языки общения: ' + get('https://ipapi.co/'+target+'/languages').text)
print(colors + 'Номер автономной системы(ASN): ' + get('https://ipapi.co/'+target+'/asn').text)
print(colors + 'Название организации: ' + get('https://ipapi.co/'+target+'/org').text)
lan = get('https://ipapi.co/'+target+'/latitude').text
lon = get('https://ipapi.co/'+target+'/longitude').text
print(colors + 'Ссылка на Google-карты: ' + 'http://www.google.com/maps/place/' + str(lan) + ',' + str(lon) + '/@' + str(lan) +','+ str(lon) + ',16z')
