def arrondir_notes(liste_notes):
    return [note + (5 - (note % 5)) if note >= 40 and (5 - (note % 5)) < 3 else note for note in liste_notes]


notes_originales = [83, 40, 83, 73, 23]
notes_arrondies = arrondir_notes(notes_originales)
print("Notes originales:", notes_originales)
print("Notes arrondies:", notes_arrondies)

