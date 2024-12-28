def sum_nums(product_list: list[str, int, float]) -> float:
    
    symbol_index_list:list = []
    loop_index:int = 0

    for item in product_list:
        if item in ['+', '-']:
            symbol_index_list.append(loop_index)
        loop_index+=1 
        

    while len(symbol_index_list) > 1:
        item_sum_1 = product_list[0: symbol_index_list[1]] #list of first product (from the beggining to before the next product character)
        item_sum_2 = product_list[symbol_index_list[1]:  ]
        new_list = [item_sum_1, item_sum_2]

        item_sum_1 = handle_sum(item_sum_1)

        symbol_index_list.pop(0) #Remove element 

        product_list = [item_sum_1] + item_sum_2

        if len(symbol_index_list) == 1:
            break

    if len(symbol_index_list) == 1:
        product_list = handle_sum(product_list)

    if len(symbol_index_list) == 0:
        product_list = product_list[0]

    return product_list
     

def handle_sum(operation_list):
    if operation_list[1] == "+":
        return operation_list[0] + operation_list[2]
    else:
        return operation_list[0] - operation_list[2]