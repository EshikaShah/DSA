class Solution:
    def __init__(self):
        self.dfs = []
        self.adj = []
    
    def DFS(self, i, vis):
        vis[i] = True
        self.dfs.append(i)
        for child in self.adj[i]:
            if(vis[child]==False):
                self.DFS(child, vis)
        
    def dfsOfGraph(self, V, adj):
        vis = [False]*V
        self.adj = adj
        self.DFS(0, vis)
        return self.dfs
        
