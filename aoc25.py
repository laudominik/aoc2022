decode = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
encode = ['=', '-', '0', '1', '2']


def snafu_to_bin(x_snafu):
    x_bin = 0
    for digit in x_snafu:
        x_bin *= 5
        x_bin += decode[digit]
    return x_bin

def bin_to_snafu(x_bin):
    x_snafu = ""
    x_base5 = ""

    while True:
        digit = x_bin % 5
        x_base5 = str(digit) + x_base5 
        x_bin //= 5 
        if x_bin == 0:
            break

    carry = 0
    for digit in reversed(x_base5):
        val = int(digit) + carry
        if val > 2:
            val -= 5
            carry = 1
        else:
            carry = 0
        x_snafu = encode[val+2]+x_snafu


    if carry == 1:
        x_snafu = '1' + x_snafu

    return x_snafu

with open("input25.txt") as f:
    print(bin_to_snafu(sum([snafu_to_bin(x) for x in f.read().split('\n')])))



bin_to_snafu(158)


