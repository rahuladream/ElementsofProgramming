def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parityLess(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

if __name__ == "__main__":
    print(parity(64))
    print(parityLess(64))
    