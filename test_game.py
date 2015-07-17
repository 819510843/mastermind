import unittest
from mastermind import Mastermind


class TestMastermind(unittest.TestCase):

    def test_single_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['BLUE', 'YELLOW', 'BLACK', 'RED']
        response = 'P'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_one_color(self):
        guess = ['BLUE', 'YELLOW', 'BLACK', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'P'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_double_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['RED', 'YELLOW', 'BLACK', 'RED']
        response = 'PP'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_two_color(self):
        guess = ['RED', 'YELLOW', 'BLACK', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'PP'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_triple_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['RED', 'RED', 'BLACK', 'RED']
        response = 'PPP'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_three_color(self):
        guess = ['RED', 'RED', 'BLACK', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'PPP'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_quad_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'WINNER'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_error1(self):
        guess = ['RED', 'YELLOW', 'YELLOW', 'BLACK']
        solution = ['RED', 'RED', 'YELLOW', 'BLACK']
        response = 'PPP'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_error2(self):
        guess = ['GREEN', 'BLACK', 'GREEN', 'GREEN']
        solution = ['RED', 'YELLOW', 'BLACK', 'BLACK']
        response = 'C'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_error3(self):
        guess = ['BLACK', 'WHITE', 'RED', 'RED']
        solution = ['RED', 'YELLOW', 'BLACK', 'BLACK']
        response = 'CC'
        self.assertEqual(response,
                         testGame(guess, solution))

    def test_error4(self):
        guess = ['RED', 'GREEN', 'YELLOW', 'BLUE']
        solution = ['RED', 'YELLOW', 'BLACK', 'BLACK']
        response = 'CP'
        self.assertEqual(response,
                         testGame(guess, solution))


def testGame(guess, solution):
    a_game = Mastermind()
    a_game.pegs = Mastermind.pegs[:] + ['EMPTY']
    a_game.guess = guess
    a_game.solution = solution
    return a_game.checkGuess()


if __name__ == '__main__':
    unittest.main()
