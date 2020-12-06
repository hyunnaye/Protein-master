def print_invalid() -> str:
    """Presenter method in Clean Architecture for printing Invalid Input
    :return invalid input string"""
    return "Invalid input"


def ask_dna_input() -> str:
    """Presenter method in Clean Architecture for asking for DNA Input
    :return input DNA sequence string"""
    return input("Input DNA sequence")


def ask_rna_input() -> str:
    """Presenter method in Clean Architecture for asking for RNA Input
    :return input RNA sequence string"""
    return input("Input RNA sequence")
