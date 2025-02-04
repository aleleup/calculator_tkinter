from functions.utilities import divide_operation_hierarquie
import math
divide_operation_hierarquie = divide_operation_hierarquie.divide_operation_hierarquie

def potencies_or_factorial(operation_list:list[list, str]) ->list[list, str]:
    print(f"""
    ---------------POTENCY_OR_FACTORIAL------------------
                OP_LIST {operation_list}
""")
    
    
    operation_list_copy = operation_list.copy()

    for operation_list_item in operation_list_copy : #operation_list_copy for testing algorithm
        #Remove elements and keep target
        if type(operation_list_item) == str:
            continue
        check_potency_or_factorial = is_potency_operation(operation_list_item)
        if not check_potency_or_factorial:
            continue

        operation_list_item = divide_operation_hierarquie(operation_list_item, ["*", "/"])
        
        for operation in operation_list_item:
            if type(operation) == str:
                continue
            check_potency_or_factorial = is_potency_operation(operation)
            if not check_potency_or_factorial:
                continue

            

            factorial_indexes = []
            potencies_indexes = []
            operation_index_count = 0
            for element in operation:
                if element in ["^", "^1/"]:
                    potencies_indexes.append(operation_index_count)
                elif element == "!":
                    factorial_indexes.append(operation_index_count)
                operation_index_count+=1
            
            print(f"Op{operation}, potencies loc{potencies_indexes}, factorial loc{factorial_indexes}")

            operation_index = operation_list_item.index(operation)
            #factorial logic:
            for factorial_index in factorial_indexes:
                factorial_number = operation[factorial_index -1]
                factorial_result = factorial(factorial_number)
                operation[factorial_index -1] = factorial_result
                operation.pop(factorial_index)


            #potencies logic:
            while True:
                print(potencies_indexes)
                if len(potencies_indexes) <=1 :
                    break

                potency_part = operation[potencies_indexes[-1] -1: ]
                future_part = operation[ : potencies_indexes[-1] -1]

                new_list = [future_part, potency_part]

                print("NEW_LIST", new_list)

                potency_part = potency_handler(potency_part)

                print("potency_part", potency_part)
                operation = future_part + [potency_part]
                potencies_indexes.pop()

            if len(potencies_indexes) == 1:
                operation = potency_handler(operation)

            print("OPERATION_AFTER_potency", operation)

            operation_list_item[operation_index] = operation

        print("OPERATION_AFTER", operation_list_item)




    #item -> list[float, str, solve this array-> list[float, str] <-]


def is_potency_operation(operation_list_item:list) -> bool:
    is_potency_or_factorial = False
    
    symbol_expected:list = ["^", "^1/", "!"]
    for element in operation_list_item:
            if element in symbol_expected: 
                is_potency_or_factorial = True
                break

    return is_potency_or_factorial
        

def factorial(number:float) -> int:
    
    try:
        check_integer_float = number % 1 == 0
        if check_integer_float:
            result = math.factorial(int(number // 1))
            return result
        else:
            raise ValueError("Factorial only accepts integer numbers")
    except Exception as e:
        print(f"Error: {e}")
        

def potency_handler(operation: list[float, str, float]) -> float:
    try:
        if operation[1] == "^":
            return operation[0] ** operation[2]
        else:
            return operation[0] ** (1/operation[2])
    except Exception:
        return 0

    