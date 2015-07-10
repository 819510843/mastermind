"""
"""

from random import randint


class Mastermind:

    def __init__(self, mode='start', guess=[], solution=[]):
        self.pegs = ['RED',
                     'GREEN',
                     'YELLOW',
                     'BLUE',
                     'WHITE',
                     'BLACK']

        if mode == 'start':
            self.startGame()
        else:
            self.guess = guess
            self.solution = solution

    def checkGuess(self, mode='start'):
        if self.guess == self.solution:
            return self.gameOver(mode)

        response = []
        nonMatchedGuess = []
        nonMatchedSolution = []
        for index, each in enumerate(self.guess):
            if each == self.solution[index]:
                response.append('P')
            else:
                nonMatchedGuess.append(each)
                nonMatchedSolution.append(self.solution[index])

        colorCount = {self.pegs[index]: 0 for index, _ in enumerate(self.pegs)}
        for index, each in enumerate(nonMatchedGuess):
            if (nonMatchedGuess.count(each) - colorCount[each] <=
                nonMatchedSolution.count(each)):
                    response.append('C')
            else:
                colorCount[each] += 1

        if mode == 'start':
            print('RESPONSE %s: %s' % (self.guessCounter - 1,
                                       ''.join(sorted(response))))
        else:
            return ''.join(sorted(response))

        self.getGuess()

    def gameOver(self, mode='start'):
        if mode == 'start':
            print('''
                        CONGRATS!!
                        You won the game in %s guesses.

                        The solution was:
                        %s
                  ''' % (self.guessCounter - 1, ' '.join(self.solution)))
            self.playAgain()
        else:
            return 'SOLVED'

    def getGuess(self):
        self.guess = input('GUESS %s: ' % self.guessCounter)
        if self.validGuess():
            self.checkGuess()
        else:
            self.getGuess()

    def playAgain(self):
        userInput = input('To stop playing, enter <STOP>:')
        userInput = userInput.lower()

        if userInput != 'stop':
            self.startGame()

    def setSolution(self, blanks=False, multiples=False):
        if blanks:
            self.pegs.append('EMPTY')

        if multiples:
            pegs = self.pegs[:] * 4
        else:
            pegs = self.pegs[:]

        self.solution = [pegs.pop(randint(0, len(pegs) - 1))
                         for each in range(4)]

    def startGame(self):
        self.guessCounter = 1
        self.printInstructions()
        params = self.getGameParams()
        self.setSolution(**params)
        self.getGuess()

    def testGame(self):
        return self.checkGuess(mode='test')

    def validGuess(self):
        try:
            attempt = self.guess.upper().split()
        except AttributeError:
            return False

        if len(attempt) != 4:
            return False

        for each in attempt:
            if each not in self.pegs:
                return False

        self.guess = attempt
        self.guessCounter += 1
        return True


# TODO make a classmethod or staticmethod
    def getGameParams(self):
        params = {'blanks': False,
                  'multiples': False}

        userInput = input('To include empty spaces, enter <1>.\n'
                          'To include multiples, enter <2>.\n')

        if '1' in userInput:
            params['blanks'] = True
        if '2' in userInput:
            params['multiples'] = True

        return params

# TODO make a classmethod or staticmethod
    def printInstructions(self):
        print('''
                Welcome to the game of MASTERMIND
                -------------------------------

                Enter your guesses in the format:
                RED WHITE BLUE YELLOW

                Valid colors are:
                ** RED
                ** GREEN
                ** YELLOW
                ** BLUE
                ** BLACK
                ** WHITE
                ** optionally ** EMPTY

              ''')


if __name__ == '__main__':
    newGame = Mastermind()
