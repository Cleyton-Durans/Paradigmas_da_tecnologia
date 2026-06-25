#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_product
{
	char	*name;
	float	price;
	int		quantity;
} t_product;

// UTILS
void waitEnter(void)
{
	printf("\nPressione Enter para continuar...");
	getchar();
}

void inputError(char *message)
{
	int	c;

	printf("\nERRO: %s\n", message);
	printf("Pressione Enter para continuar...");

	while ((c = getchar()) != '\n' && c != EOF)
		;

	getchar();
}

int productExists(t_product *database, int count, char *name)
{
	int	i;

	i = 0;
	while (i < count)
	{
		if (strcmp(database[i].name, name) == 0)
			return (1);
		i++;
	}

	return (0);
}

// MOSTRAR DATABASE
void printDatabase(t_product *database, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		printf(
			"%s %.2f %d\n",
			database[i].name,
			database[i].price,
			database[i].quantity
			);
		i++;
	}
}

// REGISTRAR PRODUTOS
void registerProduct(t_product *database, int *count, char *name, float price, int quantity)
{
	database[*count].name = strdup(name);
	database[*count].price = price;
	database[*count].quantity = quantity;

	(*count)++;
}

void registerProductMenu(t_product *database, int *count)
{
	char	name[100];
	float	price;
	int		quantity;

	system("clear");
	
	while (1)
	{
		printf("Nome: ");
		scanf("%99s", name);

		if (!productExists(database, *count, name))
			break;

		inputError("Produto ja cadastrado!");
	}

	while (1)
	{
		printf("Preco: ");

		if (scanf("%f", &price) == 1 && price >= 0)
			break;

		printf("Preco invalido!\n");

		while (getchar() != '\n')
			;
	}

	while (1)
	{
		printf("Quantidade: ");

		if (scanf("%d", &quantity) == 1 && quantity >= 0)
			break;

		printf("Quantidade invalida!\n");

		while (getchar() != '\n')
			;
	}

	registerProduct(
		database,
		count,
		name,
		price,
		quantity
	);
	//clean buffer
	while (getchar() != '\n')
		;
}

// UPDATE DATABASE
void updateSales(t_product *database, int count)
{
	char	name[100];
	int		sold;
	int		i;

	printf("Nome do produto: ");
	scanf("%99s", name);

	i = 0;
	while (i < count)
	{
		if (strcmp(database[i].name, name) == 0)
			break;
		i++;
	}

	if (i == count)
	{
		inputError("Produto nao encontrado!");
		return;
	}

	while (1)
	{
		printf("Quantidade vendida: ");

		if (scanf("%d", &sold) != 1)
		{
			inputError("Digite um numero inteiro!");
			continue;
		}

		if (sold < 0)
		{
			inputError("A quantidade nao pode ser negativa!");
			continue;
		}

		if (sold > database[i].quantity)
		{
			inputError("Estoque insuficiente!");
			continue;
		}

		break;
	}

	database[i].quantity -= sold;

	//clean buffer
	while (getchar() != '\n')
		;

	printf("\nVenda registrada!\n");
}

void updateRestock(t_product *database, int count)
{
	char	name[100];
	int		restock;
	int		i;

	printf("Nome do produto: ");
	scanf("%99s", name);

	i = 0;
	while (i < count)
	{
		if (strcmp(database[i].name, name) == 0)
			break;
		i++;
	}

	if (i == count)
	{
		inputError("Produto nao encontrado!");
		return;
	}

	while (1)
	{
		printf("Quantidade vendida: ");

		if (scanf("%d", &restock) != 1)
		{
			inputError("Digite um numero inteiro!");
			continue;
		}

		if (restock < 0)
		{
			inputError("A quantidade nao pode ser negativa!");
			continue;
		}

		break;
	}

	database[i].quantity += restock;

	//clean buffer
	while (getchar() != '\n')
		;

	printf("\nVenda registrada!\n");
}

