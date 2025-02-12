def check_for_potency_operation(operation_list_item:list) -> bool:
    is_potency_or_factorial = False
    
    symbol_expected:list = ["^", "^1/", "!"]
    for element in operation_list_item:
            if element in symbol_expected: 
                is_potency_or_factorial = True
                break

    return is_potency_or_factorial
        