import time

def part1(data:str) -> list:

    R = len(data)
    C = len(data[0])

    ans = 0
    for i in range(R):
        for j in range(C):
            try:
                if j < C - 3 and data[i][j] == 'X' and data[i][j+1] == 'M' and data[i][j+2] == 'A' and  data[i][j+3] == 'S':
                    ans += 1
                
            except IndexError:
                continue
    return ans

def main():
    data = open("sample_data/4.txt").read().strip().split("\n")
    ans = part1(data)
    print(ans)

if __name__ == "__main__":
    main()