# test.py

from Exceptiongpt import exception_gpt

@exception_gpt
def divide(a, b):
    return a / b

divide(10, 0)