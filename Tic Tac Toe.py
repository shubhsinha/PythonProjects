# milestone project 1
def check(p):
    if(tic[1] == p and tic[2] == p and tic[3] == p) or (tic[4] == p and tic[5] == p and tic[6] == p) or (tic[7] == p and tic[8] == p and tic[9] == p) or (tic[1] == p and tic[5] == p and tic[9] == p) or (tic[3] == p and tic[5] == p and tic[7] == p) or (tic[1] == p and tic[4] == p and tic[7] == p) or (tic[2] == p and tic[5] == p and tic[8] == p) or (tic[3] == p and tic[6] == p and tic[9] == p):
        if p == p1:
            print('Player 1 Wins')
            exit()
        else:
            print('Player 2 Wins')
            exit()
    else:
        for i in range(1,10):
            if tic[i] != ' ':
                pass
        print('The game is tied')


def display():
    print(tic[7] + '|' + tic[8] + '|' + tic[9])
    print(tic[4] + '|' + tic[5] + '|' + tic[6])
    print(tic[1] + '|' + tic[2] + '|' + tic[3])


def input_marker():
    im = ''
    while im != 'X' and im != 'O' and im != 'x' and im != 'o':
        im = input('Player 1, choose b/w X & O : ')

    player1 = im.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


def in_show(r, p) :
    t1 = p
    if tic[r] == ' ':
        tic[r] = p
    else:
        while tic[r] != ' ':
            print('Sorry the place is pre-occupied. Enter again.')
            if t1 == p1:
                r = int(input('Player 1 Chance : '))
            else:
                r = int(input('Player 2 Chance : '))

        tic[r] = p
    display()
    check(p)


def inplace(p1, p2):
    print("Enter your place : ")
    for i in range(0, 9):
        r = 0
        l = 0
        while r > 9 or r < 1:
            if i % 2 == 0:
                r = int(input('Player 1 Chance : '))
            else:
                r = int(input('Player 2 Chance : '))
        if i % 2 == 0:
            in_show(r, p1)
        else:
            in_show(r, p2)


tic = [' '] * 10
p1, p2 = input_marker()
display()
print(f'Player 1 - {p1} & Player 2 - {p2}\n')
inplace(p1, p2)
