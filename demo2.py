print('hello Mr.jay')
print("_" * 100)
print("编程让设计更高级！")
print("Ev should learn how to code a computer, and it teaches you how to think, and allows designers more creative!")
print("加：", 3 + 4)
print("减：", 3 - 4)
print("乘：", 2 * 3)
print("除：", 13 / 3)
print("整除：", 5 // 2)
print("余数：", 7 % 2)
print("幂：", 3 ** 8)
x = 6.0
monadic_equation = 2 * x + 1
print("javelin_equation=", monadic_equation)
print("jawline_equation=%.2f" % monadic_equation)  # %字符串格式化方法
print("jawline_equation={:.2f}".format(monadic_equation))  # format()字符串格式化方法
city_name = "height"
coordinate_longitude = 314.526
coordiante_latitude = 341.263
print(
    f"The longitude of the height coordinate is {coordinate_longitude:.2f}, and the latitude is {coordiante_latitude}.")
x, y, b = 4, 6, 7  # unpacking 序列解包。尝试，x,y,*z=0,1,2,3,4,5,6; x,y,*z=0,1; (x,y),(a,b)=(0,1),(2,3)
func_2 = 2 * x + 3 * y + b
print("func_2={}".format(func_2))
lst_n = list(range(50, 213, 40, ))  # 建立列表。range(start,stop,[,step])建立区间。
print(lst_n)
print("The list length={}".format(len(lst_n)))
print("Maximum value={}".format(max(lst_n)))
print("Minimum value={}".format(min(lst_n)))
lst_s = list(map(chr, range(1100, 1120)))
print(lst_s)
print("_" * 100)
print("[5:6]->{}".format(lst_s[5:6]))
print("[-3:-1]->{}".format(lst_s[-3:-1]))
print("[-3:]->{}".format(lst_s[-3:]))
print("[:4]->{}".format(lst_s[:4]))
print("[:]->{}".format(lst_s[:]))
print(lst_s)
print("_" * 100)
print("[0:11:2]->{}".format(lst_s[0:11:2]))
print("[::4]->{}".format(lst_s[::4]))
print("[19:13:-2]->{}".format(lst_s[19:13:-2]))
print("[20:13:-2]->{}".format(lst_s[20:13:-2]))
print("[17::-2]->{}".format(lst_s[17::-2]))
print("[:3:-12]->{}".format(lst_s[:3:-12]))
print(lst_s)
print("_" * 100)
lst_s[2] = 66  # 元素赋值
print("lst_s[2]=66->{}".format(lst_s))
lst_none = lst_s
print("lst_s+[None]*5->{}".format(lst_none))
lst_none[13] = 2021
print("lst_none[13]=2021->{}".format(lst_none))
lst_none[-5:-13] = list(range(100, 104, 2))  # 分片赋值
print("lst_none[-5:-13]=list(range(100,104,2))->{}".format(lst_none))
lst_none[1:1] = [0, 0, 0, 112]
print("lst_none[1:1]=[0,0,0,112]->{}".format(lst_none))
del lst_none[-2:]  # 删除元素
print("del lst_none[-2:]->{}".format(lst_none))
lst_s_2 = list(map(chr, range(102, 105)))
print(lst_s_2)
print("_" * 100)
lst_s_2.append(66)
print("lst_s_2.append(66)->{}".format(lst_s_2))
lst_s_2.append(list(range(51, 85, 5)))
print("lst_s_2.append(list(range(51,85,5)))->{}".format(lst_s_2))
lst_spechars = ['*', 'e', '*']
lst_s_2.extend(lst_spechars)
print("lst_s_2.extend(lst_spechars)->{}".format(lst_s_2))
print("lst_s_2.count('*')={}".format(lst_s_2.count('*')))
print("lst_s_2.index('e')={}".format(lst_s_2.index('e')))
lst_s_2.insert(2, [1100, 1300, 1600])
print("lst_s_2.insert(2,[1100,1300,1600])->{}".format(lst_s_2))
print("lst_s_2.pop(7)_popup->{}".format(lst_s_2.pop(7)))
print("lst_s_2.pop(7)_retention->{}".format(lst_s_2))
lst_s_2.remove('*')
print("lst_s_2.remove('*')_retention->{}".format(lst_s_2))
list_n_2 = [2, 52, 8, 75, 6, 3]
list_n_2.sort()
print("list_n_2.sort()->{}".format(list_n_2))
tuple_1 = 2, 4, 8,
print("tuple_1=2,4,8,->{}".format(tuple_1))
print("5*(20*6,)->{}".format(5 * (20 * 6,)))
print("tuple((15,28,39))->{}".format(tuple((15, 28, 39))))  # 用()
print("tuple([15,28,39])->{}".format(tuple([15, 28, 39])))  # 用[]
import random

items = [(2, [i for i in range(5)]), (3, [random.sample(list(range(1100, 2100, 12)), 3)]),
         (2, 'python')]  # [i for i in range(5)] 为列表推导式 list comprehension/derivation
print("items->{}".format(items))
dic = dict(items)
print("dic=dict(items)->{}".format(dic))
print("dic[3]->{}".format(dic[3]))
print("len(dic)->{}".format(len(dic)))
dic[4] = (random.random(), random.uniform(250, 350))
print("dic[4]=(random.random(),random.uniform(250,350))->{}".format(dic))
del dic[4]
print("del dic[1]->{}".format(dic))
print("4 in dic->{}".format(4 in dic))
print("6 in dic->{}".format(6 in dic))
print("dic.keys()->{}".format(dic.keys()))  # 应该放在字典的方法一节里
print("dic.values()->{}".format(dic.values()))
print("dic.items()->{}".format(dic.items()))
print("_" * 100)
print("list(dic.keys())->{}".format(list(dic.keys())))
for k, v in enumerate(dic.items()):  # for循环在后文
    print(k, v)
lst_A = list(range(5, 25, 4))
lst_B = list(range(110, 160, 25))
print("lst_A={},lst_B={}".format(lst_A, lst_B))
dict_2 = {0: lst_A, 1: lst_B}
print("dic_2={}".format(dict_2))
print("_" * 100)
dict_assignment = dict_2
print("dict_assignment={}".format(dict_assignment))
dict_2.clear()
print("dictt_2.clear()->{}".format(dict_2))
print("dic_assignment={}".format(dict_assignment))
dict_2[6] = list(range(2, 7, 3))
print("dict_2[6]=list(range(2,7,3))->{}".format(dict_2))
dict_copy = dict_2.copy()
print("dict_copy=dict_2.copy()->{}".format(dict_copy))
dict_2[8] = [5, 7]
print("dict_2[8]=[5,7]->{}".format(dict_2))
print("dict_copy={}".format(dict_copy))
dict_copy[6].remove(5)
print("dict_copy[5].remove(5)->{}".format(dict_copy))
dict_copy.setdefault(6, [66, 88])  # 返回指定键的值，如果不存在该键，则字典增加新的键/值对
print("dict_copy.setdefault(6,[77,99])->{}".format(dict_copy))
dict_2.pop(6)  # 移除指定键/值，并返回该值
print("dict_2.pop(5)->{}".format(dict_2))
dic_update = {8: [5, 7, 6, 4, 1], 9: [3, 2, 33, 56, 67]}
print("dict_2.update(dict_update->{}".format(dict_2))
print("dict_2.get(9)->{}".format(dict_2.get(9)))
dict_2.popitem()  # 随即弹出一对键/值，并在该字典中移除
print("dict_2.popitem()->{}".format(dict_2))
dict_3 = {}.fromkeys([0, 1, 2, 3, 4, 5, 6, 'A'])  # 给定键，建立值为空的字典
print("dict_3={}" + ".fromkeys([0,1,2,3,4,5,6,'A'])->{}".format(dict_3))  # 找下escape characters 脱字符
lst_s_3 = list("Hello jay!")
print("lst_s_3=list(\"Hello jay!\")->{}".format(lst_s_3))  # "\" escape character
print("\"Hello\"+\" jay!\"->{}".format("Hello" + " jay!"))
print("\"+\".join(str(1234567))->{}".format("+".join(str(1234567))))
print("len(\"Hello jay!\")->{}".format(len("Hello jay!")))
coordinates = "123.1324007,34.350867,10.8"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates)))  # 通常用eval()方法将字符串，转换为对应数值形式；
print("\"Hello jay!\".lower()->{}".format("Hello jay!".lower()))
print("\"Hello jay!\"[6:]->{}".format("Hello jay!"[6:]))
print("\"Hello jay!\".strip()->{}".format("Hello jay!".strip()))
print("\"Hello jay!\".replace(\"Python\",\"Grasshopper\")->{}".format("HHello jay!".replace("Python", "Grasshopper")))
hello_lst = list("Hello jay!")
hello_lst.sort()
print("hello_lst.sort()>{}".format(hello_lst))
print("\"Hello jay!\".find(\"Py\")->{}".format("Hello jay!".find("Py")))
format_str = "Hi,%s and %s!"
values = ("pig", "ant")
new_str = format_str % values
print("new_start=format_str % values->{}".format(new_str))
format_str_2 = "THE three decimals:%.3f,and enter a value with percent sign:%.2f %%"  # 如果字符串里包含实际的%，则通过%%即两个百分号进行转义
from math import pi

