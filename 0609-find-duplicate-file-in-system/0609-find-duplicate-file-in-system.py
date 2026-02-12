class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = {}
        for path in paths:
                cur = ""
                i=0
                flag = True
            
                while flag and i < len(path) and path[i] != " ":
                    cur += path[i]
                    i+=1
                i+=1
                j = i
                while j < len(path): 
                    name = ""
                    while j < len(path) and path[j] != ".":
                        name += path[j]
                        j+=1
                    content = ""
                    con = False
                    while j < len(path) and path[j] != " ":
                        if path[j] == "(":
                            con = True
                            j+=1
                            continue
                        if path[j] == ")":
                            con = False
                            j+=1
                            continue
                        if con:
                            content += path[j]
                            j+=1
                        else:
                            j+=1
                    j+=1
                    if content in ans:
                        ans[content].append(f"{cur}/{name}.txt")
                    else:
                        ans[content] = [f"{cur}/{name}.txt"]
        res = []
        for val in ans.values():
            if len(val) > 1:
                res.append(val)
        return res
                





                
            
