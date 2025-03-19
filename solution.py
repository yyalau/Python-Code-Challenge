from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)  # Number of nodes in the graph
        full_mask = (1 << n) - 1  # Binary representation where all nodes are visited (e.g., 11111 for 5 nodes)
        
        queue = deque()  # Queue for BFS
        visited = set()  # Set to keep track of visited states (node, mask)
        
        # Initialize BFS with all possible starting nodes
        for i in range(n):
            mask = 1 << i  # Binary mask representing the current node as visited (e.g., 00001, 00010, etc.)
            queue.append((i, mask, 0))  # (current node, visited mask, steps taken)
            visited.add((i, mask))  # Mark the initial state as visited
        
        # Perform BFS
        while queue:
            node, mask, steps = queue.popleft()  # Dequeue the current state
            
            # If all nodes are visited, return the number of steps
            if mask == full_mask:
                return steps
            
            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)  # Update the mask to include the neighbor as visited
                state = (neighbor, new_mask)  # New state after visiting the neighbor
                
                # If this state has not been visited, add it to the queue
                if state not in visited:
                    visited.add(state)  # Mark the state as visited
                    queue.append((neighbor, new_mask, steps + 1))  # Enqueue the new state
        
        # According to problem constraints, the graph is connected, so this code should never be reached
        return -1
    
if __name__ == '__main__':
    # Example graphs to test the function
    # graph = [[1,2,3],[0],[0],[0]]  # Example 1
    # graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]  # Example 2
    # graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]  # Example 3
    graph = [[1, 4], [0, 3, 4], [3], [2, 1], [0, 1]]  # Example 4
    s = Solution()
    print(s.shortestPathLength(graph))  # Expected output: 4