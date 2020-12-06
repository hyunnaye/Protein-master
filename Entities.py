class Dna:
    _sequence: str

    def __init__(self, sequence):
        self.sequence = sequence

    """Getter for DNA sequence
    :return DNA sequence"""
    def get_sequence(self) -> str:
        return self.sequence


class Rna:
    _sequence: str

    def __init__(self, sequence):
        self.sequence = sequence

    """Getter for RNA sequence
    :return RNA sequence"""
    def get_sequence(self) -> str:
        return self.sequence


