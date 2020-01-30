def parse(num):
    rim_num: dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result: int = 0
    prev: int = 0
    for counter in num[::-1]:
        if rim_num[counter] < prev != 0:
            result = result - rim_num[counter]
        else:
            result = result + rim_num[counter]
        prev = rim_num[counter]
    return result


if __name__ == "__main__":
    while True:
        r_num: str = input('please enter R num: ')
        error: bool = True
        for i in r_num:
            if i not in "IXLCDM":
                error = False
                break
        if error:
            print(f'A repr is {parse(r_num)}')
        else:
            print(f'Input error')
else:
    pass
