from typing import List
from Client import Client

from Intervention import Intervention

class Contrat:
    def __init__(self, numero: int, date: str, client: Client, montantContrat: float, intervention: List ):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions: List[Intervention] = []
        self.nbIntervention = 0
    
    def montant(self) -> float:
        return self.montantContrat
    
    def ecart(self) -> float:
        cout_interventions = sum(intervention.fraisMo() + intervention.fraisKm(self.client.distance())
                                 for intervention in self.interventions)
        return self.montantContrat - cout_interventions
