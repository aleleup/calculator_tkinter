def gradual_problem_solving(operation_list, operation_indexes, operation_handler):
    while True:
        if len(operation_indexes) <=1 :
            break
        startup_part = operation_list[operation_indexes[-1] -1: ]
        future_part = operation_list[ : operation_indexes[-1] -1]
        startup_part = operation_handler(startup_part)

        operation_list = future_part + [startup_part]
        operation_indexes.pop()

    if len(operation_indexes) == 1 :
        operation_list = operation_handler(operation_list)

    return operation_list


