from functions.operations import mult_div_handler

mult_div_handler = mult_div_handler.mult_div_handler

def multiply_nums(oredered_list:list[list, str]) -> list[float, str]:
    '''
       Recives a list and inmediatly check the type of each item. 
       If it's a list then there's an operation inside, else, it'll 
       be a string (either "+" or "-").
        When it's a list first look after the operators character
       location and store it in symbol_index_list. If the len of this 
       list > 1 then there are multiple products and as product operations 
       are associative I stablish an orther where the first operation is separated in a list
       and the rest is keep apart in another. With handle_mult func. I multiply the first 
       list (wich has two numbers and a symbol); then pop the symbol index from symbol_index_list
       and overwriting the previous list so this happens until the symbol_index_list has only one element.
       If it has only one elemnt, the same function is called and the process is ended.

       ex: [[a, *, b, *, c, *, d], +, [f, *, d]]
            loop -> [[a,  *,  b], [*, c, *, d]]
                    [ab, [*, c, *, d]]
                    [ab, *, c, *, d]
                    [ab, *, c,[ *, d]] ... -> [abcd + fd]
    '''  
    list_index = -1 
    print(oredered_list)

    for item in oredered_list:
        list_index+=1
        symbol_index_list:list = []
        loop_index:int = 0
        if type(item) == list: #if not then item == + or -
            for element in item:
                if element in ['*', '/']:
                    symbol_index_list.append(loop_index)
                loop_index+=1 
       
        while len(symbol_index_list) > 1:
            item_prod_1:list = item[0: symbol_index_list[1]] #list of first product (from the beggining to before the next product character)
            item_prod_2:list = item[symbol_index_list[1]:  ]
            new_list:list = [item_prod_1, item_prod_2]

            new_list[0] = mult_div_handler(item_prod_1)
            
            symbol_index_list.pop(0) #Remove element 

            item = [new_list[0]] + item_prod_2
            if len(symbol_index_list) == 1:
                break
            
        if len(symbol_index_list) == 1:
           item = mult_div_handler(item)
        if len(symbol_index_list) == 0:
            
            item = item[0]
        oredered_list[list_index] = item
    
    return oredered_list
