from pig_dice_game import Player, PigGame
import unittest


class TestPlayer(unittest.TestCase):
    def test_best_option(self):
        """
        Tests whether best_option can make the correct decision
        """
        player1 = Player('p1', 50, 25)
        player2 = Player('p2', 30, 19)
        player3 = Player('p3', 87, 14)
        self.assertEqual(player1.best_option(), 'h')
        self.assertEqual(player2.best_option(), 'r')
        self.assertEqual(player3.best_option(), 'h')

    def test_roll_num(self):
        """
        Tests whether roll_num can return an integer from 1 to 6
        """
        a = PigGame()
        for i in range(1000):
            number = a.roll_num()
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 6)

    def test_dice_simulator(self):
        """
        Tests whether dice_simulator can generate the line,
        according to the number of the die
        """
        a = PigGame()
        die_1 = a.dice_simulator(1)
        die_2 = a.dice_simulator(2)
        die_3 = a.dice_simulator(3)
        self.assertEqual(die_1[0], "+-------+")
        self.assertEqual(die_1[2], "|   o   |")
        self.assertEqual(die_2[2], "| o   o |")
        self.assertEqual(die_3[1], "|  o    |")
        self.assertEqual(die_3[2], "|   o   |")

    def test_board_line(self):
        """
        Tests whether board_line can produce the right line,
        given the content it should display
        """
        a = PigGame()
        blank_line = "|" + " " * 30 + "|"
        title = "|" + " " * 9 + "Score Board" + " " * 10 + "|"
        line1 = "|" + " " * 21 + "abc" + " " * 6 + "|"
        line2 = "|" + " " * 6 + "BOB" + " " * 12 + "AMY" + " " * 6 + "|"
        self.assertEqual(a.board_line(), blank_line)
        self.assertEqual(a.board_line('Score Board'), title)
        self.assertEqual(a.board_line(str2='abc'), line1)
        self.assertEqual(a.board_line('BOB', 'AMY'), line2)

    def test_ui_simulator(self):
        """ Tests whether ui_simulator can generate correct lines """
        a = PigGame()
        for i in range(1, 7):
            UI = a.ui_simulator(i)
            for line in UI:
                self.assertEqual(len(line), 51)


if __name__ == "__main__":
    unittest.main()
