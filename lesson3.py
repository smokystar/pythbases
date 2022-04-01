#number1
def del_numbers(a,b):
    res = a / b
    return res
try:
    print(del_numbers(int(input()), int(input())))
except ZeroDivisionError as e:
    print('на ноль делить нельзя')

#number2
def user_info(fio, bday, city, email, phone):
    info = (f"ФИО: {fio}, Дата рождения: {bday}, Город: {city}, Почта: {email}, Телефон: {phone}")
    return info
print(user_info('ааа', 2001, 'м', 'рпрр', 76885))

#number3
def function(a,b,c):
    list = [a, b, c]
    list.sort(reverse=True)
    max_1 = list[0]
    max_2 = list[1]
    sum = max_1 + max_2
    return sum
print(function(9,11,8))

#number4
def function(x, y):
    x = abs(x)
    y = -abs(y)
    pr = x ** y
    return pr
print(function(4, -1))



def function(x, y):
    num = 1
    x = abs(x)
    y = -abs(y)
    pr = x
    while num < abs(y):
        num +=1
        pr = pr * x
    res = 1/pr
    return res
print(function(4, -3))
#number5
def sum():
    n = 0
    while True:
        list = input("enter number, input 'q' to exit: ").split()
        for num in list:
            if num == "q":
                return n
            else:
                try:
                    n += int(num)
                except ValueError:
                    print("enter 'q' to exit")
        print({n})

print(sum())
#number6
def cap(*args):
    word = input('Input word')
    print(word.capitalize())
    print(word.title())
    return
cap()
