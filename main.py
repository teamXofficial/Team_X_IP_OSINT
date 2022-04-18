"""

2022 by _Team_X_Official_
     by A9_FM
     by krik
Скрипт написан на основе ipapi.co

"""

import os,random,time,colorama,requests
from colorama import init, Fore
from requests import get

init(autoreset=True)

# Баннер
colors = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])

class clear:
    def __call__(self):
        import os
        if os.name==('ce','nt','dos'): os.system('cls')
        elif os.name=='posix': os.system('clear')
        else: print('\n'*120)
        def __neg__(self): self()
        def __repr__(self):
            self();return ''
clear=clear()
    


def banner():
    ban1 = colors + """
╔════╗──────── ╔═╗╔═╗ ╔══╦═══╗ ╔═══╦═══╦══╦═╗─╔╦════╗
║╔╗╔╗║──────── ╚╗╚╝╔╝ ╚╣╠╣╔═╗║ ║╔═╗║╔═╗╠╣╠╣║╚╗║║╔╗╔╗║
╚╝║║╠╩═╦══╦╗╔╗ ─╚╗╔╝─ ─║║║╚═╝║ ║║─║║╚══╗║║║╔╗╚╝╠╝║║╚╝
──║║║║═╣╔╗║╚╝║ ─╔╝╚╗─ ─║║║╔══╝ ║║─║╠══╗║║║║║╚╗║║─║║
──║║║║═╣╔╗║║║║ ╔╝╔╗╚╗ ╔╣╠╣║─── ║╚═╝║╚═╝╠╣╠╣║─║║║─║║
──╚╝╚══╩╝╚╩╩╩╝ ╚═╝╚═╝ ╚══╩╝─── ╚═══╩═══╩══╩╝─╚═╝─╚╝
"""
    ban2 = colors + """

████████╗███████╗░█████╗░███╗░░░███╗  ██╗░░██╗  ██╗██████╗░   ░█████╗░░██████╗██╗███╗░░██╗████████╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ╚██╗██╔╝  ██║██╔══██╗   ██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
░░░██║░░░█████╗░░███████║██╔████╔██║  ░╚███╔╝░  ██║██████╔╝   ██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ░██╔██╗░  ██║██╔═══╝░   ██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██╔╝╚██╗  ██║██║░░░░░   ╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝  ╚═╝╚═╝░░░░░   ░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░

"""
    ban3 = colors + """

▀█▀ █▀▀ ▄▀█ █▀▄▀█   ▀▄▀   █ █▀█   █▀█ █▀ █ █▄░█ ▀█▀
░█░ ██▄ █▀█ █░▀░█   █░█   █ █▀▀   █▄█ ▄█ █ █░▀█ ░█░
"""
    ban4 = colors + """

┏━━━━┓╋╋╋╋╋╋╋╋ ┏━┓┏━┓ ┏━━┳━━━┓ ┏━━━┳━━━┳━━┳━┓╋┏┳━━━━┓
┃┏┓┏┓┃╋╋╋╋╋╋╋╋ ┗┓┗┛┏┛ ┗┫┣┫┏━┓┃ ┃┏━┓┃┏━┓┣┫┣┫┃┗┓┃┃┏┓┏┓┃
┗┛┃┃┣┻━┳━━┳┓┏┓ ╋┗┓┏┛╋ ╋┃┃┃┗━┛┃ ┃┃╋┃┃┗━━┓┃┃┃┏┓┗┛┣┛┃┃┗┛
╋╋┃┃┃┃━┫┏┓┃┗┛┃ ╋┏┛┗┓╋ ╋┃┃┃┏━━┛ ┃┃╋┃┣━━┓┃┃┃┃┃┗┓┃┃╋┃┃
╋╋┃┃┃┃━┫┏┓┃┃┃┃ ┏┛┏┓┗┓ ┏┫┣┫┃╋╋╋ ┃┗━┛┃┗━┛┣┫┣┫┃╋┃┃┃╋┃┃
╋╋┗┛┗━━┻┛┗┻┻┻┛ ┗━┛┗━┛ ┗━━┻┛╋╋╋ ┗━━━┻━━━┻━━┻┛╋┗━┛╋┗┛
"""
    ban5 = colors + """

█████████████████████████████████████████████████████████████████████████████ 
█─▄─▄─█▄─▄▄─██▀▄─██▄─▀█▀─▄███▄─▀─▄███▄─▄█▄─▄▄─██─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄─▄─█
███─████─▄█▀██─▀─███─█▄█─█████▀─▀█████─███─▄▄▄██─██─█▄▄▄▄─██─███─█▄▀─████─███
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄█▄▄▀▀▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀

"""
    ban6 = colors + """

▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ 　 ▀▄░▄▀ 　 ▀█▀ ░█▀▀█ 　 ░█▀▀▀█ ░█▀▀▀█ ▀█▀ ░█▄─░█ ▀▀█▀▀ 
─░█── █▀▀ █▄▄█ █─▀─█ 　 ─░█── 　 ░█─ ░█▄▄█ 　 ░█──░█ ─▀▀▀▄▄ ░█─ ░█░█░█ ─░█── 
─░█── ▀▀▀ ▀──▀ ▀───▀ 　 ▄▀░▀▄ 　 ▄█▄ ░█─── 　 ░█▄▄▄█ ░█▄▄▄█ ▄█▄ ░█──▀█ ─░█──
"""
    ban7 = colors + """

▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ 　 ▀▄▒▄▀ 　 ▀█▀ ▒█▀▀█ 　 ▒█▀▀▀█ ▒█▀▀▀█ ▀█▀ ▒█▄░▒█ ▀▀█▀▀ 
░▒█░░ █▀▀ █▄▄█ █░▀░█ 　 ░▒█░░ 　 ▒█░ ▒█▄▄█ 　 ▒█░░▒█ ░▀▀▀▄▄ ▒█░ ▒█▒█▒█ ░▒█░░ 
░▒█░░ ▀▀▀ ▀░░▀ ▀░░░▀ 　 ▄▀▒▀▄ 　 ▄█▄ ▒█░░░ 　 ▒█▄▄▄█ ▒█▄▄▄█ ▄█▄ ▒█░░▀█ ░▒█░░
"""
    banners = f"""{random.choice([ban1, ban2, ban3, ban4, ban5, ban6, ban7])}
{Fore.CYAN}
by _Team_X_Official_

TG-канал разработ4ика: @TeamXofficial0
TG #1 разработ4ка: @Team_X_Official
TG #2 разработ4ка: @I_hacked_you666
TG #3 разработ4ка: @a9_fm

{Fore.RED}[0]Главное меню
{Fore.GREEN}[1] Получить свой IP-адрес
{Fore.YELLOW}[2] Просканировать свой IP-адрес
{Fore.MAGENTA}[3] Просканировать чужой IP-адрес"""
    print(banners)
    menu = f"""{Fore.BLUE} >> """
    print(menu)
    menu = int(input())
    return menu


