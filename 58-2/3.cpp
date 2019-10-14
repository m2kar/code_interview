#include <iostream>
#include <stdio.h>

int main() {
    int x;
    scanf("%d",&x);
    
    if (x<=2){
        printf("%d\n",x);
        return 0;
    }
    int a=1;
    int b=2;
    int i=3;
    int t;
    while (i<=x){
        t=a;
        a=b;
        b=t+b;
        i++;
    }
    printf("%d\n",b);
    
}