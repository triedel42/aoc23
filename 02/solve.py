from pprint import pprint

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

# only 12 red cubes, 13 green cubes, and 14 blue cubes
def is_possible(game, bag):
    for turn in game:
        for cname, ccount in turn.items():
            if ccount > bag[cname]:
                return False
    return True

#testline = 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
#print(parse_game(line))
#ex_game = [{'red': 10, 'green': 13, 'blue': 20}, {'red': 10, 'green': 13, 'blue': 14}]

bag = {'red': 12, 'green': 13, 'blue': 14}
file = open('input')
games = (parse_game(l) for l in file.read().splitlines())
possible = filter(lambda g: is_possible(g[1], bag), games)
possible = list(possible)
#pprint(possible)
print(sum((p[0] for p in possible)))

