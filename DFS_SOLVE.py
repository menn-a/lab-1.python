from queue import LifoQueue

def dfs_tree(tree, root, goal, trace=None):
    stack =LifoQueue()                       # Complete Code
    stack.put([root])                   # Complete Code
    visited = []

    while not stack.empty():       # Complete Condition
        path = stack.get()                   # the node we are standing on
        node = path[-1]
        visited.append(node)

        if node == goal:                      # Complete Condition
            record(trace, node, [p[-1] for p in stack.queue], visited)
            return path

        for child in reversed(tree.get(node, [])):            # Complete Code
            stack.put(path + [child])    # new path = old path plus the child

        record(trace, node, [p[-1] for p in stack.queue], visited)

    return None                             # no path to the goal exists




                                                   ##///////////////////##
                                                   
    def dfs_graph(graph, start, goal, trace=None):
         stack = [[start]]                    
    visited = []

    while stack:                     # Complete Condition
        path = stack.pop()                 # Complete Code
        node = path[-1]

        if node in visited:                    # Complete Condition
            continue

        visited.append(node)

        if node == goal:                    # Complete Condition
            record(trace, node, [p[-1] for p in stack], visited)
            return path

        for neighbor in graph.get(node, []):       # Complete Code
            if neighbor not in visited: # Complete Condition
                stack.append(path + [neighbor])

        record(trace, node, [p[-1] for p in stack], visited)

    return None