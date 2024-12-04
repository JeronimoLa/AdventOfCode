import time 



def magic(unknown_status: list):
# print (unknown_status)
    decreasing = True
    increasing = True

    previous_status = None
    for unknown in range(len(unknown_status)-1):
        print(f"first index: {unknown_status[unknown]} second index: {unknown_status[unknown+1]}")
        if int(unknown_status[unknown]) > int(unknown_status[unknown+1]):
            level = int(unknown_status[unknown]) - int(unknown_status[unknown+1])
            print(level)
            if int(unknown_status[unknown]) > int(unknown_status[unknown+1]):
                current_status = decreasing
            else:
                current_status = increasing

            if previous_status == None:
                if level > 0 and level <= 3:
                    previous_status = current_status
                    continue 
                else:
                    return f"UNSAFE 1: {list (unknown_status)}"

            if previous_status == current_status:
                if level > 0 and level <= 3:
                    previous_status = current_status
                    continue 
                else:
                    return f"UNSAFE 2: {list(unknown_status)}"
            else:
                return f"UNSAFE 3: {list(unknown_status)}"

        elif int(unknown_status[unknown]) < int(unknown_status[unknown+1]):
            # return f"UNSAFE 4: (list(unknown_status)}"
            level = int(unknown_status[unknown+1]) - int(unknown_status[unknown])
            if int(unknown_status[unknown+1]) < int(unknown_status[unknown]):
                current_status = increasing
            else:
                current_status = False

            if previous_status == None:
                if level > 0 and level <= 3:
                    previous_status = current_status
                    continue
                else:
                    return f"UNSAFE 4: {list(unknown_status)}"
            if previous_status == current_status:
                if level >= 1 and level <= 3:
                    previous_status = current_status
                    continue 
                else:
                    return f"UNSAFE 5: {list (unknown_status)}"
            else:
                return f"UNSAFE 6: {list (unknown_status)}"
        else:
            return f"UNSAFE 7: {list (unknown_status)}"



def main():
    with open("data/2.txt") as f:
        my_list = f.read().splitlines()
        all_things = [ item.split() for item in my_list ]




        counter = 0
        i = 0
        while len(all_things) > i:
            unknown_status = all_things[i]
            condition = magic(unknown_status)
            if condition is None:
                counter+=1
            # print(condition)
            i += 1
        print(f"COUNT: {counter}")


if __name__ == "__main__":
    main()


    # 261