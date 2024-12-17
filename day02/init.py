import sys

def getData(path):
    rows = []
    with open(path, 'r') as file:
        for row in file:
            columns = row.strip().split(' ')
            rows.append(columns)
    return rows

def calc(rows):
    count = 0
    for idx, levels in enumerate(rows, start=1):
        prev = None
        direction = None
        for _curr in levels:
            curr = int(_curr)
            if prev == None:
                prev = curr
                continue
            if curr == prev:
                break
            if direction == None:
                direction = 'up' if curr > prev else 'down'
            diff = curr - prev if direction == 'up' else prev - curr
            prev = curr
            if 0 >= diff or diff >= 4:
                break
        else:
            count += 1
    return count

def calc2(rows):
    count = 0
    tolerance = 1
    for levels in rows:
        prev = None
        direction = None
        tolerance = 1

        # print(f'levels: {levels}')
        for _curr in levels:
            # print(f'curr: {_curr}')
            curr = int(_curr)
            if prev == None:
                prev = curr
                continue

            if curr == prev:
                if tolerance == 0:
                    # print(f'break (curr == prev): {_curr} {prev}')
                    break
                tolerance -= 1
                # print(f'cont (curr == prev): {_curr} {prev}')
                continue

            if direction == None:
                direction = 'up' if curr > prev else 'down'

            diff = curr - prev if direction == 'up' else prev - curr
            if 0 >= diff or diff >= 4:
                if tolerance == 0:
                    # print(f'break (diff): {diff}')
                    break
                tolerance -= 1
                # print(f'cont (diff): {diff}')
                direction = None
                continue

            prev = curr
        else:
            # print(f'count: {levels}')
            count += 1
    return count

def part1(rows, exp_ans = 246):
    ans = calc(rows)
    if ans != exp_ans:
        print(f'Part1 Incorrect: Expected {exp_ans} but got {ans}') 
        return False
    print(f'Part1 Correct: {ans}')
    return True

def part2(rows, exp_ans = 246):
    ans = calc2(rows)
    if ans != exp_ans:
        print(f'Part2 Incorrect: Expected {exp_ans} but got {ans}') 
        return False
    print(f'Part2 Correct: {ans}')
    return True

def main(path, exp_ans_p1=246, exp_ans_p2=246):
    rows = getData(path)
    p1 = part1(rows, exp_ans_p1)
    p2 = part2(rows, exp_ans_p2)
    if not p1 or not p2:
        sys.exit(1)

if __name__ == '__main__':
    main('data.py')
    # main('sample.py', 2, 4)