void	updateStockMenu(t_product *database, int count)
{
	int	num;

	while(1)
	{
		system("clear");
		printf("(0) Adicionar Venda\n");
		printf("(1) Adicionar Reposição\n");
		printf("(2) Voltar\n");

		while (1)
		{
			printf("Opção: ");

			if (scanf("%d", &num) != 1)
			{
				inputError("Digite um numero!");
				continue;
			}

			if (num < 0 || num > 2)
			{
				inputError("Input deve ser entre 0 e 2");
				continue;
			}

			while (getchar() != '\n')
				;

			break;
		}

		if (num == 2)
			break;
		if (num == 0)
		{
			updateSales(database, count);

			system("clear");
			printDatabase(database, count);

			waitEnter();
		}
		if (num == 1)
		{
			updateRestock(database, count);

			system("clear");
			printDatabase(database, count);

			waitEnter();
		}
	}
}

// MOSTRAR VALOR TOTAL DO INVENTARIO
void calculateTotal(t_product *database, int count)
{
	float	total;
	int		i;

	total = 0;
	i = 0;

	while (i < count)
	{
		total += database[i].price * database[i].quantity;
		i++;
	}

	printf("\nValor total do estoque: R$ %.2f\n", total);
}

// MOSTRAR PRODUTO MAIS BARATO E MAIS CARO
void Identify_Cheap_Expensive(t_product *database, int count)
{
	int	i;
	int	cheapest;
	int	expensive;

	if (count <= 0)
	{
		printf("Banco de dados vazio!\n");
		return;
	}

	cheapest = 0;
	expensive = 0;

	i = 1;
	while (i < count)
	{
		if (database[i].price < database[cheapest].price)
			cheapest = i;

		if (database[i].price > database[expensive].price)
			expensive = i;

		i++;
	}

	printf("Produto mais barato:\n");
	printf(
		"%s - R$ %.2f\n\n",
		database[cheapest].name,
		database[cheapest].price
	);

	printf("Produto mais caro:\n");
	printf(
		"%s - R$ %.2f\n",
		database[expensive].name,
		database[expensive].price
	);
}

// MAIN
int	main(void)
{
	t_product database[100] = {
		{"melancia", 5.0, 2},
		{"banana", 1.2, 4},
		{"maca", 0.6, 4}
	};
	int count = 3;

	printDatabase(database, count);

	int	num;

	// Interface de Seleção
	while(1)
	{
		system("clear");
		printf("O que deseja fazer?\n");
		printf("(0) Ver Banco de Dados\n");
		printf("(1) Cadastrar Produto\n");
		printf("(2) Atualizar Estoque\n");
		printf("(3) Calcular Valor Total do Estoque\n");
		printf("(4) Identificar Produtos Mais Caros e Baratos\n");
		printf("(5) Sair\n");

		// Verificação do Menu
		while (1)
		{
			printf("Opção: ");

			if (scanf("%d", &num) != 1)
			{
				inputError("Digite um numero!");
				continue;
			}

			if (num < 0 || num > 5)
			{
				inputError("Input deve ser entre 0 e 5");
				continue;
			}

			while (getchar() != '\n')
				;

			break;
		}

		// Lógica de Decisão do Menu
		if (num == 5)
			break;

		if (num == 0)
		{
			system("clear");
			printDatabase(database, count);
			waitEnter();
		}

		if (num == 1)
		{
			registerProductMenu(database, &count);

			system("clear");
			printf("\nBanco de dados atualizado:\n");
			printDatabase(database, count);

			waitEnter();
		}

		if (num == 2)
			updateStockMenu(database, count);

		if (num == 3)
		{
			system("clear");
			calculateTotal(database, count);
			waitEnter();
		}

		if (num == 4)
		{
			system("clear");
			Identify_Cheap_Expensive(database, count);
			waitEnter();
		}
	}
		return (0);
}
