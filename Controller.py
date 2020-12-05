from UseCases import DnaManager, RnaManager
import Presenter


class ProteinSystem:

    _dm: DnaManager()
    _rm: RnaManager()

    def __init__(self, dm, rm):
        self._dm = dm
        self._rm = rm

    def dna_pairing(self, sequence) -> str:
        return self._dm.find_dna_pair(sequence)

    def get_mrna(self, sequence) -> str:
        return self._dm.dna_to_rna_(sequence)

    def get_protein(self, sequence) -> str:
        sequence = sequence.upper()
        if self._dm.dna_to_rna_(sequence) != Presenter.print_invalid():
            mrna = self._dm.dna_to_rna_(sequence)
            return self._rm.rna_to_protein(mrna)
        return Presenter.print_invalid()

    def get_dna(self, sequence) -> str:
        return self._rm.rna_to_dna_pair(sequence)







