def fix_parenthesis_bug(operation_list:list) -> list:
    i = 0
    while '' in operation_list:
        if i == len(operation_list): break
        index_to_remove = operation_list.index('')
        operation_list.pop(index_to_remove)
        i+=1
    print("parenthsis bug fixed", operation_list)


