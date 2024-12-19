from TTT import TicTacToe
from Ai import Ai
import json

MENUS = {
    'main': {
        0: "Exit",
        1: "Play Tic-Tac-Toe",
        2: "History"
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
            T.clearBoard()
            print('\nReturning to main...')
            return 1
        else:
            print('\nInvalid input!')
            continue

def write(ttt: 'TicTacToe', winner: str) -> None:
    info = ttt.toJSON()
    info["winner"] = winner
    history = read()

    history.append(info)

    with open("history.json", "w") as f:
        json.dump(history, f, indent=1)

def read() -> list:
    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        history = []

    return history

if __name__ == '__main__':
    T = TicTacToe()
    AI = Ai()
    con = '\nContinue?'

    while True:
        print('\n<-----Tic_Tac_Toe Game----->')
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
                            winner = "PLAYER" if T.decision() == "X" else "AI"
                            print(f"\n*****The winner is {winner}!*****")

                            write(T, winner)

                            print(con)
                            c = cont()
                            if c == 0:
                                continue
                            else:
                                break
                        
                        if T.isTie():
                            print(T.present())
                            print("\n*****TIED*****")

                            write(T, "ai")

                            print(con)
                            c = cont()
                            if c == 0:
                                continue
                            else:
                                break

                except ValueError:
                    print('\nInput valid value')
        elif inp == "2":
            print('\nOn progress...')
            pass

        else:
            print('\nInvalid Input!')

                    