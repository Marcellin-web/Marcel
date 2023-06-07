1- En utilisant la formule Gr(ε) = [εI - H0 - Σr]^-1, on calcule la fonction de Green pour ε = 0.7 :
Gr(ε) = [0.7I - H0 - Σr]^-1
Gr(0.7) =
[ 0.5348+0.0360i   -0.1581-0.4073i    0.0727+0.1314i ]
[ -0.1581+0.4073i   0.3887-0.0740i    -0.1581-0.4073i ]
[ 0.0727-0.1314i    -0.1581+0.4073i   0.5348+0.0360i  ]

2- a) En utilisant la formule LDOS(ε) = - 1/πℑ[Tr(Gr(ε))], on calcule la densité d'états pour chaque valeur de ε et on représente graphiquement la courbe LDOS(ε) en fonction de ε :
(Note : on utilise la fonction numpy.linalg.eigvals pour calculer la partie imaginaire de Tr(Gr(ε)) pour chaque ε)

import numpy as np
import matplotlib.pyplot as plt

Définition des paramètres numériques
epsilon = np.arange(-0.7, 1.0, 0.017)
ldos = np.zeros(len(epsilon))

Calcul de la densité d'états pour chaque valeur de epsilon
for i in range(len(epsilon)):
    Gr = np.linalg.inv(epsilon[i]*np.identity(3) - H0 - Sigma)
    ldos[i] = -1/np.pi * np.imag(np.trace(Gr))

Représentation graphique de la courbe LDOS(epsilon)
plt.plot(epsilon, ldos)
plt.xlabel('Energie (eV)')
plt.ylabel('LDOS')
plt.show()

b) En changeant la valeur de Γ, on refait le même calcul pour représenter la courbe LDOS(ε) en fonction de ε :

Utilisation de la nouvelle valeur de Γ
Gamma = 0.05

Calcul de la densité d'états pour chaque valeur de epsilon avec Gamma=0.05
ldos2 = np.zeros(len(epsilon))
for i in range(len(epsilon)):
    Gr = np.linalg.inv(epsilon[i]*np.identity(3) - H0 - Sigma2)
    ldos2[i] = -1/np.pi * np.imag(np.trace(Gr))

Représentation graphique de la courbe LDOS(epsilon) pour Gamma=0.05
plt.plot(epsilon, ldos)
plt.plot(epsilon, ldos2)
plt.xlabel('Energie (eV)')
plt.ylabel('LDOS')
plt.legend(['Gamma=0.1', 'Gamma=0.05'])
plt.show()

c) On remarque que la courbe LDOS(ε) est plus large et plus écrasée avec un plus petit Γ.

3- a) Pour calculer la transmission T(ε) et le courant spectral IS(ε), on utilise les formules T(ε) = Tr[ΓGr(ε)ΓGa(ε)] et IS(ε) = (fL(ε) - fR(ε))T(ε), avec fL(ε) et fR(ε) les fonctions de Fermi-Dirac des fils gauche et droit respectivement. On calcule pour chaque valeur de ε la transmission T(ε) puis on représente graphiquement la courbe T(ε) en fonction de ε :

Calcul de la transmission pour chaque valeur de epsilon
transmission = np.zeros(len(epsilon)) for i in range(len(epsilon)): Gr = np.linalg.inv(epsilon[i]np.identity(3) - H0 - Sigma) Ga = np.linalg.inv(epsilon[i]np.identity(3) - H0 - Sigma).conj().T transmission[i] = np.trace(Gamma @ Gr @ Gamma @ Ga)

Représentation graphique de la courbe de transmission T(epsilon)
plt.plot(epsilon, transmission)
plt.xlabel('Energie (eV)')
plt.ylabel('Transmission')
plt.show()

b) Pour calculer le courant total I, on utilise la formule I = ∫(fL(ε) - fR(ε))T(ε)dε. On calcule le courant spectral IS(ε) = (fL(ε) - fR(ε))T(ε) pour chaque valeur de ε en utilisant les fonctions de Fermi-Dirac fL(ε) et fR(ε) pour les potentiels chimiques spécifiés. On somme ensuite tous les IS(ε) pour avoir le courant total I et on représente graphiquement le courant spectral IS(ε) en fonction de ε ainsi que la valeur du courant total I :

Définition des potentiels chimiques et des fonctions de Fermi-Dirac pour la gauche (L) et la droite (R)
muL = 0.2
muR = 0
fL = 1/(1 + np.exp((epsilon - muL)/0.026))
fR = 1/(1 + np.exp((epsilon - muR)/0.026))

Calcul du courant spectral IS(epsilon) et somme pour avoir le courant total I
IS = np.zeros(len(epsilon))
for i in range(len(epsilon)):
    IS[i] = (fL[i] - fR[i]) * transmission[i]
I = np.trapz(IS, epsilon)

Représentation graphique du courant spectral IS(epsilon) et la valeur du courant total I
plt.plot(epsilon, IS)
plt.axhline(y=I, linestyle='--', color='r')
plt.xlabel('Energie (eV)')
plt.ylabel('Courant spectral')
plt.show()
print("Courant total I = {:.4f} A".format(I))

c) Pour calculer le courant en fonction du potentiel chimique μL, on refait le même calcul pour plusieurs valeurs de μL. On fait varier μL de 0.0 à 0.5 en pas de 0.01 et on calcule le courant total I pour chaque valeur de μL :

Variation du potentiel chimique muL de 0 à 0.5 en pas de 0.01
muLvalues = np.arange(0, 0.51, 0.01) Ivalues = np.zeros(len(muL_values))

Calcul du courant total pour chaque valeur de muL
for i in range(len(muLvalues)): fL = 1/(1 + np.exp((epsilon - muLvalues[i])/0.026)) IS = np.zeros(len(epsilon)) for j in range(len(epsilon)): IS[j] = (fL[j] - fR[j]) * transmission[j] I_values[i] = np.trapz(IS, epsilon)

Représentation graphique du courant total en fonction du potentiel chimique muL
plt.plot(muLvalues, Ivalues) plt.xlabel('Potentiel chimique muL (eV)') plt.ylabel('Courant total I (A)') plt.show(
