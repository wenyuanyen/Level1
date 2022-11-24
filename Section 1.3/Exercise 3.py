def mean_calculate(numbers):
    if all(isinstance(x, (int, float)) for x in numbers) and numbers:
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    print(mean_calculate([-1, 0, 1, 2, 3]))
    print(mean_calculate([-1, 0, 1.1, 2, 3.0]))
    print(mean_calculate([]))
    print(mean_calculate([-1, 0, '1', 2, 3]))