from Entities import Dna, Rna
import Presenter

codon_table = {
    'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
    'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': 'Stop', 'UGA': 'Stop',
    'UUG': 'Leu', 'UCG': 'Ser', 'UAG': 'Stop', 'UGG': 'Trp',
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
    'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
    'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
    'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
    'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
    'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
    'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly',
}


class DnaManager:
    _dna_pairs: dict
    _dna_rna_pairs: dict

    def __init__(self, dna_pair=None, rna_pair=None):
        if rna_pair is None:
            rna_pair = {}
        if dna_pair is None:
            dna_pair = {}
        self._dna_pairs = dna_pair
        self._dna_rna_pairs = rna_pair

    def find_dna_pair(self, dna_sequence: str) -> str:
        dna = Dna(dna_sequence)
        pair_seq = ''
        for base in dna_sequence:
            if base in ['T', 't']:
                pair_seq += 'A'
            elif base in ['A', 'a']:
                pair_seq += 'T'
            elif base in ['C', 'c']:
                pair_seq += 'G'
            elif base in ['G', 'g']:
                pair_seq += 'C'
            else:
                return dna_sequence
        pair = Dna(pair_seq)
        self._dna_pairs[pair] = dna
        return pair.get_sequence()

    def dna_to_rna_(self, dna_sequence: str) -> str:
        dna = Dna(dna_sequence)
        rna_sequence = ''
        for base in dna_sequence:
            if base in ['T', 't']:
                rna_sequence += 'A'
            elif base in ['A', 'a']:
                rna_sequence += 'U'
            elif base in ['C', 'c']:
                rna_sequence += 'G'
            elif base in ['G', 'g']:
                rna_sequence += 'C'
            else:
                return "Invalid input"
        self._dna_rna_pairs[dna] = rna_sequence
        return rna_sequence

    def get_dna_pairs(self) -> dict:
        return self._dna_pairs

    def get_dna_rna_pairs(self) -> dict:
        return self._dna_rna_pairs


class RnaManager:
    _rna_dna_pairs: dict
    _codon_table: dict
    _rna_protein_pairs: dict

    def __init__(self, rna_dna_pairs=None, rna_protein_pairs=None):
        if rna_dna_pairs is None:
            self._rna_dna_pairs = {}
        if rna_protein_pairs is None:
            self._rna_protein_pairs = {}
        self._codon_table = codon_table

    def rna_to_dna_pair(self, rna_sequence: str) -> str:
        rna = Rna(rna_sequence)
        dna_sequence = ''
        for base in rna_sequence:
            if base in ['U', 'u']:
                dna_sequence += 'A'
            elif base in ['A', 'a']:
                dna_sequence += 'T'
            elif base in ['C', 'c']:
                dna_sequence += 'G'
            elif base in ['G', 'g']:
                dna_sequence += 'C'
            else:
                return "Invalid input"
        self._rna_dna_pairs[rna] = dna_sequence
        return dna_sequence

    def rna_to_protein(self, rna_sequence: str) -> str:
        rna = Rna(rna_sequence)
        proteinlist = []
        if len(rna_sequence) % 3 == 0:
            for letter in rna_sequence:
                if letter not in ['A', 'C', 'G', 'U']:
                    return "Invalid input"
            for i in range(0, len(rna_sequence), 3):
                codon = rna_sequence[i:i + 3]
                proteinlist.append(codon_table[codon])
            protein = '-'.join(proteinlist)
            self._rna_protein_pairs[rna] = proteinlist
            return protein
        else:
            return "Failed: Sequence not divisible by 3."

