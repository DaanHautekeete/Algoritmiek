import matplotlib.pyplot as plt

def Fibonacci(n):
    x=[]
    vorigeWaarde = 0
    nieuweWaarde = 1
    x.append(vorigeWaarde)
    x.append(nieuweWaarde)
    # loop voor waarden
    for k in range(n):
        uitkomst = vorigeWaarde + nieuweWaarde
        vorigeWaarde = nieuweWaarde
        nieuweWaarde = uitkomst
        x.append(uitkomst)
    print(x)

    for h in range(len(x)):
        plt.scatter(h, x[h], color='r')
        plt.title('Fibonacci')
        plt.xlabel('Index')
        plt.ylabel('Waarde')
    plt.show()

Fibonacci(10)