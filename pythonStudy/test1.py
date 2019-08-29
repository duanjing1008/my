'''
list1 = ['abcd', 788, 99.99, 'runoob', 90.11]
list2 = [123, 'duanjing']

print(list1)
print(list1[0])
print(list1[2:4])
print(list2 * 2)
print(list1 + list2)
'''

''''
number = 9
guess = 0

print("数字猜谜游戏")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if number == guess:
        print("恭喜，你答对了")

    elif number > guess:
        print("猜大了！")

    elif number < guess:
        print("猜小了")
'''

#n = 100

sum1 = 0
c = 1

while c <= 100:
    sum1 = sum1 + c
    c += 1

# print("1到%d之和为：%d" % (n, sum1))
print(sum1)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print(var)
print("goodbye")


def printinfo1( name, age=10):
    print("名字：", name)
    print("年龄", age)
    return

printinfo1(age=20, name='duanjing')
print("-----------")
printinfo1(name='jing')

lista = [1, 2, 3, 4]
i = iter(lista)
print(next(i))
print(next(i))

import sys

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\nPython路径为：', sys.path, '\n')