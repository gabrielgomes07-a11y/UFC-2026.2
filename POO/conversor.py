def conversor1(num, base):
    '''conversor universal.
    funciona assim:
    base de entrada -> decimal
    decimal -> base de destino
    '''
    if num == 0:
        print("0")
        return

    vetnum = []

    while num > 0:
        vetnum.append(num % base)
        num = num // base

    resultado = ""

    for i in range(len(vetnum) - 1, -1, -1):
        if vetnum[i] >= 10:
            resultado += chr(vetnum[i] + 55)
        else:
            resultado += str(vetnum[i])

    print(resultado)


def main():
    # entrada em str
    number1 = input()

    # entrada das bases
    bases = input().split()
    base_origem = int(bases[0])
    base_destino = int(bases[1])

    number = int(number1, base_origem)

    conversor1(number, base_destino)


if __name__ == "__main__":
    main()
