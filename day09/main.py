def is_low_point(grid,x,y,w,h):
    if grid[y][x] == 9:
        return False
    result = True
    point = grid[y][x]
    steps = [[1,0],[-1,0],[0,1],[0,-1]]
    for step in steps:
        nY = step[1] + y
        nX = step[0] + x
        if nX < 0 or nX == w or nY < 0 or nY == h:
            continue
        result = point < grid[nY][nX]
        if not result:
            break
    return result

def find_basins(grid,visited,x,y,w,h,basin):
    if grid[y][x] == 9 or visited[y][x]:
        return
    visited[y][x] = True
    point = grid[y][x]
    basin.append(point)
    steps = [[1,0],[-1,0],[0,1],[0,-1]]
    for step in steps:
        nY = step[1] + y
        nX = step[0] + x
        if nX < 0 or nX == w or nY < 0 or nY == h:
            continue
        find_basins(grid,visited,nX,nY,w,h,basin)


with open("/home/derekdang/adventofcode2021/day09/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.read().splitlines()
    low_points = list()
    w = len(data[0])
    h = len(data)
    grid = [[0 for x in range(w)] for y in range(h)]
    visited = [[False for x in range(w)] for y in range(h)]
    basin_sizes = list()
    for idy,line in enumerate(data):
        for idx,char in enumerate(line):
            grid[idy][idx] = int(char)
    
    for idy,line in enumerate(grid):
        for idx,point in enumerate(line):
            if is_low_point(grid,idx,idy,w,h):
                low_points.append(grid[idy][idx]+1)
                basin = list()
                find_basins(grid,visited,idx,idy,w,h,basin)
                basin_sizes.append(len(basin))
    print(f"Part 1: Sum of all low points {sum(low_points)}")
    basin_sizes.sort(reverse=True)
    print(f"Part 2: Product of 3 largest basins {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")