#include <stdio.h>

int getStackLength(char str[]){
    int i = 0;
    int length = 0;
    while (str[i]!='\0'){
        length++;
        i++;
    }
    return length;
}

char pop(char stack[]){
    int len = getStackLength(stack);
    char ret = stack[len-1];
    stack[len-1] = '\0';
    return ret;
}

void push(char stack[],char ch){
    int len = getStackLength(stack);
    stack[len] = ch;
    stack[len+1] = '\0';
}

char top(char stack[]){
    int len = getStackLength(stack);
    return stack[len-1];
}

int is_empty(char stack[]){
    if(getStackLength(stack) == 0){
        return 0;
    }
    return 1;
}

int suffix_exp(char exp[], char suffix[]){
    int len = getStackLength(exp);
    char stack[102];
    stack[0] = '\0';
    push(stack,'#');
    char ch;
    char first;
    for (int i = 0; i < len-1; ++i) {
        ch = exp[i];
        switch (ch){
            case '+':{
            }
            case '-':{
                first = top(stack);
                if(first == '#' || first == '('){
                    push(stack,ch);
                }
                else{
                    first = pop(stack);
                    while (first!='#' && first!='('){
                        push(suffix,first);
                        first = pop(stack);
                    }
                    push(stack,first);
                    push(stack,ch);
                }
                break;
            }
            case '*':{
            }
            case '/':{
                first = top(stack);
                if(first == '#' || first == '(' || first == '+' || first == '-'){
                    push(stack,ch);
                }
                else{
                    first = pop(stack);
                    while (first != '#' && first != '(' && first != '+' && first != '-'){
                        push(suffix,first);
                        first = pop(stack);
                    }
                    push(stack,first);
                    push(stack,ch);
                }
                break;
            }
            case '(':{
                push(stack,ch);
                break;
            }
            case ')':{
                first = pop(stack);
                while (first != '#' && first != '('){
                    push(suffix,first);
                    first = pop(stack);
                }
                if(first == '#'){
                    return 0;
                }
                break;
            }
            default:{
                if(ch>'9' || ch<'0'){
                    return 0;
                }
                while('0'<=ch && ch<='9'){
                    push(suffix,ch);
                    i++;
                    ch = exp[i];
                }
                push(suffix,' ');
                i--;
                break;
            }
        }
    }
    first = pop(stack);
    while (first != '#'){
        push(suffix,first);
        first = pop(stack);
    }
    return 1;
}

void calculate(char exp[]){
    char suffix[401];
    int temp=0;
    suffix[0] = '\0';
    int ret = suffix_exp(exp,suffix);
    push(suffix,'#');
    if(ret == 0){
        printf("Wrong Format!");
    }
    int arr[200];
    int j=0;
    char ch;
    for (int i = 0; i < getStackLength(suffix)-1; i++) {
        ch = suffix[i];
        switch (ch){
            case '+':{
                arr[j-2] = arr[j-2]+arr[j-1];
                j--;
                break;
            }
            case '-':{
                arr[j-2] = arr[j-2]-arr[j-1];
                j--;
                break;
            }
            case '*':{
                arr[j-2] = arr[j-2]*arr[j-1];
                j--;
                break;
            }
            case '/':{
                arr[j-2] = arr[j-2]/arr[j-1];
                j--;
                break;
            }
            default:{
                while('0'<=ch && ch<='9'){
                    temp = temp*10 + (ch - '0');
                    i++;
                    ch = suffix[i];
                }
                arr[j] = temp;
                j++;
                temp = 0;
                if(ch == '#'){
                    i--;
                }
                break;
            }
        }
    }
    printf("result: %d",arr[0]);
}

int main(){
    char exp[201];
    printf("exp: ");
    gets(exp);
    push(exp,'#');
    calculate(exp);
    return 0;
}