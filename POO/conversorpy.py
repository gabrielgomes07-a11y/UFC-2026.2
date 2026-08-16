def conversor(num, base_e):
    '''conversor universal.
        funciona assim:
        base de entrada -> decimal
        decimal -> base de destino
    '''

    saida = []

    if num == 0:
        print('0\n')
        return

    while num > 0:
        saida.append(num % base_e)
        num = num // base_e

    for i in range(len(saida) - 1, -1, -1):
        if saida[i] >= 10:
            print(chr(saida[i] + 55), end='')
        else:
            print(saida[i], end='')

    print('\n')


def main():
    # entrada em str
    number1 = input()

    # entrada das bases
    bases = input().split()
    base_origem = int(bases[0])
    base_destino = int(bases[1])

    number = int(number1, base_origem)

    conversor(number, base_destino)


if __name__ == "__main__":
    main()
