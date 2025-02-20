from functions.utilities import validate_first_negative
from functions.operations import calculate
validate_first_negative, calculate = [
    validate_first_negative.validate_first_negative,
    calculate.calculate
    ]



def parenthesis_handler(operation_list:list):

    operation_list.pop()
    left_parenthesis_indexes_store = []
    right_parenthesis_indexes_store = []
    r_p_provisore_store = []
  
    operation_list_index = 0
    for element in operation_list:
        if element == "(":
            left_parenthesis_indexes_store.append(operation_list_index)

        elif element == ")":
            r_p_provisore_store.append(operation_list_index)

        operation_list_index+=1

    for item in r_p_provisore_store:
        right_parenthesis_indexes_store.append(0) 

    for r_item in r_p_provisore_store:
        index = 0
        while True:

            if index == (len(left_parenthesis_indexes_store) -1 ) or r_item < left_parenthesis_indexes_store[index + 1]: break
            index +=1

        for rang in range(0, index + 1):
            if r_item in right_parenthesis_indexes_store: break
            if right_parenthesis_indexes_store[index - rang] == 0:
                right_parenthesis_indexes_store[index - rang] = r_item
                
            # else: 

    
    while "(" in operation_list or ")" in operation_list:

        print("ENTRING THE LOOP", operation_list)
        if len(left_parenthesis_indexes_store) == 0: break

        #start from last indexes to first
        from_index = left_parenthesis_indexes_store[-1] 
        to_index = right_parenthesis_indexes_store[-1] + 1

        parenthesis_operation = operation_list[from_index: to_index]

        if "(" in parenthesis_operation: 
            parenthesis_operation.pop(0)

        if  ")" in parenthesis_operation:
            parenthesis_operation.pop()

        validate_first_negative(parenthesis_operation)
        print("parenthesis_operation", parenthesis_operation)
        result = calculate(parenthesis_operation)   
        print("PARENTHESIS SOLVED", result)

        operation_list[from_index: to_index] = [result]
        left_parenthesis_indexes_store.pop()
        right_parenthesis_indexes_store.pop()




    return operation_list






