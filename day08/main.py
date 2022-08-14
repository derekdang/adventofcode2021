with open("/home/derekdang/adventofcode2021/day08/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.read().splitlines()
    # count_1478 = 0 # 1 = 2, 4 = 4, 7 = 3, 8 = 7
    # keys = [2,4,3,7]
    # for line in data:
    #     split = line.split('|')
    #     output = split[1].split()
    #     for value in output:
    #         if len(value) in keys:
    #             count_1478 = count_1478+1
    # print(f"Part 1: # of 1's 4's 7's 8's in output: {count_1478}")
    sum = 0
    for line in data:
        split = line.split('|')
        signals = split[0].split()

        signals.sort(key=len)
        mapping = list()
        for s in signals:
            mapping.append(''.join(sorted(s)))
        top_char = mapping[1]
        for char in mapping[0]:
            top_char = top_char.replace(char, '')
        
        up_left_mid_char = mapping[2]
        for char in mapping[0]:
            up_left_mid_char = up_left_mid_char.replace(char, '')

        bot_left_bot_char = mapping[len(mapping)-1]
        for char in mapping[0]:
            bot_left_bot_char = bot_left_bot_char.replace(char, '')
        for char in up_left_mid_char:
            bot_left_bot_char = bot_left_bot_char.replace(char, '')
        bot_left_bot_char = bot_left_bot_char.replace(top_char, '')

        nine_key = "abcdefg"
        # solve 9 by finding mapping w/o bot left char
        bot_left_char,bot_char = '',''
        for char in bot_left_bot_char:
            s = nine_key.replace(char, '')
            if s in mapping:
                nine_key = s
                bot_left_char = char
                bot_char = bot_left_bot_char.replace(bot_left_char, '')
                break

        six_key = "abcdefg"
        # solve 6 by finding mapping w/o top right char
        top_right_char,bot_right_char = '',''
        for char in mapping[0]:
            s = six_key.replace(char, '')
            if s in mapping:
                six_key = s
                top_right_char = char
                bot_right_char = mapping[0].replace(top_right_char, '')
                break
        
        zero_key = "abcdefg"
        # solve 0 by finding mapping w/o mid char
        top_left_char,mid_char = '',''
        for char in up_left_mid_char:
            s = zero_key.replace(char, '')
            if s in mapping:
                zero_key = s
                mid_char = char
                top_left_char = up_left_mid_char.replace(mid_char, '')
                break
        
        # 2
        two_key = 'abcdefg'.replace(top_left_char, '').replace(bot_right_char, '')
        # 5
        five_key = 'abcdefg'.replace(top_right_char, '').replace(bot_left_char, '')
        # 3
        three_key = 'abcdefg'.replace(top_left_char, '').replace(bot_left_char, '')
        decoder = {zero_key:'0', mapping[0]:'1', two_key:'2', three_key:'3', mapping[2]:'4', five_key:'5', six_key:'6', mapping[1]:'7', 'abcdefg':'8', nine_key:'9'}
        outputs = split[1].split()
        code = ""
        for output in outputs:
            key = "".join(sorted(output))
            code = code + decoder[key]
        sum = sum + int(code)
    print(f"Part 2 Output Total: {sum}")