
int main(){

    auto f1 = [](int x, int y, int z){return x*y*z;};
    int tmp1 = f1(2,3,4);
    printf("%d ",tmp1);

    auto f2 = (int x, int y) -> int { int z = x + y; return z; };
    int tmp2 = f2(5,10);
    printf("%d ",tmp2);
}