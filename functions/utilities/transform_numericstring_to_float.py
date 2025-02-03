def transform_numericstring_to_float(operation_history_array):
    i = 0
    for item in operation_history_array:
        try: 
            operation_history_array[i] = float(item)
        except Exception as e:
            print(e)
            pass
        i += 1
