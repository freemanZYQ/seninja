from ..expr import BV, BVV

def str_to_int(s):
    res = ""
    for c in s:
        res += hex(ord(c))[2:]
    res += "00"
    return int(res, 16)

def str_to_bv_list(s):
    res = list()
    for c in s:
        res.append(BVV(ord(c), 8))
    return res

def int_to_str(i):
    s = hex(i)[2:]
    res = ""
    for i in range(0, len(s), 2):
        res += chr(int(s[i] + s[i+1], 16))
    return res

def as_bytes(bv: BV):
    for i in range(bv.size, 0, -8):
        yield bv.Extract(i-1, i-8)

def get_byte(bv: BV, i: int):
    return bv.Extract(bv.size-i*8-1, bv.size-i*8-8)
