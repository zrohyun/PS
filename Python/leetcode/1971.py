class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        method = 'union'
        if method == 'union':

            return self.union_find(n,edges,source,destination)

        return self.dfs(n,edges,source, destination)
    
    def union_find(self,n,edges,source,destination) -> bool:
        root = [i for i in range(n)]
        rank = [0]*n
        
        def find(x):
            if x == root[x]:
                return x
            
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootx,rooty = find(x),find(y)
            
            if rootx != rooty:
                # rankx > ranky, rootx의 root는 rooty가 됨.
                # rank는 클 수록 더 높은 랭크, 더 작은 랭크의 root로 들어가게 됨.
                if rank[rootx] > rank[rooty]:
                    root[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    root[rootx] = rooty
                else:
                    # 두 rank가 같다면 아무거나 선택
                    # x를 선택했다면 x가 y의 root가 되고 우선 순위를 위해
                    # x의 rank +1을 해줌.
                    root[rooty] = rootx
                    rank[rootx] += 1
                    
        for e1,e2 in edges:
            # print(root,rank)
            union(e1,e2)
        
        
        return find(source) == find(destination)
        
    def dfs(self,n,edges,source,destination) -> bool:
        from collections import defaultdict        
        """
        condition
        1<= n <= 2 * 1e5
        0 <= edges.len <=
        
        dfs,bfs 구현
        edges를 이용해 graph map을 만든 후 dfs
        https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/2581562/Python-BFS-and-DFS
        """
        
        #basis condition
        if n == 1:
            if source == destination:
                return True
            else:
                return False
        
        # board = defaultdict(set) -> 찾는 게 아니면 hashing이 오래 걸리는 듯.
        board = defaultdict(list)

        
        # init board
        for s,d in edges:
            board[s].append(d)
            board[d].append(s)
        
        # memory visited
        visited = [False]*n
        visited[source] = True
        
        # memory q
        q = []
        for e in board[source]:
            q.append(e)
        
        while q:
            v = q.pop()
            
            #basis condition
            if v == destination:
                return True
            
            if visited[v]: continue
            
            visited[v] = True
            
            for e in board[v]:
                q.append(e)
            
        
        return False

    

            
            


        