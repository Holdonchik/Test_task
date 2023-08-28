def search_number_in_range():
    for num in range(1500, 2701):
        if(num % 5) == 0 and (num % 7) == 0:
            print(num)
        else:
            pass


search_number_in_range()