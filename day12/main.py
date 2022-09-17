import sys
path = []
num_paths = 0
p2_num_paths = 0
def dfs(graph, small_caves_visited, point):
    global num_paths
    if point == 'end':
        num_paths = num_paths+1
        return
    
    if point in small_caves_visited:
        return
    if point.islower():
        small_caves_visited.append(point)
    for next in graph[point]:
        dfs(graph, small_caves_visited, next)
    if point.islower():
        small_caves_visited.remove(point)
    
def modified_dfs(graph, visit_count, point):
    global p2_num_paths
    if point == 'end':
        p2_num_paths = p2_num_paths+1
        return
    
    if point == "start":
        return
    
    if point.islower() and (visit_count[point] == 1 or visit_count[point] == 2) and 2 in visit_count.values():
            return

    path.append(point)
    if point.islower():
        visit_count[point] = visit_count[point]+1
    for next in graph[point]:
        modified_dfs(graph, visit_count, next)
    if point.islower():
        visit_count[point] = visit_count[point]-1
    path.remove(point)

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    graph = {}
    for line in data:
        dir = line.split('-')
        if dir[0] in graph:
            graph[dir[0]].append(dir[1])
        else:
            graph[dir[0]] = [dir[1]]

        if dir[1] in graph:
            graph[dir[1]].append(dir[0])
        else:
            graph[dir[1]] = [dir[0]]
    
    # keep list of small caves visited
    # remove when backtracking from DFS
    small_caves_visited = ["start"]
    path.append("start")
    visit_count = {}
    for point in graph:
        if point.islower():
            visit_count[point] = 0
    print(visit_count)
    for child in graph["start"]:
        dfs(graph, small_caves_visited, child)
        modified_dfs(graph, visit_count, child)
    print(f"Part 1: {num_paths}")
    print(f"Part 2: {p2_num_paths}")