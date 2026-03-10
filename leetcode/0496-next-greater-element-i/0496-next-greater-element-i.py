class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mp = defaultdict(lambda : -1)
        for i in nums2:
            while stack and i > stack[-1]:
                mp[stack[-1]] = i
                stack.pop()
            stack.append(i)
        ans = []
        for i in nums1:
            if i in mp:
                ans.append(mp[i])
            else:
                ans.append((-1))
        return ans 