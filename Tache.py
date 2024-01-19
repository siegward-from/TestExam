class Tache:
    def __init__(self, nom, description, duree):
        self.nom = nom
        self.description = description
        self.duree = duree
        

def calculer_duree_totale(taches):
    if any(tache.duree < 0 for tache in taches):
        raise ValueError("La durée ne peut pas être négative")
    return sum(tache.duree for tache in taches)