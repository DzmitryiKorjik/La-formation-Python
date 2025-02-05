def get_note(note):
    if note >= 15:
        return "Excellent"
    elif note >= 10:
        return "Bon travail"
    elif note >= 5:
        return "Attention !"
    else:
        return "C'est un sans faute !"
    
note = int(input("Entrez une note : "))

commentaire = get_note(note)

print(f"La note {note} correspond à {commentaire}")