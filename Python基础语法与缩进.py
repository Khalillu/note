# 这是我的第一个Python代码程序
"""
print("hello world!")
print("你好，世界！")

多行注释
多行注释
多行注释

# print("不会显示此行Python代码！")

a = "asiodhasdlk\
aksdnalksdakjsdhakjda"


b = "akjsdkandal\
kaskndjasd"

print(a)
print(b)

a = 3

print(a)
print(id(a))
print(type(a))

b = "asdajkl"

print(b)
print(id(b))
print(type(b))

# 删除变量实例

a = 123
del a
print(a)

MAX_AGE = 150
print(MAX_AGE)
MAX_AGE = 200
print(MAX_AGE)

x=y=z=100
a,b,c=1,2,3
print(a)
print(b)
print(c)

# 交换变量的值
a,b = b,a
print(a)
print(b)

# Python 内置数据类型
a = 123
b = 3.14
b2 = 314e-2
c = True
d = "hello world!"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("b2:"+str(b2))

a = 10/5
print(a)
b = 9%4
print(b)
c = 10//5
print(c)

a = 0b101001
b = 0o11
c = 0xff
# d = int("100abc")
d = int("100")
print(a)
print(b)
print(c)
print(d)

a = 3.14
b = 314e-3
c = 9.5
d = round(c)
p=q=3
# p += q # p = p+q
p *= q+2    #p = p*(q+2)
print(p)

k = True
u = False
c = u or k
print(c)

r = 10>30 and 50<100
e = 100>200 and 50<(3/0)  #发生短路
print(r)
print(e)
f = 200
g = 50<f< 500
g2 = 50<f and f < 500
print(g)
print(g2)
h = 0b1001
j = 0b0111
c = h&j
print(c)

a = "3"
b = "4"
c = a+b
print(c)

a = list(range(10))
print(a)
b = list(range(15,9,-1))
print(b)


a = [x*2 for x in range(100)if x%9==0]  # if 过滤 in表示x在range范围中
print(a)


a =[20,30]
b =[40,50]
#a.extend(b)    #原对象修改
a = a+b         #产生新对象
print(a)

a = [100,200,300,400]
#del a[2]
#a.pop(2)
#a.remove(888)
print(a)

a = [100,200,300,400]
print(a[1:3])
print(a[1:])
print(a[-5:-2])
print(a[::-1])
print(a[2:100])

a = [20,10,30,40]

for temp in a:
    print(temp*100)

import random
a = [30,10,20,40]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
random.shuffle(a)
print(a)

a = [30,10,20,40]
b = sorted(a)
c = sorted(a,reverse=True)
print(a)
print(b)
print(c)    #b,c为新的链表对象

a = [
    ["打开",10,19,19],
    ["关闭",13,41,31],
    ["开放",23,41,13],
]
for m in range(3):
    for n in range(4):
        print(a[m][n],end="\t")
    print()
#元组
a = (10,20,30)
b = 40,50,60
c = (100,)
print(type(a))
print(type(b))
print(type(c))  #当c =(x,)小括号里加上","才是元组，不然表示的是整数

a = (20,10,30,9,8)
print(a)
print(a.index(9))
print(a.count(10))
print(a[1:4])

b = (x*10 for x in range(5))
c = tuple(b)    #若没有该语句，则会编译出关于b元组的迭代器，而不是迭代器的值
print(c)
d = tuple(b)
print(d)    #因为上次使用生成器时，迭代器已到元组最后元素的下一个位置，因此不能打印出元素
e = (x for x in range(3))
print(e.__next__())
print(e.__next__())
print(e.__next__())
#print(e.__next__())     #迭代器已到末尾的下一个元素，再打印即报错

a = {'name':'gaoqi','age':18,'job':'programmer'}
print(a)
print(a['name'])
b = dict(name='gaoqi',age=18,job="programmer")
print(b)
c = dict([("name","gaoqi"),("age",18),("job","programmer")])
print(c)
k = ["name",'age','job']
v = ['gaoqi',18,'programmer']
print(list(zip(k,v)))
d = dict(zip(k,v))
print(d)
f = dict.fromkeys(["name","age","job"])
print(f)
a = {"name":"gaoqi","age":18,"job":"programmer"}
print(a["name"])
print(a["age"])
print(a.get("age"))
print(a.get("gender","不存在"))

a = {"name":"gaoqi","age":18,"job":"programmer"}
a['address'] = "1号院"
a['age']=38     #再次给age复制，覆盖掉原来age的值

b = {'name':'gaoxixi','money':100,'gender':"male"}
a.update(b)
print(a)    #将原有的name覆盖，用b中的name

r1 = {"name":"gaoqi","age":18,"salary":30000,"city":"北京"}
r2 = {"name":"gaoxi","age":19,"salary":20000,"city":"广州"}
r3 = {"name":"gaozi","age":20,"salary":10000,"city":"上海"}

tb = [r1,r2,r3]
print(tb[2].get("city"))

name = input("请输入名称：")
salary = int(input("请输入月薪："))   #转换数据类型，原来为字符串型，应将字符串型转化为整形，print中才会将具体salary的值*12，不然则会复制12次字符串salary的值
print("名称为：",name)
print("年薪为：",salary*12)

# split()分割和join()合并
a = "just do it!"
b = a.split("do")
print(b)
c = ['aa','bb','cc']
d = "".join(c)  #连接c中的各字符串
print(d)


import time

time1 = time.time() #获取此时的time
a = ""
for i in range(1000):
    a += "sxt"
time2 = time.time() #获取执行257行代码之后的time
print("+连接的运算时间："+str(time2-time1)) #取时间差

time3 = time.time()
l1 = []
for i in range(1000):
    l1.append("sxt")

b = "".join(l1)
time4 = time.time()
print("join()连接的运算时间："+str(time4-time3))    #同上

a = "lxf"
print(a)
b = a.capitalize()  #首字母大写，其他全小写
print(b)
c = a.title()   #每一个单词的首个字母大写
print(c)
d = a.upper()   #全部字母转化为大写
print(d)
e = a.lower()   #全部字母转化为小写
print(e)
f = a.swapcase()    #大变小，小变大
print(f)        #关于Python内部与字符串相关库函数的使用

# format格式化
a = "名字是：{0},年龄是：{1},{0}是个大好人"
b = a.format("gaoqi",18)
c = a.format("gaoxixi",6)
print(b)
print(c)

d = "名字是：{name},年龄是：{age}"
e = d.format(age = 19,name = "gaoqi")
print(e)

# io模块
import io
s = "abcdef"
sio = io.StringIO(s)
print(sio.getvalue())
sio.seek(3) #将指针移动到索引3这个位置
sio.write("***")
print(sio.getvalue())

# Python中的各种循环
#1  while循环：
num = 0
while num<=10:
    print(num)
    num += 1

num1 = 0
sum = 0
while num1<=100:
    sum += num1
    num1 += 1
print(sum)

#2  for循环
for x in (20,30,40):
    print(x*10)
d = {'name':'gaoqi','age':18,'job':'programmer'}
for x in d:     #遍历字典所有的key
    print(x)
for x in d.keys():  #遍历字典所有的key
    print(x)
for x in d.items(): #遍历字典所有的“键值对”
    print(x)
for x in d.values():    #遍历字典所有的value
    print(x)
for x in range(3,10,2):
    print(x)
sum = 0
sum1 = 0
sum2 = 0#计算0~100的总和
for num in range(101):
    sum += num
    if num%2 == 0:
        sum1 +=num
    else:
        sum2+=num
print(sum)
print(sum1)
print(sum2)

#  嵌套循环

for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print()

for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,m*n),end="\t")
    print()

r1 =dict(name="gaoqi",age=18,job="programmer")
r2 =dict(name="gaoxi",age=19,job="programmer")
r3 =dict(name="gaozi",age=20,job="programmer")
tb =[r1,r2,r3]

for x in tb:
    if x.get("age")>18:
        print(x)        #嵌套循环加if语句判断

# break语句

while True:
    a = input("请输入一个字符（输入Q或q结束）")
    if a.lower()=='q':  #或者if a.upper() =='Q'
        print("循环结束，退出")
        break
    else:
        print(a)

# continue语句
empNum = 0
salarySum = 0
salarys =[]
while True:
        s = input("请输入员工的薪资（按Q或q结束）")
        if s.upper()=='Q':
            print("录用结束")
            break
        if float(s)<0:
            print("无效！继续录入！")
            continue
        print("录入成功！")
        empNum += 1
        salarySum += float(s)
        salarys.append(float(s))

print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("总发薪资：",salarySum)
print("平均薪资{0}".format(salarySum/empNum))

# zip()并行迭代

names =("高企","阿达","阿迪斯","的撒旦")
ages = (12,13,41,45)
jobs = ("学生","教师","律师")

for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

# 另一种实现方式(不使用zip()并行迭代)

for i in range(min(len(names),len(ages),len(jobs))):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))

#   列表推导式：
a = [x for x in range(1,10) if x%2==0]
print(a)

b = []
for x in range(1,10):
    if x%2==0:
        b.append(x)
print(b)

cells = [(row,col) for row,col in zip(range(1,10),range(101,110))]
print(cells)

#   字符推导式：

my_text = 'i love you ,i love asd, i love asd'

char_count = {c:my_text.count(c) for c in my_text}
print(char_count)
#   集合推导式与列表推导式相似，区别是从[]变成了{}

#   lambda表达式
f = lambda a,b,c:a+b+c

print(f)
print(id(f))
print(type(f))
print(f(10,20,30))

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]

print(g[0](4),g[1](5),g[2](6))

# map函数
numbers =[1,2,3,4,5,6,7,8,9]


def doubler(n):
    return n*2


result = map(doubler,numbers)
print(result)
print(list(result))

#   filter()函数

def is_even(n):
    return n%2 == 0

nums = [1,2,3,4,5,6,7,8,9]
even_num = filter(is_even,nums)
print(list(even_num))

class Student:
    def __init__(self,name,score):
        self.name = name    #新增name属性
        self.score = score  #新增score属性

    def say_score(self):
       print("{0}的分数是：{1}".format(self.name, self.score))


s1 = Student("张三",95)
print(s1.name,s1.score)
s1.say_score()
s2 = Student("add",95)
print(s2.name,s2.score)

class Student:
    def __init__(self,name,score):
        self.name = name    #新增name属性
        self.score = score  #新增score属性

    def say_score(self,c):
        print(c)
        print("{0}的分数是：{1}".format(self.name, self.score))

a = Student("adadasda",95)
a.say_score(68)     #Student.say_score(a,68)
print(dir(a))
print(a.__dict__)


#   类对象
class Student:
    pass
print(type(Student))
print(id(Student))
print(Student)
#   类属性


#   类方法

class Student:
    company = "asd"

    @classmethod
    def printCompany(cls):
        print(cls.company)

#   静态方法
    @staticmethod
    def add(a, b):
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b

Student.printCompany()
Student.add(50,60)


#测试私有属性、私有方法
class Employee:
    __company = "asd"   #解释器运行时，把__company转成了_Employee__company

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def say_company(self):
        print("my company is:",Employee.__company)
        print("我的年龄是：",self.__age)

    def __work(self):
        print("好好工作")


print(dir(Employee))
print(Employee._Employee__company)
a = Employee("高企",18)
#print(a.__age)
a.say_company()
print(a._Employee__age) #强行访问
print(a._Employee__work)
a._Employee__work() #私有方法强行访问

"""
class Car:  #父类是object
    pass
class Benz(Car):    #Benz-->Car-->object
    pass