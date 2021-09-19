"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок
"""
import os
from tabulate import tabulate
import _locale
_locale._getdefaultlocale = (lambda *args: ['ru', 'cp866'])

result_list = []
input_list = [
    '142',
    '142.250.185.175',
    'google.com',
    '142.250.185.177',
    '142.250.185.178',
    '142.250.185',
    '142.250.185.180',
]


def host_range_ping_tab(network_node):
    for ip in network_node:
        result = os.popen(f'ping {ip}').read()
        if "получено = 0" in result:
            result_list.append((ip, 'Узел не доступен'))
        else:
            result_list.append((ip, 'Узел доступен'))



host_range_ping_tab(input_list)

columns = ['host name', 'acces']
print(tabulate(result_list, headers=columns, tablefmt="grid"))