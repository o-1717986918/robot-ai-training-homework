# CS50P 题库一：Python 基础

题目从仓库根目录运行；保留题面规定的路径、函数接口、输入输出和边界。Windows 终端在新行按 Ctrl+Z 后回车表示 EOF；Linux 在新行按 Ctrl+D。题目译文及其来源、许可见各题末尾。 P01—P13 使用固定版本官方 check50。

<a id="p01"></a>
## P01｜表情转换（Making Faces）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task01/faces/faces.py`。

### 题目描述

早期聊天常用字符组合表示表情。请把用户输入中的笑脸`:)`转换为`🙂`，把哭脸`:(`转换为`🙁`，其余字符原样保留。一次输入可以包含多个、相邻或重复的表情。

### 实现接口

在faces.py中实现`convert(text: str) -> str`，返回转换后的新字符串；另写main()读入、调用convert并输出。main需要在直接运行文件时执行。原题不强制提示语。

### 输入格式

读入一行文本。空格、大小写、数字和标点均是输入的一部分。

### 输出格式

输出转换后的一行文本。不要额外改变空格、标点或其他文字；只出现一个普通冒号不构成需要替换的表情。

### 数据范围与边界

原题没有规定文本最大长度。可以没有表情，也可以两类表情混合出现；输入为空串时返回空串。


### 样例1输入

