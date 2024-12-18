def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return 1 / x
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return 0  # Or handle the error appropriately
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None