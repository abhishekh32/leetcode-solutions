
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the new parent of each node
        new_parent = [-1] * n

        # Stores the nearest ancestor for each character
        last = {}

        # DFS preorder
        order = []

        # Iterative DFS with backtracking
        stack = [(0, False, -1)]

        while stack:
            node, exiting, prev = stack.pop()
            char = s[node]

            if not exiting:

                # Previous ancestor with the same character
                prev = last.get(char, -1)

                # Determine the new parent
                if node != 0:
                    if prev != -1:
                        new_parent[node] = prev
                    else:
                        new_parent[node] = parent[node]

                # Update nearest ancestor
                last[char] = node

                order.append(node)

                # Exit event
                stack.append((node, True, prev))

                # Visit original children
                for child in reversed(children[node]):
                    stack.append((child, False, -1))

            else:

                # Restore previous ancestor
                if prev == -1:
                    del last[char]
                else:
                    last[char] = prev

        # Calculate subtree sizes
        size = [1] * n

        for node in reversed(order):
            p = new_parent[node]

            if p != -1:
                size[p] += size[node]

        return size
