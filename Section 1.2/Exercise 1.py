if __name__ == '__main__':
    print('Average Calculator')
    sum_ = 0.0
    n_ = 0.0
    while True:
        current_number = input('Please enter a number:')
        if current_number == 's':
            if n_ == 0.0:
                print('You did not enter any numbers.')
            else:
                print('The average of the numbers entered is ' + str(sum_ / n_))
            break
        sum_ += float(current_number)
        n_ += 1.0
