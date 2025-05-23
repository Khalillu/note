<<<<<<< Updated upstream
# Pycharm笔记(note)：

## Python基础语法：

### 基础语法与缩进：

##### 基础语法：

Python中，每个对象由标识、类型、value 组成

变量也称为：对象的引用(reference)。变量存储的就是对象的地址

变量通过地址引用了“对象”

变量位于栈内存，对象位于堆内存

标识符规则：

1.区分大小写 

2.第一个字符必须是字母、下划线。其后的字符是：字母、数字、下划线

3.不能使用关键字。比如：'if'  'or'  'while'等 

4.以双下划线开头和结尾的名称通常含有特殊含义，尽量避免这种写法

/表示连接符，就算代码中进行了换行，而实际输出中，也没有进行换行，如下：![image-20250117230500065](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250117230507067.png)

Python标识符命名规则：

![image-20250117232050054](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250117232051875.png)

尽量避免双下划线，以免与系统中的内置函数发生冲突

关键字不能作为标识符

标识符命名不能用数字开头，只能用英文字母

基本运算符：

![image-20250118135036866](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118135043980.png)

Python中整数可以为无限大，没有数据范围限制

Python中常用的四种进制：二进制（0b 或 0B），八进制（0o 或 0

O），十进制，十六进制（0x 或 0X）

#### 逻辑运算符：

or 逻辑或

and逻辑与

not 逻辑非

各逻辑运算符规则如下：

![image-20250118143535300](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118143535348.png)

#### 比较运算符：

所有比较运算符返回1表示真，返回0表示假。这分别与特殊变量True和False等价。以下假设变量a为15，变量b为30：![image-20250118143815508](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118143815545.png)

#### 位运算符

按位运算符是把数字看作二进制来进行计算的。

![image-20250118144340306](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118144340391.png)

Python中不支持自增、自减功能

#### 同一运算符

is函数与is not函数

![image-20250118145102779](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145102834.png)

![image-20250118145449810](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145449894.png)

命令行模式与文件模式的区别：命令行只能在[-5,256]区间中进行缓存

#### 成员运算符

in 和 in not 函数

具体功能如下：

![image-20250118145646867](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145646935.png)

![image-20250118145748159](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145748214.png)

***位运算和算术运算>比较运算符>赋值运算符>逻辑运算符***

##### 缩进：

Python中通常通过缩进来区分不同语句的包含与包含于关系，要时刻小心“空格”是否对代码有影响



## Python数据类型：

### Python内置的数据类型：

### int：

使用int()实现类型转换：

1.浮点数直接舍去小数部分

2.布尔值True转为1，Falise转为0（eg：int（True) = 1）

3.字符串符合整数格式（浮点数格式不行）则直接转成对应整数，否则报错。

整数和浮点数混合运算时，表达式结果自动转型成浮点数。比如：2+8.0的结果是10.0

### float：

使用float()实现类型转换（与int()相似）

round(value)可以返回四舍五入的值。但不会改变原有值，而是产生新的值

增加运算符两个符号中不能有空格，反面eg："+ ="错误，应为"+="



### bool：

bool("a") = True

bool("") = Fal se

空字符串转换为False，非空字符串转化为True

![image-20250118143228499](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118143228581.png)

### complex：



## Python数据结构：

## 序列：

序列是一种数据存储方式，用来存储一系列的数据。

在内存中，序列就是一块用来存放多个值的连续的内存空间。

序列中存储的是整数对象的地址，而不是整数对象的值。

### 字符串：

![image-20250118144520384](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118144520481.png)



#### 创建字符串：

1. 通过单引号或双引号创建字符串。a = 'abc' 或 a = "abc"

使用引号的好处是可以创建本身就包含引号的字符串，而不用使用转义字符

2. 通过三个单引号或三个双引号创建多行字符串。
3. Python中允许创建空字符串，不包含任何字符且长度为0。eg:a=''

#### len()函数：

Python内置函数，用于计算字符串长度。

#### 转义字符：

![image-20250119170131911](C:/Users/18929/AppData/Roaming/Typora/typora-user-images/image-20250119170131911.png)

#### 字符串拼接：

![image-20250119170238910](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119170238942.png)

#### 字符串复制：

使用"*"实现字符串的复制

#### 不换行打印：

在print函数中加入end,eg:print("abc",end="123")

​					     print("abc")	#输出结果为abc123abc

#### input()函数：

input()函数括号中会在终端打印出来，同时赋予变量的值。eg：name = input("asdas")	#name = 我们所输入的值，而"asdas"将会被打印出来

#### 字符串的修改：

![image-20250119180308626](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119180308665.png)

由于字符串不可改变，因此我们需要替换掉某些字符。常使用replace()函数创建新变量。

如上述图片中，则将'c'转变成'高'，然后在'c'的位置替换成高，创建一个新变量b

#### str()实现数字转型字符串：

a = str("")

#### 使用[]提取字符：

![image-20250119181124137](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119181124178.png)



#### 字符串切片slice操作：

提取子字符串（按照索引来切片）

![image-20250119182617681](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119182617722.png)

“包头不包尾”，print(a[:2]) 范围包括从[0,1]的区间内，而不包含a[2]

#### split()分割和join()合并：

![image-20250119184329723](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119184329768.png)

![image-20250119184644504](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119184644537.png)

split()函数格式为:新变量 = 变量.split("用于分割的字符串")

join()函数格式为:'用于链接各子字符串的字符串'.join(变量)	***join()函数仅创建一次新对象，而"+"会多次新建对象，不断复制。***

#### 字符串驻留机制：

a ="dd"

b ="dd"

a 与 b id相同，为同一对象，可以通过is语句判断

#### 字符串常用方法汇总：

![image-20250119193850054](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119193850101.png)

#### 通过strip()去除字符串首尾指定信息:

![image-20250119194006359](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119194006398.png)

#### 大小写转换：

![image-20250119194103757](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119194103800.png)

#### 格式排版：

center()居中对齐、ljust()左对齐、rjust()右对齐

a = "SXT"

a.center(10,"#")	'###SXT####'	#10为a字符的格式长度，而"字符串"表示你所要添加的字符串

ljust()与rjust()同理

#### 特征判断方法：

![image-20250119195129554](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119195129590.png)

#### 字符串的格式化：

![image-20250119195306231](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119195306273.png)

#### 填充与对齐：

![image-20250119202359936](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119202359975.png)

#### 数字格式化：

浮点数通过f，整数通过d进行需要的格式化。

![](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119202536932.png)

#### 可变字符串：

![image-20250119202715932](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119202715991.png)

需引入io库，即import io

具体实现如下：

![image-20250119203509964](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119203509997.png)



#### 类型转换总结：

![image-20250119203602001](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119203602053.png)

### 列表：

列表是用于存储任意数目、任意类型的数据集合。

列表是内置可变序列，是包含多个元素的有序连续的内存空间。列表的标准语法格式：

a =[10,20,30,40]

其中，10,20,30,40这些称为：列表a的**元素**。

列表中的元素可以各不相同，可以是任意类型。比如：

a = [10,20,'abc',True]

Python的列表大小可变，根据需要随时增加或缩小

#### 列表的创建：

1.range()创建整数列表

![image-20250118223335095](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118223335156.png)

2.推导式生成列表：

![image-20250118223831820](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118223831861.png)

#### 列表元素的增加：

append()方法：原地修改列表对象，是真正的列表尾部添加新的元素，速度最快，推荐使用。

![image-20250118224426219](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118224426251.png)

+运算符操作：并不是真正的尾部添加元素，而是创建新的列表对象；将原列表的元素和新列表的元素依次复制到新的列表对象中。这样，会涉及大量的复制操作，对于操作大量元素不建议使用。

![image-20250118224620724](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118224620753.png)

extend()方法：将目标列表的所有元素添加到本列表的尾部，属于原地操作，不创建新的列表对象。

![image-20250118224724897](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118224724927.png)

insert()插入元素：使用insert()方法可以将指定的元素插入到列表对象的任意指定位置。

![image-20250118225036475](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225036519.png)

乘法拓展

：![image-20250118225141068](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225141104.png)

1. 我们可以通过索引直接访问元素。索引的区间位于[0,列表长度-1]这个范围

2. index()获得指定元素在列表中首次出现的索引

   ![](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230006078.png)

   3.count()获得指定元素在列表中出现的次数。

4. len()返回列表长度，即列表中包含元素的个数。

