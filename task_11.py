def find_values(*lists):
    res = list(set(lists[0]).intersection(*lists))
    return print(res)


find_values([11, 10], [2, 11, 10, 3], [10, 11])
find_values([8, 4, 7, "hi"], [8, "hi"], [4, "hi"])
find_values([1, 4, 3, 2], [6, 2, 8], ["4", "hi"])
