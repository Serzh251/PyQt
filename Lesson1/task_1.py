"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""
import ipaddress
import os
import _locale
_locale._getdefaultlocale = (lambda *args: ['ru', 'cp866'])


def ip_address():
    ip_list = []
    for i in range(0, 256):
        ip_list.append(ipaddress.ip_address(f'192.168.0.{i}'))
    return ip_list


def host_ping(network_node):
    for ip in network_node:
        result = os.popen(f'ping {ip}').read()
        if "Превышен интервал ожидания для запроса" in result:
            print(f'ip {ip} - Узел не доступен' )
        else:
            print(f'ip {ip} - Узел доступен')


# host_ping(['google.com', 'mail.ru'])
# host_ping((ip_address()))
