def swap_case(s):
    new_str = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                x = i.lower()
            else:
                x = i.upper()
            new_str += x
        else:
            new_str += i
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
