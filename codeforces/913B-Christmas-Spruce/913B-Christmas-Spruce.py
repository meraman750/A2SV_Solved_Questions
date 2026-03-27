# print(children)

for node in range(1, n+1):
    if len(children[node]) == 0:
        continue

    count = 0
    for child in children[node]:
        if len(children[child]) == 0:
            count +=1

    if count < 3:
        print("No")
        exit()

print("Yes")