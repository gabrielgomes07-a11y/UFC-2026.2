# bloco de verificação do tipo de variavel dentro da funcao verify_type

def verify_type(value):

    if value.isdigit():
        return 'inteiro'

    elif value.isalpha():
        return 'alfabeto'

    elif value.isalnum():
        return 'alfanumerico'

    else:
        return 'string'


digit = input('Digite algo: ')

print(verify_type(digit))
