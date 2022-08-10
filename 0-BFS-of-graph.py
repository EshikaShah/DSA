class Solution:
    
    def bfsOfGraph(self, V, adj):
        bfs = []
        queue = []
        visited = [False]*V
        queue.append(0)
        visited[0] = True
        while(queue):
            node = queue.pop(0)
            bfs.append(node)
            for i in adj[node]:
                if(visited[i]==False):
                    visited[i] = True
                    queue.append(i)
        return bfs
