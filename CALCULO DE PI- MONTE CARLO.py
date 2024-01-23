# pi = 4* pin / pontos sorteados
# 0 e 1 x
# 0 e 1 y

# y**2 + x**2 <= 1

#JAVIER AGUSTIN ARANIBAR GONZÁLEZ

import numpy as np



Pontos_sorteados = 1000
Pontos_dentro = 0

for i in range (Pontos_sorteados):
    x = np.random.rand(1) # 0 a 1
    y = np.random.rand(1) # 0 a 1
    c = y**2+x**2

    if c <= 1 :
        Pontos_dentro = Pontos_dentro + 1

pi = 4 * Pontos_dentro/Pontos_sorteados
print("O numero do valor de pi por monte carlo é de :", pi)
