from pathlib import Path
import shutil

# 🔹 Dictionnaire associant les extensions aux catégories de fichiers
dirs = { 
    ".png": "Images", ".jpg": "Images",
    ".pdf": "Documents", ".txt": "Documents", ".docx": "Documents", ".xlsx": "Documents",
    ".exe": "Executables", ".msi": "Executables",
    ".dll": "Libraries",
    ".py": "Scripts", ".java": "Scripts",
    ".mp3": "Audio", ".wav": "Audio",
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
    ".7z": "Archives", ".tar": "Archives", ".rar": "Archives", ".iso": "Archives", ".dmg": "Archives", ".zip": "Archives",
    ".html": "Web", ".css": "Web", ".js": "Web", ".json": "Web", ".php": "Web",
    ".sql": "Databases", ".sqlite": "Databases", ".mysql": "Databases", ".pgsql": "Databases", ".db": "Databases"
}

# 🔹 Définition des dossiers
downloads_dir = Path("C:/Users/dmard/Downloads")  # 📂 Dossier de départ (où sont les fichiers)
tri_dir = downloads_dir / "Tri"  # 📂 Dossier où déplacer les fichiers

# ✅ Créer le dossier "Tri" s'il n'existe pas
tri_dir.mkdir(parents=True, exist_ok=True)

# 🔹 Récupérer la liste des fichiers dans "Downloads"
files = [f for f in downloads_dir.iterdir() if f.is_file()]

for f in files:
    # 📂 Déplacer le fichier dans "Tri"
    destination = tri_dir / f.name
    shutil.move(str(f), str(destination))  

    # 🔹 Déterminer la catégorie en fonction de l'extension du fichier
    output_dir = tri_dir / dirs.get(f.suffix.lower(), "Autres")
    output_dir.mkdir(exist_ok=True)  # Créer le dossier si nécessaire

    # 📂 Déplacer le fichier dans le bon sous-dossier
    destination.rename(output_dir / f.name)

print("✅ Tous les fichiers ont été déplacés et triés !")
