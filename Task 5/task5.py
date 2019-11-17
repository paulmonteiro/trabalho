ordered_lists = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

print('\n')
print("Determine the smallest range of integers that is common to all lists:")
print("Ordered lists of positive integers:")
print(ordered_lists)
print('\n')

list_of_items=[]
shortest_interval = []
i = 0
while True:
    for element in ordered_lists:
        list_of_items.append(element[0])

    # find min max range
    min_value = min(list_of_items)
    max_value = max(list_of_items)
    range = max_value - min_value
    if i == 0:
        min_range = range
        shortest_interval = [min_value, max_value]
    else:
        if range < min_range:
            min_range = range
            shortest_interval = [min_value,max_value]

    print(f'Iteration {i}:')
    print(f'Min: {min_value} Max: {max_value} Range: {range}')

    # remove the minimum value from ordered_lists:
    for element in ordered_lists:
        if element[0] == min_value:
            del element[0]

    print(ordered_lists)
    # clear list_of_items for the next iteration
    list_of_items = []
    # check if an element of the list of lists (ordered_lists) has run out of elements, this is the stop condition
    for j,element in enumerate(ordered_lists):
        if len(element) == 0:
            print(f'\nNo more items in element {j} , stop condition reached.')
            print('\n')
            print(f'The shortest interval is: {shortest_interval}')
            exit(0)
    i = i + 1
