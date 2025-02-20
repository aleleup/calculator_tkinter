from functions.utilities import divide_operation_hierarquie, check_for_potency_operation, turn_list_to_int
from functions.operations import factorial_handler, power_handler, gradual_problem_solving
divide_operation_hierarquie, check_for_potency_operation, turn_list_to_int = [
    divide_operation_hierarquie.divide_operation_hierarquie, 
    check_for_potency_operation.check_for_potency_operation,
    turn_list_to_int.turn_list_to_int
    ]

factorial_handler, power_handler, gradual_problem_solving = [
    factorial_handler.factorial_handler, power_handler.power_handler,
    gradual_problem_solving.gradual_problem_solving
    ]

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
            operation = gradual_problem_solving(operation, potencies_indexes, power_handler)
            

            operation_list_item[operation_index] = operation
        operation_list_item = turn_list_to_int(operation_list_item)
        operation_list[operationlist_index_level_1] = operation_list_item
            
    return operation_list       



