def fibonacci(n):
    a = 0
    b = 1
    sequence = [a]  # Start the sequence with the first Fibonacci number
    if n > 0:
        sequence.append(b)  # Add the second Fibonacci number if n > 0
    for i in range(2, n):
        c = a + b
        sequence.append(c)  # Add the next Fibonacci number to the sequence
        a = b
        b = c
    return sequence

def fibonacci_rec(n, sequence=None):
    if sequence is None:
        sequence = [0]  # Start with the first Fibonacci number
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(1)
        return sequence
    else:
        fibonacci_rec(n - 1, sequence)
        sequence.append(sequence[-1] + sequence[-2])  # Add the next number to the sequence
        return sequence

n = int(input("Enter the position of the Fibonacci number you want to find: "))
print(f"Fibonacci sequence up to {n}th number without recursion: ")
print(fibonacci(n))

print(f"Fibonacci sequence up to {n}th number with recursion: ")
print(fibonacci_rec(n))
