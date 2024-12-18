from TTT import TicTacToe
from Ai import Ai

MENUS = {
    'main': {
        0: "Exit",
        1: "Play Tic-Tac-Toe"
    },
    'again': {
        0: "Yes",
        1: "No"
    }
}

def showMenu(menu: dict, m: str):
    """a function that shows options

    Args:
        menu (dict): the dictionary of options
        m (str): the key to specific options
    """
    M: dict = menu[m]
    print()
    for k, v in M.items():
        print(f'({k}): {v}')

def cont() -> int:
    """a function that prompts the user to play again or not

    Returns:
        int: a specific selector
    """
    while True:
        showMenu(MENUS, 'again')
        opt = input('\nEnter choice: ')
        if opt == "0":
            T.clearBoard()
            return 0
        elif opt == "1":
            print('\nReturning to main...')
            return 1
        else:
            print('\nInvalid input!')
            continue

if __name__ == '__main__':
    T = TicTacToe()
    AI = Ai()

    while True:
        showMenu(MENUS, 'main')
        inp = input("\nEnter choice: ")
        if inp == '0':
            print('\nClosing program...')
            break
        
        elif inp == "1":
            while True:
                print(T.present())
                sl = input('\nInser in slot(1 - 9) ("q" to quit): ')
                if sl == "q":
                    print("\nReturning to main...")
                    T.clearBoard()
                    break

                try:
                    sl = int(sl) - 1
                    if type(T.decision()) != str and T.validate(sl):
                        T.insert(sl)
                        T.insert(AI.pick_choice(T.getAvaSlots()), "Ai")

                        if type(T.decision()) == str:
                            print(T.present())
                            winner = "Player" if T.decision() == "X" else "Ai"
                            print(f"\nThe winner is {winner}!")

                            c = cont()
                            if c == 0:
                                continue
                            else:
                                break
                        
                        if T.isTie():
                            print(T.present())
                            print("\nTied")

                            c = cont()
                            if c == 0:
                                continue
                            else:
                                break

                except ValueError:
                    print('\nInput valid value')

        else:
            print('\nInvalid Input!')

                    