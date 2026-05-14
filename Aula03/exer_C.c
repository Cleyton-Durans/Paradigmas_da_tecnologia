# include <stdio.h>
 
float soma(float a, float b) 

{
    return a + b;
}

int main() 

{
    float x, y;
    printf("Digite um valor: \n");
    scanf("%f", &x);
    printf("Digite outro valor: \n");
    scanf("%f", &y);
    printf("Resultado: %.2f", soma(x, y));

}
 