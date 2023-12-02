#digits = '0,1,2,3,4,5,6,7,8,9'.split(',') # for part 1
digits = 'zero,one,two,three,four,five,six,seven,eight,nine,0,1,2,3,4,5,6,7,8,9'.split(',') # for part 2

lfind = lambda s, dig: s.find(dig)
rfind = lambda s, dig: s[::-1].find(dig[::-1])
valid_index = lambda t: t[0] != -1
get_ind = lambda t: t[0]
findres = lambda s, ff: ((ff(s, d), i % 10) for i, d in enumerate(digits))
getdig = lambda s, ff: min(filter(valid_index, findres(s, ff)), key=get_ind)[1]
both = lambda s: 10 * getdig(s, lfind) + getdig(s, rfind)
total = lambda f: sum((both(l) for l in open(f)))

print('sum', total('input'))
