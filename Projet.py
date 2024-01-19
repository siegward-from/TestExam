class Projet:
    def __init__(self, nom, gestion_taches):
        self.nom = nom
        self.taches = []
        self.gestion_taches = gestion_taches

    def ajouter_tache(self, titre, description):
        self.taches.append(titre)
        self.gestion_taches.ajouter_tache(titre, description)

    def completer_tache(self, titre):
        if titre in self.taches:
            self.gestion_taches.completer_tache(titre)
        else:
            raise ValueError("Tâche non trouvée dans le projet")