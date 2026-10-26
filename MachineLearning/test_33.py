sample = [0, 1, 5, 7, 9, 10, 14]

def median(values):
    ordered = sorted(values)
    n = len(ordered)
    mid = 0

    if n % 2 == 0:
        mid = int(n / 2) - 1
    else:
        mid = int(n / 2)

    if n % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2
    else:
        return ordered[mid]

print(median(sample))