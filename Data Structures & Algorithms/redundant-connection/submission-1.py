class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent= [i for i in range(len(edges)+1)]

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x1,x2):
            rootA=find(x1)
            rootB=find(x2)

            if rootA==rootB:
                return False
            
            parent[rootB]=rootA
            return True
        
        for start,end in edges: 
            if not union(start,end):
                return [start,end]
        