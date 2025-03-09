def graphDFS(G, start, goal):
    # G = (V,E) is the graph with vertices, V, and edges, E.
    V,E = G
    stack = Stack()
    visited = Set()
    stack.push([start]) # The stack is a stack of paths

    while not stack.isEmpty():
        # A path is popped from the stack.
        path = stack.pop()
        current = path[0] # the last vertex in the path.
        if not current in visited:
            # The current vertex is added to the visited set.
            visited.add(current)

            # If the current vertex is the goal vertex, then we discontinue the
            # search reporting that we found the goal.
            if current == goal:
                return path # return path to goal

            # Otherwise, for every adjacent vertex, v, to the current vertex
            # in the graph, v is pushed on the stack of paths yet to search
            # unless v is already in the path in which case the edge
            # leading to v is ignored.
            for v in adjacent(current,E):
                if not v in path:
                    stack.push([v]+path)

    # If we get this far, then we did not find the goal.
    return [] # return an empty path
