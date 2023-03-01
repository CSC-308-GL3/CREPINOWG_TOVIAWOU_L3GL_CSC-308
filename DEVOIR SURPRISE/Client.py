from datetime import date
from typing import List

class Client:
    def __init__(self, numero: int, nom: str, adresse: str, codePostale: str, ville: str, nbKm: int):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostale = codePostale
        self.ville = ville
        self.nbKm = nbKm
    
    def distance(self) -> float:
        # La distance en kilomètres qui sépare le site du client de la société
        return float(self.nbKm)