Tiny C介绍
TinyC是一个简化版C语言的解释器。该解释器读入一个简化版C语言源文件(*.txt)，对该文件进行解释执行。

TinyC的词法和语法与C语言相同，简化的部分包括：

数据类型只包含了整数类型
语句只包含了变量声明语句、表达式和赋值语句、if语句、while语句
增加了一个show语句，用于输出表达式E的结果（对于int型，直接显示其值；对于char型，显示该字符）
除main函数外不支持函数，不支持全局变量。
TinyC文法
TinyC使用的文法如下（为便于理解，我们这里部分非终结符用中文表示，用[]表示可选部分）：

程序体->main() {函数体}
函数体->变量声明语句 函数体
函数体->赋值语句 函数体
函数体->show(E); 函数体
函数体->if (B) {函数体} [else {函数体}] 函数体
函数体->while(B) {函数体} 函数体
函数体->ε
变量声明语句->类型 id [=E] id_list ;
id_list->, id [=E] id_list | ε
类型->int | char
赋值语句->id=表达式;
E -> TE E1
E1 -> +TEE1 | -TEE1 | ε
TE->FTE1
TE1->*FTE1 | /FTE1 | ε
F->id | num | (E)
B->TBB1
B1->‘||’TBB1 | ε
TB->FBTB1
TB1->&&FBTB1 | ε
FB-> E>[=] E | E <[=] E | E== E | E!=E | E | !B | TRUE | FALSE