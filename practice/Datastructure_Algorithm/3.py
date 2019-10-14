# import sys

# list = [1,2,3,4]
# it = iter(list)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# class MyNUmbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         if self.a < 21:
#             x = self.a
#             self.a +=1
#             return x 
#         else:
#             raise StopIteration

# myclass = MyNUmbers()
# myiter= iter(myclass)

# for i in myiter:
#     print(i)

# import sys

# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return 
#         yield a 
#         a, b = b, a+b
#         counter += 1
# f = fibonacci(10)
# while True:
#     try:
#         print(next(f),end=' ')
#     except StopIteration:
#         sys.exit()

# # 可写函数说明
# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    for var in vartuple:
#       print (var)
#    return
 
# # 调用printinfo 函数
# # printinfo( 10 )
# printinfo( 70, 60, 50 )

# matrix = [
#     [1,2,3,4],
#     [4,5,6,7],
#     [9,10,11,12],
# ]
# # transposed = []
# # for i in range(4):
# #     transposed.append([row[i] for row in matrix])
# # print(transposed)
# transpond = []
# for i in range(4):
#     transpond_row = []
#     for row in matrix:
#         transpond_row.append(row[i])
#     transpond.append(transpond_row)
# print(transpond)
#!/usr/bin/python3
import pickle

# 使用pickle模块将数据对象保存到文件
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}

# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)

# output = open('data.pkl', 'wb')

# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)

# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)

# output.close()
# #!/usr/bin/python3
# import pprint, pickle

# #使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')

# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)

# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)

# # pkl_file.close()
# class MyClass:
#     def __init__(self):
#         self.data = []

#     i = 12345
#     def f(self):
#         return 'hello'
    
# x = MyClass()
# print("MyClass i:",x.i)
# print("Myclass f:",x.f())

# class people:
#     name = ''
#     age = 0
#     __weight__ = 0
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight__ = w
#     def speak(self):
#         print("%s say: I am %d years old"%(self.name,self.age))

# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade = g
#     def speak(self):
#         print("%s say: I am %d years old, i am in %d grade"%(self.name,self.age,self.grade))

# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("I am %s, i am a speaker, the topic of my speech is %s"%(self.name,self.topic))
# class sample(speaker,student):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)

# test = sample("Tim",25,80,4,"python")
# test.speak()
# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b
 
#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
 
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)
"""源自鱼C论坛用户的猜数字游戏"""

import random
import re
from sys import exit

def main():
    time = 3
    count = 1
    num = 0
    dict = {'0': 5, '1': 10, '2': 20, '3': 50, '4': 100}

    print('猜数字')
    # go = int(input('开始：1\n结束：0\n->'))

    # while go != 1 and go != 0:
    #     print('Input 1 or 0.')
    #     go = int(input('开始：1\n结束：0\n->'))  # 重复输入
    # if go == 1:
    #     pass
    # elif go == 0:
    #     exit()

#     print('｛LV0.新手}｛LV1.简单｝｛LV2.一般｝｛LV3.困难｝｛LV4.噩梦｝｛LV5.地狱｝')
#     r = input('Level:')
#     r = re.sub('\D', '', r)  # 抽出数字

#     if r.strip() == '':  # 检查是否含有数字
#         print('隐藏难度｛LV6.调戏｝')
#         n = 1000
#         time = 99
#     else:
#         n = dict.get(r, 500)

#     secret = random.randint(1, n + 1)  # 随机的范围 根据难度调整
#     print('猜猜{1-%s}之间的数:' % n)

#     while True:  # 机会内循环即可，猜中了可以用break跳出循环
#         print('一定是：' , end = '')
#         num = input(555)

#         if num.isdigit():  # 检查玩家输入是否有误，防止程序崩溃
#             num = int(num)
#             if num < 1:
#                 print('现在就放弃太可惜了')
#             elif num > n:
#                 print('超出范围')
#             elif num > secret:
#                 print('太大')
#             elif num < secret:
#                 print('太小')
#             else:
#                 if count == 1:  # 算是奖励机制？
#                     print('棒')
#                 elif count == 2:
#                     print('赞')
#                 else:
#                     print('好')
#                 break

#             time -= 1
#             count += 1  # 奖励机制计数

#             if time == 0:
#                 print('正确答案：%s' % secret)
#                 break
#             else:
#                 print('还有[%s]次机会:' % time)
#         else:
#             print('要崩溃了!!!')
#     print('游戏结束!')

# if __name__ == '__main__':
#     main()
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False

# # 测试字符串和数字
# print(is_number('foo'))   # False
# print(is_number('1'))     # True
# print(is_number('1.3'))   # True
# print(is_number('-1.37')) # True
# print(is_number('1e3'))   # True
 
# # 测试 Unicode
# # 阿拉伯语 5
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))  # True
# # 中文数字
# print(is_number('四')) # True
# # 版权号
# print(is_number('©'))  # False
# print ("Content-type:text/html")
# print ()                             # 空行，告诉服务器结束头部
# print ('<html>')
# print ('<head>')
# print ('<meta charset="utf-8">')
# print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
# print ('</head>')
# print ('<body>')
# print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
# print ('</body>')
# print ('</html>')
# Filename : test.py
# author by : www.runoob.com
 
# 定义一个函数
# def hcf(x, y):
#    """该函数返回两个数的最大公约数"""
 
#    # 获取最小值
#    if x > y:
#        smaller = y
#    else:
#        smaller = x
 
#    for i in range(1,smaller + 1):
#        if((x % i == 0) and (y % i == 0)):
#            hcf = i
 
#    return hcf
 
 
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
 
