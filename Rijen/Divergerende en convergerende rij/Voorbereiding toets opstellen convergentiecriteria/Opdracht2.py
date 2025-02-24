import matplotlib.pyplot as plt

def berekening():
    x = []

    for i in range(50):
        if (i == 0):
            i = i+1
        uitkomst = (-5*i) / (1 + 25*i)
        x.append(uitkomst)

    print(x)
    for h in range(len(x)):
        plt.scatter(h, x[h], color='r')
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

# berekening()

#besluit: rij convergeert naar -2 => convergentiecriteria opstellen

def BerekeningMetConvergentiecriteria():
    x = []

    i = 0
    j = 1
    k =0

    #beginwaarden in list steken
    x.append(j)
    x.append(k)

    residuals = []
    iteraties = []

    #convergentiecriteria opstellen
    while abs(x[-1] - x[-2]) > 0.00001:
        i = i + 1
        j = (-5*i) / (1 + 25*i)

        #uitkomst toevoegen aan lijst
        x.append(j)

        #residual toevoegen aan lijst
        residuals.append(abs(x[-1] - x[-2]))

        #aantal iteraties toevoegen aan lijst
        iteraties.append(i)

        plt.scatter(i, j, color='r')

    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

    plt.yscale('log')
    plt.scatter(iteraties, residuals, color='g', label='Residual')
    plt.xlabel('Iteraties')
    plt.ylabel('Residual')
    plt.title('Residual')
    plt.legend()
    plt.show()

BerekeningMetConvergentiecriteria()