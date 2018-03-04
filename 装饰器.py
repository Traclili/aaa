#Author: Jiang Wei
#装饰器：本质是函数，（装饰其他函数）就是为其它函数添加附加功能
'''原则：不能修改被装饰函数的源代码，不能修改被装饰函数的调用方式'''




'''
def foo():
    print("in the foo")
    bar()
def bar():
    print("in the bar")
这一段代码可以正常运行，因为调用foo之前foo跟bar都已经声明并且已经在内存中存好
foo()
'''

'''
def foo():
    print("in the foo")
    bar()
foo()    
def bar():
    print("in the bar")
这一段代码不可以正常运行，报错，因为调用foo之前bar还没有声明在内存中找不到，因此可以证明
函数即变量，它只是声明好了你不调用它就不会运行，你调用时才会去找对应的内存



def foo(fun):
    start_time = time.time()
    print("-------")
    fun()
    print("++++++++")
    stop_time = time.time()
    print("运行时间%s"%(stop_time-start_time))
    return fun

@foo #bar = foo(bar)


def bar():
    time.sleep(3)
    print("in the bar")
bar()#未修改bar函数的源码但是给它添加了新功能
'''

'''
#这是一个真正的装饰器 但是并不完美，因为如果有带参数的函数时就不能装饰
import time
def timer(func):
    def deco():
        start_time = time.time()
        print(func)
        func()

        stop_time = time.time()
    return deco
@timer #他的作用是在后面test2函数后面隐实的加上 test2 = timer(test2)，因此真正运行的是deco
# 这个函数，test2这个函数被放在deco里面去运行了
def test2():
    time.sleep(2)
    print("in the test2")
#test2 = timer(test2)
test2()
print(test2)#它们的内存地址都不一样
#装饰器的使用场景 即你的函数已经写好已经上线，在你不能修改源代码的情况之下给这个函数
# 添加功能 '''


#这是一个完美的装饰器 可以装饰任何有参没参的函数
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        print(func)
        func(*args,**kwargs)

        stop_time = time.time()
    return deco

@timer #他的作用是在后面test2函数后面隐式的加上 test2 = timer(test2)，因此真正运行的是deco
# 这个函数，test2这个函数被放在deco里面去运行了
def test2():
    time.sleep(2)
    print("in the test2")
#test2 = timer(test2)
test2()
print(test2)#它们的内存地址都不一样

@timer
def test3(name,x,z):
    print(name,x,z)
#test3 = timer(test3)
test3("jw",30,"m")

#装饰器的使用场景 即你的函数已经写好已经上线，在你不能修改源代码的情况之下给这个函数
# 添加功能