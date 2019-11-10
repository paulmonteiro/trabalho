ordered_lists = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
#ordered_lists = [[4], [0], [5]]

print(f'Number of lists: {len(ordered_lists)}')

def determine_min_range():
    current_min = 0
    current_max = 0
    current_range = []
    determined_min = 0
    determined_max = 0
    determined_range = []
    for i in range(0,len(ordered_lists)):
        # determine the shortest list, this will be used to end the iteration through the elements
        element_length = len(ordered_lists[i])
        if i == 0:
            min_length = element_length
        else:
            if element_length < min_length:
                min_length = element_length
        for j in range(0,min_length):
            print(ordered_lists[i][j])

    return determined_range

range = determine_min_range()
print(f'The minimum range common to all lists is: {range}')