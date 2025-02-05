a = 8
b = 40

try:
    resultat = a / b

except NameError as e:
    print("Une erreur a été détectée :", e)

else:
    print("Le résultat est :", resultat)

finally:
    print("Fin du code.")