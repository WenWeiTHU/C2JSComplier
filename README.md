# complier

## 建议大家先看文档和grammar.txt

* 一段程序只能由几个函数组成

* switch case的case块需要由花括号括起

* if，while,do while,for需要花括号括起

* 目前只支持char s[]的写法，传参的时候也是写成char s[]

* 不支持数组（元素是整数，浮点数），但是这个应该是可以实现的

* 没有实现指针，因为js里面没有对应的数据结构

* 实现了array（c语言没有，对应js里面的array）,实例代码为array.c

* 字符串赋初值等价于

  > char s[];           // 变成
  >
  > s = new Array()
  >
  > 
  >
  > char s[10] = "abc";               // 变成
  > s=new Array()
  > s=['a','b','c','\0']

* palindrome.c, kmp.c , calculator.c已经完成



单独把c语言的的几个库函数做了转化
* gets->readline-sync
* printf->process.stdout.write
* strlen(s)->s.length-1，原因见codeGen.py的strlen_gen的注释

## 可能的改进
* 预处理功能，增加include语句（本地文件），宏定义
* 文档里面的**创新点**部分

## 发现的问题，不改也没多大问题
①才发现已经有提过了，数组无法赋初值
②数组参数的传递必须类似char s[]，而不能是char* s
③为了让初始化的数组内容为空，要使用s[0]='\0';语句
④上面那个，即③的方法如果使用strlen是行不通的，c里面'\0'是终结，但是js里面不是，所以会难以判断，可以考虑采用我在calculator中使用的getLength。
