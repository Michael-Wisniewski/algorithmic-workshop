def count_recursive(n):
    if n > 1:
        return n + count_recursive(n - 1)
    else:
        return 1
