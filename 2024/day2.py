import time 


def magic(unknown_status: list)-> str:

    previous_status = None
    for index, current in enumerate(unknown_status[:-1]):
        next_value = unknown_status[index + 1]

        if current == next_value:
            return "UNSAFE"

        if current > next_value:
            current_status = "decreasing"
            level = current - next_value
        elif current < next_value:
            current_status = "increasing"
            level = next_value - current
        else:
            current_status = "unchanged"
        
        if level < 0 or level > 3:
            return "UNSAFE"

        if previous_status is not None and current_status != previous_status:
            return f"UNSAFE: Status changed from {previous_status} to {current_status} at index {index}"
        
        previous_status = current_status

    return "SAFE"

def main():
    with open("data/2.txt") as f:
        my_list = f.read().splitlines()
        all_things = [ item.split() for item in my_list ]

        counter = 0
        i = 0
        while len(all_things) > i:
            unknown_status = list(map(int, all_things[i]))
            condition = magic(unknown_status)
            if condition == "SAFE":
                counter+=1
            # print(condition)
            i += 1
        print(f"COUNT: {counter}")

if __name__ == "__main__":
    main()