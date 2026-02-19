def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())

for _ in range(n):
    cards = int(input()) - 1

    people = [[1, 0], [0, 0] ]
    color = 1
    turn = 1
    turn_cnt = 0 
    
    for curr in range(2, cards + 100):
        
        for j in range(curr): 
            if not cards:
                break 
            
            people[turn][color] += 1 
            cards -= 1 
            color = abs(1 - color)
            
        if not cards:
            break   
        turn_cnt += 1
        if turn_cnt == 2:
            turn = abs(1 - turn)
            turn_cnt = 0
            
    
    print(*people[0], end = " ")
    print(*people[1])




aaa

aa : 0 
1 