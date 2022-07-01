with open("/home/derekdang/adventofcode2021/day01/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.readlines()
    data = list(map(int, data))

    recent_max = data[0]
    num_increases = 0

    for num in data:
        value = num
        if value > recent_max:
            recent_max = value
            num_increases += 1
        else:
            recent_max = value       

    print(f"Part 1: Number of Increases from Previous Value: {num_increases}")   

    window1 = data[0:2]
    sum1 = sum(window1)
    window_increases = 0
    for idx,num in enumerate(data, start=3):
        window2 = data[idx-2:idx+1]
        sum2 = sum(window2)

        if sum2 > sum1:
            window_increases += 1
        sum1 = sum2
    
    print(f"Part 2: Number of Increases w/ Sliding Window: {window_increases}")