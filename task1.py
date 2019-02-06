def extract_data('street_Centrelines.csv')  #a tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR)
    f = open('street_Centrelines.csv')
    f.readline()
    list1 = []
    
    for line in f:
        list3 = line.split(',')
        list1.append((list3[2],list3[4],list3[6],list3[7]))    # theses index are to str_name, full_name,from_str,to_str)
    t = tuple(list1)
    return t




def  histogram(file):
    f = open('street_Centrelines.csv')
    f.readline()
    list2 = []
    d = dict()
    for line in f:
        list4 = line.split(',')
        list2.append(list4[12])    # the index[12] of  Maintenance
    for n in list2:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    return d



def unique_owners():
    f = open('street_Centrelines.csv')
    f.readline()
    list2 =[]
    for line in f:
        list1 = line.split(',')
        list2.append(list1[11])     # the index is to OWN
    return list2
