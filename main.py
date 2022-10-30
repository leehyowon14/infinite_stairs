from dis import dis
from random import randrange
from os import system
from wsgiref.simple_server import sys_version

#score
score = 0
#map
infinite_map = [1]
#player_direction
player_direction = 1

#make map
for i in range(13):
    if randrange(10):
        infinite_map.append(1)
    else:
        infinite_map.append(-1)
#direction : 1 -> left, -1 -> right

#if climb
def climb():
    global score, infinite_map
    score += 1
    del infinite_map[0]
    if randrange(10):
        infinite_map.append(1)
    else:
        infinite_map.append(-1)

#5*15 Map print
def display():
    system('cls')
    map_list = []
    block_x_position = 2
    if score == 0 :
        map_list.append(['  ', '  ', '  ', '  ', '  '])
    else:
        map_list.append(['  ', '  ', '==', '  ', '  '])
    for i in infinite_map:
        if i == 1:
            block_x_position -= 1
        else:
            block_x_position += 1
        map_temp_list = []
        for o in range(5):
            if o == block_x_position:
                map_temp_list.append('==')
            else:
                map_temp_list.append('  ')
        map_list.append(map_temp_list)
    map_list.reverse()
    map_list[-2][2] = 'pl'
    for i in map_list:
        for o in i:
            print(o, end=' ')
        print()
    if player_direction == 1:
        print("Direction: <")
    else:
        print("Direction: >")

while True:
    display()
    player_input = input("[Climb: (empty), Turn: (any char)] input: ")
    if len(player_input) == 0:
        if player_direction * 1 == infinite_map[0]:
            climb()
        else:
            break
    else:
        if player_direction * -1 == infinite_map[0]:
            player_direction *= -1
            climb()
        else:
            break

system('cls')
print('Game Ended!')
print('Score:', score)