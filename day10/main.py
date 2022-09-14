with open("/home/derekdang/adventofcode2021/day10/input.txt", encoding='utf-8', newline='\n') as file:
    data = file.read().splitlines()
    first_illegal_chars = {')':0, ']':0, '}':0, '>':0}
    values = {')':3, ']':57, '}':1197, '>':25137}
    incomplete_lines = []
    for line in data:
        stack = []
        legal_line = True
        for char in line:
            if char in first_illegal_chars:
                last = stack[len(stack)-1]
            if char == ')':
                if last != '(':
                    first_illegal_chars[char] = first_illegal_chars[char]+1
                    legal_line = False
                    break
                else:
                    stack.pop()
            elif char == ']':
                if last != '[':
                    first_illegal_chars[char] = first_illegal_chars[char]+1
                    legal_line = False
                    break
                else:
                    stack.pop()
            elif char == '}':
                if last != '{':
                    first_illegal_chars[char] = first_illegal_chars[char]+1
                    legal_line = False
                    break
                else:
                    stack.pop()
            elif char == '>':
                if last != '<':
                    first_illegal_chars[char] = first_illegal_chars[char]+1
                    legal_line = False
                    break
                else:
                    stack.pop()
            if char not in first_illegal_chars:
                stack.append(char)
        if legal_line:
            incomplete_lines.append(stack)
    sum = 0
    for key in first_illegal_chars:
        sum = sum + values[key] * first_illegal_chars[key]
    print(f'Part 1 - Total Syntax Error: {sum}')

    autocomplete_values = {'(':1, '[':2, '{':3, '<':4}
    completion_scores = []
    for line in incomplete_lines:
        score = 0
        for char in reversed(line):
            score = score * 5
            score = score + autocomplete_values[char]
        completion_scores.append(score)
    sorted_scores = sorted(completion_scores)
    midpoint = int (len(sorted_scores)/2)
    print(f'Part 2 - Middle Score for Autocompleter: {sorted_scores[midpoint]}')