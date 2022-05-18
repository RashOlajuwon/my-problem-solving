"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.
"""
# The first solution below is sub-optimal, running at O(n3) time.

def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        nodes = {}
        ans = []
        for i in range(len(connections)):
            if connections[i][0] in nodes:
                nodes[connections[i][0]].append(connections[i][1])
            if connections[i][1] in nodes:
                nodes[connections[i][1]].append(connections[i][0])
            if connections[i][0] not in nodes:
                nodes[connections[i][0]] = [connections[i][1]]
            if connections[i][1] not in nodes:
                nodes[connections[i][1]] = [connections[i][0]]
        for key in nodes:
            for i in nodes[key]:
                start = 0
                present = False
                while start<len(nodes[i]):
                    if nodes[i][start] in nodes[key]:
                        present = True
                        break
                    start+=1
                if not present:
                    if [key,i] not in ans and [i,key] not in ans:
                        ans.append([key,i])
        return ans
