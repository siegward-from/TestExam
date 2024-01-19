import unittest

from Tache import Tache, calculer_duree_totale

class CalculerDureeTotaleTest(unittest.TestCase):

    def test_liste_vide(self):
        self.assertEqual(calculer_duree_totale([]), 0)

    def test_durees_positives(self):
        taches = [Tache(1), Tache(2), Tache(3)]
        self.assertEqual(calculer_duree_totale(taches), 6)

    def test_durees_negatives(self):
        taches = [Tache(1), Tache(-1), Tache(2)]
        with self.assertRaises(ValueError):
            calculer_duree_totale(taches)

if __name__ == "__main__":
    unittest.main()