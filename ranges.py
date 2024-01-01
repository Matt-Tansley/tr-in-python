# Help from: https://stackoverflow.com/a/7001371

# Fantastic explanation on iterables, generators, and yield: https://stackoverflow.com/a/231855

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


for c in char_range('a', 'c'):
    print(c)
