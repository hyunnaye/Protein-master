from Controller import ProteinSystem
from UseCases import DnaManager, RnaManager
import presenter

if __name__ == '__main__':
    dm = DnaManager()
    rm = RnaManager()
    ps = ProteinSystem(dm, rm)

    while True:
        choice = presenter.menu_prompt()
        if choice == 1:
            print(ps.dna_pairing())
        elif choice == 2:
            print(ps.get_mrna())
        elif choice == 3:
            print(ps.get_protein())
        else:
            print(presenter.print_invalid())
