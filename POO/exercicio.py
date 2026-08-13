# bloco de converão de c para f e vice versa

def convertgraus(value1):
    fahr = (value1 * 1.8) + 32
    return fahr


def convertgraus1(value2):
    cels = (value2 - 32) / 1.8
    return cels


# bloco de verificação de entrada
tipo_grau = str(input('Qual a grandeza: '))

if tipo_grau == 'C':

    graus = float(input('Digite os graus celsius: '))
    print('{}°F'.format(convertgraus(graus)))

else:
    graus = float(input('Digite os graus fahrenheit: '))
    print('{}°C'.format(convertgraus1(graus)))
