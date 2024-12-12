
def getData(path):
    list1=[]
    list2=[]
    dict1={}
    dict2={}
    with open(path, 'r') as file:
        for row in file:
            [left, right] = row.strip().split()
            list1.append(left)
            list2.append(right)
            dict1[left] = dict1.get(left, 0) + 1
            dict2[right] = dict2.get(right, 0) + 1
    return  list1, list2, dict1, dict2

def parse(dict1, dict2):
    dict1=dict(sorted(dict1.items()))
    dict2=dict(sorted(dict2.items()))
    return dict1, dict2

def calc(dict1, dict2):
    total=0
    dict1={**dict1}
    dict2={**dict2}
    for val1 in dict1:
        for quantity in range(dict1[val1]):
            for val2 in dict2:
                if dict2[val2] == 0:
                    continue
                dict2[val2] -= 1
                num1, num2 = int(val1), int(val2)
                diff = num2 - num1 if num2 > num1 else num1 - num2
                total += diff
                break

    return total

def calc2(list1, dict2):
    total=0
    for val in list1:
        total += int(val) * int(dict2.get(val, 0))
    return total

def main(path):
    list1, list2, data1, data2 = getData(path)
    dict1, dict2 = parse(data1, data2)
    ans = calc(dict1, dict2)
    ans2 = calc2(list1, dict2)
    print(f'answer p1: {ans}')
    print(f'answer p2: {ans2}')

if __name__ == '__main__':
    main('data.py')
