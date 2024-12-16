import time 

def part1(data:list): 

    direction_map = {
        0: (1, 0),    # Right/East
        1: (0, -1),   # Down/South
        2: (-1, 0)    # Left/West
    }


    blocker = None
    visited = 0
    nodelist = []
   
    R = len(data)
    C = len(data[0])

    for i in range(R):
        for j in range(C):
            nodelist.append([i,j])
            if "^" == data[i][j]:
                x, y = [i, j]
    print(f"{x},{y}")
    while blocker != "#":
        try: 

            for i in range(R-y+1): 
                visited+=1
                if data[x][y] == "#":
                    x, y = [x+1, y] 
                    print(f"\nbefore hit {x}:{y}")
                    break
                x -= 1


            for i in range(R):
                visited+=1
                if data[x][y] == "#":
                    x, y = [x, y-1] 
                    print(f"before hit {x}:{y}")
                    break
                y += 1
            

            for i in range((R-x)-1):
                visited+=1
                if data[x][y] == "#":
                    x, y = [x-1, y]
                    print(f"before hit {x}:{y}")
                    break
                x+=1
            
            for i in range(R):
                visited+=1
                if data[x][y] == "#":
                    x, y = [x, y+1]
                    print(f"before hit {x}:{y}")
                    break
                y -= 1
        except IndexError:
            print("stop")
        print(visited)
        break





        # time.sleep(10)

        


        # visited += 1
        # postioon_up = x - 1 
        # starting_position = data[postioon_up][y]
        # if starting_position == "#":
        #     blocker = starting_position
        #     print(f"\n{postioon_up+1},{y}")
        # x -= 1
        

def main():
    visual = open("sample_data/6.txt").read()
    print(visual)

    data = open("sample_data/6.txt").read().strip().split()
    print(type(data))
    part1(data)


if __name__ == "__main__":
    main()

    