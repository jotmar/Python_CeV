from MódulosEx.UtilitiesCeV import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentado 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(valor, 13, True)}')
