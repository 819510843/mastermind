import unittest
from mastermind import Mastermind


class test_Guess(unittest.TestCase):

    def test_single_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['BLUE', 'YELLOW', 'BLACK', 'RED']
        response = 'P'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_one_color(self):
        guess = ['BLUE', 'YELLOW', 'BLACK', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'P'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_double_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['RED', 'YELLOW', 'BLACK', 'RED']
        response = 'PP'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_two_color(self):
        guess = ['RED', 'YELLOW', 'BLACK', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'PP'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_triple_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['RED', 'RED', 'BLACK', 'RED']
        response = 'PPP'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_three_color(self):
        guess = ['RED', 'RED', 'BLACK', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'PPP'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_quad_color(self):
        guess = ['RED', 'RED', 'RED', 'RED']
        solution = ['RED', 'RED', 'RED', 'RED']
        response = 'SOLVED'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_error1(self):
        guess = ['RED', 'YELLOW', 'YELLOW', 'BLACK']
        solution = ['RED', 'RED', 'YELLOW', 'BLACK']
        response = 'PPP'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_error2(self):
        guess = ['GREEN', 'BLACK', 'GREEN', 'GREEN']
        solution = ['RED', 'YELLOW', 'BLACK', 'BLACK']
        response = 'C'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_error3(self):
        guess = ['BLACK', 'WHITE', 'RED', 'RED']
        solution = ['RED', 'YELLOW', 'BLACK', 'BLACK']
        response = 'CC'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())

    def test_error4(self):
        guess = ['RED', 'GREEN', 'YELLOW', 'BLUE']
        solution = ['RED', 'YELLOW', 'BLACK', 'BLACK']
        response = 'CP'
        new = Mastermind('test', guess, solution)
        self.assertEqual(response, new.testGame())


if __name__ == '__main__':
    unittest.main()
