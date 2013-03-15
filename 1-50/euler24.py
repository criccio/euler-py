#!/usr/bin/python


def get_permutations(val):
    result = []
    if len(val) == 1:
        result = [val]
    else:
        for i, c in enumerate(val):
            for perm in get_permutations(val[:i] + val[i+1:]):
                result += [c + perm]

    return result	

value = "0123456789"
print sorted(get_permutations(value))[999999]