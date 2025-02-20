from functions.operations import add_substract_handler, gradual_problem_solving

add_substract_handler, gradual_problem_solving = [
    add_substract_handler.add_substract_handler,
    gradual_problem_solving.gradual_problem_solving
]
def sum_nums(product_list: list[str, int, float]) -> float:
    product_copy:list = product_list.copy()
    symbol_index_list:list = []
    loop_index:int = 0

    for item in product_list:
        if item in ['+', '-']:
            symbol_index_list.append(loop_index)
        loop_index+=1 
        


    # while len(symbol_index_list) > 1:

    #     if len(symbol_index_list) == 1:
    #         break
    #     item_sum_1 = product_list[0: symbol_index_list[1]] #list of first product (from the beggining to before the next product character)
    #     item_sum_2 = product_list[symbol_index_list[1]:  ]
    #     # new_list = [item_sum_1, item_sum_2]


    #     symbol_index_list.pop(0) #Remove element 

    #     item_sum_1 = add_substract_handler(item_sum_1)

    #     product_copy = [item_sum_1] + item_sum_2

    # if len(symbol_index_list) == 1:
    #     product_copy = add_substract_handler(product_copy)
    item = gradual_problem_solving(product_list, symbol_index_list, add_substract_handler)
    if len(symbol_index_list) == 0:
        item = item[0]

    return item
     



