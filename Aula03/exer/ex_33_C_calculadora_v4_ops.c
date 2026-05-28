// PLP - Aula 3
// 13 mai 2026
// C - Calculadora Modular - versão 4


#include <stdio.h>
#include "ex_33_C_calculadora_v4_ops.h"


float soma(float a, float b) 
{
    return a + b;
}


float subtrai(float a, float b) 
{
    return a - b;
}


float multiplica(float a, float b) 
{
    return a * b;
}


float divide(float a, float b) 
{
    if (b == 0) 
    {
        printf("Erro: divisao por zero nao e permitida.\n");
        return 0;
    }
    return a / b;
}

