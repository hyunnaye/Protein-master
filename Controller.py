from UseCases import DnaManager, RnaManager, ProteinManager
import Presenter


class ProteinSystem:

    _dm: DnaManager()
    _rm: RnaManager()
    _pm: ProteinManager()

    def __init__(self, dm, rm, pm):
        self._dm = dm
        self._rm = rm
        self._pm = pm

    def dna_pairing(self, sequence) -> str:
        """Acts in the Controller method in Clean Architecture to find
        complementary DNA pair of a given DNA sequence.

        :param sequence: DNA sequence input
        :return Complementary DNA sequence"""
        return self._dm.find_dna_pair(sequence)

    def get_mrna(self, sequence) -> str:
        """Acts in the Controller method in Clean Architecture to find
        complementary RNA pair of a given DNA sequence.

        :param sequence: DNA sequence input
        :return Complementary RNA sequence"""
        return self._dm.dna_to_rna_(sequence)

    def get_protein(self, sequence) -> str:
        """Acts in the Controller method in Clean Architecture to find
        the protein chain of a given RNA sequence.

        :param sequence: RNA sequence input
        :return matching protein chain"""
        sequence = sequence.upper()
        if self._dm.dna_to_rna_(sequence) != Presenter.print_invalid():
            mrna = self._dm.dna_to_rna_(sequence)
            return self._rm.rna_to_protein(mrna)
        return Presenter.print_invalid()

    def get_dna(self, sequence) -> str:
        """Acts in the Controller method in Clean Architecture to find
        complementary DNA pair of a given RNA sequence.

        :param sequence: RNA sequence input
        :return Complementary DNA sequence"""
        return self._rm.rna_to_dna_pair(sequence)

    def compare_dna(self, seq1, seq2) -> str:
        if len(seq1) > 70 or len(seq2) > 70:
            return Presenter.print_sequence_max()
        if not self._dm.valid_dna_seq(seq1):
            return Presenter.print_invalid_seq1()
        if not self._dm.valid_dna_seq(seq2):
            return Presenter.print_invalid_seq2()
        return self._align_helper(seq1, seq2)

    def compare_rna(self, seq1, seq2) -> str:
        if len(seq1) > 70 or len(seq2) > 70:
            return Presenter.print_sequence_max()
        if not self._rm.valid_rna_seq(seq1):
            return Presenter.print_invalid_seq1()
        if not self._rm.valid_rna_seq(seq2):
            return Presenter.print_invalid_seq2()
        return self._align_helper(seq1, seq2)

    def compare_protein(self, seq1, seq2) -> str:
        if len(seq1) > 70 or len(seq2) > 70:
            return Presenter.print_sequence_max()
        if not self._pm.valid_protein_sequence(seq1):
            return Presenter.print_invalid_seq1()
        if not self._pm.valid_protein_sequence(seq2):
            return Presenter.print_invalid_seq2()
        return self._align_helper(seq1, seq2)

    def _align_helper(self, seq1, seq2) -> str:
        mismatches = ''
        if seq1 <= seq2:
            for i in range(len(seq1)):
                if seq1[i] != seq2[i]:
                    mismatches += '|'
                else:
                    mismatches += ' '
        else:
            for i in range(len(seq2)):
                if seq1[i] != seq2[i]:
                    mismatches += '|'
                else:
                    mismatches += ' '
        return mismatches
