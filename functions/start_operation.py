def start_operation(operation_history_array:list) -> list[list, str] :
    '''
    Takes Number arrays and splits the orther of the operationx  
    '''
    transform_numericstring_to_float(operation_history_array)
    
    operation_history_array.pop()
    loop_index:int = 0
    
    symbol_index:int = 0
    new_operation_array: list = []
    while "+" in operation_history_array or "-" in operation_history_array: 
        #Look at the +- symbol index
        for num in operation_history_array:
            if symbol_index != 0: break
            if num == "+" or num == "-":
                symbol_index = loop_index
            loop_index+=1
        
        new_operation_array += [operation_history_array[0:symbol_index], operation_history_array[symbol_index]]
        operation_history_array = operation_history_array[symbol_index + 1: ]

    if not ("+" in operation_history_array or "-" in operation_history_array):
         new_operation_array += [operation_history_array]

    return new_operation_array



def transform_numericstring_to_float(operation_history_array):
    i = 0
    for item in operation_history_array:
        if item.isnumeric():
            operation_history_array[i] = float(item)
        i += 1
