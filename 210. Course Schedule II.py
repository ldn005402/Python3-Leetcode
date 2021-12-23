class Solution:
    flag = True
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for p in prerequisites:
            graph[p[0]].append(p[1])
            
        state = [0]*numCourses
        stack = []
        
        def dfs(vertex):
            state[vertex] = 1
            for node in graph[vertex]:
                if state[node]==1:
                    self.flag = False
                    break
                elif state[node]==2:
                    continue
                dfs(node)
            stack.append(vertex)
            state[vertex] = 2
            
        for i in range(0, numCourses):
            if state[i]==0:
                dfs(i)
                
        return stack if self.flag else []
