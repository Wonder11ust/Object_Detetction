edge = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A','F','G'],
    'D': ['B','H'],
    'E': ['B','I'],
    'F': ['C'],
    'G': ['C','J','K'],
    'H': ['D'],
    'I':['E'],
    'J':['G'],
    'K':['G','L'],
    'L':['K']
}


def dfs(graf, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        stack_len = len(stack) - 1
        edge = stack.pop(stack_len)
        state = edge[-1]

        if state == goal:
            return edge
        elif state not in visited:
            for cabang in graf.get(state, []):
                new_edge = list(edge)
                new_edge.append(cabang)
                stack.append(new_edge)

            visited.add(state)

        isi = len(stack)
        if isi == 0:
            print("Not found")


print(dfs(edge, 'E', 'L'))