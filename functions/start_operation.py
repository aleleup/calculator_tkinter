from functions.utilities import divide_operation_hierarquie, transform_numericstring_to_float

divide_operation_hierarquie, transform_numericstring_to_float = [
    divide_operation_hierarquie.divide_operation_hierarquie,
    transform_numericstring_to_float.transform_numericstring_to_float
    ]

def start_operation(operation_history_array:list, expected_syms:list[str,str]) -> list[list, str] :
    '''
    Takes Number arrays and splits the orther of the operationx  
    '''
    transform_numericstring_to_float(operation_history_array)
    
    operation_history_array.pop()

    new_operation_array: list = divide_operation_hierarquie(operation_history_array, expected_syms)

    return new_operation_array
