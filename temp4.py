"""Завдання 4 (Обрахувати n-те число Фібоначчі)"""

fib1 = 1
fib2 = 1
n = int(input("Введіть число "))
i = 0
if n == 0:
    print("Число Фібоначчі дорівнює 0")
else:
    while i < n-2:
        fib_sum = fib1+fib2
        fib1 = fib2
        fib2 = fib_sum
        i=i+1
print("Число фібоначчі дорівнює ", fib2)
