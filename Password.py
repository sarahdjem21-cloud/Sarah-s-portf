import random
import string

def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

# Programme principal
print("🔐 Générateur de mot de passe")

try:
    longueur = int(input("Choisis la longueur du mot de passe : "))
    mdp = generer_mot_de_passe(longueur)
    print("Ton mot de passe sécurisé :", mdp)
except:
    print("Erreur : entre un nombre valide.")