5. 成员资格判断：

![image-20250118230216790](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230216827.png)

print(100 in a)	存在返回True，不存在返回False

#### 列表元素的删除：

删除元素底层是：元素的拷贝

del删除:

![image-20250118225403982](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225404019.png)

pop()方法：

![image-20250118225436728](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225436761.png)

remove()方法：删除首次出现的指定元素，若不存在该元素抛出异常。

![image-20250118225606772](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225606802.png)

#### 列表的遍历：

![image-20250118230944216](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230944248.png)

#### 列表复制：

![image-20250118231134664](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231134702.png)

列表排序：  

 1.修改原列表：

![image-20250118231225990](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231226029.png)

 2.创建新列表：

![image-20250118231656601](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231656639.png)

3.reversed()返回迭代器

![image-20250118231759860](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231759901.png)

其他内置函数：

![image-20250118232001992](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118232002035.png)

#### 二维列表：

![image-20250118232755533](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118232755581.png)

### 字典：

#### 1.字典的概念：

字典是”键值对“的无序可变序列，字典中的每个元素都是一个”键值对“，包含：”键对象“和”值对象“。可以通过”键对象“实现快速获取、删除、更新对应的“值对象”

![image-20250118234835907](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118234835951.png)

#### 2.字典的创建：

1.我们可以通过{}、dict{}来创建字典对象

2.zip()

3.fromkeys创建值为空的字典

![image-20250118235102095](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118235102142.png)

#### 字典元素的访问：

![image-20250118235837792](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118235837842.png)

![image-20250119000018254](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000018294.png)

![image-20250119000040591](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000040630.png)

#### 字典元素的添加、修改、删除：

![image-20250119000334360](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000334404.png)

![image-20250119000546667](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000546711.png)

#### 3.序列解包：

![image-20250119000920352](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000920396.png)

#### 4.表格数据是用字典和列表存储的访问：与上述数据结构相似

将一个键值对放进字典的底层过程：

![image-20250119001904097](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119001904146.png)











### 元组： 

1.元组的基本概念

元组属于不可变序列，不能修改元组中的元素。因此，元组没有增加元素、修改元素、删除元素相关的方法。

![image-20250118232917273](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118232917317.png)

元组通过小括号()进行创建元组

2.元组的元素访问和计数：

![image-20250118233326926](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118233326971.png)

排序之后转换了数据结构，从元组变成了可修改的序列——列表 

![image-20250118233514490](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118233514538.png)

生成器推导式创建元组：

![image-20250118233852607](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118233852646.png)

元组总结：

![image-20250118234526978](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118234527016.png)

### 集合：

#### 1.集合的概念：

集合是无序可变，元素不能重复。

![image-20250119001947887](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119001947927.png)

#### 2.集合创建和删除：

![image-20250119002022593](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119002022634.png)

#### 3.集合相关操作：

![image-20250119002118012](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119002118052.png)



### 切片：

#### 切片操作：

#### 1.列表切片:

![image-20250118230502017](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230502058.png)

##### 列表其他操作：

![image-20250118230629634](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230629676.png)

#### 元组切片：



## Python跳进控制以及循环控制：

#### while循环结构：

**while 条件表达式：**

​	**循环体语句**

![image-20250119203905490](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119203905530.png)

#### for循环：

![image-20250119204213398](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119204213442.png)

![image-20250119204310583](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119204310627.png)

![image-20250119204642377](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119204642420.png)

#### 嵌套循环：

![image-20250119205828886](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119205828918.png)

使用缩进来表示for循环内的语句

#### break与continue：与c语言一致



![image-20250119211451500](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211451544.png)

#### 循环代码优化原则：

![image-20250119211615428](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211615467.png)

![image-20250119211633051](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211633084.png)

### 使用zip()并行迭代：

![image-20250120153454452](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120153454502.png)

## Python推导式：

#### 推导式创建序列：

![image-20250119211744396](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211744433.png)

#### 推导式的类型：

![image-20250119211835106](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211835145.png)

##### 列表推导式：

语法：`[表达式 for item in 可迭代对象]`

或者：`{表达式 for item in 可迭代对象 if 条件判断}`

**字典推导式**：

格式： `{key_expression: value_expression for 表达式 in 可迭代对象}`

![image-20250120154942294](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120154942342.png)

实际代码应用：

![image-20250120160023924](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120160023959.png)



**集合推导式：**

集合推导式生成集合，和列表推导式的语法格式类似：

区别是列表推导式是[]，而集合推导式是{}

![image-20250120160205930](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120160205973.png)

**生成器推导式**：

![image-20250120160249419](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120160249468.png)





## Python错误和异常捕捉：

## Python map、lambda、filter函数的使用：

#### map函数表达式：

`map(函数对象,[可迭代对象])`

作用：将可迭代对象中的每一个元素均运用到函数对象中

应用：

![image-20250120162101700](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120162101742.png)





#### lambda表达式和匿名函数：

基本语法：`lambda arg1,arg2,arg3...:	<表达式>`

arg1 arg2 arg3为函数的参数。<表达式>相当于函数体。运算结果是表达式的运算结果

![image-20250120161053108](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120161053145.png)

![image-20250120161103351](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120161103385.png)

#### filter()函数：

格式：filter(函数对象,可迭代对象)

允许你根据指定的条件从一个可迭代对象，如列表元组或字典中筛选元素。



## Python面向对象：

Python完全采用了面向对象的思想，是真正面向对象的编程语言，完全支持面向对象的基本功能。如：继承、多态、封装等。

面向过程与面向对象的区别：面向过程首先思考“怎么按步骤实现？”比如：把大象放冰箱分三步

面向对象首先思考“怎么设计这个事物”

![image-20250120163021495](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163021537.png)

![image-20250120163054910](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163054955.png)



![image-20250120163153869](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163153911.png)

### 类与实例化：

类的定义：类可以看作是一个模板，或者图纸，系统根据类的定义造出对象

类：我们称为：“class”。对象：我们叫做：object,instance

对象就是实例

#### 属性和方法：

我们通过类定义数据类型的属性(数据)和方法(行为)也就是说，“类将行为和状态打包在一起”。

![image-20250120163710190](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163710233.png)

对象是类的具体实体，一般称为“类的实例”。类看作“饼干模具”，对象就是根据这个“模具”做出来的饼干

![image-20250120163818227](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163818277.png)

定义类的语法格式如下：

`class 类名：`

​	`类体`

定义类的要点：

![image-20250120163956531](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163956573.png)

#####  init构造方法

![image-20250120165822803](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120165822844.png)

![image-20250120165934931](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120165934984.png)

##### 实例属性和实例方法：

###### 实例属性：

![image-20250120170333012](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120170333061.png)

![image-20250120170507865](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120170507922.png)

***仅在s2中加入了address，而类中是没有address的***

###### 实例方法：

![image-20250120170737615](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120170737669.png)

![image-20250120171015861](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120171015904.png)

![image-20250120171316478](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120171316521.png)

#### 类对象：

当解释器执行class语句时，就会创建一个类对象。

![image-20250120172851257](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120172851306.png)



### 类变量以及方法：

#### 类变量：

在类中，所有实例之间共享的变量。实例变量是每个实力独有的，而类变量则被所有实例共享。

#### 类方法：

类方法通过装饰器@classmethod来定义，格式如下：

`@classmethod`

`def	类方法名(cls [,形参列表]):`

​	     `方法体`

![image-20250120180350994](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120180351037.png)

#### 静态方法：

格式：

`@staticmethod`

`def 静态方法名([形参列表])：`

​	`方法体`

***与类对象无关，只是属于类中***



### 私有变量和私有方法：

通过***约定***私有变量，或私有方法，可以强制访问

#### 私有属性：

![image-20250120181710729](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120181710776.png)

![image-20250120181854150](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120181854201.png)



### 封装：

#### 封装的定义：

![image-20250120182849462](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120182849507.png)

### 继承：

继承的定义：

![image-20250120183215421](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120183215471.png)

### 多态：

多态的定义：

![image-20250120183254301](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120183254340.png)



# 数学基础：

## 线性代数：

### 向量：

### 矩阵乘法：

### 行列阵：

### 矩阵转置以及对应的性质：

### 矩阵的逆以及对应的性质：

### numpy库：

#### 基于列表构建矩阵：

#### 特殊矩阵构建：

#### 矩阵乘法：

#### 矩阵广播机制：

