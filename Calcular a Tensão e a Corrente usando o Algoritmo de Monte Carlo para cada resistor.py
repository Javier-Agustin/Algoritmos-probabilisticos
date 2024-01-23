#importar bibliotecas

import random
import matplotlib.pyplot as plt


i=0
k=0
j=0

rI=0
rK=0
rJ=0


#------------------------------------------------------
#RI

N=1000
for i in range(0,N): 
    x = random.uniform(950,1050)
    rI+=x
rI=rI/N

#------------------------------------------------------
#RK
N=560
for k in range(0,N): 
    x = random.uniform(532,588)
    rK+=x
rK=rK/N

#------------------------------------------------------
#RJ
N=2200
for j in range(0,N): 
    x = random.uniform(2090,2310)
    rJ+=x
rJ=rJ/N 
#------------------------------------------------------
#superposição

#FONTE 1
r1= rI+(((1/rK)+(1/rJ))**(-1))
I1= 5/r1
ci1=I1
ck1= (rJ*I1)/(rJ+rK)
cj1=I1-ck1


#FONTE 2

r2 = rJ+(((1/rK)+(1/rI))**(-1))
I2= 0.7/r2
cj2=I2
ck2= (rI*I1)/(rI+rK)
ci2=I2-ck2



#Resultados 
CI=(ci1-ci2)*1000
CK=(ck1-ck2)*1000
CJ=(cj1-cj2)*1000




#printar os resultados de cada resistor com a sua corrente

print("RI:",round(rI,4),"Ohms","corrente(I):",round(CI,4),"mA") 
print("RK:",round(rK,4),"Ohms","corrente(I):",round(CK,4),"mA")
print("RJ:",round(rJ,4),"Ohms","corrente(I):",round(CJ,4),"mA")       