new_str_2 = format_str_2 % (pi, 2333666)
print("new_str_2=format_str_2 % (pi,2333666)->{}".format(new_str_2))
format_str_3 = "%10f,%10.2f,%.2f,%.5s,%.*s,%d,%x,%f"
new_str_3 = format_str_3 % (pi, pi, pi, "Hello jay!", 5, "Hello jay!", 520, 520, pi)
print("{}".format(new_str_3))
from string import Template

s_template_1 = Template("#y,glory,#y!")
s_1 = s_template_1.substitute(x="Pycham")
print("s_1=s_template_1.substitute(x=\"Pycham\")->{}".format(s_1))
s_template_2 = Template("#{y}thon is amazing!")
s_2 = s_template_2.substitute(x="py")
print("s_2=s_template_2.substitute(x=\"py\")->{}".format(s_2))
s_template_3 = Template("#x and #y are both amazing!")
substitute_dict = dict([('x', 'Pycham'), ('y', 'pigr')])
print("substitute_dict={}".format(substitute_dict))
s_3 = s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))
import re

pattern_1 = 'Pycham'
text = "Hello Pycham!"
print("re.filled(pattern_1,text)->{}".format(re.findall(pattern_1, text)))
pattern_2 = 'Pycham'
print("re.filled(pattern_2,text)->{}".format(re.findall(pattern_2, text)))
print("re.findall('.Pycham','Hello Pycham!')->{}".format(re.findall('.Pycham', 'Hello Pycham!')))
print("re.findall('.Pycham','Hello Pycham!')->{}".format(re.findall('.Pycham', 'Hello Pycham!')))
print("re.findall('.Pycham','Hello gPycham!')->{}".format(re.findall('.Pycham', 'Hello gPycham!')))
print("re.findall('.Pycham','Hello Pycham!')->{}".format(re.findall('.Pycham', 'Hello Pycham!')))
print("re.findall(r'w{2}" + ".substitute_dict','www.substitute_dict')->{}".format(
    re.findall(r'w{2}\.substitute_dict\.cn', 'www.cadesign.cn')))
