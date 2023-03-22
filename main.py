import os
import chico

env = os.environ['arquivo']

print(env)

file = open('./programas/' + env,'r')
programa = file.readlines()

gaveteiro = [0 for i in range(100)]

print(chico.carregar(programa,gaveteiro))

print(chico.rodar(gaveteiro, programa))

file.close()