"""
Module include convert instruments that
convert from arab to roman and from roman to arab
"""
import re

SUB_RULES = {'IV': (4, '1'), 'IX': (9, '2'),
             'XL': (40, '3'), 'XC': (90, '4'),
             'CD': (400, '5'), 'CM': (900, '6')}

IMAGINATION = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000,
               '1': 4, '2': 9, '3': 40,
               '4': 90, '5': 400, '6': 900}

THOUSANDS_IMG = {0: ' ', 1: 'M', 2: 'MM', 3: 'MMM'}

HUNDREDS_IMG = {0: ' ', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD',
                5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

TENS_IMG = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL',
            5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}

UNITS_IMG = {0: ' ', 1: 'I', 2: 'II', 3: 'III', 4: 'IV',
             5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

roman_pt = r'^(M{0,3})(C{1,3}|CD|DC{0,3}|CM)?(X{1,3}\
                |XL|LX{0,3}|XC)?(I{1,3}|IV|VI{0,3}|IX)?$'
arab_pt = r'\d+'


def roman_to_arab(roman_string):
    for key in SUB_RULES.keys():
        roman_string = roman_string.replace(key, SUB_RULES[key][1])
    roman_list = [x for x in roman_string]
    a = list(map(lambda x: IMAGINATION[x], roman_list))
    res = sum(a)
    return res


def arab_to_roman(arab_string):
    arab_num = int(arab_string)
    if 0 <= arab_num <= 3999:
        thousand = arab_num//1000
        arab_num -= thousand*1000
        hundreds = arab_num//100
        arab_num -= hundreds*100
        tens = arab_num//10
        arab_num -= tens*10
        units = arab_num
        res = (THOUSANDS_IMG[thousand] + HUNDREDS_IMG[hundreds] +
               TENS_IMG[tens] + UNITS_IMG[units])
        return res
    return 'must be in range 1...3999'


def convert(request):
    res = ''
    inp_string = request.POST.get('data', None)
    if inp_string:
        inp_string = inp_string.strip().upper()
        if re.match(roman_pt, inp_string):
            res = roman_to_arab(inp_string)
        elif re.match(arab_pt, inp_string):
            res = arab_to_roman(inp_string)
        else:
            res = 'incorrect input'
    return res
