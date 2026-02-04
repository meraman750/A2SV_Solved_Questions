from collections import defaultdict, Counter 
def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    n,m = list_()
    cards = []

    for x in range(n):
        cards.append(list_())

    for i in cards:
        i.sort()

    dic = defaultdict(int)
    for index, deck in enumerate(cards):
        dic[deck[0]] = index
    
    cards = sorted(cards , key = lambda x : x[0])
    
    valid  = True

    for i in range(m):
        if i==0:
            prev = cards[0][i]
        for j in range(n):
            if i== 0 ==j:
                continue
            if cards[j][i] <= prev:
                valid = False
                break
            prev = cards[j][i]

    if valid:
        p =[]
        for deck in cards:
            p.append(dic[deck[0]] + 1)
        print(*p)
    else:
        print(-1)

