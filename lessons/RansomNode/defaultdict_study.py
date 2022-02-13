# -*- coding: utf-8 -*-

from collections import defaultdict

def default_value():
    return "Tokyo"

#int関数を入れることで初期値0になる。
default_dict=defaultdict(int) #こうすることで、存在しないkeyが入力されたとき、全部初期値が返される。便利!
print(default_dict)

default_dict['Name'] = 'Taro'
default_dict['Age'] = 20
print(default_dict)

#Keyが存在する値を取得する
name= default_dict['Name']
print('I am {}!'.format(name))

#Keyが存在しない値を取得する。
from_=default_dict['from']
print('I am from {}'.format(from_))
