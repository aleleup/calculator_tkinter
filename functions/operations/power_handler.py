def power_handler(operation: list[float, str, float]) -> float:
    try:
        if operation[1] == "^":
            return operation[0] ** operation[2]
        else:
            return operation[0] ** (1/operation[2])
    except Exception:
        return 0
