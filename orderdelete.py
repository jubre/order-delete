def ordered_set(in_list):
    out_list = []
    added = set()
    for val in in_list:
        if not val in added:
            out_list.append(val)
            added.add(val)
    out_list.sort()
    return out_list


myList = [10,8,1,1,3,6,2]

print(myList)

print(ordered_set(myList))
