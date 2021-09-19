"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress

from task_1 import host_ping


def host_range_ping():
    try:
        start = int(input('введите диапазон ip адресов от (вводить требуется только целые числа от 0 до 255): '))
        stop = int(input('введите диапазон ip адресов до (вводить требуется только целые числа от 0 до 255): '))
    except:
        print('введите валидный диапазон')
    ip_list = []
    for i in range(start, stop + 1):
        ip_list.append(ipaddress.ip_address(f'142.250.185.{i}'))
    return ip_list


host_ping(host_range_ping())
