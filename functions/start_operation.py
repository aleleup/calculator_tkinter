def start_operation(operation_history_array:list) -> list[list, str] :
    '''
    Takes Number arrays and splits the orther of the operationx  
    '''
    transform_numericstring_to_float(operation_history_array)
    
    operation_history_array.pop()
    operation_ripped_appart:list = operation_history_array.copy()
    loop_index:int = 0
    
    symbol_indexes:list[int] = []
    new_operation_array: list = []

    # while "+" in operation_history_array or "-" in operation_history_array: 
        #Look at the +- symbol index
    for num in operation_history_array:
        if num == "+" or num == "-":
            symbol_indexes.append(loop_index)
        loop_index+=1

    newstart_index = 0
    for symbol_index in symbol_indexes:
        print(symbol_indexes, operation_ripped_appart, new_operation_array)
        new_operation_array += [operation_history_array[newstart_index:symbol_index], operation_history_array[symbol_index]]
        operation_ripped_appart = operation_history_array[symbol_index + 1:]
        newstart_index = symbol_index + 1
        print(symbol_indexes, operation_ripped_appart, new_operation_array)
        print("-------------------------------")

    if not ("+" in operation_ripped_appart or "-" in operation_ripped_appart):
         new_operation_array += [operation_ripped_appart]

    return new_operation_array



def transform_numericstring_to_float(operation_history_array):
    i = 0
    for item in operation_history_array:
        if item.isnumeric():
            operation_history_array[i] = float(item)
        i += 1
