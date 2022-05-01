# python has bitwise operators

# as an example, convert an int32 to bytes

def int_to_bytes(i):
    # >> right shift, << left shift
    # & bitwise and
    # | bitwise or
    return bytes((
        i       & 0xff,
        i >>  8 & 0xff,
        i >> 16 & 0xff,
        i >> 24 & 0xff
    ))