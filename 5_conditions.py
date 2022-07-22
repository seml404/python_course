# УСЛОВНЫЕ ОПЕРАТОРЫ В PYTHON
# используется ключевое слово if; при этом не требуется использовать круглые скобки
# при задании условия; после условия ожидается двоеточие, а далее - код, выполняемый при
# истинности условия, отделяемый одинаковым количество отступов

# if 5 == 5:
#     print('thats true')
#     print('!!!')

# проверки >=, <=, ==, !=

#для отрицания используется ключевое слово not; для ветвления - else и elif

# else всегда пишется в самом конце

# возможно исопользование вложенных условий

# для одновременной проверки нескольких условий требуется оператор and
# для истинности хотя бы одного условия - оператор or

userData = int(input('Введите число'))

testData = True

if testData and userData>=5:
    if(userData==5):
        print('input equals 5')
    elif(userData!=5):
        print('number is bigger than 5')
    if(userData >10):
        print(userData>10)
        print('number is bigger and than 10')
    elif(userData>7):
        print('number is bigger than 7 but less than 10')
else:
    if(testData or (userData>2)):
        print('number is not bigger than 5 but bigger than 2')
    print('number is not bigger than 5')


