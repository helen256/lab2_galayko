"""Завдання if5 (чи має заданий двовимірний список цілих має горизонтальну вісь симетрії)"""

print("Введіть розмір масиву (m*n)")
def getNumber_m():
    while True:
        m = input("Введіть m ")
        if m.isdigit() : return m
        print("Введене m не є число або є не цілим число. Введіть ще раз")

m = int(getNumber_m())

def getNumber_n():
    while True:
        n = input("Введіть n ")
        if n.isdigit() : return n
        print("Введене n не є число або є не цілим числом. Введіть ще раз")

n = int(getNumber_n())

def check_n(n):
    while True:
        n = int(input("Введіть n (непарне): "))
        if n%2 != 0: return n
        print("Введене число парне, буде неможливо знайти горизонтальну вісь симетрії. Введіть ще раз")

if n%2 == 0: n = check_n(n)

multp_numbs = n*m

print(f"Ви ввели числа {m} та {n}.Тепер введіть {multp_numbs} чисел через пробіл")

def getNumbers():
    while True:
        numbs = input("Введіть цілі числа: ").split()
        ln = len(numbs)
        for i in range(len(numbs)):
            if numbs[i].isdigit() == False:
                while numbs[i].isdigit() == False:
                    print("У введеному рядку є символ, який не відповідає значенню цілого числа. Введіть ще раз")
                    numbs = input("Введіть цілі числа: ").split()
            else:
                numbs[i] = int(numbs[i])
        if ln == multp_numbs: return numbs
        print(f"Введених чисел не {multp_numbs}, а {ln}. Введіть ще раз.")

arr_numbs = getNumbers()

lst = []
r=0
for i in range(n):
    lst.append([])
    for j in range(m):
        lst[i].append(arr_numbs[r])
        r+=1

for i in range(n):
    print(lst[i])

print("Чи має даний масив горизонтальну вісь симетрії?")

k = 0
x = 0
s = 0
n2 = n-1
n3 = n-1
q=0
while k!=(n3/2):
    q=0
    while q<m:
        if lst[x][q] == lst[n2][q]:
            print(".")
        else:
           s+=1
           break
        q+=1
    k+=1
    x+=1
    n2-=1

if s == 0:
    print("Так. Масив має горизонтальну вісь симетрії")
else:
    print("Ні. Масив не має горизонтальну вісь симетрії")



