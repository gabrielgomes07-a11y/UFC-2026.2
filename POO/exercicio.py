def convertgraus(value1):
    fahr = (value1 * 1.8) + 32
    return fahr


celsius = float(input('Digite os Graus celsius: '))
print(convertgraus(celsius))
