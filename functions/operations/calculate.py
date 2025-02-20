from functions import start_operation, potencies_or_factorial, multiply_nums, sum_nums

start_operation, potencies_or_factorial, multiply_nums, sum_nums = [
    start_operation.start_operation, potencies_or_factorial.potencies_or_factorial, multiply_nums.multiply_nums, 
    sum_nums.sum_nums
]

def calculate(operation_list):
    devided_operation_hierarquie_list:list[list, str] = start_operation(operation_list, ["+", "-"])
    potencies_or_factorials_list = potencies_or_factorial(devided_operation_hierarquie_list)
    products_list = multiply_nums(potencies_or_factorials_list)
    result = sum_nums(products_list)

    return result