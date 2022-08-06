with open("/home/derekdang/adventofcode2021/day05/input.txt", encoding='utf-8', newline='\n') as file:
    w,h = 1000,1000
    grid = [[0 for x in range(w)] for y in range(h)]
    data = file.read().splitlines()
    for line in data:
        parsed = line.split(' -> ')
        point1 = parsed[0].split(',')
        point2 = parsed[1].split(',')
        x1 = int(point1[0])
        x2 = int(point2[0])
        y1 = int(point1[1])
        y2 = int(point2[1])

        # vertical line logic
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                grid[y][x1] = grid[y][x1]+1
        # horizontal line logic
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                grid[y1][x] = grid[y1][x]+1
        # diagonal line logic
        else:
            if x1 > x2:
                tmp_x = x2
                x2 = x1
                x1 = tmp_x
                tmp_y = y2
                y2 = y1
                y1 = tmp_y
            y = y1
            for x in range(x1, x2+1):
                grid[y][x] = grid[y][x]+1
                if (y1 < y2):
                    y = y+1
                else:
                    y = y-1
    count_overlap = 0
    for line in grid:
        for point in line:
            if point > 1:
                count_overlap = count_overlap + 1
    # comment out diagonal line logic for Part 1 answer
    print(f"Points w/ more than 1 overlap: {count_overlap}")