def format_int(x):
    x_str = str(x)
    num_of_digits = len(x_str)
    dot_pos = num_of_digits - ((num_of_digits - 1) // 3 * 3)
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
    

format_int(2560493690)

# 1,234,500 -> 1.23M
# 123,456,789,012 -> 123.45B