import sys

def flash(grid, flashed, x, y, w, h):
    if flashed[y][x]:
        return
    flashed[y][x] = True
    steps = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
    for step in steps:
        nY = y + step[0]
        nX = x + step[1]
        if nX < 0 or nX == w or nY < 0 or nY == h:
            continue
        grid[nY][nX] = grid[nY][nX] + 1
        if grid[nY][nX] > 9 and not flashed[nY][nX]:
            flash(grid,flashed,nX,nY,w,h)

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    w,h = 10,10
    grid = [[0 for x in range(w)] for y in range(h)]
    flashed = [[False for x in range(w)] for y in range(h)]
    for idy,line in enumerate(data):
        for idx,char in enumerate(line):
            grid[idy][idx] = int(char)
    
    num_flashes = 0
    for i in range(1000):
        for y,line in enumerate(grid):
            for x,n in enumerate(line):
                grid[y][x] = n+1
        
        for y,line in enumerate(grid):
            for x,n in enumerate(line):
                if grid[y][x] > 9 and not flashed[y][x]:
                    flash(grid,flashed,x,y,w,h)
        
        for y,line in enumerate(flashed):
            for x,bool in enumerate(line):
                if bool:
                    num_flashes = num_flashes+1
                    grid[y][x] = 0
        
        all_flashing = True
        for line in flashed:
            if all_flashing:
                for bool in line:
                    if not bool:
                        all_flashing = False
        
        if all_flashing:
            print(f"Part 2: All Flash: Step {i+1}")
            break
        if i == 99:
            print(f"Part 1: Number of Flashes after 100 steps: {num_flashes}")
        flashed = [[False for x in range(w)] for y in range(h)]
    