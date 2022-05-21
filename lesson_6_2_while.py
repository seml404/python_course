# цикл while

#синтаксис: while условие тело цикла


i = 5
while i<=15:
    print (i)
    i+=3


test = True
while test:
    userInput = input('enter value ')
    if userInput == 'stop':
            test = False
            print('stopped')