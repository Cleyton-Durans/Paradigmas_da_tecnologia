// PLP - Aula 3
// 13 mai 2026
// C - Calculadora Modular - versão 4

#include <stdio.h>
#include "ex_33_C_calculadora_v4_ops.h"
#include "ex_33_C_calculadora_v4_ui.h"

int main()
{
    float x, y, resultado;
    int opcao;

    do
    {
        mostrar_menu();

        // leitura segura da opção
        if (scanf("%d", &opcao) != 1)
        {
            printf("Entrada invalida! Digite apenas numeros.\n");
            limpar_buffer();
            opcao = -1;
        }

        switch (opcao)
        {
            case 1:
                ler_valores(&x, &y);
                resultado = soma(x, y);
                printf("Resultado: %.2f\n", resultado);
                break;

            case 2:
                ler_valores(&x, &y);
                resultado = subtrai(x, y);
                printf("Resultado: %.2f\n", resultado);
                break;

            case 3:
                ler_valores(&x, &y);
                resultado = multiplica(x, y);
                printf("Resultado: %.2f\n", resultado);
                break;

            case 4:
                ler_valores(&x, &y);
                resultado = divide(x, y);

                if (y != 0)
                {
                    printf("Resultado: %.2f\n", resultado);
                }
                break;

            case 0:
                printf("Encerrando o programa...\n");
                break;

            default:
                printf("Opcao invalida! Tente novamente.\n");
        }

    } while (opcao != 0);

    return 0;
}