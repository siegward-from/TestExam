class GestionTaches:
    def __init__(self):
        self.taches = {}

    def ajouter_tache(self, titre, description):
        if titre not in self.taches:
            self.taches[titre] = {'description': description, 'complete': False}

    def completer_tache(self, titre):
        if titre in self.taches:
            self.taches[titre]['complete'] = True
        else:
            raise ValueError("Tâche non trouvée")

    def verifier_tache(self, titre):
        if titre in self.taches:
            return self.taches[titre]['complete']
        else:
            raise ValueError("Tâche non trouvée")

