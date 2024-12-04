import re

search_pattern = r'mul\([0-9]{0,3},[0-9]{0,3}\)'

def main():
    total = []
    with open("data/3.txt") as f:
        for item in re.findall(search_pattern, f.read()):
            x, y = re.findall(r'\d+', item)
            total.append(int(x) * int(y))
        print(sum(total))



if __name__ == "__main__":
    main()
        