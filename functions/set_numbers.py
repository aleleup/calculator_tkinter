from functions import start_operation, multiply_nums, sum_nums
import sys
sys.dont_write_bytecode = True

start_operation, multiply_nums, sum_nums = [start_operation.start_operation, multiply_nums.multiply_nums, sum_nums.sum_nums]

# print(start_operation)

def set_numbers(num_or_sym, numbers_sym_array, operation_history_array, sym, display_text):

    

    if num_or_sym in sym:
        new_number = float(''.join(numbers_sym_array))
        numbers_sym_array.clear()
        operation_history_array.append(new_number)
        operation_history_array.append(num_or_sym)
        display_text.set(operation_history_array)

    else:
        numbers_sym_array.append(num_or_sym)
        display_text.set(numbers_sym_array)

    if num_or_sym == "=":
        devide_plus_n_minus_op_arr:list[list, str] = start_operation(operation_history_array)
        products = multiply_nums(devide_plus_n_minus_op_arr)
        sum = sum_nums(products)
        print(sum)
        display_text.set(sum)
        operation_history_array.clear()

