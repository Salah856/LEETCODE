def minDeletionSize(strs):
    c = 0

    for s in strs:

        b = s

        a = "".join(sorted(s))

        if a != b:
            c += 1

    return c


print("number is: ", minDeletionSize(['abc', 'cee', 'bca']))
