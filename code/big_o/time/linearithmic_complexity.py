def devide_segments(segments):
    n = len(segments)
    counter = n

    while (counter / 2) >= 1:
        for index in range(n):
            segments[index] /= 2
        counter /= 2

    return segments
