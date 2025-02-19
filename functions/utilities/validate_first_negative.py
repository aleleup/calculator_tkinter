def validate_first_negative(operation_array):
    # print("entring negative_validation", operation_array)
    if operation_array[0] == "-":
        operation_array.pop(0)
        operation_array[0] = f"-{operation_array[0]}"
        
