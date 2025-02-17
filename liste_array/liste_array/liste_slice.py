# liste = ["Utilisateur_01", 
#          "Utilisateur_02", 
#          "Utilisateur_03", 
#          "Utilisateur_04", 
#          "Utilisateur_05", 
#          "Utilisateur_06", 
#          "Utilisateur_07"]

# print(liste[0:2]) #['Utilisateur_01', 'Utilisateur_02']
# print(liste[:]) #['Utilisateur_01', 'Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05', 'Utilisateur_06', 'Utilisateur_07']
# print(liste[:-1]) #['Utilisateur_01', 'Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05', 'Utilisateur_06']
# print(liste[1:-2:2]) #['Utilisateur_02', 'Utilisateur_04']
# print(liste[::-1]) #['Utilisateur_07', 'Utilisateur_06', 'Utilisateur_05', 'Utilisateur_04', 'Utilisateur_03', 'Utilisateur_02', 'Utilisateur_01']
#================================================================
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
print(liste)
trois_premiers = liste[0:3]
print("Les trois premiers employés: ", trois_premiers)
trois_derniers = liste[3:]
print("Les trois derniers employés: ", trois_derniers)
milieu = liste[1:-1]
print("Tous les employés sauf le premier et le dernier dans une liste: ", milieu)
premier_dernier = liste[0::5]
print("Le premier et le dernier employé dans une liste: ", premier_dernier)