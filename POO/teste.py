n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite outro numero inteiro: '))

s = n1 + n2

# .format on print: serve como o printf de c, por fazer a formatacao com as variaveis e seus ponteiros.
print('A soma de {} e {} é: {}'.format(n1, n2, s))
n = input('digite um numero: ')

# variavel.ismethod() é uma verificação de tipos. Ou seja, verifica se o input sem .format pode ser convertido completamente em n tipos primitivos.
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())


# print(type(algo))
