// PLP - Aula 3
// 13 mai 2026
// C - Calculadora Modular - versão 4


#include <stdio.h>
#include "ex_33_C_calculadora_v4_ui.h"


void mostrar_menu() 
{
    printf("\n===== CALCULADORA MODULAR v4 =====\n");
    printf("1 - Soma\n");
    printf("2 - Subtracao\n");
    printf("3 - Multiplicacao\n");
    printf("4 - Divisao\n");
    printf("0 - Sair\n");
    printf("===============================\n");
    printf("Escolha uma opcao: ");
}


void limpar_buffer() 
{
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF);
}


void ler_valores(float *x, float *y) 
{
    printf("Digite o primeiro numero: ");
    while (scanf("%f", x) != 1) 
    {
        limpar_buffer();
        printf("Entrada invalida! Digite um numero: ");
    }

    printf("Digite o segundo numero: ");
    while (scanf("%f", y) != 1) 
    {
        limpar_buffer();
        printf("Entrada invalida! Digite um numero: ");
    }
}
