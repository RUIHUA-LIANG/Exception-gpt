# Exceptiongpt.py

import openai
import traceback
import os

# Set your openai api key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to catch exceptions and send them to openai
def exception_gpt(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Get the exception message and stack trace
            message = str(e)
            stack_trace = traceback.format_exc()
            # Concatenate them into a query
            query = f"Exception message: {message}\nStack trace: {stack_trace}\n\n"
            # Call openai api and get the response
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="请帮我分析下面这个代码错误、代码运行路径回溯、提供解决方法并提供相应代码：" + "\n" + query,
                max_tokens=1000,
                temperature=0,
                frequency_penalty=0,
                presence_penalty=0
            )
            # Print the response
            print(response["choices"][0]["text"])
    return wrapper