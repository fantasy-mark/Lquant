# -*- coding: utf-8 -*-


def char2num(c):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6,
            '7':7, '8':8, '9':9, '.':ord('.'), '-':ord('-')}[c]


def str2int(s):
    count = 0
    decimal = 0.0
    decimal_flag = False
    negative_flag = False

    for char in s:
        num = char2num(char)
        # chr():ascii value->char, ord():char->ascii value
        if num == ord('.'):
            decimal_flag = True
            break
        if num == ord('-'):
            negative_flag = True
            continue
        count = 10 * count + num

    if decimal_flag:
        for char in s[-1::-1]:
            num = char2num(char)
            if num == ord('.'):
                break
            decimal = (decimal + num) / 10

    if negative_flag:
        return -count-decimal
    return count+decimal
