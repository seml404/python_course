# ФУНКЦИИ СТРОК

# любая строка - аналогичен списку, где каждый элемент - это символ из строки


# пример - получение символа по индексу как у списка
from cgi import test
from csv import list_dialects
from itertools import count


word = 'coding'
print(word[1])

# ИСПОЛЬЗОВАНИЕ МЕТОДОВ СПИСКОВ ДЛЯ СТРОК

# вычисление длины слова
print(len(word))

# вычисление числа совпадающих элементов
print(word.count('d'), 'совпадение с переданным символом')


# ИСПОЛЬЗОВАНИЕ СПЕЦИАЛЬНЫХ СИМВОЛОВ ДЛЯ СТРОК
# отображение строки в верхнем регистре
print(word.upper())
word.isupper()
word.islower()
word.lower()
word.capitalize()
print(word.find('g'), 'индекс переданного и найденного символа')
# разбиение строки по определенному символу
stringExample = ' big, beatiful, modern'
print(stringExample.split(' ,'), "результат разбиения строки по символу `запятая`")
stringSplittedList = stringExample.split(',')
print(stringSplittedList[1], 'работа с созданным списком')
# возможно разбивать по несколько символам

#
for counter in range(len(stringSplittedList)):
    #  Функция range является одной из встроенных функций, доступных в Python. Он генерирует серию целых чисел, от значения start до stop
    # print(counter)
    # print(stringSplittedList[counter].upper())
    stringSplittedList[counter] = stringSplittedList[counter].upper()
    # stringExample.join(
    #     ', and these characteristics capitalized are')
    res = ','.join(
        stringSplittedList)


# метод Join позволяет объединять элементы списка в строку.
print(res)


# ИНДЕКСЫ И СРЕЗЫ
# можно применять как к строкам так и спискам
# срезы - это обращение сразу к нескольким индексам
# синтаксис: word[start:end]
testWord = 'Footbal is the best game in the world.'
print(testWord[3:13])
print(testWord[3:])
print(testWord[3:-1])
# можно указывать шаг
print(testWord[1:-1:3])


# на примере списка
listExample = [67, 123, 'mock text', 9.9, 982, 'some other text']

print(listExample[1:5:2])

# срезы - отличнй сортировщик-можно указывать только некоторые из параметров
print(listExample[::-1])
# Отрицательное значение возвращает перевернутый список
