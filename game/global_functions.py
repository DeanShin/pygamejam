# 345 -> 345
# 123,456,789,012 -> 123.45B
# 1,234,500 -> 1.23M
def format_int(x):
    x_str = str(x)
    num_of_digits = len(x_str)
    dot_pos = num_of_digits - ((num_of_digits - 1) // 3 * 3)
    if num_of_digits < 4: print(x_str)
    else:
        x_str = x_str[:dot_pos] + "." + x_str[dot_pos:dot_pos+2] + get_letter(num_of_digits)
        print(x_str)
def get_letter(num_of_digits):
    #IN PROGRESS
    if num_of_digits < 7: return "K"
    elif num_of_digits < 10: return "M"
    elif num_of_digits < 13: return "B"
    elif num_of_digits < 16: return "T"
    elif num_of_digits < 19: return "Qa"
    elif num_of_digits < 22: return "Qi"
    elif num_of_digits < 25: return "Sx"
    elif num_of_digits < 28: return "Sp"
    elif num_of_digits < 31: return "Oc"
    elif num_of_digits < 34: return "Nn"
    elif num_of_digits < 37: return "Qi"
    elif num_of_digits < 40: return "Dc"