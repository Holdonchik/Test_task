def is_prime_number(num):
    count = 0
    try:
        if num <= 1:
            count += 1
        elif num > 1:
            for i in range(2, num):
                if(num % i) == 0:
                    count += 1
        else:
            pass
        if count > 0:
            return False
        else:
            return True

    except TypeError:
        return f"Not a number"


numbers = [5, 4, 0, -1, 1, 1.5, "test", 17, 97]
for number in numbers:
    print(f"{number} {is_prime_number(number)}")
