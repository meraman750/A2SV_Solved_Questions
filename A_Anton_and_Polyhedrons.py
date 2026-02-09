def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

s = {"Tetrahedron":4,
     "Cube": 6,
     "Octahedron": 8,
     "Dodecahedron": 12,
     "Icosahedron": 20}

n = int(input())
ans = 0
for i in range(n):
    name = input()
    if name in s:
        ans += s[name]
print(ans)
