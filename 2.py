def parse(num):
    rim_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for i in num[::-1]:
        if rim_num[i] < prev and prev != 0:
            result = result - rim_num[i]
        else:
            result = result + rim_num[i]
        prev = rim_num[i]
    return result


if __name__ == "__main__":
    while True:
        r_num: str = input('please enter R num: ')
        print(f'A repr is {parse(r_num)}')
else:
    pass
