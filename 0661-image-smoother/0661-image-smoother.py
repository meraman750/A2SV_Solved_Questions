class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                temp = img[i][j]
                cur = 1
                if j-1 >= 0:
                    print("l")
                    temp += img[i][j-1]
                    cur+=1
                if j+1 < len(img[0]):
                    print("r")
                    temp += img[i][j+1]
                    cur+=1
                if i-1 >= 0:
                    print
                    temp += img[i-1][j]
                    cur+=1
                if i+1 < len(img):
                    temp += img[i+1][j]
                    cur+=1
                if i+1 < len(img) and j+1 < len(img[0]):
                    temp += img[i+1][j+1]
                    cur+=1
                if i-1 >= 0 and j-1 >= 0:
                    temp += img[i-1][j-1]
                    cur+=1
                if i-1 >= 0 and j+1 < len(img[0]):
                    temp += img[i-1][j+1]
                    cur+=1
                if j-1 >= 0 and i+1 < len(img):
                    temp += img[i+1][j-1]
                    cur+=1
                ans[i].append(temp // cur)
        return ans
            
