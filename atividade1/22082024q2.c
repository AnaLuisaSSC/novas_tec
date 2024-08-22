#include <stdio.h>
#include <stdlib.h>

/*  */
	
	int ehPrimo(int num) 
    
    {
        int ehprimo=1;
		int i = 1;
        for (i = 2; i < num; i++)
        {
            if(num % i == 00)
            {
                ehprimo = 0;
                break;
            }
        }
        return ehprimo;   
    }
int main() {	
    {
        int pos, contador = 0, n=2;

        printf("digite a posição do número primo:");
        scanf("%d", &pos);

        while(contador<pos)
        {
            if(ehPrimo(n)==1)
                contador++;
            n++;
        }
        printf("%d primo é %d.", pos, n-1);
    }
	
	
	return 0;
}