#### 矩阵转置：

#### 矩阵的逆：

#### 矩阵存取：



### pandas库：

#### 学习读取数据：

#### 掌握简单的数据清洗：



### matplotlib库：

#### 基础绘图语法：

##### 散点图：

##### 曲线图：

##### 条形图：

##### 扇形图：



# 总结：

### 泰坦尼克号数据集可视化：

#### 分别设计对各指标的生还数（率）进行对比可视化：

#### 分析可视化结果：

## 数学基础：

### 多元微分学的学习：

#### 偏导的概念：

#### 微分：

#### 方向导数和梯度：

#### 多元函数极值与偏导的关系：

#### 条件极值：

### 复习熟练矩阵内容：

### 机器学习概念入门： 

#### 有监督学习&无监督学习：

#### 训练集&验证集&测试集：

#### 过拟合 & 欠拟合：

#### 损失函数：

#### 模型评价指标： 

#### 常见数据清洗：

#### 特征工程：

### 多元线性回归解析解：

#### 最小二乘法构建损失函数：

#### 求矩阵与向量偏导并手推公式：

### 多元线性回归梯度下降法求解：

#### 梯度下降法：

### 学习K-means算法：

#### 熟练掌握K-means算法的流程：

### 完成K-means的类封装：

#### 参考slearn接口形式：

#### 仅可使用numpy，不允许调用机器学习库：

#### 以鸢尾花数据集为例，划分训练集，测试集，完成模型训练，并予以评价分析结果：

### 提前学习数据结构，为开学后的考核做准备：

#### 链表：

#### 栈：

#### 队列：

#### 树：

#### 图：

### 尝试用c或c++实现，不建议用Python

=======
# 1.Pycharm笔记(note)：

## 1.1Python基础语法：

### 基础语法与缩进：

##### 1.1.1基础语法：

Python中，每个对象由标识、类型、value 组成

变量也称为：对象的引用(reference)。变量存储的就是对象的地址

变量通过地址引用了“对象”

变量位于栈内存，对象位于堆内存

标识符规则：

1.区分大小写 

2.第一个字符必须是字母、下划线。其后的字符是：字母、数字、下划线

3.不能使用关键字。比如：'if'  'or'  'while'等 

4.以双下划线开头和结尾的名称通常含有特殊含义，尽量避免这种写法

/表示连接符，就算代码中进行了换行，而实际输出中，也没有进行换行，如下：![image-20250117230500065](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250117230507067.png)

Python标识符命名规则：

![image-20250117232050054](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250117232051875.png)

尽量避免双下划线，以免与系统中的内置函数发生冲突

关键字不能作为标识符

标识符命名不能用数字开头，只能用英文字母

基本运算符：

![image-20250118135036866](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118135043980.png)

Python中整数可以为无限大，没有数据范围限制

Python中常用的四种进制：二进制（0b 或 0B），八进制（0o 或 0

O），十进制，十六进制（0x 或 0X）

#### 1.1.2逻辑运算符：

or 逻辑或

and逻辑与

not 逻辑非

各逻辑运算符规则如下：

![image-20250118143535300](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118143535348.png)

#### 1.1.3比较运算符：

所有比较运算符返回1表示真，返回0表示假。这分别与特殊变量True和False等价。以下假设变量a为15，变量b为30：![image-20250118143815508](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118143815545.png)

#### 1.1.4位运算符

按位运算符是把数字看作二进制来进行计算的。

![image-20250118144340306](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118144340391.png)

Python中不支持自增、自减功能

#### 1.1.5同一运算符

is函数与is not函数

![image-20250118145102779](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145102834.png)

![image-20250118145449810](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145449894.png)

命令行模式与文件模式的区别：命令行只能在[-5,256]区间中进行缓存

#### 1.1.6成员运算符

in 和 in not 函数

具体功能如下：

![image-20250118145646867](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145646935.png)

![image-20250118145748159](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118145748214.png)

***位运算和算术运算>比较运算符>赋值运算符>逻辑运算符***

#### 1.1.7缩进：

Python中通常通过缩进来区分不同语句的包含与包含于关系，要时刻小心“空格”是否对代码有影响



## Python数据类型：

### 1.2Python内置的数据类型：

### 1.2.1 int：

使用int()实现类型转换：

1.浮点数直接舍去小数部分

2.布尔值True转为1，Falise转为0（eg：int（True) = 1）

3.字符串符合整数格式（浮点数格式不行）则直接转成对应整数，否则报错。

整数和浮点数混合运算时，表达式结果自动转型成浮点数。比如：2+8.0的结果是10.0

### 1.2.2 float：

使用float()实现类型转换（与int()相似）

round(value)可以返回四舍五入的值。但不会改变原有值，而是产生新的值

增加运算符两个符号中不能有空格，反面eg："+ ="错误，应为"+="



### 1.2.3 bool：

bool("a") = True

bool("") = Fal se

空字符串转换为False，非空字符串转化为True

![image-20250118143228499](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118143228581.png)

### 1.2.4 complex：



## 1.3 Python数据结构：

## 1.3.1 序列：

序列是一种数据存储方式，用来存储一系列的数据。

在内存中，序列就是一块用来存放多个值的连续的内存空间。

序列中存储的是整数对象的地址，而不是整数对象的值。

### 1.3.2 字符串：

![image-20250118144520384](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118144520481.png)



#### 创建字符串：

1. 通过单引号或双引号创建字符串。a = 'abc' 或 a = "abc"

使用引号的好处是可以创建本身就包含引号的字符串，而不用使用转义字符

2. 通过三个单引号或三个双引号创建多行字符串。
3. Python中允许创建空字符串，不包含任何字符且长度为0。eg:a=''

#### len()函数：

Python内置函数，用于计算字符串长度。

#### 转义字符：

![image-20250119170131911](C:/Users/18929/AppData/Roaming/Typora/typora-user-images/image-20250119170131911.png)

#### 字符串拼接：

![image-20250119170238910](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119170238942.png)

#### 字符串复制：

使用"*"实现字符串的复制

#### 不换行打印：

在print函数中加入end,eg:print("abc",end="123")

​					     print("abc")	#输出结果为abc123abc

#### input()函数：

input()函数括号中会在终端打印出来，同时赋予变量的值。eg：name = input("asdas")	#name = 我们所输入的值，而"asdas"将会被打印出来

#### 字符串的修改：

![image-20250119180308626](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119180308665.png)

由于字符串不可改变，因此我们需要替换掉某些字符。常使用replace()函数创建新变量。

如上述图片中，则将'c'转变成'高'，然后在'c'的位置替换成高，创建一个新变量b

#### str()实现数字转型字符串：

a = str("")

#### 使用[]提取字符：

![image-20250119181124137](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119181124178.png)



#### 字符串切片slice操作：

提取子字符串（按照索引来切片）

![image-20250119182617681](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119182617722.png)

“包头不包尾”，print(a[:2]) 范围包括从[0,1]的区间内，而不包含a[2]

#### split()分割和join()合并：

![image-20250119184329723](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119184329768.png)

![image-20250119184644504](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119184644537.png)

split()函数格式为:新变量 = 变量.split("用于分割的字符串")

join()函数格式为:'用于链接各子字符串的字符串'.join(变量)	***join()函数仅创建一次新对象，而"+"会多次新建对象，不断复制。***

#### 字符串驻留机制：

a ="dd"

b ="dd"

a 与 b id相同，为同一对象，可以通过is语句判断

#### 字符串常用方法汇总：

![image-20250119193850054](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119193850101.png)

#### 通过strip()去除字符串首尾指定信息:

![image-20250119194006359](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119194006398.png)

#### 大小写转换：

![image-20250119194103757](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119194103800.png)

#### 格式排版：

center()居中对齐、ljust()左对齐、rjust()右对齐

a = "SXT"

a.center(10,"#")	'###SXT####'	#10为a字符的格式长度，而"字符串"表示你所要添加的字符串

ljust()与rjust()同理

#### 特征判断方法：

![image-20250119195129554](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119195129590.png)

#### 字符串的格式化：

![image-20250119195306231](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119195306273.png)

#### 填充与对齐：

![image-20250119202359936](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119202359975.png)

#### 数字格式化：

浮点数通过f，整数通过d进行需要的格式化。

![](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119202536932.png)

#### 可变字符串：

![image-20250119202715932](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119202715991.png)

需引入io库，即import io

具体实现如下：

