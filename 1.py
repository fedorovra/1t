sticks: int = 10
users = []
while len(users) < 2:
    users.append(input('please write your name: '))
cur_user = 0
while sticks > 1:
    while True:
        move = input('{user} please enter number from 1 to 3: '.format(user = users[cur_user]))
        if int(move) > 3 or int(move) < 1:
            print('wrong number')
        else:
            break
    sticks -= int(move)
    print("{user} removed {move} sticks, on the table now {sticks}".format(user = users[cur_user], move = move, sticks = sticks))
    if cur_user == 0:
        cur_user = 1
    else:
        cur_user = 0
    if sticks == 1:
        print('{} is lost'.format(users[cur_user]))
