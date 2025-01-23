from functions import start_operation, sum_nums
from functions.utilities import display_operation
import sys

from functions import multiply_nums
sys.dont_write_bytecode = True

start_operation, multiply_nums, sum_nums, display_operation = [
    start_operation.start_operation, 
    multiply_nums.multiply_nums, 
    sum_nums.sum_nums, 
    display_operation.display_operation]

# print(start_operation)

def set_numbers(num_or_sym, numbers_sym_array, operation_history_array:list, sym, display_text):

    

    if num_or_sym in sym:
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
        last_display_array = operation_history_array.copy()
        devide_plus_n_minus_op_arr:list[list, str] = start_operation(operation_history_array)
        products = multiply_nums(devide_plus_n_minus_op_arr)
        total_sum = sum_nums(products)
        print("TOTAL_SUMS", total_sum)
        display_operation(last_display_array, display_text, total_sum)
 
        operation_history_array.clear()

