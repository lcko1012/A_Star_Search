def aStar(initialState, goal):

    #tao frontier, va explored
    frontier = set(initialState)
    explored = set()
    #khoang cach tu initialState
    g = {}
    parents_node = {}

    g[initialState] = 0
    parents_node[initialState] = initialState

    while len(frontier) > 0:
        n = None
        #print(frontier)
        #print(g)
        #cac phan tu dag xet trong frontier
        for m in frontier:
            #neu g(dang xet) + h(dang xet) < g(canh truoc) + h(canh truoc)
            if n == None or g[m] + heuristic(m) < g[n] + heuristic(n):
                n = m

        if n == goal or Graph_nodes[n] == None:
            pass
        else:
            for (node, weight) in get_neighbors(n):
                #neu node khong o trong frontier va khong trong explored
                #add vao frontier, nhanh con cua node la n
                #cong khoang cach toi node
                if node not in frontier and node not in explored:
                    frontier.add(node)
                    parents_node[node] = n
                    g[node] = g[n] + weight

                #neu co trong ca frontier va explored
                else:
                    #neu ma g[n] lon hon thi cap nhat lai gia
                    if g[node] > g[n] + weight:
                        g[node] = g[n] + weight
                        #thay doi luon duong di nuoc buoc
                        parents_node[node] = n

                        #truong hop co da xet thi lay ra xet lai
                        if node in explored:
                            explored.remove(node)
                            frontier.add(node)

        if n == None:
            print('Khong ton tai')
            return None

        if n == goal:
            result = []

            while parents_node[n] != n:
                result.append(n)
                n = parents_node[n]

            result.append(initialState)

            result.reverse()

            print("Result: ", result)
            return result

        frontier.remove(n)
        explored.add(n)

    print('Khong ton tai')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {
        'A': 6,
        'B': 3,
        'C': 4,
        'D': 5,
        'E': 3,
        'F': 6,
        'G': 6,
        'H': 2,
        'I': 5,
        'J': 4,
        'K': 2,
        'L': 0,
        'M': 4,
        'N': 0,
        'O': 4,
    }

    return H_dist[n]


#Describe your graph here
Graph_nodes = {
    'A': [('B', 2), ('C', 1), ('D', 3)],
    'B': [('E', 1), ('F', 4)],
    'C': [('G', 6), ('H', 3)],
    'D': [('I', 2), ('J', 4)],
    'E': None,
    'F': [('K', 2), ('L', 1), ('M', 4)],
    'G': None,
    'H': [('N', 2), ('O', 4)],
    'I': None,
    'J': None,
    'K': None,
    'L': None,
    'M': None,
    'N': None,
    'O': None

}
aStar('A', 'L')
