# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

list = []


def checker(op, in_str):
    while True:
        try:
            result = op(input(in_str))
            break
        except ValueError:
            print('Введено некорректное значение')
            continue
    return result


def analiz(my_list):
    result = {}
    for n in range(len(my_list)):
        for key, el in my_list[n][1].items():
            result.setdefault(key, []).append(el)
    for key, el in result.items():
        print('{}: {}'.format(key, el))


def not_params(param, in_str):
    while not param:
        param = input(in_str).strip()
    return param


def dict_add():
    name = ''
    units = ''
    name = not_params(name, 'Введите название товара ')
    price = checker(float, 'Введите цену товара ')
    counts = checker(int, 'Введите количество товара ')
    units = not_params(units, 'Введите единицу измерения товара ')
    result = {'Название': name, 'Цена': price, 'Количество': counts, 'Ед.': units}
    return result


while True:
    cont = input('Для завершения ввода карточек товара введите N, для продолжения нажмите Enter ').lower();
    if cont == 'n' or cont == 'т':
        break
    else:
        my_dict = dict_add()
        list.append((len(list) + 1, my_dict))
print(*list, sep='\n')

print('\n\nАналитика по товарам')
analiz(list)
