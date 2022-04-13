"""
2022 by _Team_X_Official_ & kriki
Скрипт написан на основе ipapi.co
"""
import sys, time, os, random, requests, subprocess
from requests import get
from banners import *
time.sleep(0.05)
mesage = ('Приветствую!!! \nВведите 1 если вы сейчас используете OS Windows, \n2 если OS Linux, \nили 3 если Termux: ')
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.05)
    
choose_os = int(input())       # Выбор ОС
# Если ОС Windows
if choose_os == 1:
    ban = [banner1, banner2]   # Вывод
    print(random.choice(ban))  # Баннера
    print(devs)                # И
    time.sleep(3.5)            # Разработ4иков
    
    clear = lambda: os.system('cls') # очистка консоли
clear()

###################################################
#                                                 #           
#      Непосредственно наш код для Windows        #                                              
#                                                 #          
###################################################
colors = random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
target = input(colors + "Введите IP-адрес вашей цели: ")

time.sleep(0.1)
mesage = (colors + 'Цель: ' + get('https://ipapi.co/' +target+'/ip').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nГород: ' + get('https://ipapi.co/'+target+'/city').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nРегион: ' + get('https://ipapi.co/'+target+'/region').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nКод региона: ' + get('https://ipapi.co/'+target+'/region_code').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nСтрана: ' + get('https://ipapi.co/'+target+'/country').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nСтолица страны: ' + get('https://ipapi.co/'+target+'/country_capital').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nПлощядь страны: ' + get('https://ipapi.co/'+target+'/country_area').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nНаселение страны: ' + get('https://ipapi.co/'+target+'/country_population').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nКод контингента: ' + get('https://ipapi.co/'+target+'/continent_code').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nПринадлежние IP адреса стране ЕС: ' + get('https://ipapi.co/'+target+'/in_eu').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.2)
mesage = (colors + '\nПочтовый индекс: ' + get('https://ipapi.co/'+target+'/postal').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nШирота: ' + get('https://ipapi.co/'+target+'/latitude').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nДолгота: ' + get('https://ipapi.co/'+target+'/longitude').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nЧасовой пояс: ' + get('https://ipapi.co/'+target+'/timezone').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nСмещение UTC: ' + get('https://ipapi.co/'+target+'/utc_offset/').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nТелефонный код страны: ' + get('https://ipapi.co/'+target+'/country_calling_code').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nКод валюты: ' + get('https://ipapi.co/'+target+'/currency').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nНазвание валюты: ' + get('https://ipapi.co/'+target+'/currency_name').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nЯзыки общения: ' + get('https://ipapi.co/'+target+'/languages').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nНомер автономной системы(ASN): ' + get('https://ipapi.co/'+target+'/asn').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = (colors + '\nНазвание организации: ' + get('https://ipapi.co/'+target+'/org').text)
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)


lan = get('\nhttps://ipapi.co/'+target+'/latitude').text
lon = get('\nhttps://ipapi.co/'+target+'/longitude').text


time.sleep(0.1)
mesage = (colors + '\nСсылка на Google-карты: ' + 'http://www.google.com/maps/place/' + str(lan) + ',' + str(lon) + '/@' + str(lan) +','+ str(lon) + ',16z')
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.1)
mesage = ("\nСпасибо, что воспользовался скриптом. Пока!!!")
for chat in mesage:
    sys.stdout.write(chat)
    sys.stdout.flush()
    time.sleep(0.1)

# Если ОС Linux
if choose_os == 2:
    clear = lambda: os.system('clear') # очистка консоли
    clear()
    
    ban = [banner1, banner2] #рамдом баннер
    print(random.choice(ban))
    print(devs)
    time.sleep(3.5)

    clear = lambda: os.system('clear') # очистка консоли
    clear()

