#number 1
list_len = int(input())
list = []
i = 0
while i < list_len:
    pr = input()
    list.append(pr)
    i += 1
print(list)
for element in list:
    print(type(element))

#number 2
list_len = int(input())
list = []
i = 0
middle = 0
middle1 = 0
while i < list_len:
    pr = input()
    list.append(pr)
    i += 1
if list_len % 2 == 0:
    middle = list[1]
    list[1] = list[0]
    list[0] = middle
    middle1 = list[3]
    list[3] = list[2]
    list[2] = middle1
else:
    middle = list[1]
    list[1] = list[0]
    list[0] = middle
print(list)
#number 3
month = int(input('put number from 1 to 12'))
year_time = {
1 : 'winter',
2 : 'winter',
3 : 'spring',
4 : 'spring',
5 : 'spring',
6 : 'summer',
7 : 'summer',
8 : 'summer',
9 : 'fall',
10 : 'fall',
11 : 'fall',
12 : 'winter',
}
x = year_time[month]
print(x)
#number 4
string = input("Enter string: ")
word = []
num = 1
for i in range((string.count(' ')+1)):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {num} {word[i]}")
        num += 1
    else:
        print(f" {num} {word[i][0:10]}")
        num += 1

#number 5
element = int(input('сколько человек вы хотите добавить в рейтинг? введите цифру'))
list = [7, 5, 3, 3, 2]
i = 0
while i < element:
    number = int(input('элемент рейтинга'))
    list.append(number)
    i += 1
list.sort(reverse=True)
print(list)

