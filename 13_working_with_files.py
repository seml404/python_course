# WORKING WITH FILES IN PYTHON / РАБОТА С ФАЙЛАМИ В ПАЙТОН

# любой файл перед началом работы в языке Python нужно сначала открыть - для этого существует специальная функция
# после работы с файлом его всегда необходимо закрывать; иначе будет утечка памяти


# ФУНКЦИЯ ОТКРЫТИЯ ФАЙЛОВ

# open([param_1]='path/fileName', [param_2]='name of form of working with file: w-write, a-open for exclusive createion')
# (param_2 = w) при записи в файл в нем стирается вся прошлая информация и записывается новая
# (param_2 = a) (append) при записи в файл в него добавляется новая информация, а старая не удаляется


# file_name_1 = 'lesson_13_1.txt'
#
# file = open(file_name_1, 'w+')
# file.write('some test text\n')
# file.write('new text\n')


# file_1 = open(file_name_1, 'w')
# file_1.write('testing append method')


# ФУНКЦИЯ ЗАКРЫТИЯ ФАЙЛОВ
# .close()

# file.close()


# ЗАПИСЬ В ФАЙЛ ИНФОРМАЦИИ ВВЕДЕННОЙ ПОЛЬЗОВАТЕЛЕМ

# file_name_2 = 'lesson_13_2.txt'
# data = input('Please, enter some text: ')
# file_2 = open(file_name_2, 'w')
# file_2.write(data)
# file_2.close

# СЧИТЫВАНИЕ ДАННЫХ ИЗ ФАЙЛА
# путем (1) вызова функции open и передаче в качестве второго аргумента 'r' и (2) вызова метода read на самом файле
# # функция read() принимает в качестве аргументов количество выводимых при записи симоволов
# возможно считывание по одной строке - путем вызова цикла for на полученном при ОТКРЫТИИ файла значении

file_name_3='lesson_13_3.txt'
# file_3 = open(file_name_3, 'w+')
# file_3.write('text added in Pycharm!')
# file_3.close()

# file_3 = open(file_name_3, 'r')
# file_3_content =file_3.read()
# print(file_3_content)
# file_3.close()

# построчный вывод
file = open('lesson_13_3.txt', 'r')
for line in file:
    print(line)




