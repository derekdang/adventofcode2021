with open("/home/derekdang/adventofcode2021/day02/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.readlines()
    horizontal,depth = 0,0

    for line in data:
        instruction = line.split()
        action = instruction[0]
        value = int(instruction[1])
        
        if action == 'forward':
            horizontal += value
        elif action == 'down':
            depth += value
        elif action == 'up':
            depth -= value
    
    print(f"Part 1: Final Depth * Final Horizontal: {horizontal*depth}")


with open("/home/derekdang/adventofcode2021/day02/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.readlines()
    horizontal,depth,aim = 0,0,0

    for line in data:
        instruction = line.split()
        action = instruction[0]
        value = int(instruction[1])
        
        if action == 'forward':
            horizontal += value
            depth += (aim * value)
        elif action == 'down':
            aim += value
        elif action == 'up':
            aim -= value
    
    print(f"Part 2: Final Depth * Final Horizontal with Aim logic: {horizontal*depth}")