#в python существуют 2 вида цикла - (1) for; (2) while


#for

#range - это специальный метод в python
# первый парамет - начальное значение; второй - конечное значение; третий - шаг
for i in range(1, 6, 2):
    print(i)

#возможно перебирать строки
testWord = 'somes tring'
for i in testWord:
    print(i)

#поиск символа в строке
count = 0
testWord = 'some tring and its fine!'
for i in testWord:
    if(i=='e'):
        count += 1
print(count)