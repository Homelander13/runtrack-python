def CESSSAR(message, decalage):
    resultat = ""

    for char in message:
        if char.isalpha():
            majuscule = char.isupper()
            char = char.lower()

            char_decale = chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))

            if majuscule:
                char_decale = char_decale.upper()

            resultat += char_decale
        else:
            resultat += char

    return resultat


message_original = "TRIPLE MONSTRE"
decalage = 3
message_chiffre = CESSSAR(message_original, decalage)

print("Message original:", message_original)
print("Message chiffré:", message_chiffre)
