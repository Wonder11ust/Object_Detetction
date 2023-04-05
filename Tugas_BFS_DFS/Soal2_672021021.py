graphs = {'A':[''],
          'B': ['A','C','E'],
          'C': ['D'],
          'D': ['H'],
          'E': ['C'],
          'F': ['E'],
          'G': ['F'],
          'H': ['A','G'],

       }


def bfs(graph, start, end):
    visited = []
    queue = [[start]]

    if start == end:
        # print("Node sama")
        return "Node yang dituju sama dengan node awal"

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                newNode = list(path)
                newNode.append(neighbour)
                queue.append(newNode)

                if neighbour == end:
                    return newNode
            visited.append(node)
    return "Tidak ada jalur"



print("Jalur yang dilewati dari G ke A: " + str(bfs(graphs, 'G', 'A')))