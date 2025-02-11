from datetime import timedelta, datetime

# Créer un objet timedelta de 20 jours
delta = timedelta(days=20)
print(f"Durée de 20 jours : {delta}")

# Obtenir la date et l'heure actuelles
now = datetime.now()
print(f"Date et heure actuelles : {now}")

# Ajouter 20 jours à la date actuelle
future_date = now + delta
print(f"Date après 20 jours : {future_date}")

