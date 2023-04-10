import random
import time


class Player:
    def __init__(self, name, score=0, current=0):
        """ initialize the player
        :param name: the player's name
        :param score: the player's score
        :param current: the player's current score
        """
        self.name = name
        self.score = score
        self.current = current

    def best_option(self):
        """
        Given its current score and total score, decide
        which option is the best, base on mathematical expectation
        and probability

        :return:
            string: 'h' for hold or 'r' for roll the dice
        """
        if self.current + self.score >= 100:
            return 'h'
        expectation = (20 - self.current) / 6
        if expectation > 0:
            return 'r'
        else:
            return 'h'


class PigGame:
    def __init__(self, player1='player1', player2='player2'):
        """
        initialize the game, including two players' names
        and the player who is rolling the dice
        :param player1: player1's name
        :param player2: player2's name
        """
        if not player1:
            self.player1 = Player('player1')
        else:
            self.player1 = Player(player1)
        if not player2:
            self.player2 = Player('player2')
        else:
            self.player2 = Player(player2)
        self.__current_player = self.player1

    def roll_num(self):
        """
        generates an integer, which >= 1 and <= 6
        It means the integer we got after rolling a die
        :return:
            integer: an integer from 1 to 6
        """
        return random.randint(1, 6)

    def dice_simulator(self, number):
        """
        Given an integer, generates the strings that can
        display a die in console. Strings are stored in a list
        :param number: number of the die
        :return:
            list: strings stored in a list, can be print to display a die
        """
        dice = ['' for _ in range(5)]
        border = "+-------+"
        dice[0] = border
        dice[4] = border
        blank_line = "|" + " " * 7 + "|"
        if number == 1 or number == 2:
            dice[1] = blank_line
            dice[3] = blank_line
            if number == 1:
                dice[2] = "|   o   |"
            else:
                dice[2] = "| o   o |"
        else:
            if number == 3:
                dice[1] = "|  o    |"
                dice[2] = "|   o   |"
                dice[3] = "|    o  |"
            else:
                dice[1] = "| o   o |"
                if number == 4:
                    dice[2] = blank_line
                elif number == 5:
                    dice[2] = "|   o   |"
                elif number == 6:
                    dice[2] = "| o   o |"
                dice[3] = "| o   o |"
        return dice

    def change_player(self):
        """
        When a player rolled a one or a player chose to hold,
        this player stopped and another player started to play
        :return: None
        """
        if self.__current_player == self.player1:
            self.__current_player = self.player2
        else:
            self.__current_player = self.player1

    def board_line(self, str1='', str2=''):
        """
        Uses score board to display the game's information, including
        scores, players' names, current scores
        the score board's width is fixed, 32
        this method can generate a line given what is displayed
        :param str1: the content needs to be displayed in the score board
        :param str2: if there are two things to be displayed in one line,
        then the second one is str2
        :return:
            string: represents a line in the score board
        """
        if str2 or str2 == 0:
            return "|" + f"{str1}".center(15) + f"{str2}".center(15) + "|"
        else:
            return "|" + f"{str1}".center(30) + "|"

    def board_simulator(self):
        """
        Uses board_line() to generate the lines that build a score board
        :return:
            list: a list of strings, can be print to display a score board
        """
        board = ['' for _ in range(8)]
        border = "+" + "-" * 30 + "+"
        board[0] = border
        board[-1] = border
        board[1] = self.board_line('Score Board')
        board[2] = self.board_line(self.player1.name, self.player2.name)
        board[3] = self.board_line(self.player1.score, self.player2.score)
        board[4] = self.board_line('')
        board[5] = self.board_line('current', 'current')
        board[6] = self.board_line(self.player1.current, self.player2.current)
        return board

    def ui_simulator(self, roll=0):
        """
        Combines dice and board to form a whole user interface
        :param roll: the number of the die
        :return:
            list: a list of strings, can be print to display the whole UI
        """
        dice = self.dice_simulator(roll)
        board = self.board_simulator()
        UI = []
        if not roll or roll == 0:
            for i in range(8):
                UI.append(board[i])
        else:
            for i in range(8):
                if i <= 2:
                    UI.append(' ' * 19 + board[i])
                else:
                    UI.append(dice[i - 3] + ' ' * 10 + board[i])
        return UI

    def display_UI(self, roll=0):
        """
        Prints the strings in the list, generated by ui_simulator,
        to display the UI
        :param roll: the number of the die
        :return: None
        """
        UI = self.ui_simulator(roll)
        for line in UI:
            print(line)

    def roll_dice(self):
        """
        Simulates the real-world roll-dice operation
        Roll a die, calculate the score, and display the game info
        :return: None
        """
        player = self.__current_player
        number = self.roll_num()
        if number == 1:
            self.change_player()
            player.current = 0
            self.display_UI(number)
            print(f"{player.name} rolled a 1. Bad luck :( Switch player!")
        else:
            player.current += number
            self.display_UI(number)
            print(f"{player.name} rolled a {number}!")

    def hold_score(self):
        """
        Simulates the real-world hold-score operation
        Adds the current score to total score, and switch player
        :return: None
        """
        player = self.__current_player
        player.score += player.current
        player.current = 0
        self.display_UI()
        if self.player1.score < 100 and self.player2.score < 100:
            print(f"{player.name} chose to hold. Switch player!")
            self.change_player()

    def get_command(self):
        """
        Gets command from the current player
        If the user is set to be AI, get command from best_option,
        which is based on mathematical expectation
        :return:
            string: a string denoting the player's command
        """
        player = self.__current_player
        if player.name == "AI" or player.name == "'AI'":
            print(f"{player.name} is thinking ...")
            time.sleep(2)
            return player.best_option()
        prompt = f"{player.name}, roll the die or hold your score?\n"
        command = input(prompt)
        if command.lower() in {'r', "roll"}:
            return 'r'
        elif command.lower() in {'h', 'hold'}:
            return 'h'
        else:
            print("Wrong command! Please type 'r' to roll or 'h' to hold.")
            return self.get_command()

    def process(self):
        """
        The game's main process. It won't stop unless a player wins
        :return:
            string: the name of the winner
        """
        self.welcome_msg()
        while self.player1.score < 100 and self.player2.score < 100:
            command = self.get_command()
            if command == 'r':
                self.roll_dice()
            elif command == 'h':
                self.hold_score()
            print('')
        player = self.__current_player
        print(f"{player.name} scores {player.score} and wins the game!")
        return player.name

    def welcome_msg(self):
        """
        Prints welcome and help message
        :return: None
        """
        name1 = self.player1.name
        name2 = self.player2.name
        msg = f"welcome, {name1} and {name2}! Let's start play!"
        helper = "type 'r' to roll the die, 'h' to hold your score."
        print('')
        print(msg)
        print(helper)
        print('')


def run():
    """
    Prints help information and runs the game
    :return: None
    """
    print("Please input player's name to start")
    name1 = input("Please enter player1's name ")
    print('')
    print("Let player2's name be 'AI' if you want to play with AI")
    name2 = input("Please enter player2's name ")
    game = PigGame(name1, name2)
    game.process()


def main():
    run()


if __name__ == "__main__":
    main()
