def fibonacci_sequence(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def is_fibonacci(num):
    fib_seq = fibonacci_sequence(num)
    if num in fib_seq:
        return f'O número {num} pertence à sequência de Fibonacci.'
    else:
        return f'O número {num} NÃO pertence à sequência de Fibonacci.'

# Número a ser verificado
number = int(input("Informe um número: "))
print(is_fibonacci(number))
