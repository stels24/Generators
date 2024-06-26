#  ГЕНЕРАТОРЫ

import itertools

def all_variants(my_str):
    temp_list = []
    for lstr_1 in range(1, len(my_str) + 1):
        temp_list.append(list(itertools.combinations(my_str, lstr_1)))
    for lstr_2 in temp_list:
        for lstr_3 in lstr_2:
            if ''.join(lstr_3) != 'ac':
                yield ''.join(lstr_3)


a = all_variants("abc")
for i in a:
    print(i)