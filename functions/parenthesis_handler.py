def parenthesis_handler(operation_list:list):

    left_parenthesis_indexes_store = []
    right_parenthesis_indexes_store = []
    r_p_provisore_store = []
  
    operation_list_index = 0
    for element in operation_list:
        if element == "(":
            left_parenthesis_indexes_store.append(operation_list_index)

        elif element == ")":
            r_p_provisore_store.append(operation_list_index)

        operation_list_index+=1
    print(left_parenthesis_indexes_store ,r_p_provisore_store)

    for item in r_p_provisore_store:
        right_parenthesis_indexes_store.append(0) 

    for r_item in r_p_provisore_store:
        index = 0
        while True:

            if index == (len(left_parenthesis_indexes_store) -1 ) or r_item < left_parenthesis_indexes_store[index + 1]: break
            index +=1

        for rang in range(0, index + 1):
            print("ENTREING RANGE LOOP", rang)
            if r_item in right_parenthesis_indexes_store: break
            if right_parenthesis_indexes_store[index - rang] == 0:
                right_parenthesis_indexes_store[index - rang] = r_item
                
            # else: 



    print(left_parenthesis_indexes_store ,right_parenthesis_indexes_store)


