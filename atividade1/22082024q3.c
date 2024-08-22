#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	
	int num1 = 1, num2 = 2, aux = 0, pos = 0;

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