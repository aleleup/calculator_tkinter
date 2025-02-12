import math

def factorial_handler(number:float) -> int:
    
    try:
        check_integer_float = number % 1 == 0
        if check_integer_float:
            result = math.factorial(int(number // 1))
            return result
        else:
            raise ValueError("Factorial only accepts integer numbers")
    except Exception as e:
        print(f"Error: {e}")