![image-20250119203509964](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119203509997.png)



#### 类型转换总结：

![image-20250119203602001](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119203602053.png)

### 1.3.3 列表：

列表是用于存储任意数目、任意类型的数据集合。

列表是内置可变序列，是包含多个元素的有序连续的内存空间。列表的标准语法格式：

a =[10,20,30,40]

其中，10,20,30,40这些称为：列表a的**元素**。

列表中的元素可以各不相同，可以是任意类型。比如：

a = [10,20,'abc',True]

Python的列表大小可变，根据需要随时增加或缩小

#### 列表的创建：

1.range()创建整数列表

![image-20250118223335095](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118223335156.png)

2.推导式生成列表：

![image-20250118223831820](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118223831861.png)

#### 列表元素的增加：

append()方法：原地修改列表对象，是真正的列表尾部添加新的元素，速度最快，推荐使用。

![image-20250118224426219](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118224426251.png)

+运算符操作：并不是真正的尾部添加元素，而是创建新的列表对象；将原列表的元素和新列表的元素依次复制到新的列表对象中。这样，会涉及大量的复制操作，对于操作大量元素不建议使用。

![image-20250118224620724](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118224620753.png)

extend()方法：将目标列表的所有元素添加到本列表的尾部，属于原地操作，不创建新的列表对象。

![image-20250118224724897](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118224724927.png)

insert()插入元素：使用insert()方法可以将指定的元素插入到列表对象的任意指定位置。

![image-20250118225036475](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225036519.png)

乘法拓展

：![image-20250118225141068](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225141104.png)

1. 我们可以通过索引直接访问元素。索引的区间位于[0,列表长度-1]这个范围

2. index()获得指定元素在列表中首次出现的索引

   ![](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230006078.png)

   3.count()获得指定元素在列表中出现的次数。

4. len()返回列表长度，即列表中包含元素的个数。

5. 成员资格判断：

![image-20250118230216790](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230216827.png)

print(100 in a)	存在返回True，不存在返回False

#### 列表元素的删除：

删除元素底层是：元素的拷贝

del删除:

![image-20250118225403982](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225404019.png)

pop()方法：

![image-20250118225436728](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225436761.png)

remove()方法：删除首次出现的指定元素，若不存在该元素抛出异常。

![image-20250118225606772](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118225606802.png)

#### 列表的遍历：

![image-20250118230944216](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230944248.png)

#### 列表复制：

![image-20250118231134664](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231134702.png)

列表排序：  

 1.修改原列表：

![image-20250118231225990](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231226029.png)

 2.创建新列表：

![image-20250118231656601](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231656639.png)

3.reversed()返回迭代器

![image-20250118231759860](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118231759901.png)

其他内置函数：

![image-20250118232001992](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118232002035.png)

#### 二维列表：

![image-20250118232755533](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118232755581.png)

### 1.3.4 字典：

#### 1.字典的概念：

字典是”键值对“的无序可变序列，字典中的每个元素都是一个”键值对“，包含：”键对象“和”值对象“。可以通过”键对象“实现快速获取、删除、更新对应的“值对象”

![image-20250118234835907](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118234835951.png)

#### 2.字典的创建：

1.我们可以通过{}、dict{}来创建字典对象

2.zip()

3.fromkeys创建值为空的字典

![image-20250118235102095](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118235102142.png)

#### 字典元素的访问：

![image-20250118235837792](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118235837842.png)

![image-20250119000018254](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000018294.png)

![image-20250119000040591](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000040630.png)

#### 字典元素的添加、修改、删除：

![image-20250119000334360](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000334404.png)

![image-20250119000546667](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000546711.png)

#### 3.序列解包：

![image-20250119000920352](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119000920396.png)

#### 4.表格数据是用字典和列表存储的访问：与上述数据结构相似

将一个键值对放进字典的底层过程：

![image-20250119001904097](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119001904146.png)











### 1.3.5 元组： 

1.元组的基本概念

元组属于不可变序列，不能修改元组中的元素。因此，元组没有增加元素、修改元素、删除元素相关的方法。

![image-20250118232917273](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118232917317.png)

元组通过小括号()进行创建元组

2.元组的元素访问和计数：

![image-20250118233326926](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118233326971.png)

排序之后转换了数据结构，从元组变成了可修改的序列——列表 

![image-20250118233514490](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118233514538.png)

生成器推导式创建元组：

![image-20250118233852607](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118233852646.png)

元组总结：

![image-20250118234526978](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118234527016.png)

### 1.3.6 集合：

#### 1.集合的概念：

集合是无序可变，元素不能重复。

![image-20250119001947887](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119001947927.png)

#### 2.集合创建和删除：

![image-20250119002022593](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119002022634.png)

#### 3.集合相关操作：

![image-20250119002118012](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119002118052.png)



### 1.3.7 切片：

#### 切片操作：

#### 1.列表切片:

![image-20250118230502017](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230502058.png)

##### 列表其他操作：

![image-20250118230629634](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250118230629676.png)

#### 元组切片：



## 1.4 Python跳进控制以及循环控制：

#### 1.4.1 while循环结构：

**while 条件表达式：**

​	**循环体语句**

![image-20250119203905490](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119203905530.png)

#### 1.4.2 for循环：

![image-20250119204213398](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119204213442.png)

![image-20250119204310583](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119204310627.png)

![image-20250119204642377](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119204642420.png)

#### 1.4.3 嵌套循环：

![image-20250119205828886](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119205828918.png)

使用缩进来表示for循环内的语句

#### 1.4.4 break与continue：与c语言一致



![image-20250119211451500](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211451544.png)

#### 循环代码优化原则：

![image-20250119211615428](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211615467.png)

![image-20250119211633051](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211633084.png)

### 1.4.5 使用zip()并行迭代：

![image-20250120153454452](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120153454502.png)

## 1.5 Python推导式：

#### 1.5.1 推导式创建序列：

![image-20250119211744396](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211744433.png)

#### 1.5.2 推导式的类型：

![image-20250119211835106](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250119211835145.png)

##### 列表推导式：

语法：`[表达式 for item in 可迭代对象]`

或者：`{表达式 for item in 可迭代对象 if 条件判断}`

**字典推导式**：

格式： `{key_expression: value_expression for 表达式 in 可迭代对象}`

![image-20250120154942294](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120154942342.png)

实际代码应用：

![image-20250120160023924](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120160023959.png)



**集合推导式：**

集合推导式生成集合，和列表推导式的语法格式类似：

区别是列表推导式是[]，而集合推导式是{}

![image-20250120160205930](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120160205973.png)

**生成器推导式**：

![image-20250120160249419](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120160249468.png)





## Python错误和异常捕捉：

已包含在上面笔记中

## 1.6 Python map、lambda、filter函数的使用：

#### 1.6.1 map函数表达式：

`map(函数对象,[可迭代对象])`

作用：将可迭代对象中的每一个元素均运用到函数对象中

应用：

![image-20250120162101700](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120162101742.png)





#### 1.6.2 lambda表达式和匿名函数：

基本语法：`lambda arg1,arg2,arg3...:	<表达式>`

arg1 arg2 arg3为函数的参数。<表达式>相当于函数体。运算结果是表达式的运算结果

![image-20250120161053108](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120161053145.png)

![image-20250120161103351](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120161103385.png)

#### 1.6.3 filter()函数：

格式：filter(函数对象,可迭代对象)

允许你根据指定的条件从一个可迭代对象，如列表元组或字典中筛选元素。



## Python面向对象：

Python完全采用了面向对象的思想，是真正面向对象的编程语言，完全支持面向对象的基本功能。如：继承、多态、封装等。

面向过程与面向对象的区别：面向过程首先思考“怎么按步骤实现？”比如：把大象放冰箱分三步

面向对象首先思考“怎么设计这个事物”

![image-20250120163021495](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163021537.png)

![image-20250120163054910](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163054955.png)



![image-20250120163153869](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163153911.png)

### 1.7.1 类与实例化：

类的定义：类可以看作是一个模板，或者图纸，系统根据类的定义造出对象

类：我们称为：“class”。对象：我们叫做：object,instance

对象就是实例

#### 属性和方法：

我们通过类定义数据类型的属性(数据)和方法(行为)也就是说，“类将行为和状态打包在一起”。

![image-20250120163710190](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163710233.png)

对象是类的具体实体，一般称为“类的实例”。类看作“饼干模具”，对象就是根据这个“模具”做出来的饼干

