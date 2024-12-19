""" Tic-Tac-Toe """
import time

class TicTacToe:
    def __init__(self) -> None:
        """Constructor for the tic-tac-toe game
        """
        self.__table = [[" " for _ in range(3)] for _ in range(3)]
        self.__avalable_slots = list(range(0, 9))
        self.__time_played = time.localtime()

    def __str__(self) -> str:
        """a method that displays something

        Returns:
            str: a string representation of somethings
        """
        # return str(self.__table)
        return str(self.toJSON())
    
    def toJSON(self) -> dict:
        """a method that converts python object to json object

        Returns:
            dict: json object/ python dictionary
        """
        def json(t: time.struct_time):
            return {
                "date": f"{t.tm_mon}/{t.tm_mday}/{t.tm_year}",
                "time": f"{t.tm_hour}: {t.tm_min}: {t.tm_sec}"
            }
        return {
            "table": self.__table,
            "available_slots": self.__avalable_slots,
            "time_played": json(self.__time_played),
        }
    
    def getBoard(self) -> list[list]:
        """a method that gets the table of the game

        Returns:
            list[list]: a table represented as a 2d array
        """
        return self.__table
    
    def getAvaSlots(self) -> list[int]:
        """a method that gets the available slots in the board

        Returns:
            list[list]: a list of available slots identities in the board
        """
        return self.__avalable_slots
    
    def getTime(self) -> time.strptime:
        """a method that return the time in which the match is played

        Returns:
            time.strptime: the 
        """
        return self.__time_played
    
    def clearBoard(self) -> None:
        """a method that clears the board
        """
        self.__table = [[" " for _ in range(3)] for _ in range(3)]
        self.__avalable_slots = list(range(0, 9))
    
    def validate(self, ins: int) -> bool:
        """a method that checks if a slot is empty or occupied

        Args:
            ins (int): the slot in which the choice is plotted

        Returns:
            bool: a boolean that corresponds wether permits or prohibits the newly inserted choice to be plot
        """
        if ins in self.__avalable_slots:
            return True
        return False
    
    def isTie(self) -> bool:
        """a mehtod that evaluates if the verdict of the game is tie

        Returns:
            bool: true if tie false if there is a winner
        """
        if len(self.__avalable_slots) == 0:
            return True
        return False
    
    def __occupy(self, ins: int) -> None:
        """a method that declares the plotted slot on the table

        Args:
            ins (int): the slot in which the choice is plotted
        """
        self.__avalable_slots = [num for num in self.__avalable_slots if num != ins]
    
    def insert(self, ins: int, turn: str = "player") -> None:
        """an insertion method that inserts a symbol that corresponds to whom is in turn

        Args:
            ins (int): the slot in which the choice is plotted
            turn (str, optional): a selector for the programmer to determine. Defaults to "player"or"Ai".

        Returns:
            _type_: _description_
        """
        if turn == "player":
            if ins in range(0, 3):
                self.__table[0][ins] = "X"
            elif ins in range(3, 6):
                self.__table[1][ins-3] = "X"
            elif ins in range(6, 9):
                self.__table[2][ins-6] = "X"

        else:
            if ins in range(0, 3):
                self.__table[0][ins] = "O"
            elif ins in range(3, 6):
                self.__table[1][ins-3] = "O"
            elif ins in range(6, 9):
                self.__table[2][ins-6] = "O"
        self.__occupy(ins)
        
    def decision(self) -> str:
        """a method that decides who is the winner of the game

        Returns:
            str: the symbol of the winner
        """
        tab = self.__table

        for row in tab:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        
        for col in range(3):
            if tab[0][col] == tab[1][col] == tab[2][col] and tab[0][col] != " ":
                return tab[0][col]
        
        if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] != " ":
            return tab[0][0]
        
        if tab[0][2] == tab[1][1] == tab[2][0] and tab[0][2] != " ":
            return tab[0][2]
        
        else:
            return 0 # This is if there is no winner yet OR Tie
        
    def present(self) -> str:
        """a method that displays the table in tabulation

        Returns:
            str: a string representation of the tabulated tic-tac-toe table
        """
        tab = self.__table
        label = "\n<--Table-->"
        display = ""
        j = 0
        for row in tab:
            i = 0
            for slot in row:
                display += '|' + slot if i < 2 else '|' + slot + '|'
                i += 1
            i = 0
            j += 1
            display += '\n' if j < 3 else ''
        return label + '\n' + display + label

# T = TicTacToe()
# # T.insert(0, "Ai")
# # T.insert(1, "Ai")
# # T.insert(2, "Ai")
# # T.insert(3)
# # T.insert(4)
# # T.insert(5)
# # T.insert(6, "Ai")
# # T.insert(7, "Ai")
# # T.insert(8, "Ai")
# print(T.getBoard())
# print(T.decision())
# print(T.present())

# T = TicTacToe()
# print(T)