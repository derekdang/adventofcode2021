def has_bingo(bingo_board):
    # check rows, continue if condition not met
    for row in bingo_board:
        remaining_nums = list(filter(lambda x: x != '', row))
        if len(remaining_nums) == 0:
            return True
        
    for idy,_ in enumerate(bingo_board[0]):
        for idx,_ in enumerate(bingo_board):
            if bingo_board[idx][idy] == '':
                if idx == len(bingo_board)-1:
                    return True
            else:
                break
    return False

with open("/home/derekdang/adventofcode2021/day04/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.read().splitlines()
    called_nums = data[0].split(',')
    board_inputs = list(filter(lambda x: x != '',data[1:]))
    bingo_boards = list()
    w,h = 5,5
    x = 0
    new_board = [['' for y in range(w)] for h in range(w)]
    for row in board_inputs:
        tmp = row.split()
        for y,num in enumerate(tmp):
            new_board[x][y] = '' + num
        x += 1
        if x == 5:
            x = 0
            bingo_boards.append(new_board)
            new_board = [['' for y in range(w)] for h in range(h)]

    last_called_num = ''
    bingo_found = False
    for called_num in called_nums:
        if bingo_found:
            break
        last_called_num = called_num

        for bingo_board in bingo_boards:
            for x,_ in enumerate(bingo_board):
                for y,_ in enumerate(bingo_board[x]):
                    if bingo_board[x][y] == called_num:
                        bingo_board[x][y] = ''
            if has_bingo(bingo_board):
                # comment out logic for checking if only one Bingo Board remaining in list for part 1
                if len(bingo_boards) == 1: 
                    winning_board = bingo_board
                    bingo_found = True
                else:
                    # keep every board except the one that just got Bingo
                    bingo_boards = [x for x in bingo_boards if x != bingo_board]
    board_total = 0
    for row in winning_board:
        nums_remaining = list(filter(lambda x: x != '', row))
        nums_remaining = list(map(int, nums_remaining))
        board_total += sum(nums_remaining)

    print(f"Board Total * Last Called Num: {board_total * int(last_called_num)}")