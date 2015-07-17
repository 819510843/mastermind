from random import randint
from collections import Counter


class Mastermind:

    pegs = ['RED',
            'GREEN',
            'YELLOW',
            'BLUE',
            'WHITE',
            'BLACK']

    def __init__(self):
        self.pegs = Mastermind.pegs[:]
        self.guessCounter = 1

    def startGame(self):
        printInstructions()
        self.setSolution(**getGameParams())
        self.playGame()

    def setSolution(self, **params):
        if params['blanks']:
            self.pegs.append('EMPTY')
        if params['multiples']:
            pegs = self.pegs[:] * 4
        else:
            pegs = self.pegs[:]
        self.solution = [pegs.pop(randint(0, len(pegs) - 1)) for _ in range(4)]

    def playGame(self):
        while True:
            self.getGuess()
            if self.validGuess():
                guess_response = self.checkGuess()
                if guess_response == 'WINNER':
                    return self.gameOver()
                else:
                    self.replyGuess(guess_response)

    def getGuess(self):
        self.guess = input('GUESS %s: ' % self.guessCounter)

    def validGuess(self):
        attempt = self.guess.upper().split()

        if len(attempt) != 4:
            return False

        for each in attempt:
            if each not in self.pegs:
                return False

        self.guess = attempt
        self.guessCounter += 1
        return True

    def checkGuess(self):
        if self.guess == self.solution:
            return 'WINNER'

        nonMatchedGuess = []
        nonMatchedSolution = []
        guessedPositions = 0
        for a, b in zip(self.guess, self.solution):
            if a != b:
                nonMatchedGuess += [a]
                nonMatchedSolution += [b]
            else:
                guessedPositions += 1

        guessedColors = sum((Counter(nonMatchedGuess) &
                             Counter(nonMatchedSolution)).values())

        return ('C' * guessedColors) + ('P' * guessedPositions)

    def gameOver(self):
        print('''
                    CONGRATS!!
                    You won the game in %s guesses.

                    The solution was:
                    %s
              ''' % (self.guessCounter - 1, ' '.join(self.solution)))

    def replyGuess(self, response):
        print('RESPONSE %s: %s' % (self.guessCounter - 1, response))


def printInstructions():
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


def getGameParams():
    params = {'blanks': False,
              'multiples': False}
    userInput = input('To include empty spaces, enter <1>.\n'
                      'To include multiples, enter <2>.\n')
    if '1' in userInput:
        params['blanks'] = True
    if '2' in userInput:
        params['multiples'] = True
    return params


def playAgain():
    userInput = input('To stop playing, enter <STOP>:')
    userInput = userInput.lower()
    if userInput != 'stop':
        return True
    return False


if __name__ == '__main__':
    first_game = Mastermind()
    first_game.startGame()
    while playAgain():
        new_game = Mastermind()
        new_game.startGame()
