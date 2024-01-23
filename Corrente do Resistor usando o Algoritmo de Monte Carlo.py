#declaracao de bilbioteca de numero randomico

import random

#-----------------------------------------------
R=100
res=0
i=0

res_list=[] #declaracao de lista

for i in range(0,R): 
    x = random.uniform(95,105) #Retorna numero aleatorio e incluido entre 95 e 105
    res+=x
    res_list.append(x)


I = 5.5/(res/R) #calculo usando formula


print("Valor da corrente:",I,"A") #printar o valor da corrente