~~~text
Hello :) Goodbye :(
~~~

### 样例1输出

~~~text
Hello 🙂 Goodbye 🙁
~~~

**样例说明：** 两个表情分别替换，其间空格和文字保持不变。

### 样例2输入

~~~text
Ready: 100%
~~~

### 样例2输出

~~~text
Ready: 100%
~~~

**样例说明：** 没有完整的:)或:(组合，整行保持原样。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task01\faces\faces.py
~~~

原题提供的手工检查也包括Hello :)、Goodbye :(。本题不要求修改其他Unicode表情。

来源：[Harvard CS50P — 表情转换](https://cs50.harvard.edu/python/psets/0/faces/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p02"></a>
## P02｜小费计算器（Tip Calculator）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task01/tip/tip.py`。

### 题目描述

根据餐费和小费比例计算应付小费金额。编写主程序，并实现两个“文本转换为数值”的函数；主程序按规定顺序读取数据、调用函数并计算小费。

### 实现接口

`dollars_to_float(d: str) -> float`接收如`$50.00`，去掉开头美元符号，返回50.0。`percent_to_float(p: str) -> float`接收如`15%`，返回比例0.15。main依次调用两函数，计算乘积并格式化。

### 输入格式

共两行。第一行是带前导$的餐费，第二行是带结尾%的百分数。程序可沿用原题提示`How much was the meal? `和`What percentage would you like to tip? `。

### 输出格式

输出一行`Leave $金额`，金额恰好保留小数点后两位。百分数15%表示0.15，不能当成15参与乘法。

### 数据范围与边界

原题保证输入符合预期格式，不要求对abc、缺少符号等情况循环重试。原题没有公布金额或百分数的数值上界；不要自行限制为两位金额。


### 样例1输入

~~~text
$50.00
15%
~~~

### 样例1输出

~~~text
Leave $7.50
~~~

**样例说明：** 50美元的15%是7.5美元，打印时补齐两位小数。

### 样例2输入

~~~text
$100.00
18%
~~~

### 样例2输出

~~~text
Leave $18.00
~~~

**样例说明：** 整数美元金额也必须显示小数部分。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task01\tip\tip.py
~~~

输出前缀Leave与两位小数来自原题给定主程序。不得在两个转换函数里打印结果代替返回float。

来源：[Harvard CS50P — 小费计算器](https://cs50.harvard.edu/python/psets/0/tip/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p03"></a>
## P03｜银行问候语（Home Federal Savings Bank）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task01/bank/bank.py`。

### 题目描述

银行按开头的问候语决定给出的金额。若问候以hello开头，输出0美元；否则，若以字母h开头，输出20美元；其他问候输出100美元。比较时忽略输入开头空白，并忽略字母大小写。

### 实现接口

实现可直接运行的bank.py。原题本题只要求程序，不要求实现后续测试章节中才引入的value()；如自行拆函数也必须保留相同行为。

### 输入格式

一行问候文本，可含前导空格、标点和多个单词。可使用提示`Greeting: `。

### 输出格式

只输出一行，内容严格为`$0`、`$20`或`$100`之一。hello必须作为前缀判断，不要求整行只等于hello。

### 数据范围与边界

原题未给出最大文本长度。HELLO、hello there、hello, Newman均属于第一类；How you doing?属于第二类。判断顺序不能把hello归入仅h开头的一类。


### 样例1输入

~~~text
   HELLO, Newman
~~~

### 样例1输出

~~~text
$0
~~~

**样例说明：** 忽略前导空格和大小写后，以hello开头。

### 样例2输入

~~~text
How you doing?
~~~

### 样例2输出

~~~text
$20
~~~

**样例说明：** 以h开头，且不匹配hello前缀。

### 样例3输入

~~~text
What's happening?
~~~

### 样例3输出

~~~text
$100
~~~

**样例说明：** 不符合前两类规则。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task01\bank\bank.py
~~~


来源：[Harvard CS50P — 银行问候语](https://cs50.harvard.edu/python/psets/1/bank/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p04"></a>
## P04｜用餐时间（Meal Time）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task01/meal/meal.py`。

### 题目描述

早餐时间为07:00至08:00，午餐为12:00至13:00，晚餐为18:00至19:00。请判断输入时刻属于哪一餐。三个区间都包含左右端点，其他时刻不输出用餐信息。

### 实现接口

实现main()与`convert(time: str) -> float`。convert把24小时制文本转换为以小时为单位的浮点数，例如7:30返回7.5。模块被import时不得启动交互，使用`if __name__ == "__main__": main()`保护入口。

### 输入格式

一行合法的24小时制时间，格式为h:mm或hh:mm，例如7:30、07:30。可使用提示`What time is it? `。

### 输出格式

属于早餐输出`breakfast time`，午餐输出`lunch time`，晚餐输出`dinner time`；不属于任何区间时不输出结果行。

### 数据范围与边界

输入保证符合上述24小时格式。07:00与08:00都属于早餐；08:01不属于。分钟范围00—59。原题的12小时制挑战不列入本课程基础要求。


### 样例1输入

~~~text
7:30
~~~

### 样例1输出

~~~text
breakfast time
~~~

**样例说明：** convert返回7.5，落在早餐区间内。

### 样例2输入

~~~text
13:00
~~~

### 样例2输出

~~~text
lunch time
~~~

**样例说明：** 右端点仍包含在午餐区间内。

### 无输出样例

输入`8:01`时，提示结束后不应打印任何用餐结果，包括不能打印None、空缺说明或额外状态文本。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task01\meal\meal.py
~~~

浮点返回值按分钟/60折算，7:30转换为7.5。

来源：[Harvard CS50P — 用餐时间](https://cs50.harvard.edu/python/psets/1/meal/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p05"></a>
## P05｜可乐售货机（Coke Machine）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task02/coke/coke.py`。

### 题目描述

一瓶可乐售价50美分。机器只接受25、10、5美分硬币；用户一次投入一枚，直到累计金额不少于售价。每次投币前显示尚欠金额，结束后显示找零。

### 实现接口

实现coke.py。正常投币循环必须在累计足额后停止；原题不要求指定辅助函数。

### 输入格式

若干行，每行一个整数，表示本次投入的硬币面额。保证每次键入整数；不保证面额属于支持的三种。

### 输出格式

每次读入前输出`Amount Due: d`，d为当前尚欠金额；使用`Insert Coin: `提示读入。足额后输出`Change Owed: c`，c为累计投入减50。非法面额不减少尚欠，也不计入找零。

### 数据范围与边界

价格固定50；支持面额仅5、10、25。允许恰好付清或多付；非法面额包括30等整数。已经足额后不得继续询问，也不得显示负的Amount Due。


### 交互样例1

以下每行提示后的数字由用户键入，程序读取该值后继续执行。

~~~text
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 25
Change Owed: 10
~~~

**样例说明：** 累计60美分，因此找零10美分。

### 交互样例2

~~~text
Amount Due: 50
Insert Coin: 30
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 25
Change Owed: 0
~~~

**样例说明：** 30美分不被接收，余额保持50；之后两枚25美分恰好付清。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task02\coke\coke.py
~~~


来源：[Harvard CS50P — 可乐售货机](https://cs50.harvard.edu/python/psets/2/coke/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p06"></a>
## P06｜删去元音（Just setting up my twttr）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task02/twttr/twttr.py`。

### 题目描述

某些缩写会删去单词中的元音。请读取文本，删去所有英文字母A、E、I、O、U及其小写形式，其他字符保持原有顺序和大小写。

### 实现接口

实现twttr.py并读入、输出转换结果。本题为第2组原题，不要求后续单元测试题中才规定的shorten函数；可自行拆分。

### 输入格式

一行字符串。可用提示`Input: `。内容可能包含字母、数字、标点和空格。

### 输出格式

输出去掉元音后的文本，可按原题演示用`Output: `作为提示前缀。不能删除辅音、数字、标点或空格；字母y不在本题删除范围内。

### 数据范围与边界

原题未规定文本最大长度。大写和小写元音都要处理；文本可能没有元音，也可能全由元音组成。


### 样例1输入

~~~text
Twitter
~~~

### 样例1输出

~~~text
Twttr
~~~

**样例说明：** 移除i和e；保留T的大写形式。

### 样例2输入

~~~text
AEIOUaeiou123!?
~~~

### 样例2输出

~~~text
123!?
~~~

**样例说明：** 只删除十个大小写元音，数字与标点不变。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task02\twttr\twttr.py
~~~

以上输出块只列转换结果。若自行显示Output:提示，结果本体仍须完全相同。

来源：[Harvard CS50P — 删去元音](https://cs50.harvard.edu/python/psets/2/twttr/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p07"></a>
## P07｜个性车牌（Vanity Plates）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task02/plates/plates.py`。

### 题目描述

判断一个自选车牌是否同时满足四条规则：长度2—6；开头至少两个字符为字母；只含字母和数字；数字只能连续出现在末尾，并且第一个数字不能为0。纯字母车牌可以合法。

### 实现接口

实现`is_valid(s: str) -> bool`及交互main。合法返回True，不合法返回False；主程序根据布尔值打印结果。可增加辅助函数；本课程不要求正则表达式。

### 输入格式

一行车牌字符串，字母保证为大写；仍需识别不允许的空格、句点和其他标点。可用提示`Plate: `。

### 输出格式

合法输出`Valid`，否则输出`Invalid`。只输出一种结论，不把True/False作为最终程序输出。

### 数据范围与边界

长度包含所有输入字符；允许长度2和6，拒绝更短或更长。数字部分第一位应非0，后续位置可含0：CS50合法，CS05非法。AA12A因数字后出现字母而非法。


### 样例1输入

~~~text
CS50
~~~

### 样例1输出

~~~text
Valid
~~~

**样例说明：** 前两位为字母，末尾50的首个数字是5。

### 样例2输入

~~~text
CS05
~~~

### 样例2输出

~~~text
Invalid
~~~

**样例说明：** 数字部分首个字符为0。

### 样例3输入

~~~text
CS50P
~~~

### 样例3输出

~~~text
Invalid
~~~

**样例说明：** 数字不能位于字母之间。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task02\plates\plates.py
~~~

补充边界：AB合法，A1、AA.、ABCDEFG非法。原题不强制自己编写测试文件。

来源：[Harvard CS50P — 个性车牌](https://cs50.harvard.edu/python/psets/2/plates/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p08"></a>
## P08｜水果热量（Nutrition Facts）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task02/nutrition/nutrition.py`。

### 题目描述

根据FDA水果表查询每份热量。请读取一个水果名称，忽略字母大小写，在下面给定的20项中找到则输出热量；不存在则不输出热量结果。原题要求用字典保存名称和数值。

### 实现接口

实现nutrition.py。字典键表示水果英文名，值为热量整数。以下完整数据为题目输入规则的一部分，不需另找PDF或CSV。

### 输入格式

一行水果名称，可包含空格。可使用提示`Item: `。大小写不限；除大小写以外的拼写保证与表中名称一致，未知名称也可能出现。

### 输出格式

找到时输出`Calories: n`；没有该水果时正常结束，不输出Calories行，也不输出0或KeyError。

### 数据范围与边界

原题未规定名称长度上限。不要求处理复数变化或近似拼写。热量是表中每份食物的热量，不能改成每100克；未知水果不能使程序崩溃。

| 名称 | Calories | 名称 | Calories |
|---|---:|---|---:|
| Apple | 130 | Avocado | 50 |
| Banana | 110 | Cantaloupe | 50 |
| Grapefruit | 60 | Grapes | 90 |
| Honeydew Melon | 50 | Kiwifruit | 90 |
| Lemon | 15 | Lime | 20 |
| Nectarine | 60 | Orange | 80 |
| Peach | 60 | Pear | 100 |
| Pineapple | 50 | Plums | 70 |
| Strawberries | 50 | Sweet Cherries | 100 |
| Tangerine | 50 | Watermelon | 80 |


### 样例1输入

~~~text
aPPLe
~~~

### 样例1输出

~~~text
Calories: 130
~~~

**样例说明：** 大小写不同不影响查找。

### 样例2输入

~~~text
Sweet Cherries
~~~

### 样例2输出

~~~text
Calories: 100
~~~

**样例说明：** 水果名中的空格是名称的一部分。

### 未找到的样例

输入`Tomato`，不输出任何热量结果行。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task02\nutrition\nutrition.py
~~~


来源：[Harvard CS50P — 水果热量](https://cs50.harvard.edu/python/psets/2/nutrition/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p09"></a>
## P09｜油量表（Fuel Gauge）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task03/fuel/fuel.py`。

### 题目描述

把分数表示的剩余油量转换为最接近的整数百分比。百分比不超过1时显示E，至少99时显示F，其余显示整数百分比。

### 实现接口

实现fuel.py，读取失败或比例不合法时继续询问。处理ValueError、ZeroDivisionError等预期错误，不能用程序崩溃代替重输。

### 输入格式

每轮读入一行，正常形式为X/Y，其中X为非负整数，Y为正整数且X≤Y；分母不要求是4。可能出现文字、浮点数、没有斜杠、分母为0、负分子或X>Y，均应重试。可用提示`Fraction: `。

### 输出格式

只有得到合法分数后才输出一个结果：E、F或`p%`。非法输入不产生有效油量结果，也不结束输入循环。

### 数据范围与边界

0/Y为0%，显示E；1/100显示E，99/100显示F。其余比例按最近整数处理，例如1/3→33%、2/3→67%。原题未给出分子分母上界，不额外要求大整数优化。


### 样例1输入

~~~text
3/4
~~~

### 样例1输出

~~~text
75%
~~~

**样例说明：** 合法分数对应75%。

### 样例2输入

~~~text
1/0
three/four
3/2
1/2
~~~

### 样例2输出

~~~text
50%
~~~

**样例说明：** 前三行必须被拒绝并继续询问，第四行才形成最终结果。

### 样例3输入

~~~text
0/100
~~~

### 样例3输出

~~~text
E
~~~

**样例说明：** 0是允许的分子，表示空油箱。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task03\fuel\fuel.py
~~~

样例输出只列最终油量，循环提示Fraction:可以重复出现。

来源：[Harvard CS50P — 油量表](https://cs50.harvard.edu/python/psets/3/fuel/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p10"></a>
## P10｜购物清单（Grocery List）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task03/grocery/grocery.py`。

### 题目描述

逐行记录商品，输入结束后输出汇总购物清单。名称比较忽略大小写；同一商品的不同大小写累计为同一项。最终按商品名字母序排列，每行先输出次数，再输出大写名称。

### 实现接口

实现grocery.py。读取直到EOF；处理EOFError正常结束，不需要把商品改成复数形式。

### 输入格式

零行或多行商品名称，每行一项，名称可以含空格。输入由EOF终止，不存在数字计数行或end结束标记。

### 输出格式

EOF后统一输出若干行，格式`次数 商品大写名`，次数与名称之间一个空格，按名称字母序。不要按首次出现顺序输出。空输入时没有商品行。

### 数据范围与边界

原题没有规定商品数和名称长度上限。大小写不影响计数；sweet potato为一个商品。使用EOF结束输入；Ctrl+C会中断进程。


### 样例1输入

~~~text
milk
Milk
apple
~~~

### 样例1输出

~~~text
1 APPLE
2 MILK
~~~

**样例说明：** 输入块之后发送EOF。apple排在milk之前，两种大小写milk合并为2。

### 样例2输入

~~~text
tortilla
sweet potato
~~~

### 样例2输出

~~~text
1 SWEET POTATO
1 TORTILLA
~~~

**样例说明：** 输入后发送EOF；名称内部空格不能把商品拆成两项。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task03\grocery\grocery.py
~~~

示例输入最后须发送EOF，不要额外输入字面量EOF。

来源：[Harvard CS50P — 购物清单](https://cs50.harvard.edu/python/psets/3/grocery/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p11"></a>
## P11｜FIGlet艺术字（Frank, Ian and Glen’s Letters）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task03/figlet/figlet.py`。

### 题目描述

FIGlet用普通字符绘制大型字母。本题使用pyfiglet将用户文本渲染为艺术字，支持随机字体或通过命令行指定字体。

### 实现接口

实现figlet.py。命令行不带额外参数时随机选择可用字体；带两个额外参数时，第一个必须为-f或--font，第二个为getFonts()返回列表中的字体名。选好字体后读取一行并调用renderText。参数错误时通过sys.exit带错误消息退出。

### 输入格式

先检查启动参数：`python figlet.py`或`python figlet.py -f 字体名`；之后从标准输入读一行文本。-f通过启动命令传入。其他数量的参数均为非法用法。

### 输出格式

成功时输出所选字体渲染的完整艺术字，包括换行和布局；失败时显示错误消息并以非零退出码结束，不继续索取文本。随机模式不要求每次产生相同输出。

### 数据范围与边界

只接受零个或两个额外参数。原题未限定正文长度；字体名必须真实存在。艺术字按库输出保留空格，不能用手绘固定答案代替。


### 正常样例

启动命令：`python phase1/task03/figlet/figlet.py -f standard`。

### 样例1输入

~~~text
Hi
~~~

### 样例1输出

~~~text
 _   _ _ 
| | | (_)
| |_| | |
|  _  | |
|_| |_|_|
         
~~~

**样例说明：** 使用pyfiglet 1.0.4的standard字体实际渲染；前导空格和换行属于图案，最后一行为空白。随机字体模式不使用此固定输出。

### 非法参数样例

| 启动参数 | 结果 |
|---|---|
| test | 参数个数错误，非零退出 |
| -a slant | 选项错误，非零退出 |
| -f invalid_font | 字体不存在，非零退出 |
| -f slant extra | 参数个数错误，非零退出 |


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task03\figlet\figlet.py
~~~

可用错误消息Invalid usage。原题提供的库接口为Figlet()、getFonts()、setFont(font=...)、renderText(...)；按这些接口调用库并自行实现程序。

来源：[Harvard CS50P — FIGlet艺术字](https://cs50.harvard.edu/python/psets/4/figlet/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p12"></a>
## P12｜告别名单（Adieu, Adieu）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task03/adieu/adieu.py`。

### 题目描述

读取若干姓名，在输入结束后按照英文名单连接规则向所有人告别：一个姓名直接使用；两个姓名用and连接；三个及以上用逗号分隔，最后一项前使用牛津逗号和and。

### 实现接口

实现adieu.py。使用本项已安装的inflect等库完成连接，不按固定人数逐个硬编码。

### 输入格式

每行一个姓名，直到EOF；原题保证至少输入一个姓名。姓名的输入顺序需要保留。

### 输出格式

只在名单完整后输出一行，固定前缀`Adieu, adieu, to `之后接连接好的姓名列表。两个姓名之间不加逗号；三个姓名示例中的最后一个逗号不可省略。

### 数据范围与边界

原题没有给出人数或姓名长度上界。不需要对姓名排序、变更大小写或去重。通过EOF操作结束读取姓名。


### 样例1输入

~~~text
Ada
~~~

### 样例1输出

~~~text
Adieu, adieu, to Ada
~~~

**样例说明：** 随后发送EOF；单个姓名没有and。

### 样例2输入

~~~text
Ada
Lin
~~~

### 样例2输出

~~~text
Adieu, adieu, to Ada and Lin
~~~

**样例说明：** 随后发送EOF；两个姓名只用and。

### 样例3输入

~~~text
Ada
Lin
Sam
~~~

### 样例3输出

~~~text
Adieu, adieu, to Ada, Lin, and Sam
~~~

**样例说明：** 随后发送EOF；三人使用逗号及最后的and。


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task03\adieu\adieu.py
~~~


来源：[Harvard CS50P — 告别名单](https://cs50.harvard.edu/python/psets/4/adieu/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。

<a id="p13"></a>
## P13｜小小算术老师（Little Professor）

**类型：CS50P原题中文翻译。** 提交文件：`phase1/task03/professor/professor.py`。

### 题目描述

模拟一个加法练习玩具：选择等级后，随机出十道加法题。每题最多回答三次，错误或非整数答案均输出EEE；连续三次错误后给出正确等式。最终输出答对题数。

### 实现接口

必须实现main()、`get_level() -> int`、`generate_integer(level: int) -> int`。get_level反复读取到1、2或3才返回；generate_integer对合法等级返回相应位数随机整数，非法等级抛ValueError。使用主入口保护，import模块时不开始答题。

### 输入格式

先输入等级；随后按照程序逐道显示的X + Y =输入答案。非法等级需要重输。每道题可能需要1—3行答案；输入不以EOF作为正常完成标记。

### 输出格式

非法答案输出EEE并再次询问同一题；第三次仍错时输出`X + Y = 正确和`后进入下一题。十题结束输出`Score: s`，s为答对的题数，范围0—10；任一次允许机会答对即记该题1分。

### 数据范围与边界

等级1：整数0—9；等级2：10—99；等级3：100—999。每题先生成X再生成Y；按X0,Y0,X1,Y1顺序生成，重试时不重新生成。只要求加法，不要求减乘除。每道题最多贡献1分。


### 交互片段（非固定随机样例）

~~~text
Level: 1
4 + 0 = abc
EEE
4 + 0 = 5
EEE
4 + 0 = 4
~~~

**说明：** 同一题前两次答错，第三次答对，计1分；程序继续剩余九题。上面的4和0为随机样例，程序按实际随机数出题。若三次都错，第三次EEE之后还要显示4 + 0 = 4。

### 函数边界样例

| 调用或输入 | 必须满足的结果 |
|---|---|
| get_level依次收到0、four、2 | 前两次重询问，最后返回整数2 |
| generate_integer(1) | 整数且0≤值≤9 |
| generate_integer(2) | 整数且10≤值≤99 |
| generate_integer(3) | 整数且100≤值≤999 |
| generate_integer(4) | 抛ValueError |


### 运行与提交

Windows CMD、课程根目录、Python3.13：

~~~bat
python phase1\task03\professor\professor.py
~~~

随机题没有唯一固定的整段stdout；自动评测控制随机序列并检查范围、重试、正确答案与评分，不要求学生固定随机种子。

来源：[Harvard CS50P — 小小算术老师](https://cs50.harvard.edu/python/psets/4/professor/)，原作者Harvard University / David J. Malan。题面已完整列于本页，原站仅作署名和核对。中文翻译按CC BY-NC-SA 4.0使用；不包含解答。