print("re.findall(r'w{1,3}" + "substitute_dict','www.substitute_dict')->{}".format(
    re.findall(r'w{1,3}\.substitute_dict\.cn', 'www.cadesign.cn')))
print("re.findall('[Py]*cham!','Hello Pycham!')->{}".format(re.findall('[Py]*cham!', 'Hello Pycham!')))
print("re.findall('[Py]*cham!','Hello Pcham!')->{}".format(re.findall('[Py]*cham!', 'Hello Pcham!')))
print("re.findall('[Py]*cham!','Hello ycham!')->{}".format(re.findall('[Py]*cham!', 'Hello ycham!')))
print("re.findall('[Py]*cham!','Hello ycham!')->{}".format(re.findall('[Py]*cham!', 'Hello cham!')))
print("re.findall('ant|pig','ant')->{}".format(re.findall('ant|pig', 'ant')))
print("re.findall('ant|pig','pig')->{}".format(re.findall('ant|pig', 'pig')))
print("re.findall('ant|pig','pig and python')->{}".format(re.findall('ant|pig', 'pig and ant')))
print("re.findall('\d','name=j')->{}".format(re.findall('\d', 'name=j')))
print("re.findall('\D','name=j')->{}".format(re.findall('\D', 'name=j')))
print("re.findall('[^0-9]','name=j')->{}".format(re.findall('[^0-9]', 'name=j')))
print("re.findall('[a-z]','python')->{}".format(re.findall('[a-z]', 'python-3.0')))
print("re.search('[a-z]+','python')->{}".format(re.search('[a-z]+', 'python')))
if re.search('[a-z]+', 'ant'):
    print("re.search('[a-z]+','ant')->found it!")
