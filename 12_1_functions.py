# FUNCTIONS

# FUNCTIONS
# суть функции - это подпрограмма, которая позволяет многократно выполнять по мере необходимости неоднократно используемый код в программе
# функции позволяет сократить общий объем кода всей программы блягодаря возможности вынести повторяющийся код в отдельное место
# в Python существует встроенные функции - print(), input(), etc


# СИНТАКСИС
# (1) создание - def functionName(paramsName):
# function body
# !важно - код тела функции должен отделяться одинаковым  количеством отступов
# (2) вызов - functionName()
def test_func_1():
    print('test func')
# test_func_1()


# передача параметров в функцию

def test_func_2(word):
    print(word)
# test_func_2('some word')


def test_func_3(a, b):
    res = a+b
    print('result is', res)
# test_func_3(1, 5)


# ВОЗВРАЩЕНИЕ ЗНАЧЕНИЯ ФУНКЦИЕЙ
# для возврата функцией значения необходимо указывать оператор return


def test_func_4(a, b):
    return a+b


sum = test_func_4(1, 8)
# print(sum)

# ПРИМЕР ПРОГРАММЫ (ПОИСК НАИМЕНЬШЕГО)


def findLeastNum(list):
    least = 0
    for num in list:
        if num < least:
            least = num
    return least


test_list = [100, 5, 90, 23, 25, 18, 9]
test_num_1 = findLeastNum(test_list)
print(test_num_1)
