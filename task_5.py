def reverse_bool(value):
    if type(value) is not bool:
        return 'boolean expected'
    if not value:
        return True
    if value:
        return False


values = [True, False, 0, None]
for val in values:
    print(reverse_bool(val))
