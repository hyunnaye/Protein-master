def print_invalid() -> str:
    """Presenter method in Clean Architecture for printing Invalid Input
    :return invalid input string"""
    return "Invalid input"


def print_invalid_seq1() -> str:
    """Presenter method in Clean Architecture for printing Invalid Input
    :return invalid input string"""
    return "Invalid input for 1st sequence"


def print_invalid_seq2() -> str:
    """Presenter method in Clean Architecture for printing Invalid Input
    :return invalid input string"""
    return "Invalid input for 2nd sequence"


def print_sequence_max() -> str:
    return 'At the moment this program only supports sequence ' \
           'lengths up to 70'


def ask_dna_input() -> str:
    """Presenter method in Clean Architecture for asking for DNA Input
    :return input DNA sequence string"""
    return input("Input DNA sequence")


def ask_rna_input() -> str:
    """Presenter method in Clean Architecture for asking for RNA Input
    :return input RNA sequence string"""
    return input("Input RNA sequence")
