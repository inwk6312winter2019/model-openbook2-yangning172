def extract_data('street_Centrelines.csv')
    f = open('street_Centrelines.csv')
    list1 = []
    
    for line in f:
        list3 = line.split(',')
        list1.append((list3[2],list3[4],list3[6],list3[7]))
    t = tuple(list1)
    return t