# print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))
# def recur_fibo(n):
#     if n <=1:
#         return n
#     else:
#         return(recur_fibo(n-1)+recur_fibo(n-2))

# nterms = int(input("Input:"))
# if nterms <= 0:
#     print("Input positve number:")
# else:
#     print("febonacci sequence:")
#     for i in range(nterms):
#         print(recur_fibo(i))
people = {}
for x in range(1,31):
    people[x] = 1
check = 0
i = 1
j = 0
while i <=31:
    if i == 31:
        i = 1
    elif j ==15:
        break
    else:
        if people[i] == 0:
            i += 1
            continue
        else:
            check += 1
            if check == 9:
                people[i] = 0
                check = 0
                print("{} is OK !".format(i))
                j+=1
            else:
                i += 1
                continue


        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            ln = len(nums)
            if ln == 0:
                return []
            
            queue = []
            for i in range(k):
                while queue and queue[-1][0] <= nums[i]:
                    queue.pop()
                queue.append((nums[i], i))
            
            i = k
            result = [queue[0][0]]
            while i < ln:
                #remove the first element from the queue if it is outside the window
                if i - queue[0][1] >= k:
                    queue.pop(0)
                
                # also remove any elements that are less than the current num
                # as long as the current num is in the boundary I don't care about any other number
                # if this is the max, then be it.
                while queue and queue[-1][0] <= nums[i]:
                    queue.pop()
                queue.append((nums[i], i))
                
                result.append(queue[0][0])
                i += 1
            
            return result

#朴素贝叶斯模型Naive Bayesian Model
'''最简单的监督学习分类器，模型建立在每一个类别的特征向量服从正态分布的基础上，是一个概率分类器。整个分布函数被假设为一个
高斯分布，每一类别一组系数，当给定训练数据时，算法将会估计每一个类别的向量均值和方差矩阵，然后根据这些进行预测。
特点：如果没有很多数据，该模型会比很复杂的模型获得更好的性能，因为复杂的模型用了太多假设，以致产生欠拟合。

贝叶斯：朴素贝叶斯（Naive Bayes）算法、TAN算法；'''

#K近邻K Nearest Neighbors
'''这个算法首先储存所有的训练样本，然后通过分析（包括选举、计算加权和等方式）一个新样本周围的K个最近邻，然后把新样本标记在K近邻点中频率最高的类。
又称为“基于样本的学习”，为了预测，对于给定的输入搜索最近的已知其相应的特征向量。
特点：简单有效，因需储存所有的训练数据，内存占用较大，速度较慢。使用该方法通常训练集先聚类来降低数据大小。'''
#支持向量机Support Vector Machines
'''基于核函数的方法，通过某些核函数把特征向量映射到高维空间（一般情况下高位空间上比低维空间上更线性可分），然后建立一个
线性判别函数（即将一个高维空间中的能够区分训练数据的最优超平面）。最优解在某种意义上，是两类中距离分割面最近的特征向量和
分割面的距离最大化。离分割面最近的特征向量被称为“支持向量”，其他向量则不影响分割面（决策函数）。
特点：当数据集比较小的时候，支持向量机的效果常常很好。对于核来说，不仅只存在于支持向量机内，对于任意的算法，只要计算出现了內积，都可以用
核函数代替，从而提高在高维数据上的性能。'''
#决策树Decision Tree
'''二叉树。当每个叶子节点用类别标识（多个叶子可能有相同的标识）时，它可以表示分类树；当每个叶子节点被分配一个常量（所以回归函数是分段常量）
时，它可以表示为回归树。决策树从根节点递归构造。所有数据根据初始和替代分裂点来划分给左右子结点，然后算法回归的继续分裂左右子结点。

算法停止情况：树的深度达到了指定的最大值；在该结点训练样本的数目少于指定值；在该结点所有的样本属于同一类；跟随选择相比，能选择到的最好的
             分裂已经基本没有意义则停止分裂。
优点：计算简单，易于理解；适应不同的数据类型（包括类别数据，数值数据，未归一化数据和混合的数据）；
     比较适合处理有缺失属性的样本；通过分裂的顺序给数据特征赋不同的重要性；处理不相关的特征；
     在相对短的时间内对大型数据做出可行且结果良好的结果；决策树构成了其他算法的基础（如boosting和随机数）。
缺点：容易发生过拟合（随机森林可以很大程度上减少过拟合）；忽略数据之间的相关性；对于各类别样本数量不一致的数据，在决策树中，
      信息增益的结果偏向于具有更多数值的特征（使用信息增益皆有此特点，如RF）。

决策树：ID3、C4.5（C5.0）、CART、PUBLIC、SLIQ、SPRINT算法；'''

#boosting
'''监督分类学习方法，组合多个弱分类器，产生强大的分类器组。boosting分类器和随机森林在内部使用了决策树，继承了局册数的
很多性质(如能够处理混合数据类型、没有归一化的数据、特征丢失等)。
特点：简单，不容易发生过拟合，不用做特征筛选。boosting算法是一个两类分类器（不想决策树和随机森林）。'''
#随机森林Random Trees
'''可以解决分类和回归问题。通过手机很多树的子节点对各个类别投票，然后选择获得最多投票的类别作为判断结果，通过计算森林的所有子节点
的值的平均值来解决回归问题。
随机森林建立时的基本子系统也是决策树。
特点：与boosting和决策树相比，随机森林可以使用更少的重要分量，获得更好的预测性能。可以收缩特征集的大小，在不损失性能的前提下
减少量和内存使用随机森林。'''
#神经网络Neural Networks
'''对非线可分数据的分类方法
特点：不知道隐藏层计算的东西的意义；有比较多的局部最优值，可以通过多次随机设定初始值，然后运行梯度下降算法获得最优质值。'''
