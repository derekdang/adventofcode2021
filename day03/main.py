with open("/home/derekdang/adventofcode2021/day03/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.read().splitlines()
    size = len(data)
    count_one_bits = [0] * len(data[0])

    for line in data:
        for idx,bit in enumerate(line):
            if bit == '1':
                count_one_bits[idx] += 1
    
    gamma_string = ""
    epsilon_string = ""
    for count in count_one_bits:
        if count > size/2:
            gamma_string = gamma_string + '1'
            epsilon_string = epsilon_string + '0'
        else:
            gamma_string = gamma_string + '0'
            epsilon_string = epsilon_string + '1'
    
    gamma_int = int(gamma_string, 2)
    epsilon_int = int(epsilon_string, 2)

    print(f"Part 1: Power Consumption of Submarine (gamma rate * epsilon rate): {gamma_int * epsilon_int}")


    mcb_list = data
    lcb_list = data
    count_bits = [0] * len(data[0])
    index = 0
    while len(mcb_list) > 1:
        for line in mcb_list:
            for idx,bit in enumerate(line):
                if bit == '1':
                    count_bits[idx] += 1
        
        if count_bits[index] >= len(mcb_list)/2:
            most_common_char = '1'
        else:
            most_common_char = '0'

        mcb_list = list(filter(lambda x: x[index] == most_common_char, mcb_list))

        index += 1
        count_bits = [0] * len(data[0])
            
    index = 0
    while len(lcb_list) > 1:
        for line in lcb_list:
            for idx,bit in enumerate(line):
                if bit == '1':
                    count_bits[idx] += 1

        if count_bits[index] < len(lcb_list)/2:
            least_common_char = '1'
        else:
            least_common_char = '0'

        lcb_list = list(filter(lambda x: x[index] == least_common_char, lcb_list))
        index += 1
        count_bits = [0] * len(data[0])
    
    oxygen_int = int(mcb_list[0], 2)
    co2_int = int(lcb_list[0], 2)

    print(f"Part 2: Life Support Rating (oxygen rating * co2 rating): {oxygen_int * co2_int}")