def knapsack(value, weight, cap):
    rwv = []
    for i in range(len(value)):
        rwv.append([value[i]/weight[i], weight[i], value[i], i])
    rwv.sort(reverse=True)
    ans = []
    tw = 0
    found = True
    while (found):
        found = False
        for t in rwv:
            if (t[1] + tw) <= cap:
                ans.append(t[3])
                tw += t[1]
                found = True
                break
    return ans

print(knapsack([5,8,12], [10,20,30], 838)) 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(knapsack([3,5,7,11,13], [17,23,29,31,37], 997))
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

print(knapsack([5,6,7,8], [25,36,49,64], 250))
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(knapsack([5,6,7,8], [25,36,49,64], 360))
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(knapsack([5,10,20], [5,10,20], 55))
# [2, 2, 1, 0]