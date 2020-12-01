def print_invalid() -> str:
    return "Invalid input"


def ask_dna_input() -> str:
    return input("Input DNA sequence you would like to "
                 "find the DNA pair of \n")


def menu_prompt() -> int:
    return int(
        input("Enter the number of which action you would like to perform \n"
              "1. Find matching DNA pair \n"
              "2. Find matching mRNA sequence \n"
              "3. Get polypeptide chain of DNA sequence \n"))
