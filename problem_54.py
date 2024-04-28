with open(r"poker.txt") as file:
    contents = file.read()
contents = [[i[:14].split(), i[15:].split()] for i in contents.split('\n')[:-1]]

counter = 0


def card_points(n):
    s = '23456789TJQKA'
    n.sort(key=lambda x: s.index(x[0]))
    if n.count('S') == 5 or n.count('C') == 5 or n.count('H') or n.count('D'):
        if ''.join([i[0] for i in n]) in s:
            'Straight Flush'
            points = (10, s.index(n[0][0]))
        else:
            'Flush'
            points = (7, s.index(n[0][0]))
    else:
        d = {}
        for c in n:
            d[c[0]] = d.get(c[0], 0) + 1
        d = {k: v for k, v in sorted(d.items(), key=lambda x: x[-1])}
        if list(d.items())[-1][-1] == 4:
            'Four of a Kind'
            points = (9, s.index(list(d.items())[-1][0]), s.index(list(d.items())[-2][0]))
        elif list(d.items())[-1][-1] == 3:
            if len(d) == 2:
                'Full House'
                points = (8, s.index(list(d.items())[-1][0]), s.index(list(d.items())[-2][0]))
            else:
                'Three of a Kind'
                points = (5, s.index(list(d.items())[-1][0]), s.index(list(d.items())[-2][0]))
        elif list(d.items())[-1][-1] == 2:
            if len(d) == 3:
                'Two Pairs'
                points = (
                    4, s.index(list(d.items())[-1][0]), s.index(list(d.items())[-2][0]),
                    s.index(list(d.items())[-3][0]))
            else:
                'One Pair'
                points = (
                    3, s.index(list(d.items())[-1][0]), s.index(list(d.items())[-2][0]),
                    s.index(list(d.items())[-3][0]),
                    s.index(list(d.items())[-4][0]))
        else:
            'Straight'
            if ''.join([i[0] for i in n]) in s:
                points = (6, s.index(n[0][0]))
            else:
                'High Card'
                points = (
                2, s.index(list(d.items())[-1][0]), s.index(list(d.items())[-2][0]), s.index(list(d.items())[-3][0]),
                s.index(list(d.items())[-4][0]), s.index(list(d.items())[-5][0]))
    return points


for i in contents:
    if card_points(i[0]) > card_points(i[1]):
        counter += 1
print(counter)
