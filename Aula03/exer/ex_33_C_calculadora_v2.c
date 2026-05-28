// PLP - Aula 3
// 13 mai 2026
// C - Calculadora Modular - versão 2.0


#include <stdio.h>

// --- Declaração das funções ---
float soma(float a, float b);
float subtrai(float a, float b);
float multiplica(float a, float b);
float divide(float a, float b);

// --- Função principal ---
int main() 
{
    float x, y, resultado;
    int opcao;

    printf("====================================\n");
    printf("=== CALCULADORA ESTRUTURADA v2.0 ===\n");
    printf("====================================\n");

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
    {
        resultado = soma(x, y);
        printf("\nResultado da soma: %.2f\n", resultado);
    }
    else if (opcao == 2) 
    {
        resultado = subtrai(x, y);
        printf("\nResultado da subtracao: %.2f\n", resultado);
    }
    else if (opcao == 3) 
    {
        resultado = multiplica(x, y);
        printf("\nResultado da multiplicacao: %.2f\n", resultado);
    }
    else if (opcao == 4) 
    {
        if (y == 0) 
        {
            printf("\nErro: divisao por zero nao e permitida!\n");
        } 
    else 
        {
            resultado = divide(x, y);
            printf("\nResultado da divisao: %.2f\n", resultado);
        }
    }
    else 
    {
        printf("\nOpcao invalida. Tente novamente.\n");
    }

    printf("\n=== Fim do programa ===\n");
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