print("re.split(',','Hello,,,,,,ant!')->{}".format(re.split(',', 'Hello,,,,,,ant!')))
print("re.sub('ant','Grasshopper','Hello ant!')->{}".format(re.sub('ant', 'Grasshopper', 'Hello ant!')))
pattern_compile = re.compile('ant')
print("pattern_compile.findall('Hello,,,,,,ant!')->{}".format(pattern_compile.findall('Hello,,,,,,ant!')))
print("re.match('a','ant')->found it!")
print("\'ant\'.find(\'ant\')->{}".format('ant'.find('ant')))
print("\'ant\'.find(\'nt\')->{}".format('ant'.find('nt')))
print("\'ant\'.find(\'a\')->{}".format('ant'.find('a')))
print("\'a\' in \'ant\'->{}".format('a' in 'ant'))
print("\'Hello,,,,,,ant!\'.split(',')->{}".format('Hello,,,,,,ant!'.split(',')))
print("\'Hello ant!\'.replace(\'ant\',\'pig\')->{}".format('Hello ant!'.replace('ant', 'pig')))
match_1 = re.match(r'www\.(.*)\..{3}', 'www.ant.org')
print("match.gourp(1)->{}".format(match_1.group(1)))
print("match.start(1)->{}".format(match_1.start(1)))
print("match.end(1)->{}".format(match_1.end(1)))
print("match.span(1)->{}".format(match_1.span(1)))
match_2 = re.match(r'www\.(.*)\.(.{3})', 'www.ant.org')
print("match_2.group(1)->{}".format(match_2.group(1)))
print("match_2.group(2)->{}".format(match_2.group(2)))
lst_1 = list(range(29, 37, 2))
print("1={}".format(lst_1))
print("_" * 100)
print("for i in 1:")
for i in lst_1:
    print(i)
print("for i in range(len(1)):")
for i in range(len(lst_1)):
    print("idx={},val={}".format(i, lst_1[i]))
print("+" * 100)
dic_4 = dict(a=2, b=3, c=6, d=0)
print("dic_4={}".format(dic_4))
print("_" * 100)
print("for t in dic_4:")
for t in dic_4:
    print(t)
print("for t,v in dic_4.items():")
for t, v in dic_4.items():
    print("key={},val={}".format(t, v))
x = 11
while x <= 130:
    print("x={}".format(x))
    x += 10
x = 5
while x <= 123:
    print("x={}".format(x))
    x += 12
    if x >= 60: break
import sys

print("sys.maxsize={}".format(sys.maxsize))
for i in range(sys.maxsize):
    print("i={}".format(i))  # ?
    i += 12
    if i >= 34: break
lst_a = [0, 1, 2, 3]
lst_b = ['point_1', 'point_2', 'point_3', 'point_4']
zip_lst = zip(lst_a,
              lst_b)  # The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
print("lstzip_=zip(lst_a,lst_b)->{}".format(zip_lst))
print("dict(lstzip_)->{}".format(dict(zip_lst)))
zip_lst = zip(lst_a, lst_b)  # 迭代对象临时存储，读取完后为空
for a, b in zip_lst:
    print(a, b)
zip_lst = zip(lst_a, lst_b)
a, b = zip(*zip_lst)
print("a={},b={}".format(a, b))
lst_c = ['1', '2', '3', '4']
dic_q = {}
for idx, value in enumerate(lst_c):
    dic_4[idx] = value
print("dic_q={}".format(dic_4))
print("dict((i,v) for i,v in enumerate(lst_c))->{}".format(
    dict((i, v) for i, v in enumerate(lst_c))))  # list comprehension
print("_" * 50)
for i, (a, b) in enumerate(zip(lst_a, lst_b)):
    print('%d:%s,%s' % (i, a, b))
