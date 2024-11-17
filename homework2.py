# Task 1
def is_palindrome(value):
    if not isinstance(value, (int, str)):
        return False
    value = str(value)
    return value == value[::-1]


print(is_palindrome(1.23))
print(is_palindrome('alaa'))

# Task 2
def simple_calculator(operation, a, b):
    try:
       if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
          raise TypeError(f"{a} or {b} is not a number!")
       if operation == 'add':
          return a + b
       elif operation == 'multiply':
          return a * b
       elif operation == 'subtract':
          return a - b
       elif operation == 'divide':
          if b == 0:
           return "Division by zero is not allowed!"
          return a / b
       else:
          raise ValueError(f"Invalid operation - {operation}")
    except Exception as e:
        return f"Error: {e}"

print(simple_calculator('subtract', 5, 1))

# Task 3

from functools import wraps

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 3
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if i < attempts - 1:
                    print(f"Attempt {i+1} failed! Retrying")
                else:
                    print("Max retries reached! Raising exception.")
                    raise e
    return wrapper

@retry
def example(threshold):
    from random import random
    val=random()
    if val <= threshold:
        raise Exception("Random failure")

print(example(0.9))
