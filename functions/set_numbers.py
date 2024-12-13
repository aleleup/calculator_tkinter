from functions import start_operation, multiply_nums, sum_nums
import sys
from dotenv import load_dotenv

x = load_dotenv("PYTHONDONTWRITEBYTECODE")
sys.dont_write_bytecode = True

start_operation, multiply_nums, sum_nums = [start_operation.start_operation, multiply_nums.multiply_nums, sum_nums.sum_nums]

# print(start_operation)

def set_numbers(num_or_sym, numbers_sym_array, operation_history_array, sym):

    

    if num_or_sym in sym:
        new_number = int(''.join(numbers_sym_array))
        numbers_sym_array.clear()
        operation_history_array.append(new_number)
        operation_history_array.append(num_or_sym)

    else:
        numbers_sym_array.append(num_or_sym)


    if num_or_sym == "=":
        devide_plus_n_minus_op_arr:list[list, str] = start_operation(operation_history_array)
        products = multiply_nums(devide_plus_n_minus_op_arr)
        sum = sum_nums(products)
        print(sum)
        operation_history_array.clear()

