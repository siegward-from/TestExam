import unittest
from Controller import Controller
from Tache import Tache

class ControllerTest(unittest.TestCase):

    def setUp(self):
        self.controleur = Controller()
        self.controleur.ajouter_tache(Tache("Tache1", "Description de Tache1", 1))
        self.controleur.ajouter_tache(Tache("Tache2", "Description de Tache2", 2))

    def test_ajout_tache(self):
        tache3 = Tache("Tache3", "Description de Tache3", 3)
        self.controleur.ajouter_tache(tache3)
        self.assertIn(tache3, self.controleur.taches)

    def test_lister_taches(self):
        taches = self.controleur.lister_taches()
        self.assertEqual(len(taches), 2)
        self.assertIsInstance(taches[0], Tache)

    def test_obtenir_tache_existante(self):
        tache = self.controleur.obtenir_tache("Tache1")
        self.assertIsNotNone(tache)
        self.assertEqual(tache.nom, "Tache1")
        self.assertEqual(tache.description, "Description de Tache1")

    def test_obtenir_tache_inexistante(self):
        tache = self.controleur.obtenir_tache("TacheInconnue")
        self.assertIsNone(tache)

if __name__ == '__main__':
    unittest.main()
