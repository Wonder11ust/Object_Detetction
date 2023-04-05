graphs = {'A': ['C'],
          'B': ['A'],
          'C': ['D', 'F'],
          'D': ['B', 'G'],
          'E': ['B', 'G'],
          'F': ['I'],
          'G': ['J'],
          'H': ['E'],
          'I': ['D'],
          'J': ['H', 'I']}


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


# nodeAwal = input("Masukkan node awal: ")
# nodeTujuan = input("Masukkan node tujuan: ")
print("Jalur yang dilewati: " + str(bfs(graphs, 'J', 'C')))