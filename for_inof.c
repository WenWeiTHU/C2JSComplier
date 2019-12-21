
int main(){
    array test = {1, 2, 3, true, "hello", "world", '!'};


    for (auto item in test){
        printf("[%d]:", item);
        printf("%a\t", test[item]);
    }
    printf("\n");

    char name[5] = "nihao";
    for (auto item of name){
        printf("%c ", item);
    }

}
