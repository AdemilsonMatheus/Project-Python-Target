print('_'*30)

print('Sequência de Fibonacci')

print('_'*30)

n = int(input('Insira um numero para gerar a sequência de Fibonnaci: '))

t1 = 0

t2 = 1

sim = 0
if (n == 1) or (n == 0):
      sim = 1
print('~'*30)

print('{} -> {}'.format(t1, t2), end = '')

cont = 3

while cont <= n:

   t3 = t1 + t2
   if (n == t1) or (n == t1) or (n == t3):
       sim = 1
   print('-> {}'.format(t3), end = '')

   t1 = t2

   t2 = t3

   cont += 1
if sim == 1:

    print("\n O numero",n,"pertence a sequencia de Fibonnaci!")

else:
    print("\n ",n,"Não pertence a sequência de Fibonnaci")
