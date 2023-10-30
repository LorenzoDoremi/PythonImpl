
from numpy import sort

# sorting weight value
def sortkey(items, key, key2) -> None:
    #simple bubble sort
    for i in range(0,len(items)):
        for j in range(i+1,len(items)):
            r1 =  items[i][key]/items[i][key2]
            r2 =  items[j][key]/items[j][key2]
            if(r1<r2):
                items[i], items[j] = items[j], items[i]

# O(n^2) greedy knapsack algorithm for lists of dictionaries
def knapsack(items, max_weight) -> dict:
    sortkey(items, "v","c")
    i = 0
    curr_weight = 0
    total_value = 0
    saved_items = []
    while(i < len(items)):
        if(curr_weight + items[i]["c"] < weight):
            curr_weight += items[i]["c"]
            total_value += items[i]["v"]
            saved_items.append(items[i])
            i+=1
    else:
        i+=1

    return {"saved":saved_items, "total":total_value}   




items = [
    {"v": 10, "c": 8},
    {"v": 3, "c": 4},
    {"v": 12, "c": 8},
    {"v": 14, "c": 9},
]
weight = 50

print(knapsack(items, weight))



