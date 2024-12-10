import time

def part1(data:str) -> list:

    R = len(data)
    C = len(data[0])

    ans = 0
    for i in range(R):
        for j in range(C):
            # front
            if j < C - 3 and data[i][j] == 'X' and data[i][j+1] == 'M' and data[i][j+2] == 'A' and  data[i][j+3] == 'S':
                ans += 1
            # back
            if j > 2 and data[i][j] == 'X' and data[i][j-1] == 'M' and data[i][j-2] == 'A' and  data[i][j-3] == 'S':
                ans += 1
            # down
            if i < R - 3 and data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and  data[i+3][j] == 'S':
                ans += 1
            # up
            if i > 2 and data[i][j] == 'X' and data[i-1][j] == 'M' and data[i-2][j] == 'A' and  data[i-3][j] == 'S':
                ans += 1
            # diag left down 
            if i < R - 3 and j > 2 and data[i][j] == 'X' and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and  data[i+3][j-3] == 'S':
                ans += 1
            # diag right up
            if i > 2 and j < C - 3 and data[i][j] == 'X' and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and  data[i-3][j+3] == 'S':
                ans += 1
            # diag right down
            if i < R - 3 and j < C - 3 and data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and  data[i+3][j+3] == 'S':
                ans += 1
            # diag left up 
            if j > 2 and i > 2 and data[i][j] == 'X' and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and  data[i-3][j-3] == 'S':
                ans += 1 
    
    return ans

def main():
    data = open("data/4.txt").read().strip().split("\n")
    
    ans = part1(data)
    print(ans)

if __name__ == "__main__":
    main()