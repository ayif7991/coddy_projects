op_list = ['+', '-', '*', '/', '%', '^', 'add', 'sub', 'mul', 'div', 'mod', 'pow']
def validate_input(op, a, b = None):
    if op not in op_list:
        return f'Invalid operater "{op}"'
    if not isinstance(a, (int, float)):
        return f'Invalid number "{a}"'
    if b is not None and not isinstance(b, (int, float)):

        return f'Invalid number "{b}"'
    if op == '/' or op == 'div' or op == '%' or op == 'mod':
        if b == 0:
            raise Exception('Division by zero') 

def calc(op, a, b = None):
    if op == '+' or op == 'add':
        if b is None:
            return a
        return a + b
    elif op == '-'or op == 'sub':
        if b is None:
            return a
        return a - b
    elif op == '*'or op == 'mul':
        return a * b
    elif op == '/'or op == 'div':
        return a / b
    elif op == '%'or op == 'mod':
        return a % b
    elif op == '^'or op == 'pow':
        return a ** b
    else:
        return 'Invalid operation'

if __name__ == "__main__":
    op = input('Enter operator: ')
    a = int(input('Enter first number: '))
    b_input = input('Enter second number (press Enter to use default value None): ')
    b = float(b_input) if b_input else None
    error = validate_input(op, a, b)
    if error:
        print(error)
    else:   
        result = calc(op, a) if b is None else calc(op, a, b)


        print(f"Result: {result}")
