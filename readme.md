def arithmetic(a, b, operator):
    return {
        'add': print('add'),
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]
    
arithmetic(2, 2, 'add')
