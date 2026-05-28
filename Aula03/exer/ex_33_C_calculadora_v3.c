// PLP - Aula 3
// 13 mai 2026
// C - Calculadora Modular - versão 3


#include <stdio.h>

// ---------- Funções matemáticas ----------

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


// ---------- Programa principal ----------

int main() 
{
    float x, y, resultado;
    int opcao;

    do 
    {
        // Menu principal
        printf("\n===== CALCULADORA MODULAR v3 =====\n");
        printf("1 - Soma\n");
        printf("2 - Subtracao\n");
        printf("3 - Multiplicacao\n");
        printf("4 - Divisao\n");
        printf("0 - Sair\n");
        printf("===============================\n");

        printf("Escolha uma opcao: ");
        
        // tentativa de leitura segura
        if (scanf("%d", &opcao) != 1) 
        {
            printf("Entrada invalida! Digite apenas numeros.\n");
            while (getchar() != '\n'); // limpa buffer
            opcao = -1; // força opção inválida
        }

        // Processamento das opções
        switch (opcao) 
        {
            case 1:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &x);
                printf("Digite o segundo numero: ");
                scanf("%f", &y);
                resultado = soma(x, y);
                printf("Resultado da soma: %.2f\n", resultado);
                break;

            case 2:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &x);
                printf("Digite o segundo numero: ");
                scanf("%f", &y);
                resultado = subtrai(x, y);
                printf("Resultado da subtracao: %.2f\n", resultado);
                break;

            case 3:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &x);
                printf("Digite o segundo numero: ");
                scanf("%f", &y);
                resultado = multiplica(x, y);
                printf("Resultado da multiplicacao: %.2f\n", resultado);
                break;

            case 4:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &x);
                printf("Digite o segundo numero: ");
                scanf("%f", &y);
                resultado = divide(x, y);
                if (y != 0) 
                {
                    printf("Resultado da divisao: %.2f\n", resultado);
                }
                break;

            case 0:
                printf("\nEncerrando o programa...\n");
                break;

            default:
                printf("\nOpcao invalida! Tente novamente.\n");
        }

    } 
    while (opcao != 0);  // repete até o usuário escolher sair

    return 0;
}
