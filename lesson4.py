# number 1

from sys import argv
script_name, work_hours, money_hour, prem = argv
print("Имя скрипта: ", script_name)
print("выработка часов: ", work_hours)
print("ставка в час: ", money_hour)
print("премия: ", prem)
zar_plata = ((int(work_hours) * int(money_hour)) + int(prem))
print("зарплата= ", zar_plata)

# number 2

import random
i = int(input('input quantity of els for the list'))
n = 0
list = []
while n < i:
    number = random.randint(1,1000)
    n += 1
    list.append(number)
print(list)
new_list = [el for num, el in enumerate(list) if list[num - 1] < list[num]]
print(new_list)


# number 3

list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(list)

# number 4

i = int(input('input quantity of els for the list'))
n = 0
list = []
while n < i:
    number = int(input('input element'))
    n += 1
    list.append(number)
print(list)
new_list = [el for el in list if list.count(el) < 2]
print(new_list)

# number 5

from functools import reduce
def reducer_func(el_pr, el):
    return el_pr * el

print([el for el in range(99, 1001) if el % 2 == 0])
print(reduce(reducer_func, [el for el in range(99, 1001) if el % 2 == 0]))

# number 6

from itertools import cycle, count
my_count = count(10)
my_cycle = cycle('ABCDEF')
for i in range(20):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))