class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(s)):
            mp[s[i]].append(i)

        arr = [val for key, val in mp.items()]
        prev = arr[0]
        
        start = prev[0]
        end = prev[-1]
        ans = []
        for i in range(1, len(arr)):
            if arr[i][0] < end:
                start = min(start, arr[i][0])
                end = max(end, arr[i][-1])
            else:
                ans.append(end-start+1)
                start = arr[i][0]
                end = arr[i][-1]
        ans.append(end-start+1)
        return ans