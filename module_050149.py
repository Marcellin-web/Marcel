from math import * #Importation du bibliothèque math pour faire le calcul (sqrt)
def racine(a,b,c): #Définition d'une fonction racine qui prend les paramettre a, b, et c
    delta = b**2 - 4 * a *c #Calcul du déterminant
    print("delta = ", delta)#Affichage du resultat du delta 
    if delta<0: #Condition si le déterminant est inferieur à 0
        print("L'équaion admet deux solutions complexes z1 et z2 :") #Dire à l'utilisateur que c'est 2 solutions complexes 
        z1 = (-b-1j*sqrt(abs(delta)))/2*a #Complexe 1
        z2 = (-b+1j*sqrt(abs(delta)))/2*a #Complexe 2
        print("z1 = ", z1 , " et z2 = ", z2) # Les resultats des complexes calculés
    elif delta>0: # Condition que si le déterminant est supérieur à 0
        print("L'équation admet deux solutions réelles.")  # Dire à l'utilisateur que c'est 2 solutions reeles 
        x1 = (-b-sqrt(delta))/2*a #Réel 1
        x2 = (-b+sqrt(delta))/2*a #Réel 2
        print("x1 = ", x1 , " et x2 = ", x2) #Les resultats des réels calculés
    else: #Condition sinon ( si delta =0)
        print("L'équation admet unne seule solution x0 donnée par: ") #Dire que c'est une unique solution réel
        x0 = -b/2*a #L'unique solution
        print("x0 = ", x0) #Affichage du resultat issu du calcule
#Demander à l'utilisateur d'entrer des donnés suivants:      
a = float(input("Entrer la valeur de a :.. " )) #Entrer a 
b = float(input("Entrer la valeur de b : .. ")) #Entrer b
c = float(input("Entrer la valeur de c : .. ")) #Entrer c
while a ==0:#Condition tanque a est égal à 0; 
    a = float(input("Entrer la valeur de a différent de 0 :.. " )) #Redemande à l'utilisateur d'entrer  nouveau la valeur de a different de 0
racine(a, b, c) #Appel de la fonction racine: 

#NB: Il est très important d'appeler la fonction à la fin sinon le code ne pourra pas s'exécuté.
