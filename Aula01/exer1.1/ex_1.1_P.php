<?php
echo "Digite seu nome: ";
$nome = trim(fgets(STDIN));

echo "Digite um número inteiro: ";
$numero = (int) trim(fgets(STDIN));

if ($numero > 0) {
    $resultado = "positivo";
} elseif ($numero < 0) {
    $resultado = "negativo";
} else {
    $resultado = "zero";
}

echo "$nome, o número $numero é $resultado.\n";
?>