![image-20250120163818227](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163818277.png)

定义类的语法格式如下：

`class 类名：`

​	`类体`

定义类的要点：

![image-20250120163956531](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120163956573.png)

#####  init构造方法

![image-20250120165822803](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120165822844.png)

![image-20250120165934931](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120165934984.png)

##### 实例属性和实例方法：

###### 实例属性：

![image-20250120170333012](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120170333061.png)

![image-20250120170507865](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120170507922.png)

***仅在s2中加入了address，而类中是没有address的***

###### 实例方法：

![image-20250120170737615](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120170737669.png)

![image-20250120171015861](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120171015904.png)

![image-20250120171316478](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120171316521.png)

#### 类对象：

当解释器执行class语句时，就会创建一个类对象。

![image-20250120172851257](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120172851306.png)



### 1.7.2 类变量以及方法：

#### 类变量：

在类中，所有实例之间共享的变量。实例变量是每个实力独有的，而类变量则被所有实例共享。

#### 类方法：

类方法通过装饰器@classmethod来定义，格式如下：

`@classmethod`

`def	类方法名(cls [,形参列表]):`

​	     `方法体`

![image-20250120180350994](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120180351037.png)

#### 静态方法：

格式：

`@staticmethod`

`def 静态方法名([形参列表])：`

​	`方法体`

***与类对象无关，只是属于类中***



### 1.7.3 私有变量和私有方法：

通过***约定***私有变量，或私有方法，可以强制访问

#### 私有属性：

![image-20250120181710729](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120181710776.png)

![image-20250120181854150](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120181854201.png)

#### 私有方法：

方法本质上也是属性！只不过是可以通过()执行而已。

![image-20250209224227850](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209224227924.png)

加两条下划线__，将公共方法转换成私有方法



### 1.7.4 封装：

#### 封装的定义：

![image-20250120182849462](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120182849507.png)



### 1.7.5 继承：

继承的定义：

![image-20250120183215421](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120183215471.png)

#### 继承的语法：

![image-20250120185250436](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120185250496.png)

#### 继承语法格式：

![image-20250120185550026](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120185550076.png)

***第二种***：

![image-20250120190104070](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120190104121.png)

***第三种：***

![image-20250120190250403](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120190250458.png)



### 1.7.6 多态：

多态的定义：

![image-20250120183254301](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120183254340.png)

![image-20250120190536917](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120190536969.png)

***具体例子：***

![image-20250120190709691](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250120190709741.png)



# 2. 数学基础：

## 2.1 线性代数：

### 2.1.1向量：

**向量和点的区别：**

*向量坐标：把一对数竖着写，然后用方括号括起来*

![image-20250121131532798](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250121131532855.png)

缩放(Scaling)与标量(Scalars)：

通过标量大小对向量进行缩放

**基向量：**

![image-20250121134420661](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250121134420742.png)

**将二维向量的终点抽象成向量本身，默认其为以原点为起点的向量**

*二维张成空间：两个向量所有可能的线性组合*（若两个向量不共线，几何意义常为一个平面。若共线，则为一条直线）

*三维张成空间*：三个向量所有可能的线性组合（若第三个向量刚好与前两个向量共面，则仍为一个平面，若不然，则是第三个向量将前两个向量张成的平面沿着它的方向来回移动，从而扫过整个空间）

有多个向量，并且可以移除其中一个而不减小张成的空间，当这种情况发生时，称这些向量之间是：“**线性相关**”的

线性无关：所有向量都给张成的空间增添了新的维度，则被称为**“线性无关”**

空间的一个基的严格定义是：张成该空间的一个线性无关向量的集合



### 2.1.2矩阵乘法：

**线性变换**：将向量作为输入和输出的一类函数（可以将线性变换看作对空间的挤压伸展）
*两大性质*：

1. 直线在变换后仍然保持为直线，不能有所弯曲
2. 原点必须保持固定

![image-20250122141849154](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122141849219.png)

*线性变化后，坐标的计算：*

![image-20250122142344993](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122142345053.png)

“2*2 Matrix”

![image-20250122142822994](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122142823045.png)

***把第一列(a,c)看作是第一个基向量的落脚点，第二列(b,d)看作是第二个基向量的落脚点***

*矩阵向量乘法：*

![image-20250122142834857](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122142834897.png)

***基向量经过线性变化之后的坐标***

**按习惯，我们把变换后的i帽和j帽的坐标作为一个矩阵的列，并且将两列分别缩放x和y倍后相加的结果定义为矩阵向量乘积**

**复合变换：**

![image-20250122150003258](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150003311.png)

复合矩阵的相关计算：

![image-20250122150143771](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150143822.png)

![image-20250122150157659](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150157709.png)

![image-20250122150335536](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150335587.png)

**养成思考矩阵乘法意义的习惯**

**两个变换的相继作用**

![image-20250122150450467](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150450555.png)

![image-20250122150459782](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150459875.png)

**注意乘积的顺序！！！！！**

**矩阵变换具有结合律**

![image-20250122150737341](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122150737388.png)

### 2.1.3 行列阵：

概念： **线性变换对面积产生改变的比例被称为这个变幻的行列式**

空间取向的变化：

![image-20250122152228153](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122152228222.png)

行列式为负数时的几何意义：

![image-20250122152318329](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122152318395.png)

*负的面积为什么与取向翻转相关？*

![image-20250122152443504](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122152443580.png)

三维矩阵下的行列式：

***体积的缩放***

![image-20250122152837442](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122152837545.png)

 行列式为负值时：

![image-20250122152854175](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122152854235.png)

三维矩阵中，当空间取向发生翻转，行列式为负

**右手定则，当右手为正时，行列式为负时，使用左手即代表三维空间取向的翻转**

***如何计算行列式*** ：

![image-20250122153332089](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122153332143.png)

推导过程：

![image-20250122154010709](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122154010778.png)

***两个矩阵乘积的行列式等于这两个矩阵行列式的乘积***

![image-20250122154746469](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122154746515.png)

**线性方程组：**

![image-20250122155438085](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122155438137.png)

![image-20250122155444982](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122155445028.png)

![image-20250122155541164](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122155541212.png)

将线性方程组转化为三维矩阵之后计算



### 2.1.4 矩阵转置以及对应的性质：



### 2.1.5 矩阵转置

矩阵的转置是将矩阵的行和列互换。对于一个 *m*×*n* 的矩阵 *A*，其转置矩阵 *A**T* 是一个 *n*×*m* 的矩阵，其中 *A**T* 的第 *i* 行第 *j* 列的元素等于原矩阵 *A* 的第 *j* 行第 *i* 列的元素。

![image-20250122164819450](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122164819497.png)



### 2.1.6 矩阵的逆以及对应的性质：

**假设A是一种线性变换**

矩阵的逆的性质：

![image-20250122161042797](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122161042879.png)

![image-20250122161104640](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122161104724.png)

***首先应用A代表的变换，再应用A逆代表的变换***

*只有当det(A) != 0（行列式不为零） 时，才会有逆变换。*

 *当变换的结果为一条直线时，也就是说结果是一维的。我们称这个变换的秩为1*

*如果变换后的向量落在一个二维平面上，我们称这个变换的秩为2*

*比如说对于一个2*2的矩阵，它的秩最大为2（意味着基向量仍旧能张成整个二维空间）*

**矩阵的列空间：**所有可能的输出向量构成的集合

![image-20250122163545756](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250122163545810.png)

*列空间就是矩阵的列所张成的空间*

**因此秩的更精确定义是列空间的维数**

**满秩：** *当秩与列数相等时，且秩达到最大值*



*对一个满秩变换来说，唯一能在变换后落在原点的就是零向量自身*



**在变换后落在原点的向量集合，被称为所选矩阵的“零空间”和“核”**

零空间就是变换后落在零向量上的向量所构成的空间





### 2.1.7 numpy库：

引入numpy库：

import numpy as np

#### 创建随机数字：

##### 利用Gennerator.integer，可以创建出从低到高不同精度的随机数

rng.integers(5,size=(2,4))

array([[2,3,1,3],

​	[3,3,4,1]])

第一个参数5，表示随机数从0到4，不包括5.生成的随机数矩阵的形状为(2,4)

如果想要包括数字5，可以添加属性endpoint = True

rng.integers(5,size=(2,4),endpoint=True)

#### 获得数组中的唯一值：

