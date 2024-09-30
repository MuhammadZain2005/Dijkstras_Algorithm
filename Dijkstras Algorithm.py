"""
Dijkstra Theorem

Difficulty: 4/10

Comments: Simple just map/neighbor logic. Just had to think how to implement it properly.
"""

import heapq


def dijkstra(graph, start):
    # Initialize the distances dictionary with infinite distance for each node
    distances = {node: float('inf') for node in graph}
    # Set the distance to the starting node to zero
    distances[start] = 0

    # Priority queue to hold the nodes to explore
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the distance to the current node is greater than the recorded shortest distance, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
