"""
"""

from random import randint


class Mastermind:

    def __init__(self):
        self.startGame()

    def checkGuess(self):
        if self.guess == self.solution:
            return self.gameOver()

        result = []
        solution = self.solution[:]
        guess = self.guess[:]
        for index, each in enumerate(guess):
            if each == solution[index]:
                result.append('P')
                guess.pop(index)
                solution.pop(index)

        for each in guess:
            if guess.count(each) == solution.count(each):
                result.append('C')
            elif (solution.count(each) > 0 and
                  guess.index(each) == index):
                    result.append('C')

        print('RESPONSE %s: %s' % (self.guessCounter - 1,
                                   ''.join(sorted(result))))

        self.getGuess()

    def gameOver(self):
        print('''
                    CONGRATS!!
                    You won the game in %s guesses.

                    The solution was:
                    %s
              ''' % (self.guessCounter - 1, ' '.join(self.solution)))
        self.playAgain()

    def getGuess(self):
        self.guess = input('GUESS %s: ' % self.guessCounter)
        if self.validGuess():
            self.checkGuess()
        else:
            self.getGuess()

    def playAgain(self):
        userInput = input('To stop playing, enter <no>:')
        userInput = userInput.lower()

        if userInput != 'no':
            self.startGame()

    def setSolution(self, blanks=False, multiples=False):
        self.pegs = ['RED',
                     'GREEN',
                     'YELLOW',
                     'BLUE',
                     'WHITE',
                     'BLACK']

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
