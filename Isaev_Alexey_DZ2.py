# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

list = []


def checker(op, str):
    while True:
        try:
            result = op(input(str))
            break
        except ValueError:
            continue
    return result


def dict_add():
    name = input('Введите название товара ')
    price = checker(float, 'Введите цену товара ')
    counts = checker(int, 'Введите количество товара ')
    units = input('Введите единицу измерения товара ')
    result = {'Название': name, 'Цена': price, 'Количество': counts, 'Ед.': units}
    return result


while True:
    cont = input('Для завершения ввода карточек товара введите N, для продолжения нажмите Enter ').lower();
    if cont == 'n':
        break
    else:
        my_dict = dict_add()
        list.append((len(list) + 1, my_dict))
print(*list, sep='\n')
