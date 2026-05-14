#include <stdio.h>

int main() 
{
    char fila[3][20] = {"Ana", "Bruno", "Carla"};

    printf("Primeiro da fila: %s\n", fila[0]);

    printf("Cliente atendido: %s\n", fila[0]);

    printf("Fila atual:\n");
    printf("%s\n", fila[1]);
    printf("%s\n", fila[2]);

    return 0;
}