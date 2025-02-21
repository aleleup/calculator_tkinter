from math import e, pi

def replace_e_or_pi_for_aprox(operation_list:list) ->list:
    items_index = 0
    # operation_list_copy = operation_list.copy()
    for item in operation_list:
        if item == 'π':
            operation_list[items_index] = pi
        if item == 'e':
            operation_list[items_index] = e

        items_index+=1

    print(operation_list)