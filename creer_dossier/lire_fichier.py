from pathlib import Path

chemin = Path("C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250201")

chemin = chemin / "DossierTest" / "readme.txt"

chemin.touch()

chemin.write_text("Welcome")
print(chemin.read_text())