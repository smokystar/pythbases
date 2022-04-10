# Number 1

new_file = open("text_example.txt", "w+", encoding="utf-8")
i = input('write something or type "enter" to exit ')
while i != '':
    new_file.write(i)
    i = input('write something or type "enter" to exit ')
print('exit')
new_file.close()

# Number 2

my_f = open("strings and words", "r", encoding="utf-8")
counter = 0
for i in my_f:
    symbols_counter = len(i.strip())
    counter += 1
    print('string number: ', counter, '  quantity of symbols: ', symbols_counter)

# Number 3

with open("salary", "r", encoding="utf-8") as f:
    salary_info = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'avg salary = {sum(salary_info.values()) / len(salary_info)}\n'
          f'salary min 20k {[e[0] for e in salary_info.items() if e[1] < 20000]}')

# Number 4

chisl_info = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
with open("new_chisl", "w", encoding="utf-8") as new_file:
    with open("chisl", "r", encoding="utf-8") as f:
        new_file.writelines([line.replace(line.split()[0], chisl_info.get(line.split()[0])) for line in f])

# Number 5

from random import randint
with open("new_chisl", "w", encoding="utf-8") as f:
    list = [randint(1,100) for el in range(100)]
    f.write("->".join(map(str, list)))
print(sum(list))
print(len(list))

# Number 6

import re
dict = {}
with open("new_chisl") as f:
    for line in f.readlines():
        dict[re.findall(r'ˆ\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(dict)
!Пробовал решить задачу несколькими способами из видео, не работает. Не могу понять, что не так!

# Number 7

import json
open("chisl", "r", encoding="utf-8")
with open("chisl.json", "w", encoding="utf-8") as new_file, open("chisl", "r", encoding="utf-8") as file:
    profit = {line.split()[0]: (int(line.split[2])-int(line.split[3])) for line in file}
    result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                              len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, new_file, ensure_ascii=False, indent=4)
Не работает. Не могу понять, что не так!