def sum_nums(product_list):
    
    symbol_index_list:list = []
    loop_index:int = 0
    print("sums", product_list)

    for item in product_list:
        if item in ['+', '-']:
            symbol_index_list.append(loop_index)
        loop_index+=1 

        

    while len(symbol_index_list) > 1:
        item_prod_1:list = item[0: symbol_index_list[1]] #list of first product (from the beggining to before the next product character)
        item_prod_2:list = item[symbol_index_list[1]:  ]
        new_list:list = [item_prod_1, item_prod_2]

        print(new_list)
        new_list[0] = handle_sum(item_prod_1)
        print(new_list)
        symbol_index_list.pop(0) #Remove element 

        item = [new_list[0]] + item_prod_2

        print(item)
        if len(symbol_index_list) == 1:
            break

    if len(symbol_index_list) == 1:
        item = handle_sum(item)
    print(item)
    return item
     

def handle_sum(operation_list):
    print()
    if operation_list == "+":
        return operation_list[0] + operation_list[2]
    else:
        return operation_list[0] - operation_list[2]