class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        mp = defaultdict(list)
        nums = []
        visited = set()

        heapq.heappush(nums, [nums1[0] + nums2[0], 0, 0])
        visited.add((0, 0))
        ans = []
        while nums and k:
            # print(nums)
            temp, i, j = heapq.heappop(nums)
            ans.append([nums1[i], nums2[j]])
            # print(temp, mp)
            if i+1 < len(nums1) and (i+1, j) not in visited:
                x = (nums1[i+1] + nums2[j])
                heapq.heappush(nums, [x, i+1, j])
                visited.add((i+1, j))

            if j+1 < len(nums2) and (i, j+1) not in visited:
                x = nums1[i] + nums2[j+1]
                heapq.heappush(nums, [x, i, j+1])
                visited.add((i, j+1))

            k-=1
        
        return ans


        