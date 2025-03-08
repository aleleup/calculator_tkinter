def is_expression_function(operation_list: list) -> bool:
    is_function = False
    for item in operation_list:
        if item == 'x':
            is_function = True
            break

    return is_function