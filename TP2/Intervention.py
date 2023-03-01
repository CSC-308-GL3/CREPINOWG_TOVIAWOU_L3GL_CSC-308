from datetime import date
from typing import List

from Employe import Employe



class Intervention:
    def __init__(self, numero: int, date: str, duree: int, tarifKm: float, technicien: Employe):
        self.numero = numero
        self.date = date
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien
    
    def affiche(self) -> None:
        print(f"Intervention n°{self.numero}")
        print(f"Date: {self.date}")
        print(f"Durée: {self.duree} heures")
        print(f"Tarif kilométrique retenu: {self.tarifKm} €/km")
        print(f"Technicien: {self.__technicien.getNom()}")
    
    def fraisKm(self, dist: float) -> float:
        return self.__tarifKm * dist
    
    def fraisMo(self) -> float:
        return self.__technicien.coutHoraire() * self.__duree
