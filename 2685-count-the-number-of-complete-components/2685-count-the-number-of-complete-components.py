class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n
        edgeCount = [0] * n
        componentSize = [1] * n

        def findRoot(node):
            if parent[node] == -1:
                return node
            return findRoot(parent[node])
        
        def unionComponents(node1, node2):
            root1, root2 = findRoot(node1), findRoot(node2)
            edgeCount[root1] += 1
            if root1 != root2:
                parent[root2] = root1
                edgeCount[root1] += edgeCount[root2]
                componentSize[root1] += componentSize[root2]
            
        for u, v in edges:
            unionComponents(u, v)
        
        completeComponents = 0
        for i in range(n):
            if parent[i] == -1:
                nodes = componentSize[i]
                expectedEdges = nodes * (nodes - 1) // 2
                if edgeCount[i] == expectedEdges:
                    completeComponents += 1
        
        return completeComponents