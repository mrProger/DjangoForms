1) Выполнение конкретной операции зависимо от содержания строки operator
def arithmetic(a, b, operator):
    return {
        'add': print('add'),
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]
    
arithmetic(2, 2, 'add')


2) Замена символа A на символ B
def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])
