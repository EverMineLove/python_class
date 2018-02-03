import numpy as np
#
# # c=[1,2,3,4,5]  #向量
# # d=np.array(c)
# # print('c=',c)
# # print('d=',d)
# # print(d.shape)
# #if __name__=='__main__':  ##表示从该.py文件启动，则……  去掉也可以  调用其他 __.py文件的函数，会显示其他文件名称  可不写
# print(__name__)
# print(__file__)
# print("hello,he'a boy.")
# print('how to say "wow".')
#
# x=3,4  #tuple  不可更改  等同于x=(3,4)
# print(x)
# x=[3,4] #list
#
# a=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]] # 二维数组
# b=np.array(a)
# c=np.array(a,dtype=np.float)  #指定元素类型
# d=np.array(a,dtype=np.complex) #指定元素类型
# print('type:',type(a),type(b))
# print('dtype:',b.dtype,c.dtype,d.dtype)
# print('a=',a)
# print('b=',b)
# print('c=',c)
# print('d=',d)
# print(b.shape)
# print('b转置：\n',b.transpose())
# #astype做元素类型安全转换
# c1=c.astype(np.int)
# print('c1=',c1)
# #强制转换可能出问题  面目全非
# # c.dtype=np.int
# # print('强制转换 c=',c)
#
# #强制更改行列变换解释
# # b.shape=5,3  #b.shape=5,-1  效果一致
# # print('shape变换后的b:',b)
# # print('shape变换后的b:',b.shape)
# ##reshape：数组b和bb共享内存，修改一个将会影响另外一个
# bb=b.reshape(5,-1)   #bb=b.reshape(5,3)
# print('bb: \n',bb)
#
# #修改数组中元素
# b[0][0]=20
# print('b=\n',b)
# print('bb=\n',bb)
#
# r1=np.random.rand(5)  #[0,1)
# print(r1)
# print(type(r1))
# r2=np.random.rand(3,4)
# print(r2)
# print(type(r2),r2.shape)
#
# #arrange
# a=np.arange(10)
# print(a)
# print('a[1:9:2]:',a[1:9:2])
# print('a[8:1:-2]:',a[8:1:-2])
# print('a[::-1]:',a[::-1])  #翻转
# a[1:4]=10,20,30
# print(a)
# b=a[2:5]   #b 仅为视图，不是真实数据
# b[0]=200  #a,b共享内存
# print(a)
# ###################
# a=np.logspace(0,9,10,base=2)
# print(a)
# i=np.arange(0,10,2)  #index
# b=a[i]    #整数数组作为索引，数据完成拷贝
# print(b)
# b[2]=1.6
# print(b)    #b 实际存在 b元素更改 a元素不变
# print('a未改变：',a)   # a未改变
#
# ###################
# a=np.arange(1,10)  #[1,10)
# a=np.arange(1,10,dtype=float) #得到浮点型
# print('np.arange',a)
# np.set_printoptions(linewidth=100)  #设置每行字符数
# a=np.arange(1,10,0.1)  #0.1为步长
# print('np.arange',a)
# #linspace
# b=np.linspace(1,10,10)   #11个数
# print('b=\n',b)
# b1=np.linspace(1,10,50)
# print('b1=\n',b1)
# b2=np.linspace(1,10,50,dtype=int)
# print('b2=\n',b2)
# b3=np.linspace(1,10,49,endpoint=False)   #先生成50个数，就是b1丢掉最后一个数字
# print('b3=\n',b3)
#
# #logspace 等比数列
# np.set_printoptions(suppress=True,linewidth=100)  #强制输出小数值
# c=np.logspace(1,10,11,endpoint=True,base=3)  #默认endpoint=True,base=10
# print('c=\n',c)
# c1=np.logspace(1,4,4,endpoint=True,base=2)
# print('c1=\n',c1)
#
# #
# d='abc1ABC+=[]'
# d1=np.fromstring(d,dtype=np.int8)
# print('d1:\n',d1)
#
# a=np.random.rand(10)
# print(a)
# print(a>0.5)
# print(a[a>0.5])
# a[a>0.5]=0.5
# print(a)
#
# ########
# a=np.arange(10)
# b=np.arange(0,60,10)
# b.shape=(-1,1)
# c=b+a  #行+列
# print(c)
# c=np.arange(0,60,10).reshape(-1,1)+np.arange(10)
# print(c[[0,2,5],[0,2,5]])
# print(c[2:,[0,2,5]])
# print(a+100)
# print(b+100)
#
#
# ##计时
# import time
# x=np.linspace(0,10,10)
# start=time.clock()
# y=np.sin(x)
# t1=time.clock() - start
# print(t1)
#
# ############################
# a=[8,0,1,2,4,3,2,3,4,5,6,7,8,3]
# b=np.unique(a)
# print(a)
# print('一维去重：',b)
#
# a=np.array(((1,2,3),(1,2,3),(2,3,4),(3,5,7)))
# b=np.unique(a)
# print(a)
# print('二维去重错误方案：',b)  #不对
#
# c=set()  #集合 集合不重复，没顺序
# for t in a:
#     c.add(tuple(t))   #元组tuple不能被更改，集合不重复
# print('二维去重：',c)
# print('二维去重1：\n',np.array(list(c)))
# print('二维去重2：\n',np.array(list(set([tuple(t) for t in c]))))

#####stack
# a=np.arange(1,7).reshape(2,3)
# b=np.arange(11,17).reshape(2,3)
# c=np.arange(21,27).reshape(2,3)
# d=np.arange(31,37).reshape(2,3)
# e1=np.stack((a,b,c,d),axis=0)
# print('axis=0',e1.shape,'\n',e1)
# e2=np.stack((a,b,c,d),axis=1)
# print('axis=1',e2.shape,'\n',e2)
# e3=np.stack((a,b,c,d),axis=2)
# print('axis=2',e3.shape,'\n',e3)

#####绘图
import matplotlib.pyplot as plt
import math

mu=0
sigma=1
x=np.linspace(mu-3*sigma,mu+3*sigma,51)
y=np.exp(-(x-mu)**2/(2*sigma**2))/(math.sqrt(2*math.pi)*sigma)
print('x=\n',x)
print('y=\n',y)
plt.figure(facecolor='w')
plt.plot(x,y,'ro-',linewidth=2,mec='k')
plt.show()

