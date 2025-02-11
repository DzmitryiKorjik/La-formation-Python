employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
if "id03" in employes:
    del employes["id03"]
    print(employes)

employes["id02"]["age"] = 26
print(employes["id02"])

age_paul = employes["id01"]["age"]
print(f"L'age de Paul est {age_paul} ans.")