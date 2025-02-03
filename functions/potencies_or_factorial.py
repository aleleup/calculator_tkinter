from functions.utilities import divide_operation_hierarquie

divide_operation_hierarquie = divide_operation_hierarquie.divide_operation_hierarquie

def potencies_or_factorial(operation_list:list[list, str]) ->list[list, str]:
    print(f"""
    ---------------POTENCY_OR_FACTORIAL------------------
                OP_LIST {operation_list}
""")
    
    symbol_expected:list = ["^", "^1/", "!"]
    operation_list_copy = operation_list.copy()
    for operation_list_item in operation_list_copy : #operation_list_copy for testing algorithm
        is_potency_or_factorial = False
        #Remove elements and keep target
        if type(operation_list_item) == str:
            continue
        for element in operation_list_item:
            if element in symbol_expected: 
                is_potency_or_factorial = True
                break
        print("IS potenc or factorial === True?", operation_list_item ,is_potency_or_factorial)
        if not is_potency_or_factorial:
            continue


        operation_list_item = divide_operation_hierarquie(operation_list_item, ["*", "/"])
        print(operation_list_item)

        #Find symbols indexes
        # sym_index = []
        # i = 0
        # for element in item:
        #     if element in symbol_expected:
        #         sym_index.append(i)
        #     i+=1
        
        # new_list = []
        # index_while_loop = 0
        # print("FINAL TARGETS", sym_index, item)
        
        
        
        
        
        # while len(sym_index) > 1:
        #     #symbol_expected in operation_list_copy
        #     if index_while_loop == 1: break
            
        #     operation_part:list =  item[sym_index[-1] -1 : sym_index[-1] + 2]
        #     await_part:list = item[ 0 : sym_index[-1] - 1]
        #     new_list = await_part + [operation_part]
            
        #     print(f"new_list index {index_while_loop}: ", new_list)
            

        #     index_while_loop+=1
         

    #item -> list[float, str, solve this array-> list[float, str] <-]



        

