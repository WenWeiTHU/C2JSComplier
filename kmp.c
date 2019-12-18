#include <stdio.h>
#include <string.h>

void getNext(char temp[],int next[]){
    int len = strlen(temp);
    next[0] = -1;
    int k = -1;
    int j = 0;
    while (j<len){
        if(k == -1 || temp[j] == temp[k]){
            k++;
            j++;
            if(j!=len && temp[j] == temp[k]) {
                next[j] = next[k];
            } else{
                next[j] = k;
            }
        }
        else{
            k = next[k];
        }
    }
}

void KMP(char temp[],char str[]){
    int flag = 0;
    int next[101];
    getNext(temp,next);
    int j = -1;
    for(int i = 0;i<strlen(str);i++){
        while (j>=0 && str[i]!=temp[j+1]){
            j = next[j+1]-1;
        }
        if(str[i] == temp[j+1]){
            j++;
        }
        if(j+1==strlen(temp)){
            flag = 1;
            printf("%d ",i-j);
            j = next[j+1]-1;
        }
    }
    if(flag == 0){
        printf("False");
    }
}

int main(){
    char temp[100];
    char str[1000];

    printf("pattern: ");
    gets(temp);
    printf("text: ");
    gets(str);

    KMP(temp,str);

    return 0;
}