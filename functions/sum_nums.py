def sum_nums(product_list: list[str, int, float]) -> float:
    product_copy:list = product_list.copy()
    symbol_index_list:list = []
    loop_index:int = 0

    for item in product_list:
        if item in ['+', '-']:
            symbol_index_list.append(loop_index)
        loop_index+=1 
        

    print("len", len(symbol_index_list))

    while len(symbol_index_list) > 1:
        print(f"""
--------------------------------
              product_list:{product_copy, symbol_index_list}""")
        if len(symbol_index_list) == 1:
            break
        item_sum_1 = product_list[0: symbol_index_list[1]] #list of first product (from the beggining to before the next product character)
        item_sum_2 = product_list[symbol_index_list[1]:  ]
        # new_list = [item_sum_1, item_sum_2]

        print("ITEMS ", item_sum_1, item_sum_2)

        symbol_index_list.pop(0) #Remove element 

        item_sum_1 = handle_sum(item_sum_1)

        product_copy = [item_sum_1] + item_sum_2

    if len(symbol_index_list) == 1:
        product_copy = handle_sum(product_copy)

    if len(symbol_index_list) == 0:
        print("entrying the last if")
        product_copy = product_copy[0]

    print(product_copy)
    return product_copy
     

def handle_sum(operation_list):
    if operation_list[1] == "+":
        return operation_list[0] + operation_list[2]
    else:
        return operation_list[0] - operation_list[2]
    


