
def turn_list_to_int(operation):
    indx = 0
    for element in  operation:
        if type(element) == list:
            operation[indx] = element[0]
        indx +=1 

    return operation