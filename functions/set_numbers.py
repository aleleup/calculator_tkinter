from functions import sum_nums, potencies_or_factorial, start_operation
from functions.utilities import display_operation, validate_first_negative, fix_parenthesis_bug
import sys

from functions import multiply_nums
sys.dont_write_bytecode = True

start_operation, potencies_or_factorial ,multiply_nums, sum_nums, display_operation, validate_first_negative, fix_parenthesis_bug = [
    start_operation.start_operation,
    potencies_or_factorial.potencies_or_factorial, 
    multiply_nums.multiply_nums, 
    sum_nums.sum_nums, 
    display_operation.display_operation,
    validate_first_negative.validate_first_negative,
    fix_parenthesis_bug.fix_parenthesis_bug
    ]

# print(start_operation)

def set_numbers(num_or_sym, numbers_sym_array, operation_history_array:list, sym1:list, sym2:list, display_text):

    print("OPERATION HISTORY ARRAY", operation_history_array)

    symbols_list:list = sym1 + sym2
    if num_or_sym in symbols_list:
        new_number = ''.join(numbers_sym_array)
        numbers_sym_array.clear()
        operation_history_array.append(new_number)
        operation_history_array.append(num_or_sym)
        display_text.set(num_or_sym)

        display_operation(operation_history_array, display_text, '')

    else:
        numbers_sym_array.append(num_or_sym)
        display_list = operation_history_array.copy()
        display_list.extend(numbers_sym_array)
        display_operation(display_list, display_text, '')

    if num_or_sym == "=":

        fix_parenthesis_bug(operation_history_array)
        validate_first_negative(operation_history_array)
        last_display_array = operation_history_array.copy()

        devided_operation_hierarquie_list:list[list, str] = start_operation(operation_history_array, ["+", "-"])
        print("op 1",devided_operation_hierarquie_list)

        potencies_or_factorials = potencies_or_factorial(devided_operation_hierarquie_list)
        # products = multiply_nums(devided_operation_hierarquie_list)
        # print("op2", products)
        # total_sum = sum_nums(products)
        

        # print("TOTAL_SUMS", total_sum)
        # display_operation(last_display_array, display_text, total_sum)
        # operation_history_array.clear()



