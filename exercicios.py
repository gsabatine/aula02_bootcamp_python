# # Exercícios Python

# # Inteiros (int)
# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.
Numero_1 = int(input("Digite um numero:"))
Numero_2 = int(input("Digite outro numero:"))
resultado_soma = Numero_1 + Numero_2
print("A soma dos dois numeros e:", resultado_soma)

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número: "))
num = 18  # Exemplo de entrada
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
Número_1 = int(input("Digite um número: "))
Número_2 = int(input("Digite outro número: "))
resultado_multiplicação = Número_1 * Número_2
print("A multiplicação dos dois números e:", resultado_multiplicação)

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
Número_1 = int(input("Digite um número: "))
Número_2 = int(input("Digite outro número: "))
resultado_divisão = Número_1 // Número_2
print("O resultado da sua divisão é:", resultado_divisão)

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
Número_1 = int(input("Digite um Número: "))
Número_2 = int(input("Digite outro Número: "))
resultado_do_calculo = Número_1 ** Número_2
print("O resultado da conta é: ", resultado_do_calculo)

# # Números de Ponto Flutuante (float)
# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição.
Número_1 = float(input("Digite um número: "))
Número_2 = float(input("Digite outro número: "))
resultado_adição =  Número_1 + Número_2
print("O resultado da adição foi: ", resultado_adição)

# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
Número_1 = float(input("Digite um número: "))
Número_2 = float(input("Digite outro número: "))
resultado_média = (Número_1 + Número_2) / 2
print("A média dos numeros é: ", resultado_média)

# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
Número_1 = float(input("Digite a base: "))
Número_2 = float(input("Digite o expoente: "))
resultado_calculo = Número_1 ** Número_2
print("O Resultado da potencia é:", resultado_calculo)

# 9 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.
Temperatura = float(input("Digite a temperatura: "))
Temperatura_Fahrenheit = (Temperatura * 9/5) + 32
print(f"{Temperatura}C é igual a {Temperatura_Fahrenheit}F")

#10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio: "))
area_circulo = math.pi * raio ** 2
print("A area do Circulo é: ", area_circulo)

# Strings (str)
#11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = str(input("Digite sua string: "))
string_convertida = string.upper()
print("Texto convertido:", string_convertida)

#12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = str(input("Insira seu nome: "))
nome_convertido = nome.lower()
print("Seu nome em minusculo: ", nome_convertido)

#13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
string = input("Insira sua string: ")
frase_convertida =  string.strip()
print("String final:", frase_convertida)

#14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Insira sua data aqui dd/mm/aaaa: ")
data_separada = data.split(sep="/")
print("Sua data separada:", data_separada)

#15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Primeira string: ")
string2 = input("Segunda string: ")
string_concatenada =  string1 + string2
print("String concatenada:", string_concatenada)

# # Booleanos (bool)
#16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

#17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = bool(input("Seu primeiro valor: "))
valor2 = bool(input("Segundo valor: "))
resultado_or = valor1 or valor2
print("Resultado OR:", resultado_or)

#18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor1 = True # Revertendo valores 
print(valor1)

valor1 = not valor1
print(valor1)

valor1 = not valor1
print(valor1)

valor1 = not valor1
print(valor1)

# #19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = input("Seu primeiro numero: ")
num2 = input("Seu segundo numero: ")
resultado_final = (num1 == num2)
print("Resultado comparação:", resultado_final)

# #20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = input("Seu primeiro numero: ")
num2 = input("Seu segundo numero: ")
resultado_verificação = (num1 != num2)
print("Resultado verificação:", resultado_verificação)

#### try-except e if

# 21: Conversor de Temperatura
try:
    Temperatura_celsius = float(input("Digite a temperatura: "))
    Temperatura_Fahrenheit = (Temperatura_celsius * 9/5) + 32
    print(f"{Temperatura_celsius}C é igual a {Temperatura_Fahrenheit}F")
except ValueError:
    print("Digite apenas números")

# 22: Verificador de Palíndromo
frase = input("Digite uma frase: ")
if isinstance(frase, str):
    formatado = frase.replace(" ", "").lower()
    if formatado == formatado [::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor digite uma palavra ou frase.")

# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digte o operador (+, -, * ou /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inserido inválido ou divisão por zero.")
    print("Resultado", resultado)
except ValueError:
    print("Erro: Entrada Inválida. Certifique de inserir corretamente números e operadores.")

# 24: Classificador de Números
try: 
    numero = float(input("Digite um número: "))
    if numero > 0:
        print("Positivo.")
    elif numero < 0:
        print("Negativo.")
    else: 
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")
except ValueError:
    print("Por favor, digite um número!")

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")