从一个数组或者矩阵中返回唯一值，将重复的值滤除掉

![image-20250125150155241](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125150155297.png)

![image-20250125150237490](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125150237553.png)

![image-20250125150310749](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125150310803.png)

![image-20250125150328807](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125150328865.png)

针对矩阵（二维数组）进行唯一化操作

![image-20250125150429261](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125150429315.png)

![image-20250125151453051](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125151453116.png)

[[1 2 3 4]

[5,6,7,8]

[9 10 11 12]]

![image-20250125151742344](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125151742403.png)

![image-20250125151942028](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125151942081.png)

![image-20250125151953015](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125151953064.png)



#### 基于列表构建矩阵：

`data = np.array([[1,2],[3,4],[5,6]])`

`print(data)`

array([[1,2],

​	[3,4]

​	[5,6]])

矩阵的索引和切片:

eg：

返回二维矩阵的第一行、第二列	`data[0,1]`

2

返回矩阵的第二行到第三行的所有列	`data[1:3]`

array([[3,4],

​	[5,6]])

返回矩阵从第一行到第二行的所有元素	`data[0:2,0]`

array([1,3])

![image-20250125140747031](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125140747086.png)

与数组操作方法相同，对于矩阵也可以使用统计函数求一些值

`data.min()`	1

`data.max()`	6	

`data.sum()`	21

通过axis参数，可以设定统计函数针对不同维度进行计算

`data = np.array([[1,2],`

​	`[5,3],`

​	`[4,6]])`

`data.max(axis=0)`

array([5,6])

`data.max(axis=1)`

array([2,5,6])

同样可以将多个矩阵进行相加计算，前提是这些矩阵具有相同的形状

`data = np.array([[1,2],[3,4]])`

`ones = np.array([[1,1],[1,1]])`

`print(data + ones)`

array([[2,3],[4,5]])

![image-20250125144853659](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125144853710.png)

#### 特殊矩阵构建：

#### 矩阵乘法：

第一个矩阵的行数必须与第二个矩阵的列数相等

![image-20250125160242622](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125160242685.png)

![image-20250125161348107](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125161348157.png)



#### 矩阵广播机制：

两个矩阵的某个维度的数据个数相同

data =  np.array([[1,2],[3,4],[5,6]])

ones_row = np.array([[1,1]])

print(data.shape)

print(ones_row.shape)

print()

print(data + ones_row)

(3,2)

(1,2)

[[2,3],

[4,5],

[6,7]]

矩阵ones_row的形状通过广播机制，从(1,2)改变为了(3,2)，这个形状与矩阵data的形状相同

![image-20250125145200061](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125145200107.png)

`np.ones(3)`

`array([1.,1.,1.])`	

`np.zeros(3)`

`array([0.,0.,0.])`

`rng = np.random.default_rng()`	//生成随机数种子

`rng.random(3)`

![image-20250125145330877](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125145330938.png)

![image-20250125145616149](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125145616220.png)

![image-20250125145706390](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125145706445.png)









#### 矩阵转置：

Numpy的ndarray对象提供了一个属性T可以实现矩阵的转换

`print(data)`

`print(data.shape)`

`print()`

`data2 = data.T`

`print(data2)`

`print(data2.shape)`

结果：

![image-20250125152150083](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152150130.png)

通过reshape方法可以精细化的指定需要转换成的形状。而T属性只能简单地将行和列进行互换。

data.reshape(2,3)

![image-20250125152309636](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152309696.png)

使用transpose()方法可以倒转矩阵，即调换矩阵的轴。

arr = np.arange(6).reshape((2,3))

array([[0,1,2],

​	[3,4,5]])

arr.transpose()

array([[0,3],

​	[1,4],

​	[2,5]])

![](C:/Users/18929/AppData/Roaming/Typora/typora-user-images/image-20250125152538308.png)

##### 数组的倒置：

![image-20250125152623460](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152623525.png)

对一维数组进行倒置

![image-20250125152651945](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152651991.png)

结果：![image-20250125152658271](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152658321.png)

对二维矩阵进行倒置：

![image-20250125152719527](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152719582.png)

![image-20250125152747545](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152747597.png)

![image-20250125152801540](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152801604.png)



![image-20250125152832831](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152832892.png)

![image-20250125152858246](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152858298.png)

![image-20250125152938185](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152938246.png)

![image-20250125152951530](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125152951596.png)

![image-20250125153047568](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125153047632.png)

![image-20250125153145009](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125153145069.png)

![image-20250125153210656](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125153210727.png)





#### 矩阵的逆：

np.linalg.inv(矩阵变量)

![image-20250125161528485](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125161528538.png)

代码中实现矩阵的逆

![image-20250125161716642](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125161716696.png)

![image-20250125161923803](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125161923853.png)

![image-20250125162132700](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125162132748.png)

矩阵中的值为未知数的系数

#### 矩阵存取：

CSV文件(逗号分隔值)

##### CSV文件保存：

**np.savetxt(frame.array,fmt='%.18e',delimiter=None)**

![image-20250125162516276](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125162516402.png)

eg:

![image-20250125162803538](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125162803645.png)

##### CSV文件读取：

**np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)**

![image-20250125164824178](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125164824258.png)

*CSV只能有效存储一维数组和二维数组*

### 2.1.8 pandas库：

#### 学习读取数据：

![](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125165014417.png)

#### 掌握简单的数据清洗：

![image-20250125173953503](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125173953560.png)

![image-20250125174006003](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125174006058.png)

其中：

 2.2 df.dropna(inplace=True) 会直接**对原有的数据进行修改**，而不会创建一个新的文件

 2.3 df.fillna(inplace=True) 

相关内容补充

![image-20250125174545064](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125174545118.png)

![image-20250125182422833](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250125182422895.png)

6. 会**创建**一个**新的**dataframe，而原始的dataframe**并不会发生更改**
   8. 对归一化处理的解释：

这段代码用于对 DataFrame 中的某一列进行归一化处理，具体步骤如下：

1. **导入 MinMaxScaler**:

   python

   运行复制

   ```
   from sklearn.preprocessing import MinMaxScaler
   ```

   这行代码导入了 `MinMaxScaler` 类，`MinMaxScaler` 是一个用于数据缩放的工具，可以将特征缩放到特定的范围（通常是 [0, 1]）。

2. **创建 MinMaxScaler 实例**:

   python

   运行复制

   ```
   scaler = MinMaxScaler()
   ```

   这行代码创建了一个 `MinMaxScaler` 的实例，`scaler` 将用于后续的缩放操作。

3. **应用缩放**:

   python

   运行复制

   ```
   df[['列名']] = scaler.fit_transform(df[['列名']])
   ```

   - `df[['列名']]`：选择 DataFrame 中名为 `列名` 的列。

   - `scaler.fit_transform(...)`：首先计算所选列的最小值和最大值，然后将数据缩放到 [0, 1] 之间。`fit_transform` 方法的作用是先“拟合”数据（计算所需参数），然后进行转换。

   - `df[['列名']] = ...`：将缩放后的结果重新赋值回原 DataFrame 的 `列名` 列。

     8.(补) 归一化处理**会修改**原有dataframe

### 2.1.9 matplotlib库：

#### 基础绘图语法：

1. 创建画布与创建子图：

   **plt.figure**:创建一个空白画布，可以指定画布大小，像素

   **figure.add_subplot**:创建并选中子图，可以指定子图的行数，列数，与选中图片编号

2. 添加画布内容：

   **plt.title**:在当前图形中添加标题，可指定标题的名称、位置、颜色、字体大小等参数

   **plt.x(y)label**:在当前图形添加x(y)轴名称，可以指定位置、颜色、字体大小等参数

   **plt.x(y)lim**:指定当前图形x（y）轴的范围，只能确定一个数值区间，而无法使用字符串标识

   **plt.x(y)ticks**:指定x（y）轴刻度的数目与取值

   **plt.legend**:指定当前图形的图例，可以指定图例的大小、位置、标签

3. 存与展示图形：

   **plt.savefig**:保存绘制的图片，可以指定图片的分辨率、边缘的颜色等参数

   **plt.show**:在本机显示图像
   
   ![image-20250127153358478](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127153358565.png)
   
   
   
   ![image-20250127124440505](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127124440599.png)

![image-20250127141636034](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127141636130.png)

##### **散点图、曲线图、**条形图、扇形图：

