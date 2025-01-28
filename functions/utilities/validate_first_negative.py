def validate_first_negative(operation_array):
    if not operation_array[0] and operation_array[1] == "-":
        operation_array.pop(0)
        operation_array.pop(0)
        operation_array[0] = f"-{operation_array[0]}"
        
