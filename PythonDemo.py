import pizza
from collections import OrderedDict
from random import randint
import json
if __name__ == '__main__':
    print("Hello Python World!")


    # myList=['a','b','c']
    # print(myList)
    # myList.append('d')
    # print(myList)
    # del myList[3]
    # print(myList)
    # myList.insert(3,'d')
    # print(myList)
    # poped_value=myList.pop()
    # print(myList)
    # print(poped_value)
    # myList.remove('a')
    # print(myList)
    # myList.append('a')
    # print(myList)
    # myList.sort()
    # print(myList)
    # print(sorted(myList, reverse=True))
    # print(myList)

    # for循环 for循环遍历列表时不应修改列表类似java中foreach循环无法修改集合
    # for element in myList:
    #     print(element)
    # print(list(range(1,5,2)))
    # for element in list(range(1,21)):
    #     print(element)
    # hMillion = list(range(1,1000001))
    # print("最小值:"+str(min(hMillion)))
    # print("最大值:"+str(max(hMillion)))
    # print("1加到100W:"+str(sum(hMillion)))
    # print("1 - 20的奇数有",end="")
    # for element in list(range(1,21,2)):
    #    print(element)
    # lists = [value ** 3 for value in range(1,11)]
    # for element in lists:
    #     print(element)
    # -----------------------------------------
    # 复制或者切片列表
    # lists = ["apple","banana","cherry","hotdog"]
    # print(lists[1:4])
    # myLists = lists[0:2]
    # print(myLists)

    # 元组 是不可改变的列表
    # dimensions = (1,2)
    # for dimension in dimensions :
    #     print(dimension)
    # dimensions = (2,3)
    # print(dimensions[0])

    # if 语句
    # flag = True
    # print(flag)
    # for element in lists:
    #     if element == "apple":
    #         print("I like "+element)
    #     else:
    #         print("I don't like "+element)
    # lists = ["apple","banana"]
    # if lists:
    #     for element in lists:
    #         print(element)
    # else:
    #     print("空集")

    # 字典  基本等同于map也是key,value关联存储没有存储顺序
    # pepole = {'weight':'75kg','hight':'175cm','income':'11k'}
    # print(pepole['weight'])

    # 输入函数input():将用户输入解读为字符串
    # input = input("请输入指令: 开始 or 结束\n")
    # print("收到指令\t"+input)
    # -----------------------------------------
    # int():将字符串转化为数值
    # age = input("请输入你的年龄:\t")
    # age = int(age)
    # if age < 18:
    #     print("你的年龄小于18岁无法访问")
    # else:
    #     print("你已经大于18岁可以访问")

    # while循环;
    # str()函数将对象转换为字符串
    # count = 0
    # while count < 5:
    #     count += 1
    #     print("循环第"+str(count)+"次")
    # -----------------------------------------
    # while循环中可以对列表和字典进行修改
    # pets = ["cat","dog","cat","fox","bird","chick"]
    # print(pets)
    # while "cat" in pets :
    #     pets.remove("cat")
    # print(pets)
    # -----------------------------------------
    # 循环获取输入
    # responses = {}
    # isContinue = True
    # while isContinue :
    #     name = input("请输入你的名字:")
    #     responses[name] = input("你最喜欢的食物是:")
    #     response = input("还有其他人要记录吗 yes/no")
    #     if response == "no":
    #         isContinue = False
    # print(responses)

    # 函数定义 def关键字 顺序传参
    # def print_pet(type,name):
    #     print("宠物类型是:"+type+"\n宠物名字是:"+name)
    # print_pet("狗","旺财")
    # -----------------------------------------
    # 关键字传参(参数顺序错误也不会出问题)
    # def print_pet(type,name):
    #     print("宠物类型是:"+type+"\n宠物名字是:"+name)
    # print_pet(type = "狗",name = "旺财")
    # print_pet(name = "小白",type = "猫")
    # -----------------------------------------
    # 设置默认参数值
    # def print_pet(type = "狗",name = "小白"):
    #     print("宠物类型是:"+type+"\n宠物名字是:"+name)
    # print_pet()
    # print_pet(name = "小黄")
    # -----------------------------------------
    # 等效函数调用
    # def print_pet(type,name="小白"):
    #     print("我有一只名叫:" + name +"的" + type)
    # print_pet("狗")
    # print_pet(type="狗")
    # -----------------------------------------
    # 返回值
    # def sum_calculator(num_1,num_2):
    #     sum_result = num_1 + num_2
    #     return sum_result
    # print("1 + 1 = " + str(sum_calculator(1,1)))
    # -----------------------------------------
    # python将非空字符串解读为True
    # name = ''
    # if name :
    #     print("My name is " + name)
    # else:
    #     print("我还没想好我的英文名字")
    # -----------------------------------------
    # 函数可以返回字典等任何类型的值
    # def get_dogs(type,name,age=0):
    #     dogs = {'type':type,'name':name}
    #     if age:
    #         dogs['age'] = age
    #     return dogs
    # print(get_dogs("狗","旺财",-1))
    # -----------------------------------------
    # while和函数结合
    # flag = True
    # while flag:
    #     print("\n请告诉我你的姓名")
    #     first = input("姓:")
    #     last = input("名:")
    #     print("\n你的姓名是:" + first + last)
    #     isContinue = input("\n确认请摁Y,重新输入摁N:")
    #     if isContinue == 'Y':
    #         flag = False
    #         print("结束程序~谢谢使用")
    # -----------------------------------------
    # 传递列表
    # def print_names(names):
    #     for name in names:
    #         print(name)
    # names = ['小明','小红','小白']
    # print_names(names)
    # -----------------------------------------
    # 禁止函数修改列表--可以通过传入列表切片(副本)实现
    # def print_names(names):
    #     while names:
    #         print('取出姓名:' + names.pop())
    #
    #     print('传入列表中还有姓名:\n')
    #     print(names)
    # names = ['小明', '小红', '小白']
    # print_names(names[:])
    # print('names中还有姓名:\n')
    # print(names)
    # -----------------------------------------
    # 传递任意数量的实参--加*号会使传入的所有参数组成一个元组,不确定数量的形参要放在确定的形参后面规则同java ...形参
    # def make_hamburger(*parts):
    #     print("这个汉堡的组成部分有:\n")
    #     for part in parts:
    #         print(part)
    #
    # make_hamburger("生菜",'肉饼','芝士')
    # ------------------------------------------
    # 传递任意数量的键值对实参--加** 会使传入的所有参数组成一个字典
    # def build_personal_info(name, age, ** other_info):
    #     user_info = {}
    #     user_info["name"] = name
    #     user_info['age'] = age
    #     for key,value in other_info.items():
    #         user_info[key] = value
    #     return user_info
    #
    # print(build_personal_info('韩梅梅', 16, location = '杭州', hobbies = '看书,画画'))
    # ------------------------------------------
    # import 导入模块(文件)然后才能调用函数 如果只想导入特定函数则 可使用这个格式 from module_name import function_name1,function_name2,...
    # 如果导入函数名称与其他函数冲突或者模块名称冲突 都可以在后面加 as new_name赋予别称  import pizza *的意思是导入模块中所有函数 , 调用时不用通过模块调用 , 但不建议这样导入 , 容易导致函数名冲突
    # pizza.print_pizza("yoooo~")
    # ------------------------------------------
    # 类 _init_(self)是类默认的初始化方法 , self是固定参数 , 所有类中的方法都有该参数 , 该参数即是通过类创建的具体对象
    # class Dog():
    #     def __init__(self,name,age):
    #         self.name = name
    #         self.age = age
    #     def eat(self):
    #         print(self.name + "开始吃东西")
    #
    # my_dog = Dog('小白',5)
    # print('我的小狗名字叫做:'+my_dog.name)
    # my_dog.eat()
    # your_dog = Dog('小黑',6)
    # print('你的小狗名字叫做' + your_dog.name)
    # your_dog.eat()
    # -----------------------------------------
    # python标准库有很多有用的功能模块
    # students_grades = OrderedDict()
    # students_grades['爱德华'] = 90
    # students_grades['爱丽丝'] = 80
    # students_grades['路易斯'] = 70
    # for name,score in students_grades.items():
    #     print(name.title() + '的成绩:' + str(score))
    # class Die():
    #     def __init__(self):
    #         self.sides = 6
    #     def roll_die(self):
    #         return randint(1,self.sides)
    #     def set_sides(self, sides):
    #         self.sides = sides
    # my_die = Die()
    # my_die.set_sides(20)
    # count = 1
    # while count <= 10:
    #     print('第' + str(count) + '次投出点数:' + str(my_die.roll_die()))
    #     count += 1
    # ---------------------------------------
    # 文件读取及相关操作
    # file_path = "F:\config.properties"
    # with open(file_path) as file_object:
    #     contents = file_object.read()
    #     print(contents.rstrip())
    # 按行读取
    # file_path = "F:\config.properties"
    # with open(file_path) as file_object:
    #     for line in file_object:
    #         print(line.rstrip())
    # 读取后存储在列表中 , 列表中的数据可以转化为字符串
    # file_path = "pi_digits.txt"
    # with open(file_path) as file_object:
    #     lines = file_object.readlines()
    # pi_strings = ''
    # for line in lines:
    #     pi_strings += line.strip()
    # print(pi_strings)
    # if '3.14' in pi_strings:
    #     print('3.14存在在开头')
    # 写入文件 open()第二个参数 可以是 'r':只读模式 'w':写入模式 'a':附加模式 'r+':能读能写
    # file_path = 'write_test.txt'
    # with open(file_path, 'w', encoding='utf-8') as file_object:
    #     file_object.write('我就随便写写~')
    # ---------------------------------------
    # 错误捕获 try except ZeroDivisionError:0为除数异常 FileNotFound:找不到文件异常 在捕获到异常时用pass关键词可以让程序自动忽略该异常
    # print('欢迎使用除法计算器')
    # print('输入q退出计算器')
    # while True :
    #     first_number = input('\n请输入第一个数字:')
    #     if first_number == 'q':
    #         break;
    #     second_number = input('\n请输入第二个数字:')
    #     if second_number == 'q':
    #         break;
    #     try:
    #         answer = int(first_number) / int(second_number)
    #     except ZeroDivisionError:
    #         print('请不要把0作为除数!')
    #     else:
    #         print(first_number + '/' + second_number + '=' + str(answer))
    # print('感谢使用计算器')
    # ------------------------------------
    # 存储数据 导入模块json来处理
    # file_name = 'number.json'
    # number = [1,2,3,4,5,6,7,8,9]
    # with open(file_name, 'w') as obj_file:
    #     json.dump(number, obj_file)
    # with open(file_name) as obj_file:
    #     new_number = json.load(obj_file)
    # print(new_number)
    # ------------------------------------
    # 保存和读取用户生成的数据
    # file_name = 'user_name.json'
    # try:
    #     with open(file_name, 'r') as obj_file:
    #         json_load = json.load(obj_file)
    #     print('welcome ,' + json_load)
    # except FileNotFoundError:
    #     user_name = input('please write your name:')
    #     with open(file_name, 'w') as obj_file:
    #         json.dump(user_name, obj_file)
    #     print('has remember your name : ' + user_name)
    # -------------------------------------
    # 单元测试方法
    # -------------------------------------
    #
