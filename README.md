# complier

* 一段程序只能由几个函数组成
* switch case的case块需要由花括号括起
* if，while,do while,for需要花括号括起



* palindrome.c已经完成
* kmp.c,calculator.c暂时用学长的代码（去掉了getLength）,之后要改成我们自己的



单独把c语言的的几个库函数做了转化
* gets->readline-sync
* printf->process.stdout.write
* strlen(s)->s.length-1，原因见codeGen.py的strlen_gen的注释



* 数组赋初值
> char s[10] = "abc" ->
> s=new Array()
> s=['a','b','c','\0']

## 可能的改进
* 预处理功能，增加include语句（本地文件），宏定义