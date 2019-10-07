import json

def version_overlaps(minversion1, maxversion1, minversion2, maxversion2) :
    interval1 = []
    interval2 = []
    interval1.append(minversion1)
    interval2.append(minversion2)
    # numpi has the arange method to contruct ranges of type float
    # but I'l use an old fashioned while loop to contruct the interval:
    while minversion1 < maxversion1 :
        minversion1 += 0.1
        minversion1 = round(minversion1,1)
        interval1.append(minversion1)
    #print(interval1)
    # Construct the second interval
    while minversion2 < maxversion2 :
        minversion2 += 0.1
        minversion2 = round(minversion2, 1)
        interval2.append(minversion2)
    #print(interval2)
    # check if there is overlap between the intervals
    # if there is overlap then return True, otherwise return False
    for num in interval2 :
        if num in interval1 :
            return True
    return False

with open('content.json') as jsonfile:
    data = json.load(jsonfile)
# data is now a list that contains dictionaries
# find compatibles :
compatibles = []
already_considered = []
for i in range(0,len(data)) :
    color1 = data[i]['color']
    if data[i]['name'] in compatibles :
        next
    else :
        if i != 0 :
            # insert a new line between groups, for printing
            compatibles.append('\n')
            # clear already considered list
            already_considered = []
        compatibles.append(data[i]['name'])
        # insert a space between the elements, for printing
        compatibles.append(' ')
        
    # look for every other element with the same color and compare versions:
    for j in range(i+1,len(data)) :
        color2 = data[j]['color']
        if (color2 == color1) and (version_overlaps(data[i]['min_version'],data[i]['max_version'],data[j]['min_version'],data[j]['max_version'])) :
            # do not consider the element if already on the compatibles list:
            if data[j]['name'] in compatibles or data[i]['name'] in already_considered :
                next
            else :    
                compatibles.append(data[j]['name'])
                # insert a space between the elements, for printing
                compatibles.append(' ')
        if (color2 == color1):
            already_considered.append(data[j]['name'])
# print the compatible groups list:
for element in compatibles :
    print(element, end='')
    
