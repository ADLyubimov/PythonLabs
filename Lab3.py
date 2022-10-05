#Задание 1
def SummArr(x):
    sum = 0
    arr = [int(input()) for i in range(x)]
    for i in range(x):
        sum += arr[i]
    print('Ответ к заданию 1: ',sum)
    print()

SummArr(10)



#Здание 2
def CountArr(x):
    count=0
    arr = [int(input()) for i in range(x)]
    for i in arr:
        if i == 0:
            count +=  1
    print('Ответ к заданию 2: ', count)

CountArr(10)




#Задание 3
print()

n1 = int(input('Введите число для задания 3 и получите ответ: '))
for i in range(1, n1+1):
    for j in range(1, i+1):
        print(j, end='')
    print() 


#Задание 4
print()

n2 = int(input('Введите число для задания 4 и получите ответ: '))
for i in range(1, n2+1):
    for j in range(1, i+1):
        print(j, end='')
    for j in range(1, i)[::-1]:
        print(j, end='')
    print() 