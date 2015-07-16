from random import randint


class Mastermind:

    pegs = ['RED',
            'GREEN',
            'YELLOW',
            'BLUE',
            'WHITE',
            'BLACK']

    def __init__(self):
        self.pegs = Mastermind.pegs
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

    def checkGuess(self):
        if self.guess == self.solution:
            return 'WINNER'
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
        for each in nonMatchedGuess:
            if (nonMatchedGuess.count(each) - colorCount[each] <=
                nonMatchedSolution.count(each)):
                    response.append('C')
            else:
                colorCount[each] += 1
        return ''.join(sorted(response))

    def gameOver(self):
        print('''
                    CONGRATS!!
                    You won the game in %s guesses.

                    The solution was:
                    %s
              ''' % (self.guessCounter - 1, ' '.join(self.solution)))

    def replyGuess(self, response):
        print('RESPONSE %s: %s' % (self.guessCounter - 1, response))

    def testGame(self, guess, solution):
        self.pegs = Mastermind.pegs + ['EMPTY']
        self.guess = guess
        self.solution = solution
        return self.checkGuess()


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
            new_game = Mastermind()
            new_game.startGame()
        else:
            return False
        return True


if __name__ == '__main__':
    a_game = Mastermind()
    a_game.startGame()
    while True:
        if not playAgain():
            break
