from functions.operations import mult_div_handler, gradual_problem_solving

mult_div_handler, gradual_problem_solving = [
    mult_div_handler.mult_div_handler,
    gradual_problem_solving.gradual_problem_solving]

def multiply_nums(oredered_list:list[list, str]) -> list[float, str]:
    list_index = -1 
    for item in oredered_list:
        list_index+=1
        symbol_index_list:list = []
        loop_index:int = 0
        if type(item) == list: #if not then item == + or -
            for element in item:
                if element in ['*', '/']:
                    symbol_index_list.append(loop_index)
                loop_index+=1 
        item = gradual_problem_solving(item, symbol_index_list, mult_div_handler)
        if len(symbol_index_list) == 0:
            item = item[0]
        oredered_list[list_index] = item
    
    return oredered_list
