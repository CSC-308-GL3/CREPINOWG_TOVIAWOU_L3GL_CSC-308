# Importation des classes nécessaires
from Client import Client
from Employe import Employe
from Intervention import Intervention
from Contrat import Contrat

# Création d'un employé
employe = Employe(1,"Dupont", "Jean", 25)

# Création d'un client
client = Client(1,"Martin", "123 rue de la Paix","04BP405","Lomé","15")

# Création d'une intervention pour cet employé et ce client
intervention1 = Intervention(1, "01/01/2023", 3, 0.5, employe)
intervention2 = Intervention(2, "02/01/2023", 2, 0.5, employe)

# Création d'un contrat pour ce client avec ces interventions
#contrat = Contrat(1, "01/01/2023", client, 500, [intervention1], 2)

# Calcul de l'écart entre le montant du contrat et le coût des interventions effectuées par l'employé
#ecart = contrat.ecart()

# Affichage de l'écart
#print("L'écart entre le montant du contrat et le coût des interventions est de", ecart, "euros.")
