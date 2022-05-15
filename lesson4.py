# ПРИСВАИВАНИЕ ТИПА ДАННЫХ INTEGER
number = 5
print('res', number)
# повторное присваивание значения ранее объявленной переменной
number = 7
print('new res', number)

# удаление переменных
del number

# print(number)

# ПРИСВАИВАНИЕ ЧИСЛА С ТОЧКОЙ (FLOAT)
digit = 4.54234234
# ПРИСВАИВАНИЕ СТРОКИ (STRING)
stringVar = 'some test'
print(digit, stringVar)

# ПРИСВАИВАНИЕ БУЛЕВОГО ЗНАЧЕНИЯ (BOOLEAN) (должны писаться с первой заглавной буквы)
boolVar = False
print(boolVar)

# ПРИВЕДЕНИЕ ТИПОВ
# в Python не существует строгой типизации - т.е. не требуется при объявлении переменной
# указывать тип данных, которые она может содержать
digitStr = str(digit) #функця str осуществляет приведение к строке числа Int или Float
newWord = digitStr + stringVar
print(newWord)

str_num = '5'
newDigit = int(str_num) #функця int осуществляет приведение строки к числу
print(newDigit + digit)

# также доступны функции float(), bool() для приведения в число с точкой и в булево


