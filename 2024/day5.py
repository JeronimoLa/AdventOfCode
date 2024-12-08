import time

def part1(data:list):

    split = data.index('')
    rules = data[0:split]
    updates = data[split+1:len(data)]
    print(updates)


    for update in updates:
        something = update.split(",")
        print(len(something))
        for index, value in enumerate(something):
            if index == 0:
                result = "|".join(list([something[index], something[index+1]]))
                print(result)
            
            elif index >= 1 and index < len(something)-1:
                before = "|".join(list([something[index-1], something[index]]))
                after = "|".join(list([something[index], something[index+1]]))
                print(f"before: {before} after: {after}") 


        # print(list(update))
            # time.sleep(0.5)


def main():
    data = open("sample_data/5.txt").read().strip().split("\n")
    part1(data)

if __name__ == "__main__":
    main()


# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47