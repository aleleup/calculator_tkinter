from functions import parenthesis_handler
from functions.operations import calculate
from functions.utilities import display_operation, validate_first_negative, fix_parenthesis_bug
import sys

from functions import multiply_nums
sys.dont_write_bytecode = True

display_operation, validate_first_negative, fix_parenthesis_bug, parenthesis_handler, calculate= [
    display_operation.display_operation,
    validate_first_negative.validate_first_negative,
    fix_parenthesis_bug.fix_parenthesis_bug,
    parenthesis_handler.parenthesis_handler,
    calculate.calculate
    
    ]


def set_numbers(num_or_sym:str, numbers_sym_array:list, operation_history_array:list, sym1:list, sym2:list, display_text):


    symbols_list:list = sym1 + sym2
    if num_or_sym in symbols_list:

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
                    print(number_array)
                    number_array.pop()
                    operation_history_array.pop()
                    numbers_sym_array += number_array

                else: operation_history_array.pop()
            
            else: pass
        
        else:
            numbers_sym_array.append(num_or_sym)

        if num_or_sym == 'clr':
            numbers_sym_array.clear()
            operation_history_array.clear()
           
        
        display_list = operation_history_array.copy()
        display_list.extend(numbers_sym_array)
        display_operation(display_list, display_text, '')


    

    if num_or_sym == "=":

        fix_parenthesis_bug(operation_history_array)
        validate_first_negative(operation_history_array)
        last_display_array = operation_history_array.copy()

        parenthesis_operation = parenthesis_handler(operation_history_array)
    
        result = str(calculate(parenthesis_operation))
        print("RESULT", result)
        
        display_operation(last_display_array, display_text, result)
        operation_history_array.clear()



