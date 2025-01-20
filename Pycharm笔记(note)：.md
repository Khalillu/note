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

