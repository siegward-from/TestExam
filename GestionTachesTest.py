import unittest
from GestionTaches import GestionTaches

class GestionTachesTest(unittest.TestCase):

    def setUp(self):
        self.gestion = GestionTaches()

    def test_ajouter_tache(self):
        self.gestion.ajouter_tache("Tache1", "Description1")
        self.assertIn("Tache1", self.gestion.taches)
        self.assertFalse(self.gestion.taches["Tache1"]["complete"])

    def test_completer_tache_existante(self):
        self.gestion.ajouter_tache("Tache1", "Description1")
        self.gestion.completer_tache("Tache1")
        self.assertTrue(self.gestion.taches["Tache1"]["complete"])

    def test_completer_tache_inexistante(self):
        with self.assertRaises(ValueError):
            self.gestion.completer_tache("TacheInexistante")

    def test_verifier_tache_existante(self):
        self.gestion.ajouter_tache("Tache1", "Description1")
        self.assertFalse(self.gestion.verifier_tache("Tache1"))
        self.gestion.completer_tache("Tache1")
        self.assertTrue(self.gestion.verifier_tache("Tache1"))

    def test_verifier_tache_inexistante(self):
        with self.assertRaises(ValueError):
            self.gestion.verifier_tache("TacheInexistante")

if __name__ == '__main__':
    unittest.main()
