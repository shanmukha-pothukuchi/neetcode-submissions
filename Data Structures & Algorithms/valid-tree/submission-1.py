class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        stack = [(0, -1)]  # (node, parent)

        while stack:
            node, parent = stack.pop()

            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))

        return len(visited) == n