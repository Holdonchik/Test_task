def find_numbers(items):
    result = []
    final_result = []
    for item in items:
        if not isinstance(item, int):
            pass
        else:
            result.append(item)

    for i in result:
        if i <= 5:
            pass
        else:
            final_result.append(i)
    return final_result


example = ['qwe', '1', 1.25, 5, 6, 2, 10.15, 7, 8, 'test', '5', '7']
print(find_numbers(example))
