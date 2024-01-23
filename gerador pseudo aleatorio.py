import matplotlib.pyplot as plt
Nit = 10000 #10000 interações max
a = 3
b = 5
m = 31
n = 0
L1 = []
L2 = []
while n <= Nit:
    if n==0:
        f0 = 2 #f(0) = 2
    else:
        f0 = ((a*f0+b) %m) #f(0) = ((3+f(0)+5)%m)
        if f0==0:
            print(n)

    L1.append(n)
    L2.append(f0)



    #plotar o grafico para as interações

    if n == 10 or n == 100 or n == 1000 or n == 10000:
        plt.plot(L1, L2)
        plt.xlabel('D')
        plt.ylabel('I')
        plt.show()
    n += 1
