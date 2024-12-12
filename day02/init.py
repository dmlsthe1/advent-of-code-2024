

def main(path):
    count = 0
    with open(path, 'r') as file:
        for idx, row in enumerate(file, start=1):
            levels = row.strip().split(' ')
            prev = None
            direction = None
            for i, _curr in enumerate(levels, start=1):
                curr = int(_curr)
                if prev == None:
                    prev = curr
                    continue
                if curr == prev:
                    # print(f'index: {idx}, levels: {levels}, count: {count}')
                    break
                if direction == None:
                    direction = 'up' if curr > prev else 'down'
                diff = curr - prev if direction == 'up' else prev - curr
                prev = curr
                if 0 >= diff or diff >= 4:
                    # print(f'index: {idx}, levels: {levels}, count: {count}')
                    break
            else:
                count += 1
                # print(f'increment: {count}')
    print(count)
    return count

if __name__ == '__main__':
    main('data.py')
