import re
from functools import reduce
from operator import mul


search_pattern = r'mul\([0-9]{0,3},[0-9]{0,3}\)'

def part1(data:list) ->int:
    formatted = "".join(data)
    found = re.findall(search_pattern, formatted)
    ans = [ reduce(mul,map(int, re.findall(r'\d+', item))) for item in found ]
    return sum(ans)

def part2(data:list):
    keyword = "do()"
    enable_instructions, temp = [], []
    index = 0

    while len(data) > index:            
        if data[index] == list(keyword)[0]:
            if enable_instructions == []:
                enable_instructions.append(temp)
            temp = []
        temp.append(data[index])

        if data[index:index+4] == list(keyword):
            enable_instructions.append(temp)

        index += 1
    total = [ reduce(mul, map(int,re.findall(r'\d+', c))) for instruction_list in enable_instructions for c in re.findall(search_pattern, "".join(instruction_list)) ]
    return sum(total)

def main():
    data = [ item for item in open("data/3.txt").read() ]
    ans = part1(data)
    print(f"Part 1: {ans}")

    ans2 = part2(data)
    print(f"Part 2: {ans2}")
    
if __name__ == "__main__":
    main()