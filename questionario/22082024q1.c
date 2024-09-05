#include <stdio.h>
#include <stdlib.h>

/* para descobrir o x² dos numeros */

int main() {
	
	int num, result = 0;
	
	printf("entre um numero:");
	scanf("%d",&num);
	
	int i = 0;
	
	for( i = 0; i<num ; i++){     // se for 3 o num , o i é menor q 3 logo o looping vai novamente
		result = result + 2*i+1;
	}
	printf("%d ao quadrado é %d", num, result);

	
	return 0;
}
