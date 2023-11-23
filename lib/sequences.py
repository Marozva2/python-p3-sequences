#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print('[]')
    elif length == 1:
        print('[0]')
    elif length == 2:
        print('[0, 1]')
    else:
        list = [0, 1]
        while len(list) < length:
            list.append(list[-1] + list[-2])
       # print('[{}]'.format(', '.join(map(str, list))))