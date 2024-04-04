def recursive_backwards(n):
    if len(n) == 1:
        return n
    else:
        return n[-1]+recursive_backwards(n[:-1])

print(recursive_backwards(f'Matt'))
