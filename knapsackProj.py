import csv

def knapsack(name, value, height, width, depth, cap):
    """
    Summary: A greedy solution to determine the most profitable distribution of various sized boxes that have differing values in a knapsack.
    
    Inputs:
        name: The name of the item.
        value: The value in dollars of the item.
        height: The height in inches of the item.
        width: The width in inches of the item.
        depth: The depth in inches of the item.

    Output: A statement that tells the user how many of each items to pack in order to maximize profit. It also says the profit itself and the leftover capacity.
    """

    itemInfo = []

    for i in range(len(value)):
        volume = (height[i] * width[i] * depth[i])
        itemInfo.append([value[i]/volume, volume, value[i], i, name[i]])
    itemInfo.sort(reverse=True)

    ans = {} # name: quantity of items that go into the knapsack
    totalVolume = 0
    totalValue = 0
    found = True

    while (found):
        found = False # When and item is found, this value becomes True again
        for item in itemInfo:
            if (item[1] + totalVolume) <= cap:
                ans[item[4]] = ans.get(item[4], 0) + 1 # Add the item to the ans dictionary. If that item already exists, increment its quantity by 1
                totalVolume += item[1]
                totalValue += item[2]
                found = True
                break

    phrase = f"It's suggested that you pack: {', '.join([f'{count} {item}s' for item, count in ans.items()])}. The total value will be ${totalValue}. There will be {cap - totalVolume} cubic inches left over."
    return phrase

def main():
    """
    Summary: Reads information about items from a .csv file. Calls the greedy knapsack function to determine which items should go into the knapsack to maximize profit.

    Inputs: NA

    Outputs: NA, though it prints information to the terminal.
    """
    
    name, value, height, width, depth = [], [], [], [], []

    with open("items.csv", mode="r") as file:
        reader = csv.reader(file) 
        for line in reader:
            print(line)
            name.append(line[0])
            value.append(int(line[1]))
            height.append(int(line[2]))
            width.append(int(line[3]))
            depth.append(int(line[4]))
    
    cap = int(input("What is the capacity of the knapsack in cubic inches? "))
    
    print(knapsack(name, value, height, width, depth, cap))

# =========================================================================================================
main()