

def sum_of_squares(last_number):
    if last_number == 1:
        return 1
    return last_number**2 + sum_of_squares(last_number-1)


def square_of_sum(last_number):
    return sum(range(1, last_number+1))**2


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)


print('solution:', difference(100))
