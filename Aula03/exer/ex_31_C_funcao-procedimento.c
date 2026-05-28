// PLP - Aula 3
// 13 mai 2026
// C - Função e procedimento


# include <stdio.h>

float soma(float a, float b) 
{
    return a + b;
}

int main() 
{
    float x, y;
    printf("Digite dois valores: ");
    scanf("%f %f", &x, &y);
    printf("Resultado: %.2f", soma(x, y));
}