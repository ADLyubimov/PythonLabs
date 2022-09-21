#Задание 1
a=True
b=True

print("Ответы к первой задаче:")

print(a and b)
print((a and b) or b)
print((a and b) or b)
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not (a or b))
print(1 << 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print((0b101) & (0b111) ^ (0b111) | (0b010))
print('')




#Задание 2
print("Числа для второй задачи")

m = input('Введите первое число: ')
n = input('Введите второе число: ')

if m>n:
    print("Меньшее число =",n)
elif m<n:
    print("Меньшее число =",m)
else:
    print("Числа равны")
print('')





#Задание 3 & Задание 4
print('Числа для третьей и четвертой задачи')
x = input('Введите первое число: ')
y = input('Введите второе число: ')
z = input('Введите третье число: ')

#Часть 1
print("Ответ к 3 задаче:")
if (x>y) and (x>z):
    print('Большее число =',x)
elif (y>x) and (y>z):
    print('Большее число =',y)
elif (z>y) and (z>x):
    print('Большее число =',z)
else:
    print("Числа равны")

#Часть 2
print()
print("Количество уникальных чисел среди этих 3 =", len(set([x,y,z])))






