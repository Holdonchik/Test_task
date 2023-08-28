def delete_element(elements, element):
    mnogestvo = set(str(elements))
    el = str(element)
    if len(el) > 1:
        print("Incorrect length")
    else:
        for i in mnogestvo:
            if i == el:
                mnogestvo.remove(el)
                break
            else:
                pass
        print(mnogestvo)


delete_element("elements", "e")