```python
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  #将标题设置成中文时不冲突

plt.figure(figsize=[10,7])
plt.suptitle("malib练习")


# 数据

x = np.arange(7)
y = np.random.randint(0,100,len(x))
z = np.random.randint(0,100,len(x))

# 柱状图
plt.subplot(231)    #分配空间
plt.title("柱状图")
width = 0.4
plt.bar(x,y,width=width)
plt.bar(x,z,width=width)
for x1,y1,z1 in zip(x,y,z):
    plt.text(x1,y1,s=y1,ha="center")
    plt.text(x1+width,z1,s=z1)


# 折线图
plt.subplot(232)
plt.title("折线图")
plt.plot(x,y)
plt.plot(x,z)


# 散点图
plt.subplot(234)
plt.title("散点图")
plt.scatter(x,y)
plt.scatter(x,z)


# 扇形图
plt.subplot(235)
plt.title("扇形图")
plt.pie(x=y,labels=x,autopct="%0.2f%%")

# 文本
text = ["以上为malib简单练习，尚未理解代码含义","asdadasd","adasdasdas","adsdasdasd","adasdasdasdasd","adasdasdasd","asdasdasdasdas"]
y = 0.85
for i in text:
    plt.figtext(0.65,y,s=i)
    y-=0.02
plt.show()
```



##### 散点图知识点：

**plt.scatter()**

![image-20250127154329525](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127154329586.png)

**s 代表原点，c代表点的颜色，marker表示点的形状**

![image-20250127154754252](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127154754308.png)

##### 折线图知识点：

**plt.plot()**

在 `plt.plot(x, y, "r--")` 中，`"r--"` 是一个字符串，用于指定绘图的颜色和线型。它的含义如下：

- **`r`**：表示红色（red）。你可以使用单字母来指定颜色，例如：
  - `b`：蓝色（blue）
  - `g`：绿色（green）
  - `k`：黑色（black）
  - `c`：青色（cyan）
  - `m`：品红色（magenta）
  - `y`：黄色（yellow）
- **`--`**：表示虚线（dashed line）。你可以使用不同的符号来指定线型，例如：
  - `-`：实线（solid line）
  - `--`：虚线（dashed line）
  - `:`：点线（dotted line）
  - `-.`：点划线（dash-dot line）

因此，`plt.plot(x, y, "r--")` 表示用红色虚线绘制由 `x` 和 `y` 数据点构成的曲线。

![image-20250127160533981](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127160534036.png)

##### 柱状图知识点：

**plt.bar()**

![image-20250127160708838](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127160708929.png)

![image-20250127161509826](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127161509881.png)

![image-20250127161502919](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127161503001.png)

##### 扇形图知识点:

**plt.pie()**:

1. *explode:突出想要的参数，如图中的A*
2. *labels将列表中的参数设置名称，如图中的的ABCDEFGHIJ*
3. *labeldistance设置名称与扇形图的距离*

![image-20250127162105412](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250127162105468.png)





### 2.1.10 泰坦尼克号数据集可视化：

#### 分别设计对各指标的生还数（率）进行对比可视化：

#### 分析可视化结果：

## 2.2  数学基础（机器学习）：

### 2.2.1 多元微分学的学习：

#### 多元函数基本概念：

一元函数： y = f(x),x∈D	（一条直线）

##### 多元函数：z = f(x,y),(x,y)∈D	**(空间上面的图形，引入了z轴)**

​	eg：y = x	**其本质是一个平面，沿着y=x这条直线在z轴上无限扩展**

##### 邻域：

![image-20250205160752554](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250205160752615.png)

##### 多元函数的极限：

![image-20250205161053012](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250205161053079.png)

证明函数极限不存在：（易证伪，难证实）

![image-20250206003421570](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206003421659.png)

**一元函数与多元函数的异同：**

![image-20250206003514276](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206003514340.png)

##### 两个典型eg：

![image-20250206004140091](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206004140152.png)

选取特殊的趋近方式，y=kx

k取值不同时，极限的值不相同，因此不存在极限



![image-20250206004627306](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206004627376.png)

利用夹逼定理证明函数极限存在，且为零

 

##### 多元函数的连续性:

![image-20250206004803952](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206004804013.png)





#### 偏导的概念：

![image-20250206004931277](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206004931345.png)

**多元函数中，偏导数只研究部分变化，如让y0的值不发生改变的情况下改变x0的值，研究因变量x0对自变量z的影响**



#### 多元可偏导和连续的关系：

![image-20250206011249910](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206011249983.png)

eg：

![image-20250206011737611](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206011737670.png)

同理，y变化时与x变化相同

![image-20250206012003752](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206012003815.png)

总结：

1. 多元函数可偏导未必连续
2. 连续未必可偏导

#### 微分：

全微分的定义与一元可微的对比：

![image-20250206014244060](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250206014244133.png)

**利用勾股定理求ρ**



#### 方向导数和梯度： 

##### 方向导数：

二元函数：



![image-20250210004121352](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210004121430.png)



eg：

![image-20250210005243201](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210005243276.png)





三元函数：



![image-20250210004253442](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210004253517.png)



##### 梯度：

也称为梯度向量

![image-20250210005741574](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210005741655.png)

方向余弦：

![image-20250210005832703](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210005832775.png)

eg：

![image-20250210010028335](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210010028408.png)

![image-20250210010103611](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210010103684.png)

方向导数与梯度的关系：

![image-20250210010131878](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210010131960.png)

![image-20250210010258925](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210010259012.png)





#### 多元函数极值与偏导的关系：

**一、求解步骤**

**1. 求一阶偏导数**

对多元函数 f(x1,x2,…,xn)*f*(*x*1,*x*2,…,*x**n*)，分别对每个变量求一阶偏导数：

∂f∂x1,∂f∂x2,…,∂f∂xn∂*x*1∂*f*,∂*x*2∂*f*,…,∂*x**n*∂*f*

**2. 求临界点（驻点）**

解方程组 **所有一阶偏导数同时为零**：

![image-20250210002808550](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210002808606.png)

方程组的解即为临界点（可能是极值点或鞍点）。

**3. 判断极值类型（二阶导数检验）**

通过 **Hessian矩阵** 判断临界点的性质。
**Hessian矩阵** *H* 是一个二阶偏导数矩阵，定义为：

![image-20250210002559760](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210002559822.png)

- **对于二元函数 f(x,y)\*f\*(\*x\*,\*y\*)**，Hessian矩阵简化为：

  H=[fxx   fxy]

  ​      fyx   fyy

  

  计算其行列式 *D*：

  ![image-20250210002818177](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210002818233.png)

  

  - 若 *D*>0 且 fxx>0，则为 **极小值**；
  - 若 *D*>0 且 fxx<0，则为 **极大值**；
  - 若 *D*<0，则为 **鞍点**（非极值）；
  - 若 *D*=0，无法判断，需用其他方法（如观察函数值变化）。

- **对于多元函数（n 变量）**：

  - 若 Hessian 矩阵 **正定**，临界点为极小值；
  - 若 Hessian 矩阵 **负定**，临界点为极大值；
  - 若 Hessian 矩阵 **不定**，临界点为鞍点；
  - 若 Hessian 矩阵 **半定**，需进一步分析。

#### 条件极值：

1. 定义：求目标函数z = f(x,y)在约束条件 φ(x,y)= 0下的极值问题，成为条件极值

2. 解题方法（拉格朗日乘数法）

   ![image-20250210003226731](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210003226810.png)

eg：

![image-20250210003728809](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250210003728893.png)





### 2.2.2 复习熟练矩阵内容：

### 2.2.3 机器学习概念入门： 

#### 有监督学习&无监督学习：

##### 有监督学习：

**监督学习是从正确答案中找到逻辑对输入处理得到最可能正确的结果**

**回归算法**：

1. 提供数据集，为机器设立了学习算法的任务

2. 学习输入、输出 或 x到y映射

   eg: 学会从无限多可能的数字中预测最可能正确的数字

**分类算法**：

![image-20250208142055891](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208142055975.png)

分类预测的是一个小的有限的一套可能的产出类别，如0，1，2，但并不是所有可能的数字之间，比如0.5 或者1.7

![image-20250208142455958](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208142456057.png)

##### 无监督学习：

**数据仅带有输入x而没有输出标签y并且算法必须在数据中找到相应的结构**



**聚类学习（clustering）：**

不对数据进行标签化处理，而是让机器自主分类数据，将不同的数据聚类

![image-20250208143215005](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208143215120.png)

