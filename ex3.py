import json
d = open('./dados.json')
dados = json.load(d)
aux = 0
maior = 0
menor = 0
soma = 0
media = 0

for dia in dados:
    if (dia['valor']) != 0:
        aux = dia['valor']
        if (aux > maior):
            maior = aux
        if(menor == 0):
            menor = aux
        elif (aux < menor):
            menor = aux
        soma += dia['valor']
        

print('O menor valor de faturamento ocorrido em um dia do mês: R$ ' + str(menor) + '.')
print('O maior valor de faturamento ocorrido em um dia do mês: R$ ' + str(maior) + '.')

media = soma / len(dados)
faturamentoDiario = ''

for i in dados:
    if (i['valor']) != 0:
        if (i['valor']) > media:
           faturamentoDiario += (str(i['dia']) + ' ')
      
print('\nNúmero de dias no mês em que o valor de faturamento diário foi superior à média mensal: ' + faturamentoDiario)