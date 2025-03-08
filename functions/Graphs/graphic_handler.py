import matplotlib.pyplot as plt
from functions.operations import calculate
from functions import parenthesis_handler

parenthesis_handler, calculate = [parenthesis_handler.parenthesis_handler, calculate.calculate]
def graphic_handler(operation_list:list) -> None:
    x_index = 0
    x_indexes = []
    x_values = range(-1000, 1001)
    y_values = []
    for item in operation_list:
        if item == 'x':
            x_indexes.append(x_index)
        x_index+=1

    for x_val in x_values:
        operation_copy = operation_list.copy()
        for index in x_indexes:
            operation_copy[index] = x_val


        try:
            parenthesis_operation = parenthesis_handler(operation_copy)
            y_val = calculate(parenthesis_operation)
            y_values.append(y_val)
        except: 
            print('domine error')
            y_val = 0
        
        
        print(f'x={x_val} -> ƒ(x)={y_val}')
    

    fig, ax = plt.subplots()

    ax.plot(x_values, y_values)
    ax.grid()
    plt.show()



