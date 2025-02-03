def divide_operation_hierarquie(operation_history_array:list, expected_syms:list[str,str]) -> list[list, str] :
    '''
    Takes Number arrays and splits the orther of the operationx  
    '''
    operation_ripped_appart:list = operation_history_array.copy()
    loop_index:int = 0
    
    symbol_indexes:list[int] = []
    new_operation_array: list = []
        #Look at the +- or */ symbol index
    for num in operation_history_array:
        if num in expected_syms:
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

    
    if not(expected_syms[0] in operation_ripped_appart or expected_syms[1] in operation_ripped_appart ):
        new_operation_array += [operation_ripped_appart]

    return new_operation_array



