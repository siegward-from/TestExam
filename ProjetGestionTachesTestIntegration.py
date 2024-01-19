import unittest
from GestionTaches import GestionTaches
from Projet import Projet


class ProjetGestionTachesTestIntegration(unittest.TestCase):

    def setUp(self):
        self.gestion_taches = GestionTaches()
        self.projet = Projet("Projet Test", self.gestion_taches)

    def test_ajout_tache(self):
        self.projet.ajouter_tache("Tache1", "Description de Tache1")
        self.assertIn("Tache1", self.projet.taches)
        self.assertIn("Tache1", self.gestion_taches.taches)

    def test_completer_tache(self):
        self.projet.ajouter_tache("Tache2", "Description de Tache2")
        self.projet.completer_tache("Tache2")
        self.assertTrue(self.gestion_taches.verifier_tache("Tache2"))

    def test_ajout_tache_non_existante(self):
        with self.assertRaises(ValueError):
            self.projet.completer_tache("Tache Inexistante")

if __name__ == "__main__":
    unittest.main()