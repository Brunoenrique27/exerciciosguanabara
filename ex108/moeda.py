def formatmoeda(preço):
     return f'R${preço:.2f}'.replace('.',',')

def metade(preço):
    res = preço / 2
    return res


def dobro(preço):
    res = preço * 2
    return res


def aumentar(preço, taxa):
    res = preço + (preço / 100 *taxa)
    return res


def diminuir(preço, taxa):
    res = preço - (preço / 100*taxa)
    return res