// PLP - Aula 3
// 13 mai 2026
// C - Calculadora Modular - versão 1


#include <stdio.h>

// --- Declaração das funções ---
float soma(float a, float b);
float subtrai(float a, float b);
float multiplica(float a, float b);
float divide(float a, float b);

// --- Função principal ---
int main() 
{
    float x, y;
    int opcao;

    printf("=== CALCULADORA ESTRUTURADA v1 ===\n");
    printf("Digite o primeiro numero: ");
    scanf("%f", &x);
    printf("Digite o segundo numero: ");
    scanf("%f", &y);

    printf("\nEscolha a operacao:\n");
    printf("1 - Soma\n");
    printf("2 - Subtracao\n");
    printf("3 - Multiplicacao\n");
    printf("4 - Divisao\n");
    printf("Opcao: ");
    scanf("%d", &opcao);

    if (opcao == 1)
        printf("Resultado: %.2f\n", soma(x, y));
    else if (opcao == 2)
        printf("Resultado: %.2f\n", subtrai(x, y));
    else if (opcao == 3)
        printf("Resultado: %.2f\n", multiplica(x, y));
    else if (opcao == 4)
        printf("Resultado: %.2f\n", divide(x, y));
    else
        printf("Opcao invalida.\n");

    return 0;
}

// --- Implementacao das funcoes ---
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
    return a / b;
}
