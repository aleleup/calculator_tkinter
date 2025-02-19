from functions import sum_nums, potencies_or_factorial, start_operation, multiply_nums
from functions.utilities import validate_first_negative

start_operation, potencies_or_factorial,multiply_nums, sum_nums,  validate_first_negative, = [
    start_operation.start_operation,
    potencies_or_factorial.potencies_or_factorial, 
    multiply_nums.multiply_nums, 
    sum_nums.sum_nums, 
    validate_first_negative.validate_first_negative,
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
        devided_operation_hierarquie_list:list[list, str] = start_operation(parenthesis_operation, ["+", "-"])
        potencies_or_factorials_list = potencies_or_factorial(devided_operation_hierarquie_list)
        products_list = multiply_nums(potencies_or_factorials_list)
        total_sum = sum_nums(products_list)
        print("PARENTHESIS SOLVED", total_sum)

        operation_list[from_index: to_index] = [total_sum]
        left_parenthesis_indexes_store.pop()
        right_parenthesis_indexes_store.pop()




    return operation_list






