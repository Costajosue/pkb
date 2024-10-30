#include<stdio.h>

int main(){
    int n1 = 5, n2 = 10, n3 = 5;
    
    printf("\n (n1 == n2) && (n1 == n3) = %d", ((n1 == n2) && (n1 == n3)));
    printf("\n (n1 == n2) || (n1 == n3) = %d", ((n1 == n2) || (n1 == n3)));
    printf("\n (n1 < n3) || (n1 > n2) = %d", ((n1 < n3) || (n1 > n2)));
    
}