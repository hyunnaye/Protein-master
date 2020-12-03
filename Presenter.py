def print_invalid() -> str:
    return "Invalid input"


def ask_dna_input() -> str:
    return input("Input DNA sequence")


def ask_rna_input() -> str:
    return input("Input RNA sequence you would like to "
                 "find the DNA pair of \n")


def menu_prompt() -> int:
    return int(
        input("Enter the number of which action you would like to perform \n"
              "1. Find matching DNA pair \n"
              "2. DNA to RNA \n"
              "3. RNA to DNA\n"
              "4. Get polypeptide chain of DNA sequence \n"
              ))
