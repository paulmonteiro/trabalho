ordered_lists = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

shortest_list = min(map(len, ordered_lists))-1

i = 0
list_of_items = []
while i <= shortest_list:
    for element in ordered_lists:
        list_of_items.append(element[0])
    print(list_of_items, end='')
    print(';')
    # send list to find min, max and range
    list_of_items = []
    for element in ordered_lists:
        del element[0]
    i = i + 1
