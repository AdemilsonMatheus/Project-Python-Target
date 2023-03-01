def porcentagem (estado, total):
    return round(((estado*100)/total),2)

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP + RJ + MG + ES + Outros

print("Porcentagem do faturamento de SP: " + str(porcentagem(SP, total)) + '%')
print("Porcentagem do faturamento de RJ: " + str(porcentagem(RJ, total)) + '%')
print("Porcentagem do faturamento de MG: " + str(porcentagem(MG, total)) + '%')
print("Porcentagem do faturamento de ES: " + str(porcentagem(ES, total)) + '%')
print("Porcentagem de outros faturamentos: " + str(porcentagem(Outros, total)) + '%')
