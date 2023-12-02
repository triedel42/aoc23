from pprint import pprint
from operator import mul
from functools import reduce

def parse_game(line):
    game, line = line.split(': ')
    game_id = int(game.split(' ')[1])
    turns = []
    for game in line.split('; '):
        cgame = {}
        for color in game.split(', '):
            #print(color)
            count, cname = color.split(' ')
            cgame[cname] = int(count)
        turns.append(cgame)
    return (game_id, turns)

def is_possible(game, bag):
    for turn in game:
        for cname, ccount in turn.items():
            if ccount > bag[cname]:
                return False
    return True

def getcolor(c, turn):
    if c in turn:
        return turn[c]
    else:
        return 0

def getpower(game):
    l = []
    for c in 'red,green,blue'.split(','):
        l.append(max(getcolor(c, turn) for turn in game[1]))
    return reduce(mul, l, 1)

#testline = 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
#print(parse_game(line))
#ex_game = [{'red': 10, 'green': 13, 'blue': 20}, {'red': 10, 'green': 13, 'blue': 14}]

file = open('input')
games = list(parse_game(l) for l in file.read().splitlines())

def part1():
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    bag = {'red': 12, 'green': 13, 'blue': 14}
    possible = filter(lambda g: is_possible(g[1], bag), games)
    possible = list(possible)
    #pprint(possible)
    print(sum((p[0] for p in possible)))

def part2():
    print(sum((p for p in map(getpower, games))))

print('part 1: ', end='')
part1()
print('part 2: ', end='')
part2()
