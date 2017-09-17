"""
Long variation of rolling-a-dice game created by Grzegorz Motyl.
The rules are simple: HIT the max score and win the game. You can play with your friends, as many players as you want.
There can be more then one winner!
You have to score MAX_POINTS to win the game.
The game is short so no DRY principle used.
"""

from random import randint, choice

# MAX SCORE TO HIT IN GAME
MAX_SCORE = 21


class Game():
    """ General game class """

    # number of players
    players = {}
    # max number of points
    max_points = 0
    # score boards
    score_board = []
    over_score_board = []

    def __init__(self, points):
        self.max_points = points

    def dice(self):
        """ Roll the dice """
        return randint(0,5) + 1

    def winner(self):
        """ List of players who won the game """

        for p in self.score_board:
            print('%s has %s' % (p[0], p[1]))

    def losers(self):
        """ List of player who lost the game"""

        for p in self.over_score_board:
            print('%s has %s' % (p[0], p[1]))

    def new_game(self):
        """ New Game """

        # who will roll the dice first:
        current_player = choice(list(self.players.keys()))

        # main game loop
        running = True
        while running:

            # in-game players list
            q = list(self.players.keys())

            # current players position
            for i, p in enumerate(q):
                if p == current_player:
                    position = i

            if len(self.players) > 0:
                # score board
                for player in self.players.items():
                    print(player[0] + ': ' + str(player[1]) + ', ', end="")
                # end of score board

                # roll the dice and add the points for each player
                print(' ')
                print(' ')
                print(current_player + '\'s ' + 'turn:')
                roll = input('Press ENTER to roll the dice...')
                points = self.dice()
                print(str(points) + ' points for ' + current_player)
                self.players[current_player] += points

                if self.players[current_player] == self.max_points:
                    self.score_board.append([current_player, self.players[current_player]])
                    del self.players[current_player]
                # player game over if > max_points
                elif self.players[current_player] > self.max_points:
                    print('Game Over: ' + current_player + ' ' + str(self.players[current_player]) + '/' + str(self.max_points))
                    self.over_score_board.append([current_player, self.players[current_player]])
                    del self.players[current_player]

                position = position + 1
                if position > len(q) - 1:
                    position = 0

                current_player = q[position]

            else:
                if len(self.score_board) == 0:
                    print(' ')
                    print('GAME OVER: All players scored over ' + str(self.max_points))
                    print(' ')
                    self.losers()
                else:
                    print(' ')
                    print('=' * 20)
                    print('Winners:')
                    self.winner()
                    print(' ')
                    print('Losers:')
                    self.losers()
                    print('=' * 20)

                running = False


class Player(Game):

    def __init__(self, name):
        super(Player, self).__init__(name)

        # check for duplicate names:
        for key in self.players.keys():
            if name == key:
                # if duplicate add random number
                self.name = name + str(randint(0,99))
            else:
                self.name = name

        self.players[name] = 0

    def name(self):
        return self.name

    def points(self):
        return self.name + '\'s' + ' points: ' + str(self.players.get(self.name))

print('Rolling Dice Game')
# game setup: name of each player
while True:
    try:
        p = int(input('How many players? '))
        for i in range(0, p):
            print('Players\'s ' + str(i + 1))
            name = input('name: ')
            Player(name)
        break
    except:
        print('Only numbers allowed')
        continue

g = Game(MAX_SCORE)
g.new_game()
