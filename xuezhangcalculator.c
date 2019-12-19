#include <stdio.h>
#include <string.h>


int trans(char exp[],char postexp[]){
    char ch;
    int i=0;
    int j=0;
    int stack[100];
    int top=0;
    top=-1;
    ch=exp[i]; i++;

    int current = 0;
    int length = strlen(exp);

    for (i=1;i<=length;)
    {
        switch(ch){
            case '(':
            {
                if (current == 1) {
                    return 1;
                }

                top++; stack[top]=ch;
                break;
            }
            case ')':
            {
                if (current == 0) {
                    return 1;
                }

                while(stack[top]!='(')
                {
                    postexp[j]=stack[top]; j++;
                    top--;
                }
                top--;
                break;
            }
            case '+':{
            }
            case '-':{
                if (current == 0) {
                    return 1;
                }

                while (top!=-1 && stack[top]!='(')
                {
                    postexp[j]=stack[top]; j++;
                    top--;
                }
                top++; stack[top]=ch;

                current = 0;
                break;
            }
            case '*':{
            }
            case '/':{
                if (current == 0) {
                    return 1;
                }

                while(top!=-1 && stack[top]!='('
                    && (stack[top]=='*' || stack[top]=='/')){
                    postexp[j]=stack[top]; j++;
                    top--;
                }
                top++; stack[top]=ch;

                current = 0;
                break;
            }
            case ' ': {
                break;
            }
            default:{
                if (current == 1) {
                    return 1;
                }

                if (ch<'0' || ch>'9'){
                    return 1;
                }



                while (ch>='0' && ch<='9')
                {
                    postexp[j]=ch;
                    j++;
                    ch=exp[i];
                    i++;
                }
                i--;
                postexp[j]='#'; j++;

                current = 1;
                break;
            }
        }
        ch=exp[i]; i++;
    }

    if (current == 0){
        return 1;
    }


    while(top!=-1){
        postexp[j]=stack[top]; j++;
        top--;
    }
    postexp[j]='\0';

    return 0;
}

int compvalue(char postexp[]){
    int d;
    char ch;
    int i=0;
    int stack[100];
    int top;
    top=-1;
    ch=postexp[i]; i++;

    int length = strlen(postexp);

    for (i=1;i<=length;)
    {
        switch(ch){
            case '+': {
                stack[top-1]=stack[top-1]+stack[top];
                top--; break;
            }
            case '-': {
                stack[top-1]=stack[top-1]-stack[top];
                top--; break;
            }
            case '*': {
                stack[top-1]=stack[top-1]*stack[top];
                top--; break;
            }
            case '/': {
                if(stack[top]!=0) {
                    stack[top-1]=stack[top-1]/stack[top];
                }
                else{
                    printf("\n\tdivide by 0 error!\n");
                    return -10000000;
                }
                top--; break;
            }
            default: {
                d=0;
                while (ch>='0' && ch<='9')
                {
                    d=10*d+(ch-'0');
                    ch=postexp[i]; i++;
                }
                top++;
                stack[top]=d;
            }
        }
        ch=postexp[i];
        i++;
    }

    return stack[top];
}

int calc(char s[]) {
    int len = strlen(s);
    int i=0;

    char postexp[100];
    int flag = trans(s,postexp);
    if (flag == 0){
        printf("postexp = %s\n",postexp);
    }
    else {
        printf("Bad Exp\n");
        return 0;
    }
    int result = compvalue(postexp);

    return result;
}

int main() {
    char s[100];
    int result;

    printf("Please input a expression: ");
    gets(s);
    result = calc(s);
    printf("Result: %d\n", result);

    return 0;
}

