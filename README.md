# Dijkstra's Algorithm

## Description

The **Dijkstra's Algorithm** program is a Python implementation of the classic shortest path algorithm, widely used to find the shortest path between nodes in a graph. This program provides a clear and efficient solution for weighted graphs, using a priority queue to select the minimum distance path.

## Features

- **Shortest Path Calculation:** Determines the shortest path from the starting node to all other nodes in the graph.
- **Step-by-Step Exploration:** Utilizes a priority queue (min-heap) to explore each node's neighbors based on their weights.
- **Flexible Graph Representation:** Easily modify the graph structure by adding or removing nodes and edges.
- **Distance Tracking:** The program maintains a dictionary of distances, displaying the shortest path to each node.

## How It Works

The program performs the following steps:

1. **Input:** The graph is defined using a dictionary, where each key is a node, and the value is a list of tuples representing its neighbors and corresponding weights.
2. **Initialization:** All nodes are initialized with infinite distances except the starting node, which is set to zero.
3. **Priority Queue:** Nodes are pushed into a priority queue based on their current distance values.
4. **Neighbor Exploration:** The program explores each node, updating the shortest path for its neighbors if a shorter route is found.
5. **Output:** The dictionary of shortest distances is returned, showing the shortest path from the starting node to all other nodes.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script file `dijkstra_algorithm.py`.
2. Run the script using Python:

    ```bash
    python dijkstra_algorithm.py
    ```

3. The program will compute the shortest paths for a sample graph structure.
4. Modify the graph or parameters directly in the script to customize the program's behavior.

### Example

```bash
$ python dijkstra_algorithm.py

Original Graph: {'A': [('B', 1), ('C', 4)], 'B': [('A', 1), ('C', 2), ('D', 5)], 'C': [('A', 4), ('B', 2), ('D', 1)], 'D': [('B', 5), ('C', 1)]}

Shortest Paths from Node 'A': {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```
## Program Structure

- **`dijkstra(graph, start)`**: Implements Dijkstra's algorithm to compute the shortest path.
- **`main()`**: Sets up the sample graph and displays the shortest distances.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
