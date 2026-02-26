from collections import Counter, defaultdict

s = "ababcbacadefegdehijhklij"

count = Counter(s)
ans = []
prev = 0
mp = defaultdict(int)

for i in range(len(s)):
    mp[s[i]]+=1
    if mp[s[i]] == count[s[i]]:
        j = i
        cur = 0
        set_ = set()
        while j >= prev:
            if mp[s[j]] != count[s[j]]:
                break
            if s[j] not in set_:
                cur+=mp[s[j]]
            set_.add(s[j])
            j-=1 
        else:
            if cur > 0:
                ans.append(cur)
                prev = i+1

print(ans)