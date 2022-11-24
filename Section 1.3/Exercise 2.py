def fibonacci(N):
    if N < 0:
        return None
    elif N <= 0:
        return [0]
    elif N <= 1:
        return [0, 1]
    else:
        fibonacci_seq = [0, 1]
        current = 1
        while current <= N:
            fibonacci_seq.append(current)
            current = sum(fibonacci_seq[-2:])
        return fibonacci_seq


if __name__ == '__main__':
    print(fibonacci(-2))
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(20))
    print(fibonacci(21))
    print(fibonacci(22))
    print(fibonacci(100))
    print(fibonacci(1000))
