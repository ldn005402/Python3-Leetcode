class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(i):
            seen[i] = 0
            for nei in graph[i]:
                if nei in seen:
                    if seen[nei] == 0:
                        return False
                else:
                    if not dfs(nei):
                        return False
            seen[i] = 1
            res.appendleft(i)
            return True
        
        # records all characters appeared in words
        nodes = set()
        for word in words:
            nodes |= set(word)
        
        # construct the graph
        graph = collections.defaultdict(set)
        for i in range(len(words)-1):
            k = 0
            diff = False
            while k < len(words[i]) and k < len(words[i+1]):
                if words[i][k] != words[i+1][k]:
                    graph[words[i][k]].add(words[i+1][k])
                    diff = True
                    break
                else:
                    k += 1
            if not diff and len(words[i]) > len(words[i+1]):
                return ""
                
        
        # topologically sort the characters
        res = collections.deque()
        seen = {}
        for i in nodes:
            if i not in seen:
                if not dfs(i):
                    return ""
        return "".join(res)
