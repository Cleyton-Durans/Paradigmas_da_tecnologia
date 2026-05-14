/* ==========================================================
   EXERCÍCIO GUIADO - C
   Leitura de nome e número inteiro
   Classificação do número como positivo, negativo ou zero
   ========================================================== */

#include <stdio.h>

int main()
{
    // Declaração das variáveis
    char nome[50];
    int numero;

    // Entrada de dados
    printf("Digite seu nome: ");
    scanf("%49s", nome);

    printf("Digite um número inteiro: ");
    scanf("%d", &numero);

    // Processamento e saída
    if (numero > 0)
    {
        printf("%s, o número digitado é positivo.\n", nome);
    }
    else if (numero < 0)
    {
        printf("%s, o número digitado é negativo.\n", nome);
    }
    else
    {
        printf("%s, o número digitado é zero.\n", nome);
    }

    return 0;
}