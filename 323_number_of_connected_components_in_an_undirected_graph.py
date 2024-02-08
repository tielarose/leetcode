# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.


# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1


# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a hashmap that maps each node to an array of its neighbors
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # create a dfs function to visit every node in a given component
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # loop over every node in range n; if we come to a node
        # we haven't seen, that node must be in a separate component
        seen = set()
        num_components = 0

        for node in range(n):
            if node not in seen:
                num_components += 1
                seen.add(node)
                dfs(node)

        return num_components
