# Graph Theory Algorithms in Python

A collection of graph theory algorithm implementations built as undergraduate coursework (circa 2020). Includes **Hierholzer's Algorithm** for finding Eulerian circuits and a **non-greedy Minimum Spanning Tree (MST)** algorithm.

> **Note:** This was a university assignment — the code is preserved as-is for archival purposes, bugs and all. 🎓

> **Python version:** Python 3.6+

## 💡 Quick Glossary

| Term | What it means |
|------|---------------|
| **Graph** | A set of **vertices** (nodes) connected by **edges** (links) |
| **Adjacency Matrix** | An *N×N* grid where cell *(i, j)* is `1` (or a weight) if vertices *i* and *j* are connected, `0` (or `inf`) otherwise |
| **Adjacency List** | A more compact representation — each vertex maps to a list of its neighbors |
| **Eulerian Circuit** | A path that traverses **every edge exactly once** and returns to the starting vertex. Only possible when every vertex has even degree |
| **DFS (Depth-First Search)** | A traversal strategy that explores as far as possible along each branch before backtracking |
| **MST (Minimum Spanning Tree)** | A subset of edges that connects all vertices with the minimum total weight and no cycles |
| **Cycle** | A path that starts and ends at the same vertex without repeating edges |

## 📂 Project Structure

```
├── Hierholzer/              # Eulerian circuit finder
│   ├── main.py              # Entry point
│   ├── hierholzer.py        # Core Hierholzer's algorithm
│   ├── graph.py             # Graph class (minimal)
│   ├── dfs.py               # Modified DFS for cycle detection
│   ├── converter.py         # Adjacency matrix → adjacency list
│   ├── read_input.py        # File I/O
│   ├── samples/             # Sample graph inputs
│   │   ├── base_input.txt
│   │   ├── k5_graph.txt
│   │   ├── semi_eulerian_graph.txt
│   │   ├── not_eulerian_graph.txt
│   │   └── ...
│   └── test/                # Test input directory (place your .txt here)
│       └── input.txt
│
└── MST-Not-Greedy/          # Non-greedy MST algorithm
    ├── main.py              # Entry point
    ├── mst_alt.py           # MST algorithm (add edge, break heaviest in cycle)
    ├── dfs.py               # Cycle detection via DFS
    ├── converter.py         # Matrix → list with edge weights
    ├── read_input.py        # File I/O (supports weighted/inf matrices)
    ├── samples/             # Sample weighted graph inputs
    │   ├── example-12
    │   ├── example_with_1_weight-5
    │   ├── forest
    │   ├── with_negative_weights
    │   └── ...
    └── test/                # Test input directory (place your .txt here)
        └── input.txt
```

## 🔷 Hierholzer's Algorithm

Finds **Eulerian circuits** (paths that visit every edge exactly once and return to the start) in undirected graphs using [Hierholzer's algorithm](https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm).

### Input Format

A `.txt` file placed in `Hierholzer/test/` with the following structure:

```
9                           # Number of vertices
0 1 0 1 0 0 0 0 0          # Adjacency matrix (symmetric, 0/1)
1 0 1 1 1 0 0 0 0
0 1 0 0 1 0 0 0 0
1 1 0 0 1 0 0 1 0
0 1 1 1 0 1 1 1 0
0 0 0 0 1 0 0 0 1
0 0 0 0 1 0 0 1 0
0 0 0 1 1 0 1 0 1
0 0 0 0 0 1 0 1 0
```

### Running

```bash
cd Hierholzer
cp samples/base_input.txt test/input.txt   # or use your own
python3 main.py
```

### Sample Output

```
Reading input test file inside sample directory
Graph size:  9
Adjacency Matrix:  [[0, 1, 0, 1, ...], ...]
[(0, 1), (0, 3), (1, 0), (1, 2), ...]
Cycle found:  [5]
Euler tour at the moment:  [8, 5]
Cycle found:  [4]
Euler tour at the moment:  [8, 5, 4]
...
```

## 🔶 MST — Non-Greedy Approach

Computes a **Minimum Spanning Tree** using a non-greedy strategy: edges are added one by one (in arbitrary order), and whenever a cycle is formed, the heaviest edge in that cycle is removed.

### Input Format

A `.txt` file placed in `MST-Not-Greedy/test/` with a weighted adjacency matrix (`inf` for no connection):

```
6
0 1 1 1 inf inf
1 0 1 inf 1 inf
1 1 0 1 1 1
1 inf 1 0 inf 1
inf 1 1 inf 0 1
inf inf 1 1 1 0
```

### Running

```bash
cd MST-Not-Greedy
cp samples/example_with_1_weight-5 test/input.txt   # or use your own
python3 main.py
```

### Sample Output

```
Reading input test file inside test/ directory...
Graph:  {0: [1, 2], 1: [0, 2], 2: [0, 1], ...}
Edges:  {(0, 1): 1, (0, 2): 1, ...}
Aresta inserida:  (0, 1) Peso:  1
Solucao parcial MST:  {(0, 1): 1}
...
Solucao final MST:  {...}
Peso total da MST obtida:  5
```

## ⚙️ Requirements

- Python 3.6+
- No external dependencies (stdlib only)

## 👥 Contributors

- **Victor Medeiros** ([@medeirosvictor](https://github.com/medeirosvictor))
- **Diogo Lopes** ([@cirddan](https://github.com/cirddan))

## 📚 References

- [Hierholzer's Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm)
- [The Hitchhiker's Guide to Python — Project Structure](http://docs.python-guide.org/en/latest/writing/structure/)