def script():
    menu = banner()
    # №1 Скан нашего IP
    if menu == 1:
        ip = get('https://api.ipify.org').text
        time.sleep(0.03)
        print(f'{colors}Ваш IP-адрес: {ip}')

        # Просканировать наш IP?
        print(colors + """Просканировать ваш IP?\n[1] - да\n[2] - нет""")
        sel = f"""{Fore.BLUE} >> """
        print(sel)
        sel = int(input())
        
        # Если сканируем
        if sel == 1:
            scanning(ip)
        else:
            log_out()
    # 2 Скан+вывод инфы о нашем  IP
    elif menu == 2:
        ip = get('https://api.ipify.org').text
        scanning(ip)

    # Если нужно просканить чужой IP
    elif menu == 3:
        time.sleep(0.03)
        scanning(input(colors + 'Введите IP-адрес вашей цели: '))

    # Если не сканируем
    else:
        log_out()

def scanning(ip):
    print(colors + 'IP: ' + get(f'https://ipapi.co/{ip}/ip').text)
    print(colors + 'Город: ' + get(f'https://ipapi.co/{ip}/city').text)
    print(colors + 'Регион: ' + get(f'https://ipapi.co/{ip}/region').text)
    print(colors + 'Код региона: ' + get(f'https://ipapi.co/{ip}/region_code').text)
    print(colors + 'Страна: ' + get(f'https://ipapi.co/{ip}/country').text)
    print(colors + 'Столица страны: ' + get(f'https://ipapi.co/{ip}/country_capital').text)
    print(colors + 'Площядь страны: ' + get(f'https://ipapi.co/{ip}/country_area').text)
    print(colors + 'Население страны: ' + get(f'https://ipapi.co/{ip}/country_population').text)
    print(colors + 'Код контингента: ' + get(f'https://ipapi.co/{ip}/continent_code').text)
    print(colors + 'Принадлежние IP адреса стране ЕС: ' + get(f'https://ipapi.co/{ip}/in_eu').text)
    print(colors + 'Почтовый индекс: ' + get(f'https://ipapi.co/{ip}/postal').text)
    print(colors + 'Широта: ' + get(f'https://ipapi.co/{ip}/latitude').text)
    print(colors + 'Долгота: ' + get(f'https://ipapi.co/{ip}/longitude').text)
    print(colors + 'Часовой пояс: ' + get(f'https://ipapi.co/{ip}/timezone').text)
    print(colors + 'Смещение UTC: ' + get(f'https://ipapi.co/{ip}/utc_offset/').text)
    print(colors + 'Телефонный код страны: ' + get(f'https://ipapi.co/{ip}/country_calling_code').text)
    print(colors + 'Код валюты: ' + get(f'https://ipapi.co/{ip}/currency').text)
    print(colors + 'Название валюты: ' + get(f'https://ipapi.co/{ip}/currency_name').text)
    print(colors + 'Языки общения: ' + get(f'https://ipapi.co/{ip}/languages').text)
    print(colors + 'Номер автономной системы(ASN): ' + get(f'https://ipapi.co/{ip}/asn').text)
    print(colors + 'Название организации: ' + get(f'https://ipapi.co/{ip}/org').text)

    lan = get(f'https://ipapi.co/{ip}/latitude').text
    lon = get(f'https://ipapi.co/{ip}/longitude').text

    print(colors + 'Ссылка на Google-карты: ' + 'http://www.google.com/maps/place/' + str(lan) + ',' + str(
        lon) + '/@' + str(lan) + ',' + str(lon) + ',16z')

    log_out()
 

def log_out():
    time.sleep(0.02)
    print(f"""{Fore.CYAN}Спасибо, что воспользовался скриптом. Пока!!!""")
    time.sleep(0.5)
    print(f"""{Fore.CYAN}Завершение работы скрипта через 15 сек.....""")
    time.sleep(15)
    exit()


if __name__ == "__main__":
    script()
    