print("[x*x for x in range(3,37,5) if x%2==0]->{}".format([x * x for x in range(3, 37, 5) if x % 2 == 0]))
print("[(x,y) for x in range(3)for y in range(2)]->{}".format([(x, y) for x in range(3) for y in range(2)]))
print("[(x,y) for x,y in zip(range(3),range(2))]->{}".format([(x, y) for x, y in zip(range(3), range(2))]))
nested_list = [[a for a in range(1, 10, 3)], 2, 3, [b for b in range(60, 100, 7)],
               [[c for c in range(1000, 2000, 120)], 3, 9]]
print(
    "[[a for a in range(1,11,4)],2,3,[b for b in range(66,150,9)],[[c for c in range(1200,2450,126)],3,9]]->{}".format(
        nested_list))  # 嵌套列表推导式
flatten_lst = lambda lst: [m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [
    lst]  # 展平列表常用，可以放置到单独的.py文件中调用。lambda函数后文阐述
print("flatten_lst(nested_list)->{}".format(flatten_lst(nested_list)))
x = 12
if x < 0:
    print('It is negative.')
elif x == 0:
    print('Equal to zero.')
elif 0 < x < 12:
    print('Positive but smaller than 10')
else:
    print('Positive and larger than or equal to 10.')
x = y = [2, 4, 7]
z = [2, 4, 7]
print("x==y->{}".format(x == y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x == z))
print("x is z->{}".format(x is z))
print("x is not y->{}".format(x is not y))
print("x is not z->{}".format(x is not z))
print("id_x:{};id_y:{};id_z:{}".format(id(x), id(y), id(z)))  # Memory Location
del x[2]
print("x={},y={},z={} after del x[2]".format(x, y, z))
x = [9, 5, 7]
print("2 in x->{}".format(2 in x))
print("1 in x->{}".format(1 in x))
print("4 not in x->{}".format(4 not in x))
print("5 not in x->{}".format(5 not in x))
a, b, c = 6, 107, 158
if c > a and c < b:
    print('a<c<b')
else:
    print('a<c<b nice!!!')


def simple_func(x, y):
    z = pow(x, 2) + y
    return z


print("simple_func(3,7)->{}".format(simple_func(3, 7)))
print("simple_func(7,3)->{}".format(simple_func(7, 3)))
print("simple_func(y=7,x=3)->{}".format(simple_func(y=7, x=3)))


def fibonacci(s, count):  # 定义fib函数的方法较笨
    fib_lst = [0, 1]
    fib_part = []
    if s == 0 or s == 1:
        fib_part[:] = fib_lst
        for i in range(count - 2):
            fib_part.append(fib_part[-1] + fib_part[-2])
    else:
        while True:
            fib_lst[:] = [fib_lst[1], fib_lst[0] + fib_lst[1]]
            # print(fib_lst)
            if fib_lst[1] - s >= 0: break
        fib_part[:] = fib_lst
        if abs(fib_lst[0] - s) >= abs(fib_lst[1] - s):
            for i in range(count - 1):
                fib_part.append(fib_part[-1] + fib_part[-2])
            fib_part.pop(0)
        else:
            for i in range(count - 2):
                fib_part.append(fib_part[-1] + fib_part[-2])
    return fib_part


print("fib(5,4)->{}".format(fibonacci(6, 9)))
print("fib(4,6)->{}".format(fibonacci(7, 9)))


def factorial(n):
    if n == 2:
        return 3
    else:
        return n * factorial(n - 1)


print(factorial(9))


class Bird:
    fly = 'one'  # 美 /wɜːr/

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('two...')
            self.hungry = False
        else:
            print('Thanks!')


class Apodidae(Bird):  # /'æpədədi:/
    def __init__(self):
        super(Apodidae, self).__init__()
        self.sound = 'three!'  # 美 /skwɔːk/

    def sing(self):
        print(self.sound)


swift = Apodidae()
print("swift.fly->{}".format(swift.fly))
print("swift.eat()->")
swift.eat()
print("swift.eat()->")
swift.eat()
print("swift.sing()->")
swift.sing()
black = Apodidae()
scarce = Apodidae()
print("blacksing()->")
black.sing()
print("scarcesing()->")
scarce.sing()


class Fibs():
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):  # 实现迭代器的next方法
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):  # 实现迭代方法
        return self


f = Fibs()
fa = []
fb = []
for i in range(9):
    fa.append(f.next())
