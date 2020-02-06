class Game:


    def __init__(self):
        self.gamefield = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def set_move(self, u, umove):
        self.u = u
        self.umove = umove
        self.gamefield[int(self.umove)] = self.u

    def print_gamefield(self):
        a = 1
        for i in self.gamefield:
            print(i, end=' ')
            a = a + 1
            if a > 3:
                print('\n')
                a = 1

    def check_len_field(self):
        if '-' not in self.gamefield:
            return True
        else:
            return False

    def check_winner(self, u):
        self.u = u
        if self.gamefield[0] == self.gamefield[1] == self.gamefield[2] == self.u:
            return True
        elif self.gamefield[3] == self.gamefield[4] == self.gamefield[5] == self.u:
            return True
        elif self.gamefield[6] == self.gamefield[7] == self.gamefield[8] == self.u:
            return True
        elif self.gamefield[0] == self.gamefield[3] == self.gamefield[6] == self.u:
            return True
        elif self.gamefield[1] == self.gamefield[4] == self.gamefield[7] == self.u:
            return True
        elif self.gamefield[2] == self.gamefield[5] == self.gamefield[8] == self.u:
            return True
        elif self.gamefield[0] == self.gamefield[4] == self.gamefield[8] == self.u:
            return True
        elif self.gamefield[2] == self.gamefield[4] == self.gamefield[6] == self.u:
            return True


game = Game()
user = 'X'

while True:
    usermove = input(f'User {user} please make a move: ')
    game.set_move(user, usermove)
    game.print_gamefield()
    if game.check_winner(user):
        print(f'User {user} win!')
        break
    if game.check_len_field():
        break
    if user == 'X':
        user = 'O'
    else:
        user = 'X'
