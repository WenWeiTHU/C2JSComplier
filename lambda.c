
int main(){
    (()=>{
        printf("GOOD!\n");
    })();

    ((int x,int y,int z)=>{
        x = x*2;
        y = y - 3;
        z = z+1;
        printf("%d %d %d\n",x,y,z);
    })(1+5,2,3);


     int a = ((int x,int y,int z)=>{
        int p = x*y*z;
        return p;
    });
    int tmp = a(2,3,4);
    printf("%d",tmp);
}