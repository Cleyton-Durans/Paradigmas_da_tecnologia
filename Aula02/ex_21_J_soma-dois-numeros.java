// PLP - Aula 2
// J - Executa a soma de dois números inteiros


import java.util.Scanner; // biblioteca para leitura de dados

public class ex_21_J_soma
{
    public static void main(String[] args)
    {
        Scanner entrada = new Scanner(System.in); // cria o leitor de entrada

        int a, b;
        System.out.print("Digite o 1o. número: ");
        a = entrada.nextInt();
        System.out.print("Digite o 2o. número: ");
        b = entrada.nextInt();

        System.out.println("Soma = " + (a + b));

        entrada.close(); // boa prática: fechar o Scanner
    }
}
