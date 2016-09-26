from unittest import TestCase
from PyPDBe.PDBe_module import PyPDBe

#TODO sprawdzac zwracanie konkretnych wartosci

class PDBeTest(TestCase):

    def test_get_summary(self):
        p = PyPDBe()
        self.assertTrue(p.get_summary('2ce3'))
        self.assertTrue(p.get_summary('2CE3'))
        self.assertIsNone(p.get_summary('asdasdasd'))
        self.assertIsNone(p.get_summary('2'))
        self.assertIsNone(p.get_summary(''))

    def test_get_molecules(self):
        p = PyPDBe()
        self.assertTrue(p.get_molecules('2ce3'))
        self.assertTrue(p.get_molecules('2CE3'))
        self.assertIsNone(p.get_molecules('asdasdasd'))
        self.assertIsNone(p.get_molecules('2'))
        self.assertIsNone(p.get_molecules(''))

    def test_get_publications(self):
        p = PyPDBe()
        self.assertTrue(p.get_publications('2ce3'))
        self.assertTrue(p.get_publications('2CE3'))
        self.assertIsNone(p.get_publications('asdasdasd'))
        self.assertIsNone(p.get_publications('2'))
        self.assertIsNone(p.get_publications(''))

    # TODO test_get_related_publications

    def test_get_experiment(self):
        p = PyPDBe()
        self.assertTrue(p.get_experiment('2ce3'))
        self.assertTrue(p.get_experiment('2CE3'))
        self.assertIsNone(p.get_experiment('asdasdasd'))
        self.assertIsNone(p.get_experiment('2'))
        self.assertIsNone(p.get_experiment(''))

    def test_get_NMR_resources(self):
        p = PyPDBe()
        self.assertTrue(p.get_NMR_resources('2k8v'))
        self.assertTrue(p.get_NMR_resources('2k7v'))
        self.assertIsNone(p.get_NMR_resources('asdasdasd'))
        self.assertIsNone(p.get_NMR_resources('2'))
        self.assertIsNone(p.get_NMR_resources(''))

    def test_get_ligands(self):
        p = PyPDBe()
        self.assertTrue(p.get_ligands('1cbs'))
        self.assertIsNone(p.get_ligands('asdasdasd'))
        self.assertIsNone(p.get_ligands('2'))
        self.assertIsNone(p.get_ligands(''))

    def test_get_modified_residues(self):
        p = PyPDBe()
        self.assertTrue(p.get_modified_residues('4v5j'))
        self.assertTrue(p.get_modified_residues('4V5J'))
        self.assertIsNone(p.get_modified_residues('asdasdasd'))
        self.assertIsNone(p.get_modified_residues('2'))
        self.assertIsNone(p.get_modified_residues(''))

    def test_get_mutated_residues(self):
        p = PyPDBe()
        self.assertTrue(p.get_mutated_residues('4v5j'))
        self.assertTrue(p.get_mutated_residues('4V5J'))
        self.assertIsNone(p.get_mutated_residues('asdasdasd'))
        self.assertIsNone(p.get_mutated_residues('2'))
        self.assertIsNone(p.get_mutated_residues(''))
        #TODO check - test fails

    def test_get_release_status(self):
        p = PyPDBe()
        self.assertTrue(p.get_release_status('1cbs'))
        self.assertTrue(p.get_release_status('1CBS'))
        self.assertIsNone(p.get_release_status('asdasdasd'))
        self.assertIsNone(p.get_release_status('2'))
        self.assertIsNone(p.get_release_status(''))

    def test_get_observed_ranges(self):
        p = PyPDBe()
        self.assertTrue(p.get_observed_ranges('1cbs'))
        self.assertTrue(p.get_observed_ranges('1CBS'))
        self.assertIsNone(p.get_observed_ranges('asdasdasd'))
        self.assertIsNone(p.get_observed_ranges('2'))
        self.assertIsNone(p.get_observed_ranges(''))

    def test_get_observed_ranges_in_chain(self):
        p = PyPDBe()
        self.assertTrue(p.get_observed_ranges('1cbs', 'A'))
        self.assertTrue(p.get_observed_ranges('1CBS', 'A'))
        self.assertIsNone(p.get_observed_ranges('asdasdasd', 'asdadas'))
        self.assertIsNone(p.get_observed_ranges('2', '222'))
        self.assertIsNone(p.get_observed_ranges('', ''))
        # TODO check - test fails

    def test_get_secondary_structure(self):
        p = PyPDBe()
        self.assertTrue(p.get_secondary_structure('1cbs'))
        self.assertTrue(p.get_secondary_structure('1CBS'))
        self.assertIsNone(p.get_secondary_structure('asdasdasd'))
        self.assertIsNone(p.get_secondary_structure('2'))
        self.assertIsNone(p.get_secondary_structure(''))

    def test_get_residues(self):
        p = PyPDBe()
        self.assertTrue(p.get_residues('1cbs'))
        self.assertTrue(p.get_residues('1CBS'))
        self.assertIsNone(p.get_residues('asdasdasd'))
        self.assertIsNone(p.get_residues('2'))
        self.assertIsNone(p.get_residues(''))

    def test_get_residues_for_chain(self):
        p = PyPDBe()
        self.assertTrue(p.get_residues('1cbs', 'A'))
        self.assertTrue(p.get_residues('1CBS', 'A'))
        self.assertIsNone(p.get_residues('asdasdasd', 'asdadas'))
        self.assertIsNone(p.get_residues('2', '222'))
        self.assertIsNone(p.get_residues('', ''))
        #TODO check - test fails

    def test_get_binding_sites(self):
        p = PyPDBe()
        self.assertTrue(p.get_binding_sites('1cbs'))
        self.assertTrue(p.get_binding_sites('1CBS'))
        self.assertIsNone(p.get_binding_sites('asdasdasd'))
        self.assertIsNone(p.get_binding_sites('2'))
        self.assertIsNone(p.get_binding_sites(''))

    def test_get_files(self):
        p = PyPDBe()
        self.assertTrue(p.get_files('1cbs'))
        self.assertTrue(p.get_files('1CBS'))
        self.assertIsNone(p.get_files('asdasdasd'))
        self.assertIsNone(p.get_files('2'))
        self.assertIsNone(p.get_files(''))

    def test_get_observed_residues_ratio(self):
        p = PyPDBe()
        self.assertTrue(p.get_observed_residues_ratio('1cbs'))
        self.assertTrue(p.get_observed_residues_ratio('1CBS'))
        self.assertIsNone(p.get_observed_residues_ratio('asdasdasd'))
        self.assertIsNone(p.get_observed_residues_ratio('2'))
        self.assertIsNone(p.get_observed_residues_ratio(''))

    # TODO test_get_assembly
