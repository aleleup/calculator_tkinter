from functions import parenthesis_handler
from functions.operations import calculate
from functions.utilities import display_operation, validate_first_negative, fix_parenthesis_bug, replace_e_or_pi_for_aprox
from functions.Graphs import is_expression_function, graphic_handler
from functions import multiply_nums
display_operation, validate_first_negative, fix_parenthesis_bug, parenthesis_handler, calculate, replace_e_or_pi_for_aprox, is_expression_function, graphic_handler= [
    display_operation.display_operation,
    validate_first_negative.validate_first_negative,
    fix_parenthesis_bug.fix_parenthesis_bug,
    parenthesis_handler.parenthesis_handler,
    calculate.calculate,
    replace_e_or_pi_for_aprox.replace_e_or_pi_for_aprox,
    is_expression_function.is_expression_function,
    graphic_handler.graphic_handler

    ]

def set_numbers(num_or_sym:str, numbers_sym_array:list, operation_history_array:list, sym1:list, sym2:list, display_text, result_list:list) -> None:
    symbols_list:list = sym1 + sym2
    if num_or_sym in symbols_list:

        if result_list and not numbers_sym_array and not (num_or_sym in ['(', ')']) :
            operation_history_array.append(result_list[-1])
        else:
            new_number = ''.join(numbers_sym_array)
            numbers_sym_array.clear()
            operation_history_array.append(new_number)
        
        operation_history_array.append(num_or_sym)
        display_text.set(num_or_sym)

        display_operation(operation_history_array, display_text, '')
    else:       
        if num_or_sym == 'del':
            if numbers_sym_array: 
                numbers_sym_array.pop()         
            if not numbers_sym_array and operation_history_array:
                if operation_history_array[-1].isnumeric():
                    number_array = list(operation_history_array[-1])
                    number_array.pop()
                    operation_history_array.pop()
                    numbers_sym_array += number_array

                else: operation_history_array.pop()        
        else:
            numbers_sym_array.append(num_or_sym)

        if num_or_sym == 'clr':
            numbers_sym_array.clear()
            operation_history_array.clear()
            result_list.clear()
   
        display_list = operation_history_array.copy()
        display_list.extend(numbers_sym_array)
        display_operation(display_list, display_text, '')

    if num_or_sym == "=":
        
        last_display_array = operation_history_array.copy()
        fix_parenthesis_bug(operation_history_array)
        replace_e_or_pi_for_aprox(operation_history_array)
        validate_first_negative(operation_history_array)
        is_function = is_expression_function(operation_history_array)
        if is_function:
            graphic_handler(operation_history_array)
        else:    
            parenthesis_operation = parenthesis_handler(operation_history_array)
            result = str(calculate(parenthesis_operation))
            result_list.append(result)
            display_operation(last_display_array, display_text, result)
        operation_history_array.clear()