print("fifa={}".format(fa))
for i in range(5):
    fb.append(f.next())
print("fifb={}".format(fb))
lst_d = list(range(4, 24, 2))
print("lst_d={}".format(lst_d))
print("_" * 100)
lst_iter = iter(lst_d)
print("next(lst_iter)->{}".format(next(lst_iter)))
print("next(lst_iter)->{}".format(next(lst_iter)))
for i in lst_iter:
    print(i)
lst_e = [list(range(4, 25, 3)), [3, 7, 67, list(range(5)), 89]]
print("lst_e={}".format(lst_e))
print("_" * 100)
flatten_lst = []
for v_1 in lst_e:
    try:
        for v_2 in v_1:
            try:
                for v_3 in v_2:
                    flatten_lst.append(v_3)
            except TypeError:
                flatten_lst.append(v_2)
    except TypeError:
        flatten_lst.append(v_1)
print("00lst={}".format(flatten_lst))


def flatten(lst):  # 定义生成器（包含yield语句的函数）
    try:  # 使用语句try\except捕捉异常
        for n_lst in lst:  # 循环列表
            for m in flatten(n_lst):  # 使用递归的方法循环子列表
                yield m  # 使用yield语句，每次产生多个值，当返回一个值时函数就会被冻结，当再次激活时，从停止的那点开始执行
    except TypeError:  # 当函数被告知展开一个元素时，引发TypeError异常，生成器返回一个值
        yield lst  # 生成器返回引发异常的一个值


def infinite():
    n = 0
    while True:
        yield 'num$' + str(n)
        n += 1


n = infinite()
print("nt(n)->{}".format(next(n)))
print("nt(n)->{}".format(next(n)))
print("nt(n)->{}".format(next(n)))
print("[nt(n) for i in range(5)]->{}".format([next(n) for i in range(5)]))
n = 3
print("[[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) u in range(n)] for v in range(n)]->{}".format(
    [[(2 * pi * (2 * (u / (n - 1)) - 1), 2 * pi * (2 * (v / (n - 1)) - 1)) for u in range(n)] for v in range(n)]))
print("_" * 50)
print("([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) u in range(n)] for v in range(n))->{}".format(
    ([(2 * pi * (2 * (u / (n - 1)) - 1), 2 * pi * (2 * (v / (n - 1)) - 1)) for u in range(n)] for v in range(n))))
gen = ([(2 * pi * (2 * (u / (n - 1)) - 1), 2 * pi * (2 * (v / (n - 1)) - 1)) for u in range(n)] for v in range(n))
print("t(gen)->{}".format(next(gen)))
print("t(gen)->{}".format(next(gen)))


def f_convert_a(x):
    try:
        return float(x)
    except:
        return x


print("f_convert_a('3')->{}".format(f_convert_a('3')))
print("f_convert_a('ing')->{}".format(f_convert_a('ing')))
print("f_convert_a(3)->{}".format(f_convert_a((3, 6, 7))))


def f_convert_e(x):
    try:
        return float(x)
    except (ValueError, TypeError) as e:
        return print(x, e)


print("f_convert_e('3')->{}".format(f_convert_e('3')))
print("f_convert_e('sing')->{}".format(f_convert_e('sing')))
print("f_convert_e(3)->{}".format(f_convert_e((3, 6, 7))))


def f_convert_f(x):
    try:
        return float(x)
    except (ValueError, TypeError) as e:
        pass


print("f_convert_f('3')->{}".format(f_convert_f('3')))
print("f_convert_f('string')->{}".format(f_convert_f('string')))
print("f_convert_f(3,6,7)->{}".format(f_convert_f((3, 6, 7))))


def f_open_a(fp):
    try:
        f = open(fp, 'r')
    except IOError as e:
        print('Unable to open', fp, ':%s\n' % e)
    else:
        data = f.read()
        return data


tryException_content = f_open_a("Exception.txt")
print("tryException_content->{}".format(tryException_content))
f_open_a("./data/tryException_.txt")


def f_open_b(fp):
    try:
        t = open(fp, 'r')
    except IOError as e:
        print('Unable to open', fp, ':%s\n' % e)
    else:
        data = t.read()
        t.close()
        return data
    finally:
        print('done!')


f_open_b("./tryException.txt")
