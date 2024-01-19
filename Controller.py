class Controller:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def lister_taches(self):
        return self.taches

    def obtenir_tache(self, nom):
        for tache in self.taches:
            if tache.nom == nom:
                return tache
        return None