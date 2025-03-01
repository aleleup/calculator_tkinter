from functions.operations import add_substract_handler, gradual_problem_solving

add_substract_handler, gradual_problem_solving = [
    add_substract_handler.add_substract_handler,
    gradual_problem_solving.gradual_problem_solving
]
def sum_nums(product_list: list[str, int, float]) -> float:
    symbol_index_list:list = []
    loop_index:int = 0

    for item in product_list:
        if item in ['+', '-']:
            symbol_index_list.append(loop_index)
   
    item = gradual_problem_solving(product_list, symbol_index_list, add_substract_handler)
    if len(symbol_index_list) == 0:
        item = item[0]

    return item
     



