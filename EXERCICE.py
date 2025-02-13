
#Exercice 1 : Fibonacci et recherche du premier supérieur à n
#Nous allons créer une classe Fibonacci qui :

#Génère la suite de Fibonacci.
#Trouve le premier nombre de Fibonacci supérieur à un seuil donné.

class Fibonacci:
    def __init__(self):
        self.sequence = [1, 1]  # Initialisation avec les deux premiers termes

    def get_fibonacci_greater_than(self, n):
        #Retourne le premier nombre de Fibonacci supérieur à n
        while self.sequence[-1] <= n:
            next_fib = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_fib)
        return self.sequence[-1]







#Exercice 2 :# Analyse des précipitations
#Nous allons créer une classe Precipitations qui :

#Calcule les précipitations totales et moyennes.
#Détermine combien de mois ont eu des précipitations supérieures à la moyenne.
#Identifie les mois où Boston a eu moins de précipitations que Seattle.

class Precipitations:
    def __init__(self, city_name, data):
        self.city = city_name
        self.data = data

    def total_precipitations(self):
        return sum(self.data)

    def average_precipitations(self):
        return sum(self.data) / len(self.data)

    def months_above_average(self):
        avg = self.average_precipitations()
        return sum(1 for p in self.data if p > avg)

# Données des précipitations
BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
SEA = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

boston = Precipitations("Boston", BOS)
seattle = Precipitations("Seattle", SEA)

print(f"Total des précipitations à Boston : {boston.total_precipitations()} pouces")
print(f"Total des précipitations à Seattle : {seattle.total_precipitations()} pouces")

print(f"Mois avec précipitations supérieures à la moyenne à Boston : {boston.months_above_average()}")
print(f"Mois avec précipitations supérieures à la moyenne à Seattle : {seattle.months_above_average()}")

# Identifier les mois où Boston a eu moins de pluie que Seattle
months_boston_less = [i+1 for i in range(12) if BOS[i] < SEA[i]]
print(f"Mois où Boston a eu moins de précipitations que Seattle : {months_boston_less}")





#Exercice 3 : Corrélation et test de Fisher
#Nous allons créer une classe Correlation qui :

#Calcule le coefficient de corrélation entre deux variables X et Y.
#Effectue un test de corrélation basé sur la transformation Z de Fisher.

import numpy as np
import scipy.stats as stats

class Correlation:
    def __init__(self, X, Y):
        self.X = np.array(X)
        self.Y = np.array(Y)

    def compute_correlation(self):
        return np.corrcoef(self.X, self.Y)[0, 1]

    def fisher_test(self, rho_0=0):
        r = self.compute_correlation()
        Z = 0.5 * np.log((1 + r) / (1 - r))
        Z_0 = 0.5 * np.log((1 + rho_0) / (1 - rho_0))
        n = len(self.X)
        Z_stat = (Z - Z_0) * np.sqrt(n - 3)
        p_value = 2 * (1 - stats.norm.cdf(abs(Z_stat)))
        return r, p_value

# Exemple de données
X = [10, 20, 30, 40, 50, 60, 70]
Y = [8, 18, 28, 38, 48, 58, 68]

corr = Correlation(X, Y)
print(f"Coefficient de corrélation : {corr.compute_correlation()}")
r_0, p_val_0 = corr.fisher_test(0)
print(f"Test de Fisher pour rho_0=0 : r={r_0}, p-value={p_val_0}")
r_06, p_val_06 = corr.fisher_test(0.6)
print(f"Test de Fisher pour rho_0=0.6 : r={r_06}, p-value={p_val_06}")






#Exercice 4 : Modèle de Nicholson-Bailey
#Nous allons créer une classe NicholsonBaileyModel pour simuler la dynamique hôte-parasitoïde.


import numpy as np
import matplotlib.pyplot as plt

class NicholsonBaileyModel:
    def __init__(self, generations=30, H_init=20, P_init=2, R=2, a=0.05, b=1):
        self.generations = generations
        self.H = [H_init]  # Population des hôtes
        self.P = [P_init]  # Population des parasitoïdes
        self.R = R  # Taux d'augmentation des hôtes
        self.a = a  # Zone d'attaque
        self.b = b  # Nombre de parasitoïdes produits par hôte parasité

    def simulate(self):
        for t in range(1, self.generations):
            H_next = self.H[-1] * self.R * np.exp(-self.a * self.P[-1])
            P_next = self.H[-1] * self.b * (1 - np.exp(-self.a * self.P[-1]))
            self.H.append(H_next)
            self.P.append(P_next)

    def plot_results(self):
        plt.figure(figsize=(10, 5))
        plt.plot(range(self.generations), self.H, label="Hôtes", marker="o")
        plt.plot(range(self.generations), self.P, label="Parasitoïdes", marker="s")
        plt.xlabel("Générations")
        plt.ylabel("Population")
        plt.title("Modèle de Nicholson-Bailey")
        plt.legend()
        plt.show()







