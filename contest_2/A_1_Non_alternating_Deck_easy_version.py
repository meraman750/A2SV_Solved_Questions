def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())

for _ in range(n):
    cards = int(input()) - 1

    alice, bob = 1, 0 
    turn = "b"
    turn_cnt = 0
    curr = 2

    while cards > 0:
        if turn == "b":
            bob += min(curr, cards)
        else:
            alice += min(curr, cards)
        cards -= curr
        curr += 1
        turn_cnt += 1
        if turn_cnt == 2:
            turn = "a" if turn == "b" else "b"
            turn_cnt = 0
    
    print(alice, bob)