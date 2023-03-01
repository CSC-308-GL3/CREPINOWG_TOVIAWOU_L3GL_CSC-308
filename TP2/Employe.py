from datetime import date
from typing import List

from Grade import Grade

class Employe:
    def __init__(self, numero: int, nom: str, qualification: Grade, dateEmbauche: str):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = dateEmbauche
    
    def coutHoraire(self) -> float:
        anciennete = self.getAnciennete(self.dateEmbauche)
        coefficient = 1.0
        if anciennete >= 5 and anciennete <= 10:
            coefficient = 1.05
        elif anciennete > 10 and anciennete <= 15:
            coefficient = 1.08
        elif anciennete > 15:
            coefficient = 1.12
        return self.qualification.tauxHoraire() * coefficient
    
    def getNumero(self) -> int:
        return self.numero
    
    def getNom(self) -> str:
        return self.nom
    
    def getQualification(self) -> Grade:
        return self.qualification
    
    def getDateEmbauche(self) -> str:
        return self.dateEmbauche
    
    def getAnciennete(self, date: str) -> int:
        annee_embauche = int(date[:4])
        mois_embauche = int(date[5:7])
        jour_embauche = int(date[8:])
        date_embauche = date(annee_embauche, mois_embauche, jour_embauche)
        today = date.today()
        anciennete = today.year - date_embauche.year - ((today.month, today.day) < (date_embauche.month, date_embauche.day))
        return anciennete
