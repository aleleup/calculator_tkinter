def add_substract_handler(operation_list):
    if operation_list[1] == "+":
        return operation_list[0] + operation_list[2]
    else:
        return operation_list[0] - operation_list[2]