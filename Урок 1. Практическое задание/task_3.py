"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

import operator

"""
Задача, к сожалению не доделана в силу дефецита времени, 
но так мне понравилось элеганное первое решение, что не смог не запостить.
"""

company_dict = {'Kopor': 1033,
                'Kirish': 800,
                'SZt': 870,
                'PskG': 0,
                'Kal_TES': 900,
                'Kilingi-Nim': 640}

"""
Хороший вариант, чёткий, по питоновски.
Сложность, за счёт sorted, O(n log n)
"""


def top_comp_1(company_dict):  # O(n log n)
    return sorted(company_dict.items(), key=operator.itemgetter(1), reverse=True)[:3]


"""
Плохой вариант, не доделаный потому что.
А недоделанный, потому что плохой.
"""


def top_comp_2(company_dict):
    values = company_dict.values()
    top_company = []
    top_list = sorted(company_dict.values(), reverse=True)
    top_list_3 = top_list[:3]
    for el in top_list_3:
        return 'aaaaa, my brain'


print(top_comp_1(company_dict))
# print(top_comp_2(company_dict))