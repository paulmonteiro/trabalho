import json
data = []
with open('content.json') as jsonfile:
    data = json.load(jsonfile)
# data is now a list that contains dictionaries
# find compatibles : THIS FIRST VERSION CONSIDERS ONLY SAME COLOR, NOT INTERVALS
compatibles = []
for i in range(0,len(data)) :
    color1 = data[i]['color']
    if data[i]['name'] in compatibles :
        next
    else :
        if i != 0 :
            # insert a new line between groups, for printing
            compatibles.append('\n')  
        compatibles.append(data[i]['name'])
        # insert a space between the elements, for printing
        compatibles.append(' ')
    # look for every other element with the same color:    
    for j in range(i+1,len(data)) :
        color2 = data[j]['color']
        if color2 == color1 : # e se intervalos forem compativeis
            # do not consider the element if already on the compatibles list:
            if data[j]['name'] in compatibles :
                next
            else :    
                compatibles.append(data[j]['name'])
                # insert a space between the elements, for printing
                compatibles.append(' ')
                                    
# print the compatible groups list:
for element in compatibles :
    print(element, end='')
    
