def export_num(s):
    num_string = ""
    for character in s:
        if character.isdigit() or character == '.':
            num_string += character
    num = float(num_string)
    return "{:.2f}".format(num)

print(export_num("abcd123.456"))
print(export_num("abcd123"))
