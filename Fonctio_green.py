# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


espi1 = -0.5
epsi2 = 0.7
epsi3 = 0.7
beta = 0.2 
gamma = 0.1 
µL = 0.2 
µR = 0.0 
KBT = 0.025 
epsi = 0.7

#Fonction de green Gr(epsi)

def green_fonction(epsi):
    H0 = np.array([[espi1, -beta,0 ], [-beta , epsi2 , -beta], [0, -beta,epsi3]])
    Fr = np.array([[-1j * gamma, 0, 0], [0,0,0],[0,0,-1j*gamma]])
    Gr = np.linalg.inv(epsi*np.eye(3)-H0 - Fr)
    return Gr 

# Fonction de Fermi-Dirac
def fermi_dirac(epsi, µ):
    return 1.0 / (1.0 + np.exp((epsi - µ) /(KBT)))


#Q1

epsi_valeures = 0.7 
Gr = green_fonction(epsi_valeures)
print("Fonction de green Gr(epsi) pour epsi = ", epsi_valeures)
print("La valeur de Gr(epsi) = ", Gr)

#Q2a)
epsi_valeures  = np.arange(-0.7, 1.0, 0.017)
LDOS_valeures = []

for epsi in epsi_valeures:
    Gr = green_fonction(epsi)
    LDOS = (-1.0/np.pi) * np.imag(np.trace(Gr))
    LDOS_valeures.append(LDOS)
    

plt.plot(epsi_valeures,LDOS_valeures)
plt.xlabel("espi")
plt.ylabel("LDOS")
plt.title("Courbe LDOS(epsi)")
plt.grid(True)
plt.show()



#Q2b)

gamma = 0.05
LDOS_valeures_2b = []

for epsi in epsi_valeures:
    Gr = green_fonction(epsi)
    LDOS = (-1.0/np.pi) *np.imag(np.trace(Gr))
    LDOS_valeures_2b.append(LDOS)
    
    
plt.plot(epsi_valeures, LDOS_valeures_2b)
plt.xlabel("epsi")
plt.ylabel("LDOS")
plt.title("Courbe LDOS(epsi) avec gamma = 0.05")
plt.grid(True)
plt.show()


#Q2c)

plt.plot(epsi_valeures, LDOS_valeures, label = "gamma= 0.1")
plt.plot(epsi_valeures, LDOS_valeures_2b, label = "gamma = 0.05")
plt.xlabel("epsi")
plt.ylabel("LDOS")
plt.title("Courbe de comparaison des valeures de LDOS(epsi)")
plt.legend()
plt.grid(True)
plt.show()



#Q3a)

T_valeures = []
for epsi in epsi_valeures:
    Gr = green_fonction(epsi)
    Ga = np.conjugate(np.transpose(Gr))
    T = np.trace(np.dot(gamma* Gr, gamma*Ga))
    T_valeures.append(T)

plt.plot(epsi_valeures, T_valeures)
plt.xlabel("epsi")
plt.ylabel("T(epsi)") 
plt.title("Courbe de transimission T(espi)")
plt.grid(True)
plt.show() 


#Q3b)

IS_valeures = []
for epsi in epsi_valeures:
    fL = fermi_dirac(epsi, µL)
    fR = fermi_dirac(epsi,µR)
    IS = (fL-fR)*T
    IS_valeures.append(IS)
    
    
plt.plot(epsi_valeures, IS_valeures)
plt.xlabel("epsi")
plt.ylabel("IS(epsi)")
plt.title("Courbe IS(epsi)")
plt.grid(True)
plt.show()


#Calcul du courant total I

I = np.sum(IS_valeures)

print()
print()
print("La valeure de I total est : ", I)
print()
print()

#Q3c)

µL_valeures = np.arange(0.0,0.5,0.01)
IS_valeures1 = []
IM = []

for µL in µL_valeures:
    for epsi in epsi_valeures:
        fL = fermi_dirac(epsi, µL)
        fR = fermi_dirac(epsi,µR)
        IS = (fL-fR)*T
        IS_valeures1.append(IS)
    I = np.sum(IS_valeures1)
    IM.append(I)

plt.plot(µL_valeures,IM)
plt.xlabel("µL")
plt.ylabel("I(µL)")
plt.title("Courbe de I(µL)")
plt.grid(True)
plt.show()

