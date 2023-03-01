from datetime import date
from typing import List


class Grade:
    def __init__(self, code: str, libelle: str, taux: float):
        self.code = code
        self.libelle = libelle
        self.taux = taux
    
    def getCode(self) -> str:
        return self.code
    
    def getLibelle(self) -> str:
        return self.libelle
    
    def tauxHoraire(self) -> float:
        return self.taux