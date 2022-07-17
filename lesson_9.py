# КОРТЕЖИ - tuple

# это списки, но без возможности изменения элементов. То есть по сути это неизменямые списки
# кортежи весят меньше
# СОЗДАНИЕ
# синтаксис - круглые скобки: tuple = ()

from operator import le


tupleExample = (1, 2, 3, 2, 'test')

print(tupleExample)

# ПОЛУЧЕНИЕ ЭЛЕМЕНТА КОРТЕЖА
# так же как и в списке - по индексу через круглые скобки
# пример:
print(tupleExample[1], 'should be equal to 2')

# СРЕЗЫ
# так же возможно
print(tupleExample[1:3])


# ГЛАВНАЯ ОСОБЕННОСТЬ
# значение не переприсваиваются

# ФУНКЦИИ КОРТЕЖЕЙ
# почти все что и у списка за исключением тех, что изменяют кортеж
# * подсчет числа переданных как аргумент элементов - count
print(tupleExample.count(2))
# *len - позволяет получить длину всего кортежа
print(len(tupleExample))

#  СОЗДАНИЕ
# возможно и без круглых скобок

data = 3, 5, 9, True

print(data)

# ВАЖНО: невозможно создание кортежа из одного элемента без указания запятой

# ПЕРЕБОР
# любой цикл - while, for

for el in tupleExample:
    print(el, 'this is tuple el')

# ПРЕОБРАЗОВАНИЕ В КОРТЕЖ
# с помощью функции tuple()
nums = [5, 7, 8, 9, 10]

tupleFromList = tuple(nums)
print(tupleFromList)

# преобразование возможно и строки
stringTest = 'Some text example'
tuppleFromString = tuple(stringTest)
print(tuppleFromString)
