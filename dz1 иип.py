#1
a, b = map(float, input('введите два числа:').split())
if a <= b: a = 0
print(a, b)

#2
nums = list(map(float, input("введите три числа:").split()))
nums = [x**2 if x >= 0 else x for x in nums]
print(nums)

#3
n = int(input("введите положительное целое число:"))
sumn = sum(int(el) for el in str(n))
print(sumn)


#4
nums = list(map(float, input("введите три числа:").split()))
res = [x for x in nums if 1 < x < 3]
print(res)

#5
num = int(input("введите целое число:"))
while True:
    num1 = int(input("введите следующее число:"))
    if num1 < num:
        break
    else: num = num1
print('считанное число меньше предыдущего')



#6
import math

x = float(input("введите действительное число x:"))
print("1 – возвести в квадрат; 2 – извлечь корень квадратный; 3 – вычислить синус; 4 – вычислить косинус")
action = int(input("введите номер действия:"))
if action == 1:
    print(x**2)
elif action == 2:
    print(math.sqrt(x) if x >= 0 else "корень из отрицательного числа не извлекается")
elif action == 3:
    print(math.sin(x))
elif action == 4:
    print(math.cos(x))

#7
k = float(input("введите k:"))
for i in range(2, 10):
    print(f"{i} × {k} = {i * k}")

#8
char = input("введите символ (a-f):")
if 'a' <= char <= 'f':
    print(char.upper())
else:
    print("Неверный ввод.")

#9
a, b, c, d = map(float, input("введите четыре числа:").split())
if a <= b <= c <= d:
    maxx = max(a, b, c, d)
    a = b = c = d = maxx
elif a > b > c > d:
    pass
else:
    a, b, c, d = a**2, b**2, c**2, d**2
print(a, b, c, d)

#10
m, n = map(int, input("введите m и n:").split())
for i in range(m):
    print("1 " * n)

#11
a, b = map(int, input("введите целые числа a и b:").split())
z = float(input("введите число z:"))

if b != 0:
    x = a % b
    if x == 0:
        z = z * x
    else:
        z = z / x
else:
    z = None

if z is not None:
    print(z)

#12
nums = list(map(float, input("введите последовательность чисел:").split()))
lokmax = any(nums[i] % 2 == 0 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1] for i in range(1, len(nums) - 1))
print("есть чётный локальный максимум" if lokmax else "нет чётного локального максимума")


#13
nums = list(map(int, input("введите последовательность чисел:").split()))
posl = [x for x in nums if x % 5 == 0 and x % 7 != 0]
print("количество:", len(posl), "сумма:", sum(posl))

#14
nums = list(map(float, input("введите последовательность чисел:").split()))
positive_sum = sum(x for x in nums if x > 0)
print("удвоенная сумма:", 2 * positive_sum)

#15
nums = list(map(int, input("введите последовательность чисел:").split()))
prodd = 1
for x in nums:
    if x % 7 == 0:
        prodd *= x
print(prodd)

#16
a = float(input("введите число a:"))
if -2 <= a < 2:
    f = a ** 2
else:
    f = 4
print(f"f(a) = {f}")


#17
a = float(input("введите действительное число a:"))
n = int(input("введите натуральное число n:"))

power = a ** n
print(f"а) a^n = {power}")
#пункты б и в я не поняла


#18

n, i = map(int, input("введите натуральные числа n и i:").split())
a = list(map(float, input(f"введите {n} действительных чисел:").split()))

if i <= n and i > 0:
    excluded = a[i-1]
    a_sum = sum(a) - excluded
    mean = a_sum / (n - 1)
    print(f"среднее арифметическое всех чисел, кроме a[{i}] = {excluded}: {mean}")


#19
x, y, z = map(float, input("введите действительные положительные числа:").split())
if x + y > z and x + z > y and y + z > x:
    print("а) треугольник существует")
    if x**2 + y**2 > z**2 and y**2 + z**2 > x**2 and x**2 + z**2 > y**2:
        print("остроугольный")
    else:
        print("не остроугольный")
else:
    print("треугольник с такими сторонами не существует")

#20
x, y, z = map(float, input("введите три различных числа:").split())
if x + y + z < 1:
    if x != y and x != z and y != z:
        small = min(x, y, z)
        if small == x:
            x = (y + z) / 2
        elif small == y:
            y = (x + z) / 2
        else:
            z = (x + y) / 2
    else:
        if x < y:
            x = (y + z) / 2
        else:
            y = (x + z) / 2
print(x, y, z)

#21
import math

a, b, c = map(float, input("введите a, b, c:").split())
if a == 0:
    print("a != 0")
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print("действительных корней нет")
    elif D == 0:
        print("корень один:", -b / (2 * a))
    else:
        print("корни:", (-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a))

#22
n = int(input("введите положительное число:"))
print(bin(n)[2:])
print(f'{n:b}')

