import dis

def greet(name, question):
    return f'Hello, {name}. How {question}?'

greet('Bob', 'deals')
# dis.dis(greet)


SECRET = 'this is secret!'

class Error:
    def __init__(self):
        pass

err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))
