# Exception-gpt
Catch code exceptions and query and return solutions through the OpenAI interface.

```markdown
# Exceptiongpt.py

这是一个使用openai api来分析和解决python代码错误的项目。

## 动机

当我们编写python代码时，有时会遇到一些异常或错误，这些异常或错误可能很难理解或解决。如果我们能够利用openai的强大的自然语言处理能力来帮助我们分析和解决这些问题，那么我们就可以节省很多时间和精力。这就是本项目存在的原因。

## 安装

要使用本项目，你需要先安装openai库：

```bash
pip install openai
```

然后，你需要设置你的openai api密钥，你可以在[这里](https://beta.openai.com/docs/api-reference/authentication)找到如何获取和设置密钥的方法。

## 快速开始

本项目提供了一个名为`exception_gpt`的装饰器函数，它可以捕获任何异常，并将其发送给openai api，然后打印出openai api返回的分析和解决方案。你只需要将这个装饰器应用到你想要检查错误的函数上即可。例如：

```python
from exceptiongpt import exception_gpt

@exception_gpt
def divide(a, b):
    return a / b

divide(1, 0) # This will raise a ZeroDivisionError and send it to openai api
```

## 使用参考

本项目使用了openai库来调用openai api，你可以在[这里](https://beta.openai.com/docs/api-reference/introduction)查看openai api的详细文档。

本项目使用了`text-davinci-003`模型来生成分析和解决方案，这是一个专门针对文本生成任务优化的模型，你可以在[这里](https://beta.openai.com/docs/api-reference/completions/create)查看模型的详细信息。

本项目使用了中文作为查询和响应的语言，如果你想要使用其他语言，你可以修改`exception_gpt`函数中的`prompt`参数，将其改为你想要使用的语言。

## 引用方式

如果你使用了本项目，请在你的文档中引用以下信息：

```bibtex
@misc{exceptiongpt,
  author = {Your name},
  title = {Exceptiongpt.py: A project that uses openai api to analyze and solve python code errors},
  year = {2021},
  howpublished = {\url{https://github.com/yourusername/exceptiongpt}}
}
```

## 另见

如果你对本项目感兴趣，你可能也会对以下一些相关工具感兴趣：

- [Pyflakes](https://pypi.org/project/pyflakes/)：一个检查python代码错误和风格问题的工具。
- [PyLint](https://www.pylint.org/)：一个检查python代码质量和可维护性的工具。
- [Black](https://black.readthedocs.io/en/stable/)：一个自动格式化python代码的工具。
``
