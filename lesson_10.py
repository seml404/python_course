# СЛОВАРЬ - DICT
# обращение к элементам происходит по ключу
# синтаксис создания - (1) литерал -  фигурные скобки, {} (2) оператор dict()
# у каждого элемента должен быть ключ, то есть название
# для получения значения элемента используются квадратные скобки

dictNo1 = {4:3}

# ключом могут быть: числа, булевы, кортежи

# НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ КАК КЛЮЧ - списки

print(dictNo1[4])


# УДОБСТВО ИСПОЛЬЗОВАНИЯ
# для описания


dictNo2 = {'code':'RU', 'name': 'Russian', 'population': 144}

print(dictNo2['name'])

dictNo3 = dict(code=2345, name='Portugal', gdp=1341234, lang='Portugal')

print(dictNo3['code'])

# МЕТОДЫ СЛОВАРЯ
# конвертация в список - .items()
# получение элемента - .get(key)
# очищение словаря - .clear()

# print(dictNo2.items())

# ПЕРЕБОР СЛОВАРЯ

# print(dictNo3.items())

# for key in dictNo3.items():
#     print(type(key))
#     print(key[1])

for key, value in dictNo3.items():
    print(key, value)
    