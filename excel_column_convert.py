"""
转换Excel中列的名字为数字。
比如 A = 1，AA=27等等
A, B, C ... X, Y, Z, AA, AB, AC ... AY, AZ, BA, BB ... BZ ... ZY, ZZ, AAA ...
(26 进制转为 10 进制)
"""
def get_excel_column_name(index):
    if index < 0:
        raise ValueError("index must >= 0")

    index += 1  # starts from 0, so tweak index here
    result = ""
    while True:
        if index > 26:
            index, mod = divmod(index - 1, 26)
            result = chr(mod + ord('A')) + result
        else:
            return chr(index + ord('A') - 1) + result

