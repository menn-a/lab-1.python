from collections import deque

def bfs_tree(tree, root, goal, trace=None):
    queue =deque()                    # Complete Code
    queue.append([root])
    
                   # Complete Code
    visited = []

    while queue:                        # Complete Condition
        path = queue.popleft()             # Complete Code
        node = path[-1]                      # the node we are standing on
        visited.append(node)

        if node==goal:                       # Complete Condition
            record(trace, node, [p[-1] for p in queue], visited)
            return path

        for child in tree.get(node, []):             # Complete Code
            queue.append(path + [child])     # new path = old path plus the child

        record(trace, node, [p[-1] for p in queue], visited)

    return None                              # no path to the goal exists



#//////////////////////////////////////////////////////////////////////////////////////////////#

def bfs_graph(graph, start, goal, trace=None):
    queue = [[start]]                      # a list used as a queue
    visited = []

    while  queue :                   # Complete Condition
        path = queue.pop(0)             # Complete Code
        node = path[-1]

        if node in visited:                # already handled through another route
            continue                      # Complete Code
       
        visited.append(node)

        if node == goal:                      # Complete Condition
            record(trace, node, [p[-1] for p in queue], visited)
            return path

        for neighbor in graph.get(node, []):         # Complete Code
            if neighbor not in visited:  # Complete Code
                queue.append(path + [neighbor])

        record(trace, node, [p[-1] for p in queue], visited)

    return None