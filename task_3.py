def count_digit_sum(num):
    digit_sum = 0

    try:
        if num < 0:
            num = abs(num)
        else:
            pass

        for digit in str(num):
            digit_sum += int(digit)
        return digit_sum

    except (TypeError, ValueError):
        return "This is not a number"


numbers = [57, -9876, 7013, 100001, 0, 1.7, "test"]
for number in numbers:
    print(count_digit_sum(number))
