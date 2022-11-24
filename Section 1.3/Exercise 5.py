def mean_calculate(numbers):
    if all(isinstance(x, (int, float)) for x in numbers) and numbers:
        return sum(numbers) / len(numbers)


def var_calculate(numbers, degOfFreedom=1.0):
    if all(isinstance(x, (int, float)) for x in numbers) and numbers:
        mu = mean_calculate(numbers)
        square_error = [(x - mu) ** 2 for x in numbers]
        if len(numbers) > 1:
            return sum(square_error) / (len(numbers) - degOfFreedom)
        else:
            return 0.0


if __name__ == '__main__':
    print(var_calculate([-1, 0, 1, 2, 3]))
    print(var_calculate([-1, 0, 1, 2, 3], degOfFreedom=1))
    print(var_calculate([-1, 0, 1, 2, 3], degOfFreedom=0))
    print(var_calculate([-1, 0, 1.1, 2, 3.0]))
    print(var_calculate([]))
    print(var_calculate([2]))
    print(var_calculate([1, 2]))
    print(var_calculate([-1, 0, '1', 2, 3]))
