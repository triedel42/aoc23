alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper()

s = 0
for l in open('input'):
    line = l.replace('\n', '')
    print('orig:', line)
    line = line.lstrip(alphabet)
    line = line.rstrip(alphabet)
    print('stripped:', line)
    a = int(line[0])
    b = int(line[-1])
    print(a, b)
    s += 10 * a + b
    print()

print(s)
