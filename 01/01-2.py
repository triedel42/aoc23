digits = 'zero,one,two,three,four,five,six,seven,eight,nine,0,1,2,3,4,5,6,7,8,9'.split(',')
#digits = '0,1,2,3,4,5,6,7,8,9'.split(',')

def find_right(s, sub):
    for i in range(len(s) - 1, -1, -1):
        res = s.find(sub, i)
        if res != -1:
            return res
    return -1

s = 0
for l in open('input'):
    line = l.replace('\n', '')
    print('orig:', line)
    left, right = len(line), -1
    left_i, right_i = -1, -1
    for i, d in enumerate(digits):
        fromleft = line.find(d)
        #print('found fromleft: ', d, 'at', i)
        fromright = find_right(line, d)
        if fromleft != -1 and fromleft < left:
            left = fromleft
            left_i = i
        if fromright != -1 and fromright > right:
            right = fromright
            right_i = i
    a = left_i
    b = right_i
    a %= 10
    b %= 10
    print(a, b)
    s += 10 * a + b
    print()

print(s)
