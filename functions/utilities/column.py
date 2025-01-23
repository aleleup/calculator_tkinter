def column(i):
    if i % 3 == 1:
        return 0
    if i % 3 == 2 or i == 0:
        return 1
    if i % 3 == 0:
        return 2
    