![image-20250208143333178](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208143333300.png)

![image-20250208143740072](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208143740208.png)

**异常检测**：

**降维：**



**无监督学习与监督学习的区别**：

![image-20250208143049107](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208143049208.png)



#### 训练集&验证集&测试集：

**训练集：训练模型  使用预先设定的超参数，训练常规参数**



**验证集：验证超参数是否是合适的，如何不合适，调整超参数，重新使用训练集再次训练，反复迭代比较，获取到基本的模型**



**测试集：验证整个模型常规参数和超参数实现的整体效果。**



#### 过拟合 & 欠拟合：

##### 过拟合:

- **定义**：模型在训练数据上表现得很好，但在未见过的数据（测试集）上表现较差。模型过于复杂，捕捉到了训练数据中的噪声和细节。

- **表现**：

  - 训练误差低，但验证/测试误差高。

  - 模型过于复杂（如使用了过多的特征、层或参数）。

    **解决方法**：

    降低模型复杂性（如减少特征或模型层数）。

    使用正则化（如L1、L2正则化）。

    增加训练数据量。

    使用交叉验证。

##### 欠拟合：

- **定义**：模型在训练数据和未见过的数据上都表现不佳。模型过于简单，无法捕捉数据中的重要模式。

- **表现**：

  - 训练误差和验证/测试误差都高。

  - 模型过于简单（如使用了过少的特征或层）。

    **解决方法：**

    1. 增加模型复杂性（如增加特征或层数）。

    2. 进行特征工程，选择更有效的特征。

    3. 选择更合适的算法。
    4. 降低正则化程度

​	

#### 损失函数：

![image-20250208163842411](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250208163842527.png)

   



#### 模型评价指标： 

eg：预测



![image-20250209232110951](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209232111031.png)

![image-20250209232222201](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209232222269.png)

![image-20250209232312564](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209232312643.png)

![image-20250209232546077](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209232546163.png)



#### 常见数据清洗：

数据是否符合相关的规则	国家分类中，不能出现城市名称（国家有首都，而城市没有首都这一概念）

数据是否能统一数据类型	将数据转换成相同的类（int、float......）

数据是否符合相应的模式

![image-20250209235226143](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209235226238.png)

#### 特征工程：



![image-20250209183527847](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209183527945.png)

特征工程是指从原始数据中提取、构造和选择对模型训练有帮助的特征的过程。

##### **特征工程的主要步骤**：

特征工程通常包括以下几个步骤：

**(1) 数据理解**

- 了解数据的类型（数值型、类别型、时间序列等）。
- 分析数据的分布、缺失值、异常值等。

**(2) 数据清洗**

- **处理缺失值**：
  - 删除缺失值过多的样本或特征。
  - 填充缺失值（如用均值、中位数、众数填充，或使用模型预测）。
- **处理异常值**：
  - 使用统计方法（如3σ原则）检测异常值。
  - 根据业务逻辑处理异常值（删除、修正或保留）。

**(3) 特征构造**

- **从原始数据中提取新特征**：
  - 例如，从日期中提取年份、月份、星期几等。
  - 从文本中提取词频、TF-IDF等。
- **组合特征**：
  - 通过加减乘除等操作构造新特征。
  - 例如，在电商数据中，用“购买次数”和“平均购买金额”构造“总消费金额”。

**(4) 特征变换**

- **标准化/归一化**：
  - 将特征缩放到相同的尺度（如0到1之间或均值为0、方差为1）。
  - 常用方法：Min-Max归一化、Z-Score标准化。
- **对数变换**：
  - 对偏态分布的数据进行对数变换，使其更接近正态分布。
- **离散化**：
  - 将连续特征分箱（如将年龄分为“少年”、“青年”、“中年”、“老年”）。
- **编码类别特征**：
  - 对类别型特征进行编码，如One-Hot编码、Label编码、Target编码等。

**(5) 特征选择**

- **过滤法**：
  - 根据统计指标（如方差、相关系数、卡方检验）选择特征。
- **包裹法**：
  - 使用模型评估特征的重要性（如递归特征消除RFE）。
- **嵌入法**：
  - 在模型训练过程中选择特征（如L1正则化、决策树特征重要性）。

**(6) 降维**

- **主成分分析（PCA）**：
  - 将高维数据映射到低维空间，保留主要信息。
- **线性判别分析（LDA）**：
  - 在降维的同时保留类别信息。
- **t-SNE、UMAP**：
  - 用于可视化高维数据。

### 多元线性回归解析解：

**线性：**

1. 可加性：f(x + y) =f(x) + f(y)
2. 齐次性：f(ax)=af(x),其中a为与x无关的常数 f(x,y) = f(ax + by) = af(x) + bf(y)

**回归：** 确定多个变量间相互依赖的定量关系



#### 最小二乘法构建损失函数：

![image-20250209165338968](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209165346066.png)

m代表样本个数

一元最小二乘法：

![image-20250209165907859](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209165907937.png)

**分别对k和b求偏导，在对b求导后可以直接得到b的值，而k值则需要将2 - 3式得到。**



推广至多元最小二乘法：

![image-20250209170306763](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209170306832.png)



L2范数为下图中的右上角中的公式

![image-20250209171352085](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209171352157.png)

从第三步到第四步的解释：

**![image-20250209172239569](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209172239633.png)**





#### 求矩阵与向量偏导并手推公式：

损失函数对w求偏导得到以下式子

![image-20250209172421555](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209172421612.png)

求导后第二步到第三步化简运用到的矩阵性质：



![image-20250209172416779](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209172416836.png)

第二步到第三步化简偏导数公式：后半段

![image-20250209173451887](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209173451935.png)



### 多元线性回归梯度下降法求解：

#### 梯度下降法：

**梯度下降是一种可用于尝试最小化任何函数的算法，而不仅仅是线性回归的成本函数**

梯度下降法中最小值的解称为**解析解**

而不能求出来的称为**数值解**

![image-20250209181346988](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209181347051.png)

![image-20250209181613683](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209181613746.png)



![image-20250209182039048](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209182039118.png)

梯度下降算法中的Adam算法：

![image-20250209182453861](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250209182453929.png)



**在对w和b同时更改时，要进行完修正工作之后，再对w和b进行赋值，否则会对b的值产生影响**



![image-20250217150546607](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250217150546759.png)



![image-20250217200258101](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250217200258180.png)

**标准化处理例子：**

![image-20250217202228526](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250217202228585.png)

### 学习K-means算法：

#### 熟练掌握K-means算法的流程：



1. *确定k值（分成k类）*
2. *随机选取样本点作为簇（cluster）中心*
3. *比对样本点与各簇中心的距离，距离某个簇最近的样本点归为其簇中*
4. *更新簇中心（各点坐标的中心点）*
5. *重复3，4步骤，直到各簇中心都没有发生偏移为止*



### 完成K-means的类封装：

pycharm中已完成

#### 参考sklearn接口形式：

​	根据sklearn中的库函数底层原理，自己构建相似的类方法（class）

### 完成逻辑回归的类封装：

#### 逻辑回归的假设函数hθ(x):

![image-20250320184447480](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320184454662.png)

**在使用逻辑回归预测样本的类别时，会提前设置一个阈值p，用来控制分类的界限**

![image-20250320184657873](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320184657967.png)

**使hθ(x)的输出∈[0,1]，引入sigmooid函数：**

![image-20250320184939367](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320184939457.png)



逻辑回归函数的损失函数：

交叉熵损失函数：

![image-20250320185135581](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320185135666.png)

**代价函数：**

衡量了模型在训练集上所犯的错误大小，需要准确地描述样本预测值与真实值之间的误差

**当代价函数J取得最小值时，求逻辑回归参数θ0到θn的具体值是多少**

为什么是交叉熵损失函数？

由cost函数图像入手：

![image-20250320185542438](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320185542525.png)

![image-20250320185528260](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320185528352.png)

引入log函数，关于0.5对称，因此可以表示

![image-20250320185917136](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320185917241.png)

将自变量x的值，控制在0到1之间

![image-20250320190615212](https://khalillu.oss-cn-guangzhou.aliyuncs.com/khalillu/20250320190615310.png)

**自变量x：模型的预测值h**

**蓝色函数：**

**样本为正例时，代价cost随预测值h的变化**

**橙色函数：**
**样本为负例时，代价cost随预测值h的变化**





>>>>>>> Stashed changes
