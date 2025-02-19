from functions.utilities import divide_operation_hierarquie, check_for_potency_operation
from functions.operations import factorial_handler, power_handler
divide_operation_hierarquie, check_for_potency_operation = [
    divide_operation_hierarquie.divide_operation_hierarquie, 
    check_for_potency_operation.check_for_potency_operation
    ]

factorial_handler, power_handler = [factorial_handler.factorial_handler, power_handler.power_handler]

def potencies_or_factorial(operation_list:list[list, str]) ->list[list, str]:
 
    for operation_list_item in operation_list :
        operationlist_index_level_1 = operation_list.index(operation_list_item)
        #Remove elements and keep target
        if type(operation_list_item) == str:
            continue
        check_potency_or_factorial = check_for_potency_operation(operation_list_item)
        if not check_potency_or_factorial:
            continue

        operation_list_item = divide_operation_hierarquie(operation_list_item, ["*", "/"])
        for operation in operation_list_item:
            operation_index = operation_list_item.index(operation)
            if type(operation) == str:
                continue
            check_potency_or_factorial = check_for_potency_operation(operation)
            if not check_potency_or_factorial:
                continue

            factorial_indexes = []
            potencies_indexes = []
            operation_index_count = 0
            for element in operation:
                if element in ["^", "^1/"]:
                    potencies_indexes.append(operation_index_count)
                elif element == "!":
                    factorial_indexes.append(operation_index_count)
                operation_index_count+=1
            
            #factorial logic:
            for factorial_index in factorial_indexes:
                factorial_number = operation[factorial_index -1]
                operation.pop(factorial_index)
                operation[factorial_index - 1] = factorial_handler(factorial_number)

            #potencies logic:
            operation = potencies_logic(operation, potencies_indexes)
            

            operation_list_item[operation_index] = operation
        operation_list_item = turn_list_to_int(operation_list_item)
        operation_list[operationlist_index_level_1] = operation_list_item
            
    return operation_list       



def potencies_logic(operation, potencies_indexes):
    while True:
        if len(potencies_indexes) <=1 :
            break
        potency_part = operation[potencies_indexes[-1] -1: ]
        future_part = operation[ : potencies_indexes[-1] -1]
        new_list = [future_part, potency_part]
        potency_part = power_handler(potency_part)

        operation = future_part + [potency_part]
        potencies_indexes.pop()

    if len(potencies_indexes)  == 1 :
        
        operation = power_handler(operation)

    return operation



def turn_list_to_int(operation):
    indx = 0
    for element in  operation:
        if type(element) == list:
            operation[indx] = element[0]
        indx +=1 

    return operation