# 1.Python 标识符
'''
以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import而导入
以双下划线开头的 __foo 代表类的私有成员
以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__()代表类的构造函数
'''

# 2.Python 保留字符
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# Python 注释
'''
这是多行注释，使用单引号
'''

"""
这是多行注释，使用双引号
"""

# 3.行和缩进
'''
Python 的代码块不使用大括号 {} 来控制类，函数以及其它逻辑判断 python 最具特色的就是用缩进来写模块
缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行
'''

# 4.多行语句
greeting = "Hello " + \
        "Python" + \
        "Nice to meet you"

lang = {"Python", "PHP", "Perl", 
        "JavaScript", "C++"}

print(greeting)
print(lang)

# 5.数据类型
'''
Python 3 中数有三种类型：整数、浮点数和复数
    整数， 如 1, 12345556666666
    浮点数，如 1.23、3E-2
    复数，如 1 + 2j、 1.1 + 2.2j
'''

# 6.字符串
'''
字符串是不可变的
'''
str = "hello"
str += ", world"
print(str)

# 7.Python 空白行
'''
如果一行只包含空格，制表符，回车换行符，那么我们称该行为空白行

空白行不是 Python 语句的一部分，主要用于分隔两段不同功能或含义的代码

比如函数之间或类的方法之间用空行分隔，表示一段新的代码的开始

类和函数入口之间也用一行空行分隔，以突出函数入口的开始

空行与代码缩进不同，空行并不是 Python 语法的一部分

书写时可以不插入空白行，Python 解释器运行也不会出错
'''

# 8.读取用户输入
'''
可以使用 input([prompt]) 提示和读取用户的输入，prompt 参数为提示语句
默认情况下读取到回车换行符就停止读取
'''
s = input("\n\nsay some words:")
print(s)

# 9.print 输出
x = "Hello"
y = "World"
print(x)
print(y)

print(x, end="")
print(y, end="")

# 10.Python 语句分隔符
'''
Python 每条语句结尾的分号 (;) 不是强制需要的，因为 Python 默认以换行符(新行) 分隔每条语句
'''

# 11.Python 引号
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落
包含了多个语句"""

# 12.代码块
'''
一般情况下，我们把缩进相同的语句称之为一个代码块
if 、while 、def 和 class 这样的复合语句，首行以关键字开始，以冒号( : )结束， 该行之后的一行或多行代码构成代码块
'''

# 13.命令行参数
'''
python -V 查看版本
python -h 帮助菜单
python setup.py build 安装第三方包
python setup.py install
'''
