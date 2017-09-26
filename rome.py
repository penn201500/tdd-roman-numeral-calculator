ROMAN_NUMERAL = ('I', 'V', 'X')
def add(augend, addend):
    if not isinstance(addend, basestring) or not isinstance(augend, basestring):
        raise ValueError
    simple_augend = augend.replace('IV', 'IIII').replace('IX', 'VIIII')
    simple_addend = addend.replace('IV', 'IIII').replace('IX', 'VIIII')
    simple_num = simple_addend + simple_augend
    if any(char not in ROMAN_NUMERAL for char in simple_num):
        raise ValueError

    order_sum = ''.join(reversed(sorted(simple_num)))
    canonical_sum = order_sum.replace('IIIII', 'V').replace('IIII', 'IV').replace('VV', 'X').replace('VIV', 'IX')
    return canonical_sum
