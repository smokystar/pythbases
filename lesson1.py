#number 1
a = input('введите число')
b = input('введите число')
c = input('введите строку')
d = input('введите строку')
print(type(a), type(b), type(c), type(d))
#это действие не влияет на вывод, но если нам нужно изменить тип переменной, то можно сделать это через if или присвоить изначально через int(input())
# if type(a) == str:
#     print(int(a))
# if type(b) == str:
#     print(int(b))
print(a)
print(b)
print(c)
print(d)

#number 2

time = int(input('введите время в секундах'))
hour = 3600
minute = 60
if time < hour:
    a = 0
    b = time // 60
    c = time % 60
else:
    a = time // 3600
    b = time % 3600 // 60
    c = time % 3600 % 60
print(a,b,c, sep=':')

#number 3

n = input('введите n')
nn = n + n
nnn =n + n + n
sum = int(n) + int(nn) + int(nnn)
print(sum)

#number 4

n = input('введите n')
list = []
a = len(n)
while a >= 1:
    st = a - 1
    delit = 10 ** st
    middle = int(n) // delit
    n = int(n) % delit
    a = a - 1
    list.append(middle)
print(max(list))


#number 5

pr = int(input('введите выручку'))
ex = int(input('введите затраты'))
net_pr = pr - ex
rent = net_pr/pr
if pr > ex:
    print('выручка больше издержек')
    print('рентабельность составляет ', rent)
    q = int(input('введите число сотрудников'))
    net_pr_q = net_pr / q
    print('прибыль на каждого сотрудника', net_pr_q)
else:
    print('издержки больше выручки')

#number 6

a = int(input('start km'))
b = int(input('finish km'))
d = 1
while a < b:
    a *= 1.1
    d += 1
print(d
    