###################################################
#                                                 #           
#      Непосредственно наш код для OS Linux       #                                              
#                                                 #          
###################################################
    colors = random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
    target = input(colors + "Введите IP-адрес вашей цели: ")

    time.sleep(0.1)
    mesage = (colors + 'Цель: ' + get('https://ipapi.co/' +target+'/ip').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nГород: ' + get('https://ipapi.co/'+target+'/city').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nРегион: ' + get('https://ipapi.co/'+target+'/region').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nКод региона: ' + get('https://ipapi.co/'+target+'/region_code').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nСтрана: ' + get('https://ipapi.co/'+target+'/country').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nСтолица страны: ' + get('https://ipapi.co/'+target+'/country_capital').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nПлощядь страны: ' + get('https://ipapi.co/'+target+'/country_area').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nНаселение страны: ' + get('https://ipapi.co/'+target+'/country_population').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nКод контингента: ' + get('https://ipapi.co/'+target+'/continent_code').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nПринадлежние IP адреса стране ЕС: ' + get('https://ipapi.co/'+target+'/in_eu').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nПочтовый индекс: ' + get('https://ipapi.co/'+target+'/postal').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nШирота: ' + get('https://ipapi.co/'+target+'/latitude').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nДолгота: ' + get('https://ipapi.co/'+target+'/longitude').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nЧасовой пояс: ' + get('https://ipapi.co/'+target+'/timezone').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nСмещение UTC: ' + get('https://ipapi.co/'+target+'/utc_offset/').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nТелефонный код страны: ' + get('https://ipapi.co/'+target+'/country_calling_code').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nКод валюты: ' + get('https://ipapi.co/'+target+'/currency').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nНазвание валюты: ' + get('https://ipapi.co/'+target+'/currency_name').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nЯзыки общения: ' + get('https://ipapi.co/'+target+'/languages').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nНомер автономной системы(ASN): ' + get('https://ipapi.co/'+target+'/asn').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\nНазвание организации: ' + get('https://ipapi.co/'+target+'/org').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)


    lan = get('\nhttps://ipapi.co/'+target+'/latitude').text
    lon = get('\nhttps://ipapi.co/'+target+'/longitude').text


    time.sleep(0.1)
    mesage = (colors + '\nСсылка на Google-карты: ' + 'http://www.google.com/maps/place/' + str(lan) + ',' + str(lon) + '/@' + str(lan) +','+ str(lon) + ',16z')
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = ("\nСпасибо, что воспользовался скриптом. Пока!!!")
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

# Если у вас Android и используете Termux
if choose_os == 3:
    clear(chat) # очистка консоли
    
    
    ban = [banner1, banner2] #рамдом баннер
    print(random.choice(ban))
    print(devs)
    time.sleep(3.5)

    clear = lambda: os.system('clear') # очистка консоли
    clear()

###################################################
#                                                 #           
#      Непосредственно наш код для Termux       #                                              
#                                                 #          
###################################################
    colors = random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
    target = input(colors + "Введите IP-адрес вашей цели: ")

    time.sleep(0.1)
    mesage = (colors + '~#root@termux Цель: ' + get('https://ipapi.co/' +target+'/ip').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Город: ' + get('https://ipapi.co/'+target+'/city').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Регион: ' + get('https://ipapi.co/'+target+'/region').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Код региона: ' + get('https://ipapi.co/'+target+'/region_code').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Страна: ' + get('https://ipapi.co/'+target+'/country').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Столица страны: ' + get('https://ipapi.co/'+target+'/country_capital').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Площядь страны: ' + get('https://ipapi.co/'+target+'/country_area').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Население страны: ' + get('https://ipapi.co/'+target+'/country_population').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Код контингента: ' + get('https://ipapi.co/'+target+'/continent_code').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Принадлежние IP адреса стране ЕС: ' + get('https://ipapi.co/'+target+'/in_eu').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Почтовый индекс: ' + get('https://ipapi.co/'+target+'/postal').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Широта: ' + get('https://ipapi.co/'+target+'/latitude').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Долгота: ' + get('https://ipapi.co/'+target+'/longitude').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Часовой пояс: ' + get('https://ipapi.co/'+target+'/timezone').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Смещение UTC: ' + get('https://ipapi.co/'+target+'/utc_offset/').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Телефонный код страны: ' + get('https://ipapi.co/'+target+'/country_calling_code').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Код валюты: ' + get('https://ipapi.co/'+target+'/currency').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Название валюты: ' + get('https://ipapi.co/'+target+'/currency_name').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Языки общения: ' + get('https://ipapi.co/'+target+'/languages').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Номер автономной системы(ASN): ' + get('https://ipapi.co/'+target+'/asn').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Название организации: ' + get('https://ipapi.co/'+target+'/org').text)
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)


    lan = get('\nhttps://ipapi.co/'+target+'/latitude').text
    lon = get('\nhttps://ipapi.co/'+target+'/longitude').text


    time.sleep(0.1)
    mesage = (colors + '\n~#root@termux Ссылка на Google-карты: ' + 'http://www.google.com/maps/place/' + str(lan) + ',' + str(lon) + '/@' + str(lan) +','+ str(lon) + ',16z')
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.1)
    mesage = ("\n~#root@termux Спасибо, что воспользовался скриптом. Пока!!!")
    for chat in mesage:
        sys.stdout.write(chat)
        sys.stdout.flush()
        time.sleep(0.1)
