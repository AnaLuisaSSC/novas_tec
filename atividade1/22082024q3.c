#include <stdio.h>
#include <stdlib.h>

/* Fibonacci */

int main() {
	
	long num1 = 1, num2 = 2, aux = 0;
    int pos = 0;

    printf("digite a posição do termo de Fibonacci:");
    scanf("%d",&pos);

    int i = 2;
    for(i=2; i < pos; i++){
        aux = num2;
        num2 = num1 + num2;
        num1 = aux;
    }
	printf("o %d termo de Fibonacci  é %d", pos, num2);
	
	return 0;
}