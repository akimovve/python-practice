# Задача 2.2
def f22(h):
    a = (h & 0x1f) << 27
    b = (h & 0xfe0) << 15
    c = (h & 0x3ff000) >> 4
    d = (h & 0x3fc00000) >> 22
    e = (h & 0xc0000000) >> 12
    return hex(a + b + c + d + e)

print(f22(0x96eda4cd))
print(f22(0